import tkinter as tk

window = tk.Tk()

window.title("Tiêu đề cửa sổ")

checkbutton = tk.Checkbutton(window, text="Chọn")

checkbutton.pack()

label = tk.Label(window, text="Trạng thái: Không chọn")

label.pack()

def on_change_checkbutton():
    state = checkbutton.instate(["selected"])

    if state:
        label.config(text="Trạng thái: Chọn")
    else:
        label.config(text="Trạng thái: Không chọn")

checkbutton.config(command=on_change_checkbutton)

window.mainloop()