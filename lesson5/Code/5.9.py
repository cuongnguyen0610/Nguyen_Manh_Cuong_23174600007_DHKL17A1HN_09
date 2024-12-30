import sqlite3
path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/region.db"


conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE region (
    Region_ID INTEGER PRIMARY KEY,
    Region_Name TEXT NOT NULL
)

''')

cursor.execute('INSERT INTO region (Region_ID,Region_Name) VALUES (1,"European")')
cursor.execute("INSERT INTO region (Region_ID,Region_Name) VALUES (2,'Americas')")
cursor.execute('INSERT INTO region (Region_ID,Region_Name) VALUES (3,"Asia")')
cursor.execute('INSERT INTO region (Region_ID,Region_Name) VALUES (4,"Middle East and Africa")')

conn.commit()

cursor.execute("SELECT * FROM region")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()