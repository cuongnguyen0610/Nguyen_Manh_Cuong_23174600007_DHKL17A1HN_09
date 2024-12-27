import sqlite3
path = 'C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/product.db'
conn = sqlite3.connect(path)
cursor = conn.cursor()

# Tạo bảng 'product' nếu chưa tồn tại
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        amount INTEGER NOT NULL
    )
''')

# Commit và đóng kết nối
conn.commit()
conn.close()

import sqlite3

# Hàm hiển thị danh sách sản phẩm
def show_products():
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    print("\nDanh sách sản phẩm:")
    for product in products:
        print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    conn.close()

# Hàm thêm sản phẩm mới
def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    amount = int(input("Nhập số lượng sản phẩm: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO product (name, price, amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    conn.close()
    print("Sản phẩm đã được thêm thành công!")

# Hàm tìm kiếm sản phẩm theo tên
def search_product():
    name = input("Nhập tên sản phẩm cần tìm: ")
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM product WHERE name LIKE ?', ('%' + name + '%',))
    products = cursor.fetchall()
    if products:
        print("\nKết quả tìm kiếm:")
        for product in products:
            print(f"ID: {product[0]}, Tên: {product[1]}, Giá: {product[2]}, Số lượng: {product[3]}")
    else:
        print("Không tìm thấy sản phẩm!")
    conn.close()

# Hàm cập nhật thông tin sản phẩm theo ID
def update_product():
    product_id = int(input("Nhập ID sản phẩm cần cập nhật: "))
    new_price = float(input("Nhập giá mới: "))
    new_amount = int(input("Nhập số lượng mới: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE product SET price = ?, amount = ? WHERE id = ?', (new_price, new_amount, product_id))
    conn.commit()
    conn.close()
    print("Thông tin sản phẩm đã được cập nhật!")

# Hàm xóa sản phẩm theo ID
def delete_product():
    product_id = int(input("Nhập ID sản phẩm cần xóa: "))
    
    conn = sqlite3.connect('product.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM product WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()
    print("Sản phẩm đã được xóa!")

# Menu chương trình
def menu():
    while True:
        print("\n----- Menu -----")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Tìm kiếm sản phẩm theo tên")
        print("4. Cập nhật thông tin sản phẩm")
        print("5. Xóa sản phẩm")
        print("6. Thoát")
        
        choice = input("Chọn chức năng: ")
        
        if choice == '1':
            show_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            search_product()
        elif choice == '4':
            update_product()
        elif choice == '5':
            delete_product()
        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng thử lại.")

# Chạy chương trình
menu()

