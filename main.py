import requests
import selectorlib
from datetime import datetime
import sqlite3


# SQL Commands Examples
"INSERT INTO events VALUES ('Tigers', 'Tiger City', '2088.10.14')"
"SELECT * FROM events WHERE date='2088.10.15'"
"SELECT band, date FROM events WHERE date='2088.10.15'"

# Connect SQL Database
sql_connection = sqlite3.connect("sqldata.db")
cursor = sql_connection.cursor()

URL = "https://programmer100.pythonanywhere.com"
req = requests.get(url=URL)
text_html = req.text
extractor = selectorlib.Extractor.from_yaml_file("dat.yaml")
value = extractor.extract(text_html)["temperature"]

times = datetime.now().strftime(format="%y-%m-%d-%H-%M-%S")
tabledata = times + "," + str(value)

# Insert and Commit Changes
new_rows = [(times, str(value))]
cursor.executemany("INSERT INTO event VALUES(?,?)", new_rows)
sql_connection.commit()

with open("data.txt", "a") as file:
    file.write(tabledata + "\n")

# Find and fetch all of the data according to WHERE command if exist
cursor.execute("SELECT * FROM event")
rows = cursor.fetchall()
print(rows)
