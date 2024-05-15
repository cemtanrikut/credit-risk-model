from pydantic import BaseModel

class RiskRequest(BaseModel):
    risk_measure: str
    assessment_date: str
