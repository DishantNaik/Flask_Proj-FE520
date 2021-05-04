from flask import Flask, render_template, request
import sqlite3
from stk_data import get_data_by_date, get_current_data
import pandas as pd
import plotly.graph_objects as go
from flask_jsonpify import jsonpify

app = Flask(__name__)

@app.route('/stock', methods=['post', 'get'])
def stock():
    stk_info = []
    if request.method == 'POST':
        search = request.form.get('key')
        stk_info, hist_data = get_data_by_date(search, '2017-04-22','2021-05-02')

    df = pd.read_csv('dat.csv')
    # df_list = list(df.values.flatten())
    # date_df: list = df['Date']
    # close_df: list = df['Close']
    # print(list(date_df))

    return render_template('stock.html', search = search, stk_info = stk_info, hist_data = hist_data.values)


@app.route('/')
def index():

    stk_info_apple = get_current_data("AAPL")
    stk_info_btc = get_current_data("BTC-USD")
    stk_info_amazon = get_current_data("AMZN")
    stk_info_clover = get_current_data("CLOV")
    stk_info_pfizer = get_current_data("PFE")
    stk_info_tesla = get_current_data("TSLA")
    stk_info_netflix = get_current_data("NFLX")
    stk_info_walmart = get_current_data("WMT")
    stk_info_google = get_current_data("GOOG")
    
    return render_template('index.html', stk_info_walmart = round(stk_info_walmart.values[0][0],2), stk_info_netflix = round(stk_info_netflix.values[0][0],2), stk_info_google = round(stk_info_google.values[0][0], 2), stk_info_apple = round(stk_info_apple.values[0][0], 2), stk_info_pfizer = round(stk_info_pfizer.values[0][0], 2), stk_info_btc = round(stk_info_btc.values[0][0], 2), stk_info_clover = round(stk_info_clover.values[0][0],2), stk_info_amazon = round(stk_info_amazon.values[0][0], 2), stk_info_tesla = round(stk_info_tesla.values[0][0], 2))

@app.route('/plot')
def plot():
    # df = read_csv('dat.csv)
    # fig = go.Figure(go.Scatter(x = df['Date'], y = df['Close'],
    #                 name='Share Prices (in USD)'))

    # fig.update_layout(title='Share Prices over time (2017-2021)',
    #                 plot_bgcolor='rgb(230, 230,230)',
    #                 showlegend=True)
    
    return render_template('plot.html')
if __name__ == '__main__':
   app.run(debug=True)