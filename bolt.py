import sqlite3
import streamlit as st

def create_database():
    
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='customers'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE customers
                     (name text, address text, phone text)''')
        conn.commit()
    conn.close()
