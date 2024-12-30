import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/user.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER
               
)


''')
conn.commit()

print("Cơ sở dữ liệu user.db đã được tạo và bảng user đã sẵn sàng")

conn.close()