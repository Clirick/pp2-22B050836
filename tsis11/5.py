import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

def delete_contact_by_username_or_phone(username=None, phone=None):
    cursor = conn.cursor()
    if username is not None:
        cursor.execute("DELETE FROM contacts WHERE first_name=%s OR last_name=%s", (username, username))
        print(f"Deleted contacts with username '{username}'")
    elif phone is not None:
        cursor.execute("DELETE FROM contacts WHERE phone=%s", (phone,))
        print(f"Deleted contacts with phone number '{phone}'")
    else:
        print("No username or phone number specified")
    conn.commit()
    cursor.close()
username=str(input())
phone=str(input())
delete_contact_by_username_or_phone(username)