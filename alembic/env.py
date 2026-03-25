from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config, pool, create_engine
from alembic import context

from dotenv import load_dotenv
from database import Base

# ========================================
# Load .env
# ========================================
load_dotenv()

# ========================================
# Alembic config
# ========================================
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

database_url = os.getenv("DATABASE_URL")

if not database_url:
    raise Exception("DATABASE_URL is not set in environment variables")

config.set_main_option("sqlalchemy.url", database_url)


target_metadata = Base.metadata

def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # tworzymy engine bezpośrednio z DATABASE_URL (stabilniejsze niż engine_from_config)
    connectable = create_engine(
        database_url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # wykrywa zmiany typów kolumn
        )

        with context.begin_transaction():
            context.run_migrations()



if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()