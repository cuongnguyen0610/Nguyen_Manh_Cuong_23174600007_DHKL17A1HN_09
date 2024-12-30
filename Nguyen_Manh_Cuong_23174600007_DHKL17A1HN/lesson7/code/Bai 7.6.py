import tkinter as tk

def dao_nguoc_chuoi(chuoi):
    chuoi_dao_nguoc = ''
    for ky_tu in chuoi:
        chuoi_dao_nguoc = ky_tu + chuoi_dao_nguoc
    return chuoi_dao_nguoc

def dao_nguoc_va_hien_thi():
    tu_nhap = entry.get()
    tu_dao_nguoc = dao_nguoc_chuoi(tu_nhap)
    label_ket_qua.config(text="Từ đảo ngược là: " + tu_dao_nguoc)

window = tk.Tk()
window.title("Chương trình đảo ngược từ")

label_nhap_tu = tk.Label(window, text="Nhập từ cần đảo ngược:")
label_nhap_tu.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=10)

button_dao_nguoc = tk.Button(window, text="Đảo ngược", command=dao_nguoc_va_hien_thi)
button_dao_nguoc.pack(pady=10)

label_ket_qua = tk.Label(window, text="")
label_ket_qua.pack(pady=10)

window.mainloop()
