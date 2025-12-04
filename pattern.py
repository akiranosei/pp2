import psycopg2
from config import load_config

def search_contacts(pattern):
    sql = """
        SELECT id, name, phone
        FROM phonebook
        WHERE name ILIKE %s OR phone LIKE %s
        ORDER BY id
    """
    pattern_like = f"%{pattern}%"
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (pattern_like, pattern_like))
                results = cur.fetchall()
                return results
    except Exception as e:
        print("Error searching contacts:", e)
        return []

def main():
    while True:
        print("1 — Search by pattern")
        print("2 — Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            pattern = input("Enter pattern (part of name or phone): ").strip()
            contacts = search_contacts(pattern)
            if contacts:
                print("\nFound contacts:")
                for c in contacts:
                    print(f"ID: {c[0]}, Name: {c[1]}, Phone: {c[2]}")
            else:
                print("No contacts found matching that pattern.")
        elif choice == '2':
            print("Exiting search menu.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
