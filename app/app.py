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
    client_ip = request.remote_addr
    server_ip = request.host
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO access_log (client_ip, server_ip, timestamp) VALUES (%s, %s, %s)", 
                   (client_ip, server_ip, timestamp))
    conn.commit()

    cursor.execute("UPDATE counter SET count = count + 1")
    conn.commit()

    # response = make_response(f"Server IP: {server_ip}")
        
    # Get the local machine name
    host_name = socket.gethostname()
    # Get the IP address using the host name
    local_ip = socket.gethostbyname(host_name)
    response = make_response(f"app IP Address: {local_ip}")
    
    response.set_cookie("server_ip", server_ip, max_age=300)  # Sticky session for 5 min
    return response

@app.route("/showcount")
def show_count():
    cursor.execute("SELECT count FROM counter")
    count = cursor.fetchone()[0]
    return f"Global Count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
