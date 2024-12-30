import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/version.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute("SELECT SQLITE_VERSION()")
version = cursor.fetchone()

print(f"Phiên bản SQL hiện tại:{version[0]}")
conn.close()

