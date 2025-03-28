<!-- @format -->

# Conference API

A FastAPI-based REST API for managing conference speakers and talks. This API provides endpoints to create and retrieve information about conference speakers and their talks.

## Features

- Create and retrieve conference speakers
- Create and retrieve conference talks
- SQLAlchemy ORM integration for database operations
- FastAPI automatic API documentation

## Prerequisites

- Python 3.7+
- PostgreSQL database
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone github.com/Falasefemi2/fastapi-neon-conference-api
cd fastapi-neon-conference-api
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your environment variables:
   Create a `.env` file in the root directory with your database configuration:

```
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Project Structure

```
fastapi-neon-conference-api/
├── src/
│   ├── main.py          # Main FastAPI application
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── database.py      # Database configuration
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## API Endpoints

### Speakers

- `POST /speakers/` - Create a new speaker
- `GET /speakers/` - List all speakers (with pagination)
- `GET /speakers/{speaker_id}` - Get detailed information about a specific speaker

### Talks

- `POST /talks/` - Create a new talk
- `GET /talks/` - List all talks (with pagination)
- `GET /talks/{talk_id}` - Get detailed information about a specific talk

## Running the Application

1. Start the FastAPI server:

```bash
uvicorn src.main:app --reload
```

2. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Development

The project uses:

- FastAPI for the web framework
- SQLAlchemy for database ORM
- Pydantic for data validation
- PostgreSQL as the database

## License

Falase Femi 2025
