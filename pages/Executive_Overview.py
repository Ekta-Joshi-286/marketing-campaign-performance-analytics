import streamlit as st
from utils import load_data
import plotly.express as px

df = load_data()

st.title("Executive Overview")

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric(
    "Revenue",
    f"${df['revenue'].sum():,.0f}"
)

col2.metric(
    "Spend",
    f"${df['spend'].sum():,.0f}"
)

col3.metric(
    "Conversions",
    f"{df['conversions'].sum():,.0f}"
)

col4.metric(
    "Leads",
    f"{df['leads'].sum():,.0f}"
)

roi = (
    (
        df['revenue'].sum()
        -
        df['spend'].sum()
    )
    /
    df['spend'].sum()
)*100

col5.metric("ROI %",f"{roi:.2f}")

trend = (
    df.groupby("date")
    ["revenue"]
    .sum()
    .reset_index()
)

fig = px.line(
    trend,
    x="date",
    y="revenue",
    title="Revenue Trend"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
