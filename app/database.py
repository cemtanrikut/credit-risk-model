import sqlite3
import pandas as pd

def get_database_connection():
    conn = sqlite3.connect('credit_risk.db')
    return conn

def get_obligors():
    conn = get_database_connection()
    obligors_df = pd.read_sql('SELECT * FROM Obligor', conn)
    conn.close()
    return obligors_df

def get_facilities(assessment_date):
    conn = get_database_connection()
    facilities_df = pd.read_sql(f'''
    SELECT * FROM Facility WHERE Start_date >= "{assessment_date}"
    ''', conn)
    conn.close()
    return facilities_df
