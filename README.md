# Stock-Screening-Financial-Analysis-Model-Python-Pandas-NumPy-
Built a Python tool using pandas and numpy to calculate key financial ratios (PE Ratio, ROE, Debt/Equity) and assign scores based on custom thresholds. Combined scores to rank stocks for investment analysis, enabling data-driven stock selection and portfolio insights.

# Stock Screening & Financial Analysis Model

This project demonstrates a Python-based financial analysis tool that screens stocks using fundamental financial ratios and assigns scores to evaluate their investment potential.

## Features
- Calculates essential financial metrics:
  - **PE Ratio** (Price-to-Earnings)
  - **ROE** (Return on Equity)
  - **Debt-to-Equity Ratio**
- Applies multi-tier conditional scoring logic to each metric based on custom thresholds.
- Combines scores to provide an overall ranking for each stock.
- Processes raw stock data from CSV files and outputs a comprehensive DataFrame with scores.

## Technologies Used
- Python 3.x
- pandas for data manipulation
- numpy for efficient conditional logic and scoring

## Usage
1. Clone the repo.
2. Place your stock financial data CSV (with columns: Price, EPS, Net_Income, Equity, Debt) in the project directory.
3. Run `stock_scoring.py` (or your main script) to generate scores and rankings.
4. Explore the output DataFrame for investment insights.

## Example Output

| Stock | PE Ratio | ROE  | D/E  | Score | Final Score |
|-------|----------|------|------|-------|-------------|
| AAPL  | 25.4     | 0.28 | 0.40 | 250   | 83.33       |
| MSFT  | 30.2     | 0.23 | 0.50 | 240   | 80.00       |

---

Feel free to open issues or contribute!

---

If you want, I can also help prepare a clean Python script with comments or a Jupyter notebook version to include in the repo. Would that be helpful?
