import streamlit as st
import plotly.express as px
from utils import load_data

df = load_data()

st.title("Campaign Performance")

campaign = (
    df.groupby("campaign_id")
    .agg({
        "revenue":"sum",
        "conversions":"sum"
    })
    .reset_index()
)

top10 = (
    campaign
    .sort_values(
        "revenue",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top10,
    x="campaign_id",
    y="revenue",
    title="Top 10 Campaigns by Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)