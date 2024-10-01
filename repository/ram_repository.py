import sqlite3
import time

from models.ram_model import RAMStats

class RAMRepository:
    DB_FILE = 'ram_usage.db'

    def __init__(self):
        self._initialize_db()

    def _initialize_db(self):
        conn = sqlite3.connect(self.DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ram_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_mb REAL,
                used_mb REAL,
                free_mb REAL,
                timestamp TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def insert_ram_stats(self, total_mb: float, used_mb: float, free_mb: float):
        conn = sqlite3.connect(self.DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ram_stats (total_mb, used_mb, free_mb, timestamp) 
            VALUES (?, ?, ?, ?)
        ''', (total_mb, used_mb, free_mb, time.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        conn.close()

    def get_last_n_stats(self, n: int):
        conn = sqlite3.connect(self.DB_FILE)
        cursor = conn.cursor()
        cursor.execute(f"SELECT total_mb, used_mb, free_mb, timestamp FROM ram_stats ORDER BY id DESC LIMIT {n}")
        data = cursor.fetchall()
        conn.close()
        return [RAMStats(*row) for row in data]
