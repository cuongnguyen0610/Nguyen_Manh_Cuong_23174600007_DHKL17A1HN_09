import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/user.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name;")
tables = cursor.fetchall()

print(f"Cơ sở dữ liệu {path} chứa các bảng sau:")
for table in tables:
    print(f"-{table[0]}")

conn.close()
