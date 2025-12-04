import psycopg2
from config import load_config

def delete_by_name(name):
    sql = "DELETE FROM phonebook WHERE name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                deleted_count = cur.rowcount
            conn.commit()
        print(f"Deleted {deleted_count} contact(s) with name: {name}")
    except Exception as e:
        print("Error deleting by name:", e)

def delete_by_phone(phone):
    sql = "DELETE FROM phonebook WHERE phone = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (phone,))
                deleted_count = cur.rowcount
            conn.commit()
        print(f"Deleted {deleted_count} contact(s) with phone: {phone}")
    except Exception as e:
        print("Error deleting by phone:", e)

def main():
    while True:
        print("\nDelete Menu")
        print("1 — Delete by name")
        print("2 — Delete by phone")
        print("3 — Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            name = input("Enter the name to delete: ").strip()
            if name:
                delete_by_name(name)
            else:
                print("Name cannot be empty.")
        elif choice == '2':
            phone = input("Enter the phone to delete: ").strip()
            if phone:
                delete_by_phone(phone)
            else:
                print("Phone cannot be empty.")
        elif choice == '3':
            print("Exiting delete menu.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()