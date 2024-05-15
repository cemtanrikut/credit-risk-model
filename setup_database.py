import sqlite3
import pandas as pd

def setup_database():
    conn = sqlite3.connect('credit_risk.db')
    c = conn.cursor()

    # Create Obligor table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Obligor (
        Obligor_ID INTEGER PRIMARY KEY,
        EBITDA REAL,
        Total_assets REAL
    )
    ''')

    # Create Facility table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Facility (
        Facility_ID INTEGER PRIMARY KEY,
        Obligor_ID INTEGER,
        Facility_type TEXT,
        Start_date TEXT,
        Maturity_date TEXT,
        Outstanding_amount REAL,
        Credit_limit REAL,
        Contractual_rate REAL,
        Collateral_level REAL,
        FOREIGN KEY (Obligor_ID) REFERENCES Obligor (Obligor_ID)
    )
    ''')

    # Load data from CSV files
    obligor_df = pd.read_csv('data/Obligor.csv')
    obligor_df.to_sql('Obligor', conn, if_exists='replace', index=False)

    facility_df = pd.read_csv('data/Facility.csv')
    facility_df.to_sql('Facility', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
