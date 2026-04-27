
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import shutil
import warnings
warnings.filterwarnings("ignore")

# Path Definition
DESKTOP_PATH = os.path.expanduser("~/Desktop")
MAIN_FOLDER = os.path.join(DESKTOP_PATH, "ACC102 Track4")
DATA_FOLDER = os.path.join(MAIN_FOLDER, "Data")
SRC_FOLDER = os.path.join(MAIN_FOLDER, "SRC")
OUTPUT_FOLDER = os.path.join(MAIN_FOLDER, "Output")

os.makedirs(DATA_FOLDER, exist_ok=True)
os.makedirs(SRC_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

DATA_FILE_NAME = "TSLA_TM_Financial_Data_2020_2025.csv"

# Load Data
df = pd.read_csv(os.path.join(DATA_FOLDER, DATA_FILE_NAME))
target_companies = ['TSLA', 'TM']
df_filtered = df[df["tic"].isin(target_companies)]
df_filtered = df_filtered[df_filtered["fyear"].between(2020, 2025)]

# Financial Metrics Calculation
df_calc = df_filtered.copy()
df_calc["gross_margin"] = (df_calc["revt"] - df_calc["cogs"]) / df_calc["revt"] * 100
df_calc["net_margin"] = df_calc["ni"] / df_calc["revt"] * 100
df_calc["asset_turnover"] = df_calc["revt"] / df_calc["at"]
df_calc["dsi"] = (df_calc["invt"] / df_calc["cogs"].replace(0, np.nan)) * 365
df_calc["rd_intensity"] = df_calc["xrd"] / df_calc["revt"]
df_calc["net_income_millions"] = df_calc["ni"] / 1000
df_calc["firm_size"] = np.log(df_calc["at"])

print("ACC102 Final Analysis Code Run Successfully!")
print(f"Total Data Rows: {len(df_calc)}")
