#%%
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

#%%
# Use environment variables (Coolify supports them)
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST")  # fixed default
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")
# POSTGRES_URL = os.getenv("POSTGRES_URL")  # fixed default

#%%
# Connection string
#  DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# postgresql://[user]:[password]@yg0c48okc8skscco0wkws0gc:5432/[database] 
DATABASE_URL = "postgres://postgres:QjRfozIQ4xzQj1oiOUIyvDSrgNrFCXwZosvgFOXVKmhO4h7uBbYqKfXhbGpNq4pI@jc80c4ow8kw04gcg8c4kcc4g:5432/postgres"
# SQLAlchemy engine
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
