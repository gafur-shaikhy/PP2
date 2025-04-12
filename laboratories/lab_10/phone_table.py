import psycopg2

connect = psycopg2.connect(
    database="Phone",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)

cur = connect.cursor()

# PhoneBook таблица
cur.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        phone VARCHAR(20)
    )
""")

connect.commit()
cur.close()
connect.close()

print("PhoneBook кестесі сәтті құрылды.")
