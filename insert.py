import psycopg2
from config import load_config
def insert_user(name, phone, cur):
    if not phone.isdigit():
        return False
    sql_check = "SELECT id FROM phonebook WHERE name = %s"
    sql_insert = "INSERT INTO phonebook(name, phone) VALUES (%s, %s)"
    sql_update = "UPDATE phonebook SET phone = %s WHERE name = %s"

    cur.execute(sql_check, (name,))
    row = cur.fetchone()
    if row:
        cur.execute(sql_update, (phone, name))
    else:
        cur.execute(sql_insert, (name, phone))
    return True

def insert_console():
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                while True:
                    name = input("Name: ").strip()
                    if not name:
                        break
                    phone = input("Phone: ").strip()
                    insert_user(name, phone, cur)
            conn.commit()
    except Exception as e: pass

if __name__ == "__main__":
    insert_console()