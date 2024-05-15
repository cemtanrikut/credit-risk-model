import pytest
from fastapi.testclient import TestClient
from main import app
from app.calculator import calculate_rwa
import pandas as pd

client = TestClient(app)

def test_calculate_rwa():
    obligors_df = pd.DataFrame({
        'Obligor_ID': [1, 2],
        'EBITDA': [50000, 40000],
        'Total_assets': [200000, 150000]
    })
    facilities_df = pd.DataFrame({
        'Facility_ID': [1, 2],
        'Obligor_ID': [1, 1],
        'Facility_type': ['Loan', 'Credit Line'],
        'Start_date': ['2022-01-01', '2022-02-01'],
        'Maturity_date': ['2023-01-01', '2024-02-01'],
        'Outstanding_amount': [100000, 50000],
        'Limit': [150000, 100000],
        'Contractual_rate': [0.05, 0.04],
        'Collateral_level': [0.8, 0.5]
    })
    rwa = calculate_rwa(facilities_df, obligors_df)
    assert rwa == pytest.approx(27.281249999999996)  # Example expected result

def test_api():
    response = client.post("/calculate_risk", json={
        "risk_measure": "RWA", 
        "assessment_date": "2021-12-31"
        })
    assert response.status_code == 200
    assert response.json() == {"RWA": 2109.6846812406534}  # Example expected result
