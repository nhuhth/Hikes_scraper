from flask import Flask, render_template ,request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# @app.route('/', methods=['GET', 'POST'])
# def search():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM hiking_trails")
#     data = cursor.fetchall()
#     conn.close()
#     # return render_template('index.html', data=data)
#     return render_template('search.html',data=data)

@app.route('/', methods=['GET'])
def search():
    # Lấy dữ liệu từ các trường tìm kiếm
    name = request.args.get('name')
    levels = request.args.getlist('level')
    # Lấy giá trị min và max từ request
    min_duration = request.args.get('min_duration')
    max_duration = request.args.get('max_duration')
    min_distance = request.args.get('min_distance')
    max_distance = request.args.get('max_distance')
    print(levels)
    # min_duration = int(min_duration)
    # max_duration = int(max_duration)
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Xây dựng câu truy vấn SQL
    query = "SELECT * FROM hiking_trails WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append('%' + name + '%')

    if levels:
        query += " AND level IN (" + ','.join(['?'] * len(levels)) + ")"
        params.extend(levels)
    if min_duration is None or max_duration is None or min_duration.strip() == '' or max_duration.strip() == '':
        return render_template('search.html')
    else :
        print(type(min_duration))
        query += " AND duration BETWEEN ? AND ?"
        params.extend([min_duration, max_duration])
    if min_distance is None or max_distance is None or max_distance.strip() == '' or min_distance.strip() == '':
        return render_template('search.html')
    else :
        print(type(min_distance))
        query += " AND distance BETWEEN ? AND ?"
        params.extend([min_distance, max_distance])
    print(query)

    # Thực thi truy vấn SQL
    cursor.execute(query, params)
    data = cursor.fetchall()

    # Đóng kết nối đến cơ sở dữ liệu
    conn.close()
    # Trả về kết quả tìm kiếm
    return render_template('search.html', data=data)

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, app, use_reloader=False, use_debugger=False)
