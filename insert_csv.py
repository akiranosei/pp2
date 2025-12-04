import psycopg2, csv
from config import load_config

def insert_from_csv(filename):
    sql = "INSERT INTO phonebook (name, phone) VALUES (%s, %s)"
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(filename, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file, delimiter=',')
                    header = next(reader, None)
                    for row in reader:
                        if len(row) < 2:
                            continue
                        name = row[0].strip()
                        phone = row[1].strip()
                        cur.execute(sql, (name, phone))
            conn.commit()
        print("CSV data uploaded successfully.")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except Exception as e:
        print("CSV insert error:", e)

if __name__ == "__main__":
    insert_from_csv(r"C:\Users\User\Downloads\phonb.csv")
