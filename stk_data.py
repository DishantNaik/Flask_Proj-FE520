import pandas as pd
import yfinance as yf
import datetime as dt
import pprint
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import plotly.offline as pyo
import plotly.graph_objs as go



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

# def MACD_calc(st_name):

#     dd = yf.Ticker(st_name)
        
#     df1 = dd.history(period='30d')

#     exp1 = df1.Close.ewm(span=12, adjust=False).mean()
#     exp2 = df1.Close.ewm(span=26, adjust=False).mean()
#     macd = exp1 - exp2
#     # macd is pandas series
#     return macd

def MACD_NACDline(st_name):
    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='6mo')

    exp1 = df1.Close.ewm(span=12, adjust=False).mean()
    exp2 = df1.Close.ewm(span=26, adjust=False).mean()
    macd = exp1 - exp2

    exp3 = macd.ewm(span=9, adjust=False).mean()

    trace0 = go.Scatter(
    x = macd.index,
    y = macd,
    mode = 'lines',
    name = 'MACD Line' 
    )

    trace1 = go.Scatter(
    x = exp3.index,
    y = exp3,
    mode = 'lines',
    name = 'MACD Signal Line' 
    )

    data  = [trace0, trace1]
    layout = go.Layout(title='hahaha')

    fig = go.Figure(data=data, layout=layout)

    # pyo.plot(fig)
    return fig

def Stock_Line(st_name):

    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='6mo')

    trace0 = go.Scatter(
    x = df1.index,
    y = df1.Close,
    mode = 'lines',
    name = 'Stock Line Chart' 
    )

    data  = [trace0]
    layout = go.Layout(title='hahaha')

    fig = go.Figure(data=data, layout=layout)
    fig.update_layout(xaxis_range=[df1.index.min(),df1.index.max()])

    fig.update_layout(
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                            step="day",
                            stepmode="backward"),
                    ])
                ),
                rangeslider=dict(
                    visible=True
                ),
            )
    )


    # pyo.plot(fig)
    return fig

def Stock_Candel(st_name):
    dd = yf.Ticker(st_name)
        
    df1 = dd.history(period='1y')



    fig = go.Figure( data=[ 
                    go.Candlestick(
                    x = df1.index,
                    low = df1['Low'],
                    high = df1['High'],
                    open = df1['Open'],
                    close = df1['Close'],
                    increasing_line_color = 'green',
                    decreasing_line_color = 'red'
                    )
    ])
    fig.update_layout(xaxis_range=[df1.index.min(),df1.index.max()])
    
    return fig

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