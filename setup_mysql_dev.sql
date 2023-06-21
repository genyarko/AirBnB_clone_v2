#!/bin/bash

# Create database if it doesn't exist
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS hbnb_dev_db;"

# Create user if it doesn't exist
mysql -u root -p -e "CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';"

# Grant all privileges to the user on hbnb_dev_db
mysql -u root -p -e "GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';"

# Grant SELECT privilege on performance_schema to the user
mysql -u root -p -e "GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';"
