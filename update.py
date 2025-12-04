import psycopg2
from config import load_config
def insert_or_update_user(name, phone):
    sql_check = "SELECT id, phone FROM phonebook WHERE name = %s"
    sql_insert = "INSERT INTO phonebook(name, phone) VALUES (%s, %s)"
    sql_update = "UPDATE phonebook SET phone = %s WHERE name = %s"
    config = load_config()
    message = ""

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql_check, (name,))
                row = cur.fetchone()
                if row:
                    cur.execute(sql_update, (phone, name))
                    message = f"Updated phone for {name} to {phone}."
                else:
                    cur.execute(sql_insert, (name, phone))
                    message = f"Inserted new user: {name} with phone {phone}."
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        message = f"Operation failed: {error}"

    return message

def main():
    print("Phonebook Update")
    name = input("Enter name: ").strip()
    if not name:
        print("Name can't be empty.")
        return
    phone = input("Enter phone: ").strip()
    if not phone.isdigit():
        print("Phone must be digits only.")
        return
    result = insert_or_update_user(name, phone)
    print(result)

if __name__ == "__main__":
    main()