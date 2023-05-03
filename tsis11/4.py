import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

def get_contacts(limit, offset):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cursor.fetchall()
    cursor.close()
    return rows

contacts = get_contacts(10, 0) 
for contact in contacts:
    print(contact)
