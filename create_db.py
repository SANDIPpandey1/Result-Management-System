import sqlite3
def create_db():
    conn = sqlite3.connect('RMS.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid integer primary key autoincrement, name text, duration text, charges text, description text)")
    conn.commit()
create_db()
