import pandas as pd
import yfinance as yf
import datetime as dt
import pprint


def get_data_by_date(stock_code,start_date, end_date):

    d = yf.Ticker(stock_code)

    df = d.history(start=start_date, end=end_date)

    df['Date'] = df.index
    df['Date'] = df['Date'].dt.date
    df['Change'] = (df['Close'].diff())
    df['% Change'] = (df['Close'].pct_change() * 100)

    df = df.reindex(index=df.index[::-1])
    # pprint.pprint(d.info)
    # df.to_csv('dat.csv')
    return d.info, df

def get_current_data(stock_code):

    d = yf.Ticker(stock_code)

    # print(d.info)
    df = d.history(period = '1d')

    
    df['Date'] = df.index
    df['Change'] = (df['Close'].diff())
    df['% Change'] = (df['Close'].pct_change() * 100)

    return df

def RSI_calc(st_name):
    # Calculating RSI
    # Formula 100 - [100 / 1 + (Avg Gain/Avg Loss)]
    # Default Look back period 30 days

    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='30d')
    change = df1['Close'].diff().dropna()

    gain = change.apply(lambda x : x if x > 0 else 0)
    index_names = gain[ gain == 0 ].index
    gain.drop(index_names, inplace = True)

    loss = change.apply(lambda x : x if x < 0 else 0)
    index_names1 = loss[ loss == 0 ].index
    loss.drop(index_names1, inplace = True)
    loss = loss.abs()

    avg_gain = gain.mean()
    avg_loss = loss.mean()

    avg_g_l = 1 + (avg_gain/avg_loss)
    RSI = 100 - (100 / avg_g_l) 

    return RSI

def SMA_cal(st_name):
    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='30d')
    sma = df1.Close.mean()

    return sma

def MACD_calc(st_name):

    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='30d')

    exp1 = df1.Close.ewm(span=12, adjust=False).mean()
    exp2 = df1.Close.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2
    # macd is pandas series
    return mcad


# get_data_by_date('amzn','2017-04-22','2021-05-02')

# dayHigh* 
# dayLow*
# volume*
# averageVolumne*
# averageVolumne10days
# exchangeTimezoneName
# marketCap*
# ask*
# bid*
# bidSize
# beta
# beta3Year*
# open*
# previousClose*
# symbol