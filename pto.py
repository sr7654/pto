import sqlite3
import uuid
from datetime import datetime

con = sqlite3.connect("pto.db")
date_format_storage = "%Y-%m-%d"

# Register a site
def register_site(site_name):
    try:
        cur = con.cursor()
        sql = "SELECT count(*) FROM sites WHERE site = ?;"
        data = (site_name)
        cur.execute(sql, data)
        con.commit()
    except sqlite3.Error as error:
            return f"Error checking existing site: {error}"

    try:
        sql = "INSERT INTO sites(site) VALUES(?, ?);"
        todays_date = datetime.today()
        data = (site_name, todays_date)
        cur.execute(sql, data)
        con.commit()
        cur.close()
        return site_name
    except sqlite3.Error as error:
        return f"Error inserting site: {error}"

# Add a new PTO request
def add_pto(site, person, description, from_date, to_date=None):
    # generate id
    id = str(uuid.uuid1())

    # validate and convert dates
    from_date_formatted = ""
    to_date_formatted = ""
    try:
        from_date_formatted = datetime.strptime(from_date, date_format_storage)
    except ValueError:
        return f"Error adding PTO: from date is not in a date format: {from_date}"

    if not to_date:
        # default the to date to from date if empty
        to_date_formatted = from_date_formatted
    else:
        try:
            to_date_formatted = datetime.strptime(to_date, date_format_storage)
        except ValueError:
            return f"Error adding PTO: to date is not in a date format: {to_date}"

    # add to database
    try:
        cur = con.cursor()
        sql = "INSERT INTO ptos(id, site, person, from_date, to_date, description) VALUES(?, ?, ?, ?, ?, ?);"
        data = (id, site, person, from_date_formatted, to_date_formatted, description)
        cur.execute(sql, data)
        con.commit()
        cur.close()
        return id
    except sqlite3.Error as error:
        return f"Error adding PTO: {error}"

# View PTO: returns a list of upcoming PTO
def view_pto():
    cur = con.cursor()
    sql = "SELECT * FROM ptos;"
    cur.execute(sql)
    records = "Upcoming PTO:\n"
    for row in cur.fetchall():
        if row[3] == row[4]:
            totext = ""
        else:
            totext = " to " + row[4][0:10]
        records += row[2] + " " + row[3][0:10] + totext + ": " + row[5] + "\n"
    cur.close()
    return records