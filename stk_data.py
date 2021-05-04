import pandas as pd
import yfinance as yf
import datetime as dt
import pprint


def get_data_by_date(stock_code,start_date, end_date):

    d = yf.Ticker(stock_code)

    df = d.history(start=start_date, end=end_date)
    # pprint.pprint(d.info)
    df.to_csv('dat.csv')
    return d.info, df

def get_current_data(stock_code):

    d = yf.Ticker(stock_code)

    # print(d.info)
    
    df = d.history(period='1d')
    return df

# get_data_by_date('amzn','2017-04-22','2021-05-02')

# dayHigh 
# dayLow
# averageVolumne
# averageVolumne10days
# exchangeTimezoneName
# marketCap
# ask
# bid
# bidSize
# beta
# beta3Year
# open
# previousClose
# symbol