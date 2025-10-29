import tkinter
from tkinter import messagebox
import pymysql

# Initialize DB and table
def init_db():
    db = pymysql.connect(user='root', password='', host='localhost')
    cur = db.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS syitademo")
    db.select_db("syitademo")

    # Create table only if it doesn't exist
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student(
        fn VARCHAR(50),
        ln VARCHAR(50),
        age INT,
        sex VARCHAR(10),
        PERCENTAGE FLOAT
    )
    """)
    db.commit()
    db.close()

# Insert record
def put():
    try:
        db = pymysql.connect(user='root', password='', host='localhost', db='syitademo')
        cur = db.cursor()
        query = "INSERT INTO student (fn, ln, age, sex, PERCENTAGE) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(query, (fn.get(), ln.get(), age.get(), sex.get(), percentage.get()))
        db.commit()
        messagebox.showinfo("Info", "Record inserted successfully")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        db.close()

# Display all records
def get():
    try:
        db = pymysql.connect(user='root', password='', host='localhost', db='syitademo')
        cur = db.cursor()
        cur.execute("SELECT * FROM student")
        results = cur.fetchall()
        if results:
            print("All records:")
            for row in results:
                print(row)
        else:
            print("No records found.")
            messagebox.showinfo("Info", "No records found.")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        db.close()

# Delete record by percentage
def dele():
    try:
        db = pymysql.connect(user='root', password='', host='localhost', db='syitademo')
        cur = db.cursor()
        query = "DELETE FROM student WHERE PERCENTAGE = %s"
        cur.execute(query, (IENTRY.get(),))
        db.commit()
        messagebox.showinfo("Info", "Record deleted successfully")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        db.close()

# Update age by percentage
def upd():
    try:
        db = pymysql.connect(user='root', password='', host='localhost', db='syitademo')
        cur = db.cursor()
        query = "UPDATE student SET age = 20 WHERE PERCENTAGE = %s"
        cur.execute(query, (IENTRY.get(),))
        db.commit()
        messagebox.showinfo("Info", "Record updated successfully")
    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        db.close()

# Initialize database
init_db()

# Tkinter GUI
root = tkinter.Tk()
root.title("Student Data CRUD")

# Labels and Entries
tkinter.Label(root, text='First Name').grid(row=0, column=0)
tkinter.Label(root, text='Last Name').grid(row=1, column=0)
tkinter.Label(root, text='Age').grid(row=2, column=0)
tkinter.Label(root, text='Sex').grid(row=3, column=0)
tkinter.Label(root, text='Percentage').grid(row=4, column=0)

fn = tkinter.Entry(root, width=15); fn.grid(row=0, column=1)
ln = tkinter.Entry(root, width=15); ln.grid(row=1, column=1)
age = tkinter.Entry(root, width=15); age.grid(row=2, column=1)
sex = tkinter.Entry(root, width=15); sex.grid(row=3, column=1)
percentage = tkinter.Entry(root, width=15); percentage.grid(row=4, column=1)

# Buttons
tkinter.Button(root, text="Insert", command=put).grid(row=5, column=0, pady=5)
tkinter.Button(root, text="Display", command=get).grid(row=5, column=1, pady=5)

tkinter.Label(root, text='Percentage for Update/Delete').grid(row=6, column=0)
IENTRY = tkinter.Entry(root, width=15); IENTRY.grid(row=6, column=1)

tkinter.Button(root, text="Update", command=upd).grid(row=7, column=0, pady=5)
tkinter.Button(root, text="Delete", command=dele).grid(row=7, column=1, pady=5)

root.mainloop()
