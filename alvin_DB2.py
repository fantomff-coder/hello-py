import pymysql
import tkinter
from tkinter import messagebox

#initialization of database and table
def init_db():
    try:
        db = pymysql.connect(
             user="root",
             password="",
             host="localhost",
             )
        cur = db.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS demob")
        db.select_db("demob")

        cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        surname VARCHAR(50),
        age INT,
        sex VARCHAR(10),
        percentage FLOAT)
        """)
        db.commit()
    except pymysql.MySQLError as e:
        messagebox.showerror("Database error",str(e))
    finally:
        db.close()

#insertion of record in table
def put():
    try:
        db = pymysql.connect(user="root", password="", host="localhost", db="demob")
        cur = db.cursor()
        query = "INSERT INTO student(name,surname,age,sex,percentage) VALUES(%s,%s,%s,%s,%s)"
        cur.execute(query,(name.get(),surname.get(),age.get(),sex.get(),percentage.get()))
        db.commit()
        messagebox.showinfo("Success !", "Record inserted in database successfully")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database error",str(e))
    finally:
        db.close()

#Display all records
def get():
    try:
        db = pymysql.connect(user="root", password="", host="localhost", db="demob")
        cur = db.cursor()
        cur.execute("SELECT * FROM student")
        result = cur.fetchall()
        if result:
            print("All records:")
            for row in result:
                print(row)
                messagebox.showinfo("Data Retrieved", "\n".join(str(r) for r in result))
        else:
            print("No records found")
            messagebox.showinfo("Info", "No records found")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error",str(e))
    finally:
         db.commit()
         db.close()

#Delete record by percentage         
def dele():
    try:
        db = pymysql.connect(user="root", password="", host="localhost", db="demob")
        cur = db.cursor()
        query = "DELETE FROM student WHERE percentage = %s"
        cur.execute(query,(IENTRY.get(),))
        db.commit()
        messagebox.showinfo("Info", "Record Deleted successfully")
    except pymysql.MySQLError as e:
         messagebox.showerror("Database Error",str(e))
    finally:
         db.close()

#Update age by percentage
def upd():
    try:
        db = pymysql.connect(user="root", password="", host="localhost", db="demob")
        cur = db.cursor()
        query = "UPDATE student SET age=20 WHERE percentage = %s"
        cur.execute(query,(IENTRY.get(),))
        db.commit()
        messagebox.showinfo("Info", "Record Updated successfully")
    except pymysql.MySQLError as e:
         messagebox.showerror("Database Error",str(e))
    finally:
         db.close()

#Initialize database
init_db()

#Tkinter GUI
root = tkinter.Tk()
root.title("Student Data CRUD") 

#labels and entries
tkinter.Label(root, text = "First Name:").grid(row=0, column=0)        
name = tkinter.Entry(root); name.grid(row=0, column=1)        
tkinter.Label(root, text = "Last Name:").grid(row=1, column=0)    
surname = tkinter.Entry(root); surname.grid(row=1, column=1)
tkinter.Label(root, text = "Age:").grid(row=2, column=0)
age = tkinter.Entry(root); age.grid(row=2, column=1)
tkinter.Label(root, text="Sex:").grid(row=3, column=0)
sex = tkinter.Entry(root); sex.grid(row=3, column=1)
tkinter.Label(root, text="Percentage:").grid(row=4, column=0)
percentage = tkinter.Entry(root); percentage.grid(row=4, column=1)

#Buttons
tkinter.Button(root, text = "Insert", command=put).grid(row=5, column=0, pady=5)
tkinter.Button(root, text = "Display", command=get).grid(row=5, column=1, pady=5)

#label & entry
tkinter.Label(root, text="percentage for update/delete").grid(row=6, column=0)
IENTRY = tkinter.Entry(root, width=15); IENTRY.grid(row=6, column=1)

#buttons
tkinter.Button(root, text = "Update", command=upd).grid(row=7, column=0, pady=5)
tkinter.Button(root, text = "Delete", command=dele).grid(row=7, column=1, pady=5)

root.mainloop()
