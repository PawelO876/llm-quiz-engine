LLM Quiz Engine

Quiz engine powered by LLM with Pydantic models.

Features
Data validation using Pydantic
Database integration (MySQL)
Clean project structure
Unit tests with pytest
Project structure

src/
  init.py
  models.py

tests/
  test_models.py

.env.example
requirements.txt

Setup

Create virtual environment:

python -m venv .venv

Activate (PowerShell):

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Environment variables

Create .env file based on .env.example:

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=llm_quiz

Testing

Run tests:

pytest

If pytest is not recognized:

python -m pytest

Tech stack
Python
Pydantic
pytest