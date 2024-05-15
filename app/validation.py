import pandas as pd

def validate_data(obligors_df, facilities_df):
    valid_obligors = obligors_df[obligors_df['Total_assets'] > 0]
    valid_facilities = facilities_df[
        (facilities_df['Limit'] > 0) & 
        (pd.to_datetime(facilities_df['Start_date']) < pd.to_datetime(facilities_df['Maturity_date']))
    ]
    valid_obligors = valid_obligors[valid_obligors['Obligor_ID'].isin(valid_facilities['Obligor_ID'])]
    return valid_obligors, valid_facilities
