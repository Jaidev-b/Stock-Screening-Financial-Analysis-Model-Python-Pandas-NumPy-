import csv
import pandas as pd
from pandas import read_csv
import numpy as np


#importing csv and applying pd to create df
stocks = pd.read_csv('stocks_clean.csv')

#calculating all values
stocks ["PE Ratio"] = stocks["Price"] / stocks["EPS"]
stocks ["ROE"] = stocks["Net_Income"] / stocks["Equity"]
stocks ["D/E"] = stocks["Debt"] / stocks["Equity"]
stocks ["Score"] = 0

#defining conditions to use numpy for PE
PE_conditions = [
    stocks["PE Ratio"] > 100,
    (stocks["PE Ratio"] <= 100) & (stocks["PE Ratio"] > 90),
    (stocks["PE Ratio"] <= 90) & (stocks["PE Ratio"] > 80),
    (stocks["PE Ratio"] <= 80) & (stocks["PE Ratio"] > 70),
    (stocks["PE Ratio"] <= 70) & (stocks["PE Ratio"] > 60),
    (stocks["PE Ratio"] <= 60) & (stocks["PE Ratio"] > 50),
    (stocks["PE Ratio"] <= 50) & (stocks["PE Ratio"] > 40),
    (stocks["PE Ratio"] <= 40) & (stocks["PE Ratio"] > 30),
    (stocks["PE Ratio"] <= 30) & (stocks["PE Ratio"] > 20),
    (stocks["PE Ratio"] <= 20) & (stocks["PE Ratio"] > 10),
    (stocks["PE Ratio"] <= 10) & (stocks["PE Ratio"] > 0),
    stocks["PE Ratio"] <= 0
]

#defining corresponding scores to pe conditions
PE_scores = [25,30,35,40,50,60,70,80,90,100,90,30]

#definign Roe conditions
ROE_conditions = [
    stocks["ROE"] > 0.25,
    (stocks["ROE"] <= 0.25) & (stocks["ROE"] > 0.20),
    (stocks["ROE"] <= 0.20) & (stocks["ROE"] > 0.15),
    (stocks["ROE"] <= 0.15) & (stocks["ROE"] > 0.10),
    (stocks["ROE"] <= 0.10) & (stocks["ROE"] > 0.05),
    (stocks["ROE"] <= 0.05) & (stocks["ROE"] >= 0),
    stocks["ROE"] < 0
]

#ROE corresponding scores
ROE_scores = [100, 90, 80, 70, 60, 50, 30]

#DE Score conditions
DE_conditions = [
    stocks["D/E"] < 0.1,
    (stocks["D/E"] >= 0.1) & (stocks["D/E"] < 0.3),
    (stocks["D/E"] >= 0.3) & (stocks["D/E"] < 0.5),
    (stocks["D/E"] >= 0.5) & (stocks["D/E"] < 1.0),
    (stocks["D/E"] >= 1.0) & (stocks["D/E"] <= 2.0),
    stocks["D/E"] > 2.0
]

#De corresponding Scores
DE_scores = [100, 90, 80, 70, 50, 30]

stocks ["Score"] = np.select(PE_conditions, PE_scores)
stocks ["Score"] += np.select(ROE_conditions, ROE_scores)
stocks ["Score"] += np.select(DE_conditions, DE_scores)

stocks ["Final Score"] = stocks ["Score"] / 3

print (stocks)
