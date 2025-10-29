import pymysql

# Step 1: Connect to MySQL (without specifying DB)
conn = pymysql.connect(
    host="localhost",
    user="root",        # Your MySQL username
    password=""         # Your MySQL password (default is empty in WAMP)
)

cursor = conn.cursor()

# Step 2: Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS demoa;")
print("Database 'demoa' is ready.")

# Step 3: Connect to the newly created database
conn.select_db("demoa")

# Step 4: Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")
print("Table 'students' is ready.")

# Step 5: Insert sample data
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Gaurav", 22))
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Rimsy", 21))
conn.commit()
print("Sample data inserted.")

# Step 6: Fetch and display data
cursor.execute("SELECT * FROM students;")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Step 7: Close connection
cursor.close()
conn.close()
