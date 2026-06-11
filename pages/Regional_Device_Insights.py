import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("Regional & Device Insights")

region = (
    df.groupby("region")
    ["revenue"]
    .sum()
    .reset_index()
)

device = (
    df.groupby("device")
    ["revenue"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    region,
    x="region",
    y="revenue",
    title="Revenue by Region"
)

fig2 = px.pie(
    device,
    names="device",
    values="revenue",
    title="Revenue by Device"
)

st.plotly_chart(fig1,use_container_width=True)
st.plotly_chart(fig2,use_container_width=True)