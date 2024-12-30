import sqlite3

path = "C:/Users/Admin/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab04/Data/product_1.db"
conn = sqlite3.connect(path)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS product (
    Id INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Amount INTEGER NOT NULL
               
               
)


''')

conn.commit()

#Hiển thị danh sách sản phẩm
def displays_product():
    cursor.execute("SELECT * FROM product")
    rows = cursor.fetchall()

    if rows:
        print("Danh sách sản phẩm")
        for row in rows:
            print(row)
    else:
        print("Không có sản phẩm")
#Thêm các sản phẩm vào bảng sản phẩm
def add_product():
    Name = input("Nhập tên sản phẩm:") 
    Price = float(input("Nhập đơn giá:"))
    Amount = int(input("Nhập số lượng:"))
    cursor.execute("INSERT INTO product (Name,Price,Amount) VALUES (?,?,?)",(Name,Price,Amount))
    conn.commit()
    print("Đã thêm sản phẩm")
#Tìm kiếm thông tin sản phẩm theo tên
def search_product():
    Name = input("Nhập sản phẩm cần tìm:")
    cursor.execute("SELECT * FROM product WHERE Name LIKE ?",('%'+Name+'%',))
    rows = cursor.fetchall()
    if rows:
        print("Danh sách sản phẩm")
        for row in rows:
            print(row)
    else:
        print("Không tìm thấy sản phẩm nào")    
#Cập nhật đơn giá và số lượng của mỗi sản phẩm theo id cụ thể
def update_product():
    product_Id = int(input("Nhập số thứ tự sản phẩm của bạn:"))
    Price = float(input("Nhập giá sản phẩm:"))
    Amount = int(input("Nhập số lượng sản phẩm:"))
    cursor.execute("UPDATE product SET Price = ?,Amount = ?,Price = ?",(Price,Amount,product_Id))
    conn.commit()
    print("Cập nhật sản phẩm thành công")   
#Xóa một sản phẩm theo id cụ thể
def delete_product():
    while True:
        product_id = int(input("Nhập id sản phẩm của bạn:"))
        cursor.execute("DELETE FROM product WHERE id = ?",(product_id,))
        conn.commit()
        print("Đã xóa sản phẩm thành công!")
        cont = input("Do you want to delete different product (y/n):")
        if cont.lower != 'y':
            break
#Main chính :))
def main():
    while True:
        print("Quản lí sản phẩm \n")
        print("1.Hiển thị sản phẩm")
        print("2.Thêm các sản phẩm vào bảng sản phẩm")
        print("3.Tìm kiếm thông tin sản phẩm theo tên")
        print("4.Cập nhật đơn giá và số lượng của mỗi sản phẩm theo mỗi id cụ thể")
        print("5.Xóa một sản phẩm theo id cụ thể")
        print("6. Thoát")

        choice = input("Nhập lựa chọn của bạn:")
        if choice == "1":
            displays_product()
        elif choice == "2":
            add_product()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ vui lòng chọn lại!!!")

if __name__ == "__main__":
    main()
conn.close()