import sqlite3
def create_db():
    conn = sqlite3.connect('RMS.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid integer primary key autoincrement, name text, duration text, charges text, description text)")
    conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll integer primary key , name text, email text, gender text, dob text, contact text, admission text, course txt, state text, City text, Address text)")
    conn.commit()
    conn.close()
create_db()
