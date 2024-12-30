#1. Tạo và Kết Nối với CSDL:
import sqlite3

conn = sqlite3.connect('product.db')
cursor = conn.cursor()

#2. Tạo Bảng product:
cursor.execute('''
    CREATE TABLE IF NOT EXISTS product (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Amount INTEGER NOT NULL
    )
''')
conn.commit()

#3. Phát Triển Các Chức Năng:
def display_products():
    cursor.execute('SELECT * FROM product')
    products = cursor.fetchall()
    if not products:
        print("Không có sản phẩm nào.")
    else:
        for product in products:
            print(product)

def add_product(name, price, amount):
    cursor.execute('''
        INSERT INTO product (Name, Price, Amount)
        VALUES (?, ?, ?)
    ''', (name, price, amount))
    conn.commit()
    print("Sản phẩm đã được thêm thành công.")

def search_product_by_name(name):
    cursor.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    result = cursor.fetchall()
    if not result:
        print("Không tìm thấy sản phẩm nào.")
    else:
        for product in result:
            print(product)

def update_product(product_id, price, amount):
    cursor.execute('''
        UPDATE product
        SET Price = ?, Amount = ?
        WHERE Id = ?
    ''', (price, amount, product_id))
    conn.commit()
    print("Thông tin sản phẩm đã được cập nhật thành công.")

def delete_product(product_id):
    cursor.execute('DELETE FROM product WHERE Id = ?', (product_id,))
    conn.commit()
    print("Sản phẩm đã được xóa thành công.")

#4. Tạo Menu Giao Diện Console:
def main():
    while True:
        print("\n===== Quản Lý Sản Phẩm =====")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")

        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            display_products()
        elif choice == '2':
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            amount = int(input("Nhập số lượng sản phẩm: "))
            add_product(name, price, amount)
        elif choice == '3':
            search_name = input("Nhập tên sản phẩm cần tìm kiếm: ")
            search_product_by_name(search_name)
        elif choice == '4':
            product_id = int(input("Nhập ID của sản phẩm cần cập nhật: "))
            price = float(input("Nhập giá mới: "))
            amount = int(input("Nhập số lượng mới: "))
            update_product(product_id, price, amount)
        elif choice == '5':
            product_id = int(input("Nhập ID của sản phẩm cần xóa: "))
            delete_product(product_id)
        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

#5. Kiểm Thử và Debug:
if __name__ == "__main__":
    main()
conn.close()



