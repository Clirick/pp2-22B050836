import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

cursor = conn.cursor()

while True:
    first_name = input("Enter first name (or 'exit' to quit): ")
    if first_name == 'exit':
        break
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    if not phone.isdigit():
            print(f"Invalid phone number for {first_name} {last_name}: {phone}")
            continue
    cursor.execute("INSERT INTO contacts (first_name, last_name, phone) VALUES (%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()

cursor.close()
conn.close()
