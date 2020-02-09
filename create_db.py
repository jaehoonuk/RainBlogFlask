import sqlite3

# Step 1: Create a connection object that represents the database
conn = sqlite3.connect('rain_sqlite.db')

# Step 2: Create a cursor object
c = conn.cursor()

# Step 3: Create the person and address tables
c.execute('''
          CREATE TABLE user
          (user_id INTEGER PRIMARY KEY,
          username TEXT NOT NULL, 
          email TEXT NOT NULL)
          ''')

c.execute('''
          CREATE TABLE city
          (city_id INTEGER PRIMARY KEY,
          city_name TEXT)
          ''')

c.execute('''
          CREATE TABLE forecast
          (forecast_id INTEGER PRIMARY KEY,
          datetime TEXT, 
          forecast TEXT,
          comment TEXT,
          city_id INTEGER NOT NULL,
          user_id INTEGER NOT NULL,
          FOREIGN KEY(city_id) REFERENCES city(city_id),
          FOREIGN KEY(user_id) REFERENCES user(user_id))
          ''')

# Step 5: Save (commit) the changes
conn.commit()

# Step 6 (optional): Close the connection if you are done with it
# Be sure any changes have been committed or they will be lost.
conn.close()