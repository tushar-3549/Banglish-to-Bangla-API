from database import get_db_connect
import sqlite3

def get_translation_by_id(id: int):
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, banglish, bangla FROM translations WHERE id = ?", (id,))
        result = cur.fetchone()
        return result

def get_translation_by_banglish(banglish: str):
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, banglish, bangla FROM translations WHERE banglish = ?", (banglish,))
        result = cur.fetchone()
        return result

def add_translation(banglish: str, bangla: str):
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("INSERT OR IGNORE INTO translations (banglish, bangla) VALUES (?, ?)", (banglish, bangla))

def update_translation(id: int, new_banglish: str, new_bangla: str):
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("UPDATE translations SET banglish = ?, bangla = ? WHERE id = ?", (new_banglish, new_bangla, id))

def delete_translation(id: int):
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM translations WHERE id = ?", (id,))

def get_all_translations():
    with get_db_connect() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM translations")
        results = cur.fetchall()
    return [{"id": row[0], "banglish": row[1], "bangla": row[2]} for row in results]