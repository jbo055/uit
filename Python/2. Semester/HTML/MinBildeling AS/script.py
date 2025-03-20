from flask import Flask, jsonify
import pymysql


app = Flask(__name__)

db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Sintkatt97",
    "database": "minbildeling"
}

def get_db_connection():
    return pymysql.connect(
        host = db_config["host"],
        user = db_config["user"],
        password = db_config["password"],
        database = db_config["database"],
        cursorclass = pymysql.cursors.DictCursor
    )

@app.route('/api/biler', methods=['GET'])
def get_cars():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT id, make, model, year, imageUrl FROM cars"
            cursor.execute(sql)
            cars = cursor.fetchall()
    finally:
        connection.close()
    return jsonify(cars)

if __name__ == '__main__':
    app.run(debug=True)