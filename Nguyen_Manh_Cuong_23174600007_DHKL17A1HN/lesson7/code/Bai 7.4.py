import tkinter as tk

def submit():
    name = entry_name.get()
    student_id = entry_student_id.get()
    password = entry_password.get()

    print(f"Tên sinh viên: {name}")
    print(f"ID sinh viên: {student_id}")
    print(f"Mật khẩu: {password}")

window = tk.Tk()
window.title("Nhập thông tin sinh viên")

label_name = tk.Label(window, text="Tên sinh viên:")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_student_id = tk.Label(window, text="ID sinh viên:")
label_student_id.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_student_id = tk.Entry(window)
entry_student_id.grid(row=1, column=1, padx=10, pady=5)

label_password = tk.Label(window, text="Mật khẩu:")
label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

entry_password = tk.Entry(window, show="*")  
entry_password.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(window, text="Gửi", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

window.mainloop()
