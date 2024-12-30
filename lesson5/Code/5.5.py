import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/employees.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    salary REAL NOT NULL           
    )


''')

cursor.execute("INSERT INTO employees (name,position,salary) VALUES (?,?,?)",('Alice','Manager',10000))
cursor.execute("INSERT INTO employees (name,position,salary) VALUES (?,?,?)",('Alicu','Developer',10000))
cursor.execute("INSERT INTO employees (name,position,salary) VALUES (?,?,?)",('Alica','Anaylst',10000))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Danh sách nhân viên:")
for row in rows:
    print(row)

conn.close()
