import sqlite3

try:
    con = sqlite3.connect("pto.db")
    cur = con.cursor()

    # Truncate ptos
    sql = "DELETE FROM ptos;"
    cur.execute(sql)
    con.commit()

    # Truncate sites
    sql = "DELETE FROM sites;"
    cur.execute(sql)
    con.commit()

    cur.close()

except sqlite3.Error as error:
    print("Error truncating table: ", error)
finally:
    if con:
        con.close()
        print("Success. Tables truncated")