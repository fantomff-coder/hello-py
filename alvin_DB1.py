import pymysql
import tkinter
from tkinter import messagebox

def get():
    try:
        #connect to server without selecting a database
        db = pymysql.connect(
            host='localhost',
            user='root',
            password=''
            )
        cur=db.cursor()
        
        #Creating a database if not exists
        cur.execute('CREATE DATABASE IF NOT EXISTS demob')
        db.select_db("demob")                       
        
        #Creating a table in database if not exists
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS students(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(50),
                    surname VARCHAR(50),
                    age INT,
                    sex VARCHAR(10),
                    percentage FLOAT
                    )
                    ''')
        db.commit()

        #Parameterized query to prevent sql injection
        query = "SELECT * FROM students WHERE percentage = %s"
        cur.execute(query,(IENTRY.get(),))

        results = cur.fetchall()
        if results:
            for id, name, surname, age, sex, percentage in results:
                print(f"Name: {name}, Surname: {surname}, Age: {age}, sex: {sex}, Percentage: {percentage}")
        else:
            print("No record found")
            messagebox.showinfo("Results","No records found")

    except pymysql.MySQLError as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        cur.close()
        db.close()
        

#Tkinter GUI
root = tkinter.Tk()
root.title("Search Data")
tkinter.Label(root,text="Percentage").grid(row=0, column=0, padx=5, pady=5)        
IENTRY = tkinter.Entry(root, width=10)
IENTRY.grid(row=0, column=1, padx=5, pady=5)
tkinter.Button(root, text="Search", command = get).grid(row=0, column=2, padx=5, pady=5)
root.mainloop()





















