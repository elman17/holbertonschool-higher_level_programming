-- Root user

CREATE USER IF NOT EXISTS '0_0d_1'@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANTS ALL PRIVILEGES ON *.* 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;