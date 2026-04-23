# ACC102-Track4
A Python Streamlit interactive dashboard analyzing &amp; visualizing key financial ratios of Tesla (TSLA) and Toyota (TM) over 2020-2025 WRDS dataset for ACC102 coursework.
# ACC102 Track4: Tesla vs Toyota Financial Performance Interactive Dashboard

## Project Overview
This is an interactive data analysis dashboard built for ACC102 Mini Assignment Track4. The tool provides a comprehensive financial performance comparison between Tesla (TSLA) and Toyota Motor (TM) from fiscal year 2020 to 2025, designed for accounting students, automotive industry analysts, and investors to evaluate the operational efficiency and profitability of traditional and new energy automakers.

## Core Features
- Interactive company filter (select TSLA, TM, or both for side-by-side comparison)
- Customizable fiscal year range slider (2020-2025)
- Visualization of 6 core financial metrics: Net Income (Millions USD), Gross Margin (%), Net Margin (%), Asset Turnover Ratio, Days Sales Inventory (DSI), R&D Intensity
- Real-time filtered raw data table display

## Data Source
All financial data is retrieved from the WRDS (Wharton Research Data Services) Compustat database, covering 2020-2025 fiscal year data for Tesla and Toyota.

## Project File Structure
- Main Folder: ACC102 Track4
  - Data Folder: Contains the raw data file TSLA_TM_Financial_Data_2020_2025.csv
  - SRC Folder: Contains the Streamlit dashboard main code app.py, and the data analysis code ACC102_final_Analysis_Code.py
  - Output Folder: Contains Figure1-9 full analysis visualizations
  - requirements.txt: Lists all required Python dependencies for the project
  - README.md: This project introduction document

## How to Run Locally
1. Ensure Python 3.8+ is installed on your device
2. Install required dependencies with the command: pip install -r requirements.txt
3. Launch the interactive dashboard with the command: streamlit run SRC/app.py

## Public Access Link
[Paste your Streamlit Cloud deployment link here after deployment]
