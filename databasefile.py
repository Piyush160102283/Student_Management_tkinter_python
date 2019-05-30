import sqlite3
# import tkguifile as tgf
connection = sqlite3.connect("student_details.db")
print("Database opened successfully")


connection.execute("CREATE TABLE IF NOT EXISTS Student (STUDENT_NAME TEXT, STUDENT_ROLLNO INTEGER, STUDENT_SAPID INTEGER, STUDENT_COLLEGE TEXT, STUDENT_ADDRESS TEXT, STUDENT_EMAIL TEXT, STUDENT_PHONEN0 INTEGER);")

# NAME = tgf.name_field.get()
# ROLLNO = tgf.rollno_field.get()
# SAPID = tgf.sapid_field.get()
# COLLEGE = tgf.college_field.get()
# ADDRESS = tgf.address_field.get()
# EMAIL = tgf.email_field.get()
# PHONE = tgf.mobileno_field.get()

def insert_data(n,r,s,c,a,e,m):

    connection.execute("INSERT INTO Student VALUES ( '" + n + "' , " + r + " , " + s + " , '" + c + "' ,  '" + a + "', '" + e + "' ,  " + m + ");")
    connection.commit()

def showall_data():
    cursor = connection.execute("SELECT * FROM Student ;")
    for row in cursor:
        print("Student No-1 :",row)
        print(row[0], end="")
        print(row[1], end="")
        print(row[2], end="")
        print(row[3], end="")
        print(row[4], end="")
        print(row[5], end="")
        print(row[6], end="")

def show_data(r):
    cursor = connection.execute("SELECT * FROM Student where STUDENT_ROLLNO= '"+r+"';")
    for row in cursor:
        print("Student Name is : ", row[0])
        print("Student Roll No is ", row[1])
        print("Student Sap ID is ", row[2])
        print("Student College is : ", row[3])
        print("Student Address is ", row[4])
        print("Student Email ID is ", row[5])
        print("Student Phone No is ", row[6])
def delete_data(r):
    connection.execute("DELETE FROM Student WHERE STUDENT_ROLLNO= "+r+" ;")
    connection.commit()
