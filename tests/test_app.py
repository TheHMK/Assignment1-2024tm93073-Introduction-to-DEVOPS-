import json
from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data

def test_add_workout_success():
    client = app.test_client()
    res = client.post("/add_workout", json={"workout": "Running", "duration": 30})
    assert res.status_code == 201
    assert b"Running" in res.data

def test_add_workout_validation():
    client = app.test_client()
    res = client.post("/add_workout", json={"workout": "Swim"})
    assert res.status_code == 400
    assert b"required" in res.data

    res = client.post("/add_workout", json={"workout": "Swim", "duration": "thirty"})
    assert res.status_code == 400
    assert b"integer" in res.data

def test_get_workouts():
    client = app.test_client()
    # Add one workout
    client.post("/add_workout", json={"workout": "Cycling", "duration": 20})
    res = client.get("/workouts")
    assert res.status_code == 200
    assert b"Cycling" in res.data
