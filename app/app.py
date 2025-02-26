from flask import Flask, request, make_response
import mysql.connector
import os
from datetime import datetime
import socket

app = Flask(__name__)

# Database connection
db_config = {
    "host": os.getenv("DB_HOST", "db"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "rootpassword"),
    "database": os.getenv("DB_NAME", "app_db")
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

@app.route("/")
def index():
    # Get the local machine name
    cursor.execute("SELECT count FROM counter")
    count = cursor.fetchone()[0]
    return f"Global Count: {count}"
@app.route("/showcount")
def show_count():
    cursor.execute("SELECT count FROM counter")
    count = cursor.fetchone()[0]
    return f"Global Count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
