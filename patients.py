from db_connection import connect_db

def add_patient():
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    phone = input("Enter phone: ")
    disease = input("Enter disease: ")

    query = """
    INSERT INTO patients
    (name, age, gender, phone, disease)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, age, gender, phone, disease)

    cursor.execute(query, values)
    db.commit()

    print("Patient added successfully!")

    cursor.close()
    db.close()


def view_patients():
    db = connect_db()

    if db is None:
        return

    cursor = db.cursor()

    cursor.execute("SELECT * FROM patients")

    for patient in cursor.fetchall():
        print(patient)

    cursor.close()
    db.close()