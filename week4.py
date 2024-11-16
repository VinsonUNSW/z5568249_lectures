"""
yf_example3.py

This module downloads Qantas stock prices for a given year and saves them as a CSV file.
"""

import os
import toolkit_config as cfg
import yf_example2

def qan_prc_to_csv(year):
    """
    Downloads Qantas stock prices for a given year and saves them to a CSV file.

    Parameters:
    year (int): The year for which to download the stock prices.
    """
    start = f"{year}-01-01"
    end = f"{year}-12-31"

    ticker = 'QAN.AX'

    output_file = f"qan_prc_{year}.csv"
    output_path = os.path.join(cfg.DATADIR, output_file)

    yf_example2.yf_prc_to_csv(ticker, start, end, output_path)

if __name__ == "__main__":
    qan_prc_to_csv(2020)
