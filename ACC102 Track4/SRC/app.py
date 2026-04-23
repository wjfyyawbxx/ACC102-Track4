import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# --- 1. Page Configuration ---
st.set_page_config(
    page_title="ACC102 Track4: Auto Financial Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .big-font { font-size:20px !important; }
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.title("🚗 Tesla vs Toyota: Executive Financial Dashboard")
st.markdown("### ACC102 Mini Assignment | Track4 Interactive Tool | 2020-2025 WRDS Data")
st.divider()

# --- 2. Data Loading & Calculation ---
@st.cache_data
def load_and_calculate_data():
    # Keep your specific file path
    file_path = "/Users/betty/Desktop/ACC102 Track4/Data/TSLA_TM_Financial_Data_2020_2025.csv"
    
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        return pd.DataFrame()

    df = pd.read_csv(file_path)
    df = df[df["tic"].isin(["TSLA", "TM"])]
    df = df[df["fyear"].between(2020, 2025)]
    
    # Calculate financial metrics
    df["gross_margin"] = (df["revt"] - df["cogs"]) / df["revt"].replace(0, np.nan) * 100
    df["net_margin"] = df["ni"] / df["revt"].replace(0, np.nan) * 100
    df["asset_turnover"] = df["revt"] / df["at"].replace(0, np.nan)
    df["dsi"] = (df["invt"] / df["cogs"].replace(0, np.nan)) * 365
    df["rd_intensity"] = df["xrd"] / df["revt"].replace(0, np.nan)
    df["net_income_millions"] = df["ni"] / 1000
    # Additional: ROA (Return on Assets)
    df["roa"] = df["ni"] / df["at"].replace(0, np.nan) * 100
    
    return df

df = load_and_calculate_data()

if df.empty:
    st.stop()

# --- 3. Sidebar Controls ---
st.sidebar.header("📊 Dashboard Controls")

# 3.1 Company Selection
selected_companies = st.sidebar.multiselect(
    "Select Automakers",
    options=["TSLA", "TM"],
    default=["TSLA", "TM"]
)

# 3.2 Year Range
all_years = sorted(df["fyear"].unique())
selected_years = st.sidebar.slider(
    "Fiscal Year Range",
    min_value=int(min(all_years)),
    max_value=int(max(all_years)),
    value=(int(min(all_years)), int(max(all_years)))
)

# 3.3 Metric Selection
metrics_map = {
    "Net Income (Millions USD)": "net_income_millions",
    "Gross Margin (%)": "gross_margin",
    "Net Margin (%)": "net_margin",
    "Asset Turnover Ratio": "asset_turnover",
    "Days Sales Inventory (DSI)": "dsi",
    "R&D Intensity": "rd_intensity",
    "Return on Assets (ROA %)": "roa"
}

selected_metric_name = st.sidebar.selectbox(
    "Select Financial Metric",
    options=list(metrics_map.keys())
)
selected_metric_col = metrics_map[selected_metric_name]

# 3.4 Benchmark Toggle
show_benchmark = st.sidebar.checkbox("Show Benchmark (Avg of Selected)", value=True)

# --- 4. Data Filtering Logic ---
df_filtered = df[df["tic"].isin(selected_companies)].copy()
df_filtered = df_filtered[
    (df_filtered["fyear"] >= selected_years[0]) & 
    (df_filtered["fyear"] <= selected_years[1])
]

# --- 5. Main Interface Layout ---
tab1, tab2, tab3 = st.tabs(["📈 Executive Overview", "📉 Trend Analysis", "📑 Raw Data"])

# ================= TAB 1: Overview =================
with tab1:
    st.subheader("Latest Year Snapshot Comparison")
    
    # Get latest year data
    latest_year = df_filtered["fyear"].max()
    df_latest = df_filtered[df_filtered["fyear"] == latest_year]
    
    # Display KPIs in columns
    cols = st.columns(len(selected_companies))
    
    for i, company in enumerate(selected_companies):
        company_data = df_latest[df_latest["tic"] == company]
        if not company_data.empty:
            val = company_data[selected_metric_col].values[0]
            # Format numbers
            if "Margin" in selected_metric_name or "ROA" in selected_metric_name or "Intensity" in selected_metric_name:
                display_val = f"{val:.2f}%"
            else:
                display_val = f"{val:.2f}"
            
            cols[i].metric(
                label=f"{company} ({latest_year})", 
                value=display_val,
                delta="Latest Data"
            )

    st.divider()
    
    # Bar Chart Comparison
    st.subheader(f"Bar Chart Comparison ({selected_years[0]} - {selected_years[1]})")
    fig_bar, ax_bar = plt.subplots(figsize=(10, 5))
    sns.barplot(
        data=df_filtered, 
        x="fyear", 
        y=selected_metric_col, 
        hue="tic", 
        palette={"TSLA": "#E82127", "TM": "#EB0A1E"}, 
        ax=ax_bar
    )
    ax_bar.set_title(f"{selected_metric_name} Bar Comparison", fontweight='bold')
    ax_bar.set_ylabel(selected_metric_name)
    ax_bar.set_xlabel("Fiscal Year")
    st.pyplot(fig_bar)

# ================= TAB 2: Trend Analysis =================
with tab2:
    st.subheader(f"{selected_metric_name} Trend Analysis")
    
    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
    
    # 1. Plot selected companies
    sns.lineplot(
        data=df_filtered, x="fyear", y=selected_metric_col,
        hue="tic", marker="o", linewidth=2.5, markersize=8,
        palette={"TSLA": "#E82127", "TM": "#005A9C"}, 
        ax=ax
    )
    
    # 2. Plot Benchmark if enabled
    if show_benchmark and len(selected_companies) > 1:
        benchmark_df = df_filtered.groupby("fyear")[selected_metric_col].mean().reset_index()
        sns.lineplot(
            data=benchmark_df, x="fyear", y=selected_metric_col,
            color="gray", linestyle="--", linewidth=2, label="Benchmark (Avg)",
            ax=ax
        )

    # Styling
    ax.set_ylabel(selected_metric_name, fontsize=12)
    ax.set_xlabel("Fiscal Year", fontsize=12)
    ax.set_title(f"{selected_metric_name} Trend ({selected_years[0]}-{selected_years[1]})", fontsize=14, fontweight="bold")
    ax.grid(True, linestyle="--", alpha=0.5, axis="y")
    ax.legend(title="Legend")
    plt.tight_layout()
    
    st.pyplot(fig)
    
    # Text Insight
    with st.expander("📝 Analysis Insight"):
        st.write(f"""
        - **Selected Range**: {selected_years[0]} to {selected_years[1]}.
        - **Metric**: {selected_metric_name}.
        - **Observation**: This chart visualizes the performance gap between {', '.join(selected_companies)}.
        """)
        if show_benchmark:
            st.write("- A gray dashed line represents the average of the selected companies to serve as a benchmark.")

# ================= TAB 3: Raw Data =================
with tab3:
    st.subheader("Filtered Raw Data Table")
    st.dataframe(df_filtered, use_container_width=True)
    
    st.divider()
    
    # Data Export Feature
    st.subheader("Export Data")
    csv = df_filtered.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name=f'acc102_financial_data_{selected_years[0]}_{selected_years[1]}.csv',
        mime='text/csv',
    )

st.divider()
st.caption("ACC102 Mini Assignment | Track4 Interactive Data Analysis Tool | Built with Python & Streamlit")
