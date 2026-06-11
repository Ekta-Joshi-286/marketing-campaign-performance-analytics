import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("Channel Analysis")

channel = (
    df.groupby("channel")
    .agg({
        "revenue":"sum",
        "spend":"sum"
    })
    .reset_index()
)

channel["ROI"] = (
    (
        channel["revenue"]
        -
        channel["spend"]
    )
    /
    channel["spend"]
)*100

fig1 = px.bar(
    channel,
    x="channel",
    y="revenue",
    title="Revenue by Channel"
)

fig2 = px.bar(
    channel,
    x="channel",
    y="ROI",
    title="ROI by Channel"
)

st.plotly_chart(fig1,use_container_width=True)
st.plotly_chart(fig2,use_container_width=True)