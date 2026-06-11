import streamlit as st
import plotly.express as px
from utils import load_data
import pandas as pd

df = load_data()

st.title("Marketing Funnel")

funnel = pd.DataFrame({

    "Stage":[
        "Impressions",
        "Clicks",
        "Leads",
        "Conversions"
    ],

    "Value":[
        df["impressions"].sum(),
        df["clicks"].sum(),
        df["leads"].sum(),
        df["conversions"].sum()
    ]
})

fig = px.funnel(
    funnel,
    x="Value",
    y="Stage"
)

st.plotly_chart(
    fig,
    use_container_width=True
)