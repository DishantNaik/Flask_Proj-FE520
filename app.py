from flask import Flask, render_template, request
import sqlite3
from stk_data import get_data_by_date, get_today

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
        stk_info = get_data_by_date(search, '2017-04-22','2018-04-22')
    return render_template('stock.html', stk_info = stk_info.values)

@app.route('/')
def index():
    
    stk_info_apple, stk_info_btc, stk_info_clover, stk_info_amazon, stk_info_pfizer = [], [], [], [], []
    stk_info_apple = get_today("AAPL", '2021-04-17')
    stk_info_btc = get_today("BTC-USD", '2021-04-17')
    stk_info_amazon = get_today("AMZN", '2021-04-17')
    stk_info_clover = get_today("CLOV", '2021-04-17')

    stk_info_pfizer = get_today("PFE", '2021-04-17')
    return render_template('index.html', stk_info_apple = stk_info_apple.values, stk_info_pfizer = stk_info_pfizer.values, stk_info_btc = stk_info_btc.values, stk_info_clover = stk_info_clover.values, stk_info_amazon = stk_info_amazon.values)

if __name__ == '__main__':
   app.run(debug=True)