import sqlite3

try:
    con = sqlite3.connect("pto.db")
    cur = con.cursor()

    # drop ptos table
    sql = "DROP TABLE ptos;"
    cur.execute(sql)
    con.commit()

except sqlite3.Error as error:
    print("Error dropping table: ", error)

try:
    # drop sites table
    sql = "DROP TABLE sites;"
    cur.execute(sql)
    con.commit()

    cur.close()

except sqlite3.Error as error:
    print("Error dropping table: ", error)
finally:
    if con:
        con.close()
        print("Success. Database dropped.")