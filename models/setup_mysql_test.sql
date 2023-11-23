-- A script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- A new user hbnb_test (in localhost)
-- User has the password hbnb_test_pwd and privileges on the database
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Granting all privileges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- Granting SELECT privilege for the user in the db performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
