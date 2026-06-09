-- Read user

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0c_0 hbtn_0c_0.* TO 'user_0d_2'@'localhost';

FLUSH PRIVILEGES;