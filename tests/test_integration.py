import pytest
from fastapi.testclient import TestClient
from main import app
from setup_database import setup_database
import os
import sqlite3

client = TestClient(app)

@pytest.fixture(scope='module')
def setup_and_teardown():
    # Set up the database before tests
    setup_database()
    yield
    # Teardown: Remove the database file after tests
    os.remove('credit_risk.db')

def test_integration_rwa(setup_and_teardown):
    response = client.post("/calculate_risk", json={"risk_measure": "RWA", "assessment_date": "2021-12-31"})
    assert response.status_code == 200
    data = response.json()
    assert "RWA" in data
    assert isinstance(data["RWA"], (int, float))