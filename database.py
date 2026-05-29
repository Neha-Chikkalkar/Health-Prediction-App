import sqlite3

conn = sqlite3.connect("patients.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    dob TEXT,
    email TEXT,
    glucose REAL,
    haemoglobin REAL,
    cholesterol REAL,
    remarks TEXT
)
""")

conn.commit()


def add_patient(name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    cursor.execute("""
    INSERT INTO patients 
    (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, dob, email, glucose, haemoglobin, cholesterol, remarks))
    conn.commit()


def get_patients():
    cursor.execute("SELECT * FROM patients")
    return cursor.fetchall()


def update_patient(id, name, dob, email, glucose, haemoglobin, cholesterol, remarks):
    cursor.execute("""
    UPDATE patients
    SET name=?, dob=?, email=?, glucose=?, haemoglobin=?, cholesterol=?, remarks=?
    WHERE id=?
    """, (name, dob, email, glucose, haemoglobin, cholesterol, remarks, id))
    conn.commit()


def delete_patient(id):
    cursor.execute("DELETE FROM patients WHERE id=?", (id,))
    conn.commit()