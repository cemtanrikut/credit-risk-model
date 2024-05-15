import pandas as pd

def calculate_risk_factor_transf_PD(ebitda, total_assets):
    return ebitda / total_assets

def calculate_pd_score(risk_factor_transf_pd):
    return risk_factor_transf_pd * 0.1

def calculate_pd(pd_score):
    return pd_score / 100

def calculate_risk_factor_transf_EAD(outstanding_amount, limit, contractual_rate):
    return (outstanding_amount + (limit * contractual_rate)) / (limit + outstanding_amount)

def calculate_ead_score(risk_factor_transf_ead):
    return risk_factor_transf_ead * 1.5

def calculate_ead(ead_score, outstanding_amount, limit):
    return ead_score * (outstanding_amount + limit)

def calculate_risk_factor_transf_LGD(collateral_level):
    return 1 - collateral_level

def calculate_lgd_score(risk_factor_transf_lgd):
    return risk_factor_transf_lgd * 1.5

def calculate_lgd(lgd_score):
    return lgd_score

def calculate_rwa(facilities, obligors):
    facilities = facilities.merge(obligors, on="Obligor_ID")
    
    facilities['Risk_factor_transf_PD'] = facilities.apply(
        lambda row: calculate_risk_factor_transf_PD(row['EBITDA'], row['Total_assets']), axis=1)
    
    facilities['PD_score'] = facilities['Risk_factor_transf_PD'].apply(calculate_pd_score)
    
    facilities['PD'] = facilities['PD_score'].apply(calculate_pd)
    
    facilities['Risk_factor_transf_EAD'] = facilities.apply(
        lambda row: calculate_risk_factor_transf_EAD(row['Outstanding_amount'], row['Limit'], row['Contractual_rate']), axis=1)
    
    facilities['EAD_score'] = facilities['Risk_factor_transf_EAD'].apply(calculate_ead_score)
    
    facilities['EAD'] = facilities.apply(
        lambda row: calculate_ead(row['EAD_score'], row['Outstanding_amount'], row['Limit']), axis=1)
    
    facilities['Risk_factor_transf_LGD'] = facilities['Collateral_level'].apply(calculate_risk_factor_transf_LGD)
    
    facilities['LGD_score'] = facilities['Risk_factor_transf_LGD'].apply(calculate_lgd_score)
    
    facilities['LGD'] = facilities['LGD_score'].apply(calculate_lgd)
    
    facilities['RWA'] = facilities['PD'] * facilities['EAD'] * facilities['LGD']
    
    total_rwa = facilities['RWA'].sum()
    
    return total_rwa
