import tkinter as tk
from PIL import Image, ImageTk

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Chương trình xem ảnh")

try:
    # Mở và thay đổi kích thước ảnh
    image = Image.open("oto.png")
    new_size = (400, 400)
    image = image.resize(new_size, Image.Resampling.LANCZOS)  # Sử dụng Resampling.LANCZOS thay vì ANTIALIAS

    # Chuyển ảnh sang định dạng Tkinter
    img = ImageTk.PhotoImage(image)

    # Tạo widget Label để hiển thị ảnh
    label = tk.Label(window, image=img)
    label.image = img  # Lưu tham chiếu để tránh bị xóa bởi garbage collector
    label.pack()

    # Chạy vòng lặp chính
    window.mainloop()

except FileNotFoundError:
    print("Không tìm thấy tệp ảnh 'oto.png'. Vui lòng kiểm tra lại đường dẫn.")
