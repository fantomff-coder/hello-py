import pymysql

#Step 1: We will connect to the server
conn = pymysql.connect(
    host="localhost",
    user="root",                 #MySql username
    password=""                  #MySql password(empty by default in wamp)
    )
cursor=conn.cursor ()              #created a cursor object to execute sql queries(CREATE,SELECT,INSERT)

#Step 2: Creating database if it does not exists already
cursor.execute("CREATE DATABASE IF NOT EXISTS demoa")
print("Database 'demoa' is ready")  

#Step 3: Seleting the database which we want to use
conn.select_db("demoa")

#step 4: Creating table in database if does not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS students(
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(50),
age INT
)
 """)
print("Table 'students' is ready")

#Step 5: Inserting values in the table
cursor.execute("INSERT INTO students(name, age) VALUES(%s,%s)",("Alvin",19))
cursor.execute("INSERT INTO students(name, age) VALUES(%s,%s)",("Shreya",19))
conn.commit()                      #to confirm input values    
print("Data inserted")

#Step 6: To fetch and display data
cursor.execute("SELECT * FROM students;")
rows=cursor.fetchall()
for row in rows:
    print(row)

#Step 7: Close Connection
cursor.close()
conn.close()
