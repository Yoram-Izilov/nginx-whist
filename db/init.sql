CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

CREATE TABLE IF NOT EXISTS access_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    client_ip VARCHAR(45),
    server_ip VARCHAR(45),
    timestamp DATETIME
);

CREATE TABLE IF NOT EXISTS counter (
    count INT DEFAULT 0
);
INSERT INTO counter (count) VALUES (0);
