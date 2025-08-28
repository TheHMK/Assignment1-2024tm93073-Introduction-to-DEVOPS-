# ACEest Fitness & Gym – DevOps Assignment

![CI](https://github.com/TheHMK/Assignment1-2024tm93073-Introduction-to-DEVOPS-/actions/workflows/ci.yml/badge.svg)

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

## Quick Test with curl
```bash
curl -X POST http://127.0.0.1:5000/add_workout       -H "Content-Type: application/json"       -d '{ "workout": "Running", "duration": 30 }'

curl http://127.0.0.1:5000/workouts
```

## Run Tests
```bash
pytest
```

## Docker Usage
Build and run the app inside a container:

```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

Then open: [http://localhost:5000](http://localhost:5000)

## GitHub Actions CI/CD
This repo includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that runs on every push/PR to `main`:
- Install dependencies
- Run Pytest tests
- Build Docker image

CI status badge is shown at the top of this README.

## Notes
- Storage is **in-memory only** for simplicity.
- For production, add a database and persist workouts.
- Add secrets in GitHub if pushing to DockerHub or deploying.
