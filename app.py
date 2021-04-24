from flask import Flask, render_template, request
import sqlite3
from stk_data import get_data_by_date, get_current_data

app = Flask(__name__)

# def get_db_connection():
#     conn = sqlite3.connect('database.db')
#     conn.row_factory = sqlite3.Row
#     return conn


@app.route('/stock', methods=['post', 'get'])
def stock():
    # conn = get_db_connection()
    # posts = conn.execute('SELECT * FROM posts').fetchall()
    # conn.close()
    # return render_template('index.html', posts=posts)
    stk_info = []
    if request.method == 'POST':
        search = request.form.get('key')
        stk_info = get_data_by_date(search, '2017-04-22','2021-04-24')
    return render_template('stock.html', stk_info = stk_info.values)

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

    
    return render_template('index.html', stk_info_walmart = stk_info_walmart.values, stk_info_netflix = stk_info_netflix.values, stk_info_google = stk_info_google.values, stk_info_apple = stk_info_apple.values, stk_info_pfizer = stk_info_pfizer.values, stk_info_btc = stk_info_btc.values, stk_info_clover = stk_info_clover.values, stk_info_amazon = stk_info_amazon.values, stk_info_tesla = stk_info_tesla.values)

@app.route('/plot')
def plot():
    return render_template('plot.html')
if __name__ == '__main__':
   app.run(debug=True)