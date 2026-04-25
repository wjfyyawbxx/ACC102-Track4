# ACC102-Track4
A Python Streamlit interactive dashboard analyzing &amp; visualizing key financial ratios of Tesla (TSLA) and Toyota (TM) over 2020-2025 WRDS dataset for ACC102 coursework.
# ACC102 Track4: Tesla vs Toyota Financial Performance Interactive Dashboard


## 1. Problem & User
This interactive dashboard addresses the need to move beyond static accounting ratio calculations, enabling a dynamic, real-world comparison of traditional and new energy automaker business models. It is designed for ACC102 course instructors, undergraduate accounting/finance students, and industry analysts seeking a transparent, customisable cross-firm financial benchmarking tool.

## 2. Data
- **Source**: Wharton Research Data Services (WRDS) Compustat database
- **Access Date**: 20–25 April 2026
- **Key Fields**: 2020–2025 fiscal year data for Tesla Inc. (TSLA) and Toyota Motor Corporation (TM), including Net Income (Millions USD), Gross Margin (%), Net Margin (%), Asset Turnover Ratio, Days Sales Inventory (DSI), and R&D Intensity.

## 3. Methods
The Python workflow follows four sequential stages:
1. Secure WRDS API connection and raw financial data extraction
2. Rigorous data cleaning (fiscal year alignment, missing value imputation, outlier adjustment for pandemic-related items)
3. Core financial ratio calculation and static trend visualisation via Pandas, Matplotlib, and Seaborn
4. Interactive Streamlit dashboard development with real-time filtering and dynamic chart synchronisation

## 4. Key Findings
- Toyota’s lean production model delivered consistent, recession-resilient profitability and stable inventory efficiency across the 2020–2025 period.
- Tesla’s direct-to-consumer sales model drove higher early-cycle asset turnover, offset by post-2022 margin compression amid intensifying market competition.
- Sustained R&D investment was a key strategic priority for both firms, though with different timing and intensity profiles relative to revenue growth.

## 5. How to Run Locally
1. Ensure Python 3.8+ is installed on your device
2. Install required dependencies: `pip install -r requirements.txt`
3. Launch the interactive dashboard: `python3 -m streamlit run SRC/app.py`

## 6. Product link / Demo
*(Local access only)*: http://localhost:8501

## 7. Limitations & Next Steps
- **Limitations**: Narrow sample of only two firms without broader industry benchmarking; no integration of macroeconomic or non-financial operational data.
- **Next Steps**: Expand the sample to include additional global automakers; incorporate industry average benchmarks; integrate time-series financial forecasting models for predictive analysis.
