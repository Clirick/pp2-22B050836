import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="12345"
)

def get_records_by_pattern(pattern):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts WHERE first_name LIKE %s OR last_name LIKE %s OR phone LIKE %s", (f"%{pattern}%", f"%{pattern}%", f"%{pattern}%"))
    records = cursor.fetchall()
    cursor.close()
    return records

pattern = str(input())
results = get_records_by_pattern(pattern)
for result in results:
    print(result)