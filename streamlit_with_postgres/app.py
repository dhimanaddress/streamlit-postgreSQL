#%%
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

#%%
DATABASE_URL = os.getenv("DATABASE_URL")  # fixed default

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
