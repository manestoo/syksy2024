import mysql.connector
import csv
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='C:/Users/matia/sovellusprojekti/rasberrylle/hae_tiedot/.env')

print("DB_HOST:", os.getenv("DB_HOST"))
print("DB_USER:", os.getenv("DB_USER"))
print("DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("DB_NAME:", os.getenv("DB_NAME"))

db_connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)


cursor = db_connection.cursor()

query = "SELECT * FROM rawdata"

cursor.execute(query)

data = cursor.fetchall()

with open('hae_tiedot_mysql.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    x = 0
    for i in data:
        line = str(data[x][0]), str(data[x][1]), str(data[x][2]), str(data[x][4]), str(data[x][5]), str(data[x][6]), str(data[x][7]), str(data[x][8]), str(data[x][9]), str(data[x][10])
        writer.writerow(line)
        x += 1

cursor.close()
db_connection.close()
