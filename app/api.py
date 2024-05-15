from fastapi import APIRouter, HTTPException
from app.models import RiskRequest
from app.database import get_obligors, get_facilities
from app.calculator import calculate_rwa
from app.validation import validate_data
import pandas as pd

router = APIRouter()

@router.post("/calculate_risk")
def calculate_risk(request: RiskRequest):
    if request.risk_measure != "RWA":
        raise HTTPException(status_code=400, detail="Invalid risk measure")

    try:
        assessment_date = pd.to_datetime(request.assessment_date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format")

    obligors_df = get_obligors()
    facilities_df = get_facilities(assessment_date.strftime('%Y-%m-%d'))

    if facilities_df.empty:
        return {"RWA": 0}

    obligors_df, facilities_df = validate_data(obligors_df, facilities_df)
    rwa = calculate_rwa(obligors_df, facilities_df)

    return {"RWA": rwa}
