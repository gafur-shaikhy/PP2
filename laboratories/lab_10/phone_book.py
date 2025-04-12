import psycopg2
import csv


connect = psycopg2.connect(
    database="Phone",
    user="postgres",
    password="admin",
    host="localhost",
    port=5432
)

cur = connect.cursor()

# Қолмен қосу
def insert_user():
    name = input("Атыңызды енгізіңіз: ")
    phone = input("Телефон нөміріңізді енгізіңіз: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    connect.commit()
    print(" Қолданушы сәтті қосылды.\n")

# CSV-дан жүктеу
def insert_from_csv():
    path = input("CSV файл : ")
    try:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                name = row['name']
                phone = row['phone']
                cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
                count += 1
            connect.commit()
            print(f"{count} қолданушы CSV-дан қосылды.\n")
    except Exception as e:
        print(f"Қате: {e}\n")

# Жаңарту
def update_user():
    old_name = input("Кімді өзгертеміз (аты): ")
    new_phone = input("Жаңа телефон нөмірі: ")
    cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, old_name))
    connect.commit()
    print(" Жаңартылды.\n")

# Іздеу
def search_user():
    name = input("Іздеу үшін аты: ")
    cur.execute("SELECT * FROM PhoneBook WHERE name = %s", (name,))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f" {row}")
    else:
        print(" Қолданушы табылмады.\n")

# Фильтрация (аты бойынша)
def filter_by_name_sorted():
    cur.execute("SELECT * FROM PhoneBook ORDER BY name ASC")
    rows = cur.fetchall()
    if rows:
        print(" Қолданушылар алфавит бойынша:")
        for row in rows:
            print(row)
    else:
        print(" Жазбалар жоқ.\n")

# Өшіру
def delete_user():
    name = input("Кімді өшіреміз (аты): ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s", (name,))
    connect.commit()
    print(" Қолданушы өшірілді.\n")

# Барлығын көрсету
def show_all():
    cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    if rows:
        print(" Барлық жазбалар:")
        for row in rows:
            print(row)
    else:
        print(" Жазбалар жоқ.\n")
    print()

# Мәзір
while True:
    print("===  Телефон кітапшасы ===")
    print("1. Қолмен қосу")
    print("2. Жаңарту")
    print("3. Іздеу")
    print("4. Өшіру")
    print("5. Барлығын көрсету")
    print("6. CSV файлдан қосу")
    print("7. Фильтрация (аты бойынша)")
    print("0. Шығу")

    choice = input("Таңдаңыз: ")

    if choice == "1":
        insert_user()
    elif choice == "2":
        update_user()
    elif choice == "3":
        search_user()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        show_all()
    elif choice == "6":
        insert_from_csv()
    elif choice == "7":
        filter_by_name_sorted()
    elif choice == "0":
        print(" Бағдарлама жабылды.")
        break
    else:
        print(" Қате таңдау. Қайта көріңіз.\n")

# Байланысты жабу
cur.close()
connect.close()
