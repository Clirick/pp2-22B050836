import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

def insert_or_update_contact(first_name, last_name, phone):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM contacts WHERE first_name=%s AND last_name=%s", (first_name, last_name))
    count = cursor.fetchone()[0]
    if count > 0:
        cursor.execute("UPDATE contacts SET phone=%s WHERE first_name=%s AND last_name=%s", (phone, first_name, last_name))
    else:
        cursor.execute("INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    cursor.close()

first_name = str(input())
last_name = str(input())
phone= str(input())
insert_or_update_contact(first_name, last_name, phone)
