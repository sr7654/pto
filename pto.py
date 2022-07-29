import sqlite3
import uuid

con = sqlite3.connect("pto.db")

def add_pto(person, description, from_date, to_date=""):
    id = uuid.uuid1()
    print(f"id: {id} person: {person} what: {description}")

add_pto("Sanford", "Germany trip", "2022-08-01", "2022-08-20")