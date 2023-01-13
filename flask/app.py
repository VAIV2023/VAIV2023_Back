import os
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()

#Flask 객체 인스턴스 생성
app = Flask(__name__)
CORS(app)
mysql = MySQL(app)

app.config['MYSQL_USER'] = os.getenv("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.getenv("MYSQL_PASSWORD")
app.config['MYSQL_HOST'] = os.getenv("MYSQL_HOST")
app.config['MYSQL_DB'] = os.getenv("MYSQL_DB")



@app.route('/')
def index():
    return jsonify(
        {
            "result" : "hello",
            "id": 1
        },
        {
            "result" : "world",
            "id": 2
        }
   )




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)



