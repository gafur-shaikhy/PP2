import psycopg2
import csv

# PostgreSQL-ге қосылу
connect = psycopg2.connect(
    database="Phone",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)
cur = connect.cursor()


# 1. новыйдан юзер қосамын или бар болса старыйды обнова жасаймын
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;
""")

# 2 CSV файлдан юзерлер қосамын
cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users(p_names TEXT[], p_phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
BEGIN
    WHILE i <= array_length(p_names, 1) LOOP
        IF p_names[i] IS NULL OR p_phones[i] IS NULL THEN
            RAISE NOTICE 'Қате мәлімет %', i;
        ELSE
            CALL insert_or_update_user(p_names[i], p_phones[i]);
        END IF;
        i := i + 1;
    END LOOP;
END;
$$;
""")

# 3. контакты іздемін по куска стринга
cur.execute("DROP FUNCTION IF EXISTS search_contacts(TEXT);")
cur.execute("""
CREATE OR REPLACE FUNCTION search_contacts(pattern TEXT)
RETURNS TABLE(name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.name, pb.phone FROM phonebook pb
    WHERE pb.name ILIKE '%' || pattern || '%' OR pb.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

# 4. от N до M очередьтағы лист шығарамын
cur.execute("DROP FUNCTION IF EXISTS get_users_with_pagination(INT, INT);")
cur.execute("""
CREATE OR REPLACE FUNCTION get_users_with_pagination(p_limit INT, p_offset INT)
RETURNS TABLE(name VARCHAR(100), phone VARCHAR(20)) AS $$
BEGIN
    RETURN QUERY
    SELECT pb.name, pb.phone FROM phonebook pb
    ORDER BY pb.name
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
""")

# 5. удалит юзер
cur.execute("""
CREATE OR REPLACE PROCEDURE delete_user(p_identifier TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = p_identifier OR phone = p_identifier;
END;
$$;
""")

connect.commit()

def insert_or_update_user():
    name = input("Атыңызды енгізіңіз: ")
    phone = input("Телефон нөміріңізді енгізіңіз: ")
    cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
    connect.commit()
    print("Қолданушы сәтті қосылды немесе жаңартылды.\n")

def insert_many_from_csv():
    path = input("CSV файл жолы: ")
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            names = []
            phones = []
            for row in reader:
                names.append(row['name'])
                phones.append(row['phone'])
            cur.execute("CALL insert_many_users(%s, %s);", (names, phones))
            connect.commit()
            print(f"{len(names)} қолданушы CSV-дан қосылды.\n")
    except Exception as e:
        print(f"Қате: {e}\n")

def search_user():
    pattern = input("Іздеу үлгісі (мысалы: ali): ")
    cur.execute("SELECT * FROM search_contacts(%s);", (pattern,))
    rows = cur.fetchall()
    if rows:
        print("Нәтижелер:")
        for row in rows:
            print(row)
    else:
        print("Ештеңе табылмады.\n")

def show_with_pagination():
    limit = int(input("Қанша жазба көрсету: "))
    offset = int(input("Қай жерден бастау (offset): "))
    cur.execute("SELECT * FROM get_users_with_pagination(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    if rows:
        print("Нәтижелер:")
        for row in rows:
            print(row)
    else:
        print("Жазбалар жоқ.\n")

def delete_user():
    identifier = input("Аты немесе номері бойынша өшіру: ")
    cur.execute("CALL delete_user(%s);", (identifier,))
    connect.commit()
    print("Қолданушы өшірілді.\n")

# ——— МӘЗІР ———
while True:
    print("\n======= PhoneBook  =======")
    print("1. Қолданушы қосу/жаңарту")
    print("2. CSV-дан бірнеше қолданушы қосу")
    print("3. Іздеу (үлгі бойынша)")
    print("4. Pagination арқылы көру")
    print("5. Қолданушыны өшіру")
    print("0. Шығу")

    choice = input("Таңдаңыз: ")
    if choice == "1":
        insert_or_update_user()
    elif choice == "2":
        insert_many_from_csv()
    elif choice == "3":
        search_user()
    elif choice == "4":
        show_with_pagination()
    elif choice == "5":
        delete_user()
    elif choice == "0":
        print("Бағдарлама жабылды.")
        break
    else:
        print("Қате таңдау. Қайта көріңіз.\n")

# ——— Байланысты жабу ———
cur.close()
connect.close()
