import pandas as pd
import yfinance as yf
import datetime as dt


def get_data_by_date(stock_code,start_date, end_date):

    d = yf.Ticker(stock_code)

    df = d.history(start=start_date, end=end_date)
    return df

def get_current_data(stock_code):

    d = yf.Ticker(stock_code)

    df = d.history(period='1d')
    return df
