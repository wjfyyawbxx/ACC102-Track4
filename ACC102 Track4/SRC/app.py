import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title="ACC102 Track4: Auto Financial Dashboard",
    layout="wide"
)

st.title("Tesla vs Toyota: Financial Performance Analysis Dashboard")
st.markdown("### ACC102 Mini Assignment | Track4 Interactive Tool | 2020-2025 WRDS Data")
st.divider()

@st.cache_data
def load_and_calculate_data():
    df = pd.read_csv("/Users/betty/Desktop/ACC102 Track4/Data/TSLA_TM_Financial_Data_2020_2025.csv")
    df = df[df["tic"].isin(["TSLA", "TM"])]
    df = df[df["fyear"].between(2020, 2025)]
    
    df["gross_margin"] = (df["revt"] - df["cogs"]) / df["revt"] * 100
    df["net_margin"] = df["ni"] / df["revt"] * 100
    df["asset_turnover"] = df["revt"] / df["at"]
    df["dsi"] = (df["invt"] / df["cogs"].replace(0, np.nan)) * 365
    df["rd_intensity"] = df["xrd"] / df["revt"]
    df["net_income_millions"] = df["ni"] / 1000
    
    return df

df = load_and_calculate_data()

st.sidebar.header("Dashboard Controls")
selected_companies = st.sidebar.multiselect(
    "Select Automakers",
    options=["TSLA", "TM"],
    default=["TSLA", "TM"]
)
selected_years = st.sidebar.slider(
    "Fiscal Year Range",
    min_value=2020,
    max_value=2025,
    value=(2020, 2025)
)
selected_metric = st.sidebar.selectbox(
    "Select Financial Metric",
    options=[
        "Net Income (Millions USD)",
        "Gross Margin (%)",
        "Net Margin (%)",
        "Asset Turnover Ratio",
        "Days Sales Inventory (DSI)",
        "R&D Intensity"
    ]
)

df_filtered = df[df["tic"].isin(selected_companies)]
df_filtered = df_filtered[
    (df_filtered["fyear"] >= selected_years[0]) & 
    (df_filtered["fyear"] <= selected_years[1])
]

st.subheader(f"{selected_metric} Trend")
company_palette = {"TSLA": "orange", "TM": "lightblue"}

fig, ax = plt.subplots(figsize=(12, 6), dpi=100)

if selected_metric == "Net Income (Millions USD)":
    sns.lineplot(
        data=df_filtered, x="fyear", y="net_income_millions",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("Net Income (Millions USD)", fontsize=12)
elif selected_metric == "Gross Margin (%)":
    sns.lineplot(
        data=df_filtered, x="fyear", y="gross_margin",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("Gross Margin (%)", fontsize=12)
elif selected_metric == "Net Margin (%)":
    sns.lineplot(
        data=df_filtered, x="fyear", y="net_margin",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("Net Margin (%)", fontsize=12)
elif selected_metric == "Asset Turnover Ratio":
    sns.lineplot(
        data=df_filtered, x="fyear", y="asset_turnover",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("Asset Turnover Ratio", fontsize=12)
elif selected_metric == "Days Sales Inventory (DSI)":
    sns.lineplot(
        data=df_filtered, x="fyear", y="dsi",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("Days Sales Inventory (Days)", fontsize=12)
elif selected_metric == "R&D Intensity":
    sns.lineplot(
        data=df_filtered, x="fyear", y="rd_intensity",
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette=company_palette, ax=ax
    )
    ax.set_ylabel("R&D Intensity", fontsize=12)

ax.set_xlabel("Fiscal Year", fontsize=12)
ax.set_title(f"{selected_metric} Trend (2020-2025)", fontsize=14, fontweight="bold")
ax.grid(True, linestyle="--", alpha=0.5, axis="y")
plt.tight_layout()

st.pyplot(fig)

st.divider()
st.subheader("Filtered Raw Data Table")
st.dataframe(df_filtered, use_container_width=True)

st.divider()
st.caption("ACC102 Mini Assignment | Track4 Interactive Data Analysis Tool | Built with Python & Streamlit")