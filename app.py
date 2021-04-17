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
    
    stk_info, stk_name = [], ''
    stk_info = get_today("BTC-USD", '2021-04-17')
    return render_template('index.html', stk_name = 'BTC-USD', stk_info = stk_info.values)

if __name__ == '__main__':
   app.run(debug=True)