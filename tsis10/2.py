import csv
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

cursor = conn.cursor()

with open('C:/Users/oneta/pp2/pp2-22B050836/tsis10/contacts.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)", row)

conn.commit() 

cursor.close()
conn.close()
