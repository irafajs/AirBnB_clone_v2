-- A script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- A new user hbnb_dev (in localhost)
-- User has the password hbnb_dev_pwd and privileges on the database
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all privileges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
-- Granting SELECT privilege for the user in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
