# Author: Clinton Daniel, University of South Florida
# Date: 4/4/2023
# Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called students 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python create_table.py

import sqlite3
import pandas as pd
import csv
conn = sqlite3.connect('database.db')
print("Connected to database successfully")

cursor = conn.cursor()

cursor.execute('''DELETE FROM hiking_trails;''')

# Create a table in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS hiking_trails (
                    name TEXT,
                    rating REAL,
                    level TEXT,
                    duration REAL,
                    distance REAL,
                    height REAL
                    );''')

# Path to your CSV file
csv_file_path = 'komoot.csv'

# Read data from CSV file and insert into the table
with open(csv_file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cursor.execute('''INSERT INTO hiking_trails (name, rating, level, duration, distance, height)
                          VALUES (:Name, :Rating, :Level, :Duration, :Distance, :Height);''', row)

# Commit changes and close connection

conn.commit()

print("Created table successfully!")

conn.close()
