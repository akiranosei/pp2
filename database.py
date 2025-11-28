import sqlite3
def connect_db():
    return sqlite3.connect('snake_game.db')

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            level INTEGER,
            score INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_score (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            score INTEGER,
            level INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES user(id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Tables created (if they didn't exist already)")

def user_login():
    conn = connect_db()
    cursor = conn.cursor()
    username = input("Enter your username: ")
    cursor.execute("SELECT * FROM user WHERE username=?", (username,))
    user = cursor.fetchone()
    
    if user:
        user_id, username, level, score = user
        print(f"Welcome back, {username}! Current Level: {level}, Score: {score}")
    else:
        cursor.execute("INSERT INTO user (username, level, score) VALUES (?, ?, ?)", (username, 1, 0))
        conn.commit()
        user_id = cursor.lastrowid
        level = 1
        score = 0
        print(f"New user created: {username}")
    
    conn.close()
    return user_id, username, level, score


def save_game_state(user_id, score, level):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO user_score (user_id, score, level)
        VALUES (?, ?, ?)
    ''', (user_id, score, level))
    conn.commit()
    conn.close()
    print("Game state saved successfully!")
    

def get_all_user_scores():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT u.username, us.score, us.timestamp
        FROM user_score us
        JOIN user u ON us.user_id = u.id
        ORDER BY us.score DESC
    ''')
    
    all_scores = cursor.fetchall()
    conn.close()
    
    return all_scores



if __name__ == "__main__":
    create_tables()
    conn = sqlite3.connect('snake_game.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:", tables)
    conn.close()
