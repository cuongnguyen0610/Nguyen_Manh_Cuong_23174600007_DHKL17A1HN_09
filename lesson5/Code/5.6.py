import sqlite3

# Kết nối tới cơ sở dữ liệu
conn = sqlite3.connect('C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/employees.db')

# Tạo một con trỏ để thực hiện các lệnh SQL
cursor = conn.cursor()

# Truy vấn đếm số bản ghi trong bảng
cursor.execute('SELECT COUNT(*) FROM employees')
record_count = cursor.fetchall()[0]

# Hiển thị số lượng bản ghi
print(f"Số lượng bản ghi trong bảng 'employees' là: {record_count}")

# Đóng kết nối
conn.close()
