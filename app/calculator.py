def calculate_rwa(obligors_df, facilities_df):
    facilities_df = facilities_df.merge(obligors_df[['Obligor_ID', 'Total_assets']], on='Obligor_ID')
    facilities_df['PD'] = facilities_df.apply(lambda row: calculate_pd(row), axis=1)
    facilities_df['EAD'] = facilities_df['Outstanding_amount']
    facilities_df['LGD'] = 1 - facilities_df['Collateral_level']

    facilities_df['RWA_contribution'] = facilities_df['PD'] * facilities_df['EAD'] * facilities_df['LGD']
    rwa = facilities_df['RWA_contribution'].sum()

    return rwa

def calculate_pd(row):
    # Placeholder PD calculation logic
    return 0.01
