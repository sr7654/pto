import sqlite3

try:
    con = sqlite3.connect("pto.db")
    cur = con.cursor()

    # Create sites table
    sql = '''CREATE TABLE sites (
            site text PRIMARY KEY,
            registered_date datetime);'''

    cur.execute(sql)
    con.commit()
    print("Created sites table.")

    # Create ptos table
    sql = '''CREATE TABLE ptos (
            id text PRIMARY KEY,
            site text,
            person TEXT NOT NULL,
            from_date text NOT NULL,
            to_date text NOT NULL,
            description text NOT NULL,
            FOREIGN KEY (site) REFERENCES sites(site));'''

    cur.execute(sql)
    con.commit()
    print("Created ptos table.")

    cur.close()

except sqlite3.Error as error:
    print("Error creating database: ", error)
finally:
    if con:
        con.close()
        print("Success. Database tables created.")