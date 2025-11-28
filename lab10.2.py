import sqlite3
import csv

DB_NAME = "phonebook1.db"
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()
    print("Table created successfully.")

def insert_from_console():
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO phonebook1 (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Inserted successfully!")
    except sqlite3.IntegrityError:
        print("Error: phone already exists.")
    conn.close()

def insert_from_csv(filepath):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    with open(filepath, mode="r", newline="") as file:
        reader = csv.reader()
        for row in reader:
            name, phone = row
            try:
                cur.execute("INSERT INTO phonebook1 (name, phone) VALUES (?, ?)", (name, phone))
            except sqlite3.IntegrityError:
                print(f"Skipping duplicate phone: {phone}")

    conn.commit()
    conn.close()
    print("CSV upload completed successfully.")

def update_phone(old_phone, new_phone):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE phonebook1 SET phone=? WHERE phone=?", (new_phone, old_phone))
    conn.commit()
    conn.close()
    print("Phone updated.")


def update_name(old_name, new_name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE phonebook1 SET name=? WHERE name=?", (new_name, old_name))
    conn.commit()
    conn.close()
    print("Name updated.")

def query_all():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook1")
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)


def query_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook1 WHERE name LIKE ?", (f"%{name}%",))
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)


def query_by_phone(phone):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM phonebook1 WHERE phone=?", (phone,))
    rows = cur.fetchall()
    conn.close()
    for row in rows:
        print(row)

def delete_by_name(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook1 WHERE name=?", (name,))
    conn.commit()
    conn.close()
    print("Deleted by name.")


def delete_by_phone(phone):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM phonebook1 WHERE phone=?", (phone,))
    conn.commit()
    conn.close()
    print("Deleted by phone.")

def menu():
    create_table()
    while True:
        print("""
==== PHONEBOOK MENU ====
1. Insert from console
2. Insert from CSV
3. Update phone
4. Update name
5. Query all
6. Query by name
7. Query by phone
8. Delete by name
9. Delete by phone
0. Exit
""")
        choice = input("Choose option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            filepath = input("C:/Users.User/Downloads/phonb")
            insert_from_csv(filepath)
        elif choice == "3":
            old = input("Old phone: ")
            new = input("New phone: ")
            update_phone(old, new)
        elif choice == "4":
            old = input("Old name: ")
            new = input("New name: ")
            update_name(old, new)
        elif choice == "5":
            query_all()
        elif choice == "6":
            name = input("Name filter: ")
            query_by_name(name)
        elif choice == "7":
            phone = input("Phone: ")
            query_by_phone(phone)
        elif choice == "8":
            name = input("Name to delete: ")
            delete_by_name(name)
        elif choice == "9":
            phone = input("Phone to delete: ")
            delete_by_phone(phone)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
