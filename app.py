#%%
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine
import os

#%%
# Use environment variables (Coolify supports them)
# DB_USER = os.getenv("POSTGRES_USER", "postgres_user")
# DB_PASS = os.getenv("POSTGRES_PASSWORD", 'strongP@ss123!')
# DB_HOST = os.getenv("POSTGRES_HOST", "postgres_host")  # fixed default
# DB_PORT = os.getenv("POSTGRES_PORT", "5432")
# DB_NAME = os.getenv("POSTGRES_DB", "postgres")
POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres_user:strongP%40ss123%21@bg08gs8occ0ggw40o44cc4kc:5432/postgres?sslmode=require")  # fixed default

#%%
# Connection string
# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL = POSTGRES_URL
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
