# import the new sqlite package
import sqlite3

# connect to the db we made
db = sqlite3.connect("database/student_marks.db")
# when I get data, also give me the field names
db.row_factory = sqlite3.Row

# Run a SELECT query on students
students = db.execute("SELECT * FROM Students").fetchall()

# Display the first students
for person in students:
    print(f"Firstname: {person['firstname']}")
    print(f"Lastname : {person['lastname']}")
    print(f"DOB      : {person['dob']}")