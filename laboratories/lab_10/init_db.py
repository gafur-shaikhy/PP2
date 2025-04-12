import psycopg2

conn = psycopg2.connect(
    database="snake",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)
cur = conn.cursor()

# Кестелерді құру
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        level INTEGER,
        score INTEGER
    )
""")

conn.commit()
cur.close()
conn.close()
print("Tables created successfully")
