import sqlite3

def check_credentials(username, password) -> bool:
    # Внимание: Этот код уязвим для SQL-инъекций и только для отладки!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("Исполняемый SQL-запрос:", query)  # Вывод запроса для проверки инъекции
    conn = sqlite3.connect('vulnerable.db')
    cursor = conn.cursor()
    cursor.execute(query)
    
    user = cursor.fetchone()
    conn.close()
    
    return user is not None


def init_db():
    try:
        conn = sqlite3.connect('vulnerable.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', 'password123'))
        conn.commit()
        print("Таблица 'users' создана или уже существует.")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)
    finally:
        conn.close()