import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/memory.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sample(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL                          
)
''')

#tHÊM dữ liệu vào bảng
cursor.execute("INSERT INTO sample (name) VALUES (?)", ('Alice',))
cursor.execute("INSERT INTO sample (name) VALUES (?)",('Bob',))

cursor.execute("SELECT * FROM sample")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()