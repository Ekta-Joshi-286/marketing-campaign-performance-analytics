import pandas as pd

def load_data():

    df = pd.read_csv(
        "marketing_final.csv"
    )

    df["date"] = pd.to_datetime(df["date"])

    df["CTR"] = (
        df["clicks"] /
        df["impressions"]
    ) * 100

    df["Lead Rate"] = (
        df["leads"] /
        df["clicks"]
    ) * 100

    df["Conversion Rate"] = (
        df["conversions"] /
        df["leads"]
    ) * 100

    df["ROI"] = (
        (df["revenue"] - df["spend"])
        / df["spend"]
    ) * 100

    df["Profit"] = (
        df["revenue"] -
        df["spend"]
    )

    return df