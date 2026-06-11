import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("Customer Segmentation")

age = (
    df.groupby("age_group")
    ["revenue"]
    .sum()
    .reset_index()
)

fig = px.pie(
    age,
    names="age_group",
    values="revenue",
    title="Revenue by Age Group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)