import sqlite3

def get_db_connect():
    conn = sqlite3.connect("banglish_to_bangla_db.db")
    return conn
def init_db():
    conn = None
    try:
        conn = get_db_connect()
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS translations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            banglish TEXT UNIQUE NOT NULL,
            bangla TEXT NOT NULL
        )
        """)
        conn.commit()
    finally:
        if conn:
            conn.close()

init_db()
