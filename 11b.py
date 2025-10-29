import pymysql
import tkinter
from tkinter import messagebox

def get():
    try:
        # Connect to MySQL without specifying a database first
        db = pymysql.connect(
            user='root',
            password='',
            host='localhost'
        )
        cur = db.cursor()

        # Create database if it doesn't exist
        cur.execute("CREATE DATABASE IF NOT EXISTS syitademo;")
        db.select_db("syitademo")

        # Create student table if it doesn't exist
        cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            fn VARCHAR(50),
            ln VARCHAR(50),
            age INT,
            sex VARCHAR(10),
            PERCENTAGE FLOAT
        )
        """)

        # Parameterized query to prevent SQL injection
        query = "SELECT * FROM student WHERE PERCENTAGE = %s"
        cur.execute(query, (IENTRY.get(),))

        results = cur.fetchall()
        if results:
            for fn, ln, age, sex, percentage in results:
                print(f"fn: {fn}, ln: {ln}, age: {age}, sex: {sex}, percentage: {percentage}")
        else:
            print("No records found.")
            messagebox.showinfo("Result", "No records found.")

        db.commit()

    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))
    finally:
        db.close()

# Tkinter GUI
root = tkinter.Tk()
root.title("Search Data")

tkinter.Label(root, text="Percentage").grid(row=0, column=0, padx=5, pady=5)
IENTRY = tkinter.Entry(root, width=10)
IENTRY.grid(row=0, column=1, padx=5, pady=5)

tkinter.Button(root, text="Search", command=get).grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
