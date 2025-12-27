# Backend - Profile Manager API

FastAPI REST API with SQLite database.

## Prerequisites

- Python 3.10+
- pip

## Setup

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment file
cp .env.example .env
```

## Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=sqlite:///./data/profiles.db
```

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `sqlite:///./data/profiles.db` |

## Run Locally

```bash
# Make sure virtual environment is activated
source .venv/bin/activate  # macOS/Linux

# Run development server
uvicorn app.main:app --reload --port 8000
```

API available at: **http://localhost:8000**

- Health check: http://localhost:8000/health

## Production-like Run

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API info |
| GET | `/health` | Health check |
| * | `/api/v1/profiles/*` | Profile CRUD operations |

## Troubleshooting

### Port 8000 already in use

```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use a different port
uvicorn app.main:app --reload --port 8001
```

### CORS errors from frontend

The API allows requests from:
- `http://localhost:3000`
- `http://localhost:5173`

If using a different frontend port, update `allow_origins` in `app/main.py`.

### Database not found / SQLite errors

1. Ensure the `data/` directory exists:
   ```bash
   mkdir -p data
   ```
2. The database file is created automatically on first run
3. Check `DATABASE_URL` in `.env` points to a valid path

### Missing dependencies

```bash
pip install -r requirements.txt
```

### Module not found errors

Ensure you're running from the `backend/` directory and the virtual environment is activated.