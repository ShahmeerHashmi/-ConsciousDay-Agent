import sqlite3

def init_db():
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        journal TEXT,
        dream TEXT,
        intention TEXT,
        priorities TEXT,
        reflection TEXT,
        strategy TEXT
    )''')
    conn.commit()
    conn.close()

def save_entry(date, journal, dream, intention, priorities, result):
    conn = sqlite3.connect("entries.db")
    c = conn.cursor()
    c.execute("INSERT INTO entries (date, journal, dream, intention, priorities, reflection, strategy) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (str(date), journal, dream, intention, priorities, result["reflection"], result["strategy"]))
    conn.commit()
    conn.close()
    
    # ✅ Add this line for debug confirmation
    print(f"[✅] Entry for {date} saved to SQLite.")