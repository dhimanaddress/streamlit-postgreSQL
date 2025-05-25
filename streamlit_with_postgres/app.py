#%%
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

#%%
# Use environment variables (Coolify supports them)
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")  # fixed default
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"  # updated DATABASE_URL

#%%
engine = create_engine(DATABASE_URL)

st.title("PostgreSQL + Streamlit (Coolify)")

query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"

try:
    df = pd.read_sql(query, engine)
    st.dataframe(df)
    fig = px.bar(df, x="table_name", y=[1]*len(df), title="Tables in DB", labels={"y": "Count"})
    st.plotly_chart(fig)
except Exception as e:
    st.error(f"Database error: {e}")
