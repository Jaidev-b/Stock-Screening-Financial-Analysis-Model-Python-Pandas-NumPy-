# Copyright (c) 2025 Jaidev Bathineni 
# All rights reserved.
# This source code is for personal use only. Unauthorized copying,
# modification, or distribution is prohibited.

import csv
import pandas as pd
import os
import numpy as np

print ("This is a stock screener")
while True:
    file_name = input("Enter file name (include .csv)(Type Exit to quit): ")
    if file_name.lower() == "exit":
        exit()
    elif not os.path.isfile(file_name):
        print("File not found.")
    elif not file_name.endswith(".csv"):
        print("This is not a CSV file.")
    else:
        break

stocks = pd.read_csv(file_name)

def options():
    print ("Choose which stock do you want to evaluate")
    for stock in stocks.loc[:,"Stock"]:
        print (stock)
options()

while True:
    stock = input("Enter stock code: ")
    stock = stock.upper()
    if stock in stocks.values:
        break
    else:
        print ("stock not found")

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

score = stocks.loc[stocks["Stock"] == stock, "Final Score"].values[0]
print(f"The Final Score for {stock} is: {score}")

if score > 75:
    print ("The stock score is very good")
elif score > 50:
    print ("The stock is good")
elif score > 25:
    print ("The stock is bad")
else:
    print ("The stock is very bad")
