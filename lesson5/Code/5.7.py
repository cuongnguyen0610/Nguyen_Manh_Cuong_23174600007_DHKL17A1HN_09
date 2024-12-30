import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/employees.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

new_salary = 80000
cursor.execute('UPDATE employees SET salary = ?',(new_salary,))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()