# ACEest Fitness & Gym – DevOps Assignment

A minimal Flask API for logging workouts, packaged with tests, Docker, and a GitHub Actions CI pipeline.

## Endpoints
- `GET /` → health/welcome
- `POST /add_workout` → add a workout (JSON body: `{ "workout": "Running", "duration": 30 }`)
- `GET /workouts` → list workouts (in-memory for demo)

## Run Locally
```bash
pip install -r requirements.txt
python app.py
# open http://127.0.0.1:5000/
```

## Quick test with curl
```bash
curl -X POST http://127.0.0.1:5000/add_workout       -H "Content-Type: application/json"       -d '{ "workout": "Running", "duration": 30 }'

curl http://127.0.0.1:5000/workouts
```

## Run Tests
```bash
pytest
```

## Docker
```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

## GitHub Actions
CI runs on every push / PR to `main`:
- Install deps
- Run `pytest`
- Build Docker image
```yaml
.github/workflows/ci.yml
```

## Notes
- Storage is in-memory for simplicity (meets the assignment scope).
- For production, add a database and persist workouts.
