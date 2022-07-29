import sqlite3

con = sqlite3.connect("pto.db")
cur = con.cursor()

cur.execute('''CREATE TABLE ptos
               (id text, person text, from_date text, to_date text, description text)''')
con.commit()
con.close()