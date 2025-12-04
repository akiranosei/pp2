import psycopg2
from config import load_config

def search_contacts(pattern, limit=None, offset=None):
    sql = "SELECT id, name, phone FROM phonebook WHERE name ILIKE %s OR phone LIKE %s ORDER BY id"
    if limit is not None:
        sql += " LIMIT %s"
        if offset is not None:
            sql += " OFFSET %s"

    pattern_like = f"%{pattern}%"
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if limit is not None and offset is not None:
                cur.execute(sql, (pattern_like, pattern_like, limit, offset))
            elif limit is not None:
                cur.execute(sql, (pattern_like, pattern_like, limit))
            else:
                cur.execute(sql, (pattern_like, pattern_like))
            return cur.fetchall()

def show_all(limit=None, offset=None):
    sql = "SELECT id, name, phone FROM phonebook ORDER BY id"
    if limit is not None:
        sql += " LIMIT %s"
        if offset is not None:
            sql += " OFFSET %s"

    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if limit is not None and offset is not None:
                cur.execute(sql, (limit, offset))
            elif limit is not None:
                cur.execute(sql, (limit,))
            else:
                cur.execute(sql)
            return cur.fetchall()

def print_contacts(rows):
    if not rows:
        print("No contacts found.")
        return
    print(f"{'ID':<5} {'Name':<25} {'Phone':<20}")
    print("-" * 50)
    for row in rows:
        print(f"{row[0]:<5} {row[1]:<25} {row[2]:<20}")
    print()

def main():
    print("\nPhoneBook Menu")
    print("1 — Show all contacts")
    print("2 — Search by name or phone pattern")
    print("3 — Exit")

    choice = input("Enter your choice: ").strip()
    if choice == "1":
        limit = input("Enter limit (or leave empty for all): ").strip()
        offset = input("Enter offset (or leave empty for 0): ").strip()
        limit_val = int(limit) if limit.isdigit() else None
        offset_val = int(offset) if offset.isdigit() else 0
        rows = show_all(limit=limit_val, offset=offset_val)
        print_contacts(rows)
    elif choice == "2":
        pattern = input("Enter full or partial name/phone to search: ").strip()
        if pattern:
            limit = input("Enter limit (or leave empty for all): ").strip()
            offset = input("Enter offset (or leave empty for 0): ").strip()
            limit_val = int(limit) if limit.isdigit() else None
            offset_val = int(offset) if offset.isdigit() else 0
            rows = search_contacts(pattern, limit=limit_val, offset=offset_val)
            print_contacts(rows)
        else:
            print("Pattern cannot be empty.")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
