import tkinter as tk
from math import gcd

def calculate_gcd_lcm():
    try:
        m = int(entry_m.get())
        n = int(entry_n.get())

        selected_function = function_var.get()

        if selected_function == "GCD":
            result = gcd(m, n)
        elif selected_function == "LCM":
            result = (m * n) // gcd(m, n)
        else:
            result = "Chọn chức năng"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Nhập giá trị hợp lệ cho m và n")

root = tk.Tk()
root.title("Tính GCD và LCM")

label_m = tk.Label(root, text="Nhập giá trị của m:")
label_m.grid(row=0, column=0, padx=10, pady=5)
entry_m = tk.Entry(root)
entry_m.grid(row=0, column=1, padx=10, pady=5)

label_n = tk.Label(root, text="Nhập giá trị của n:")
label_n.grid(row=1, column=0, padx=10, pady=5)
entry_n = tk.Entry(root)
entry_n.grid(row=1, column=1, padx=10, pady=5)

function_var = tk.StringVar()
function_var.set("GCD")  
function_menu = tk.OptionMenu(root, function_var, "GCD", "LCM")
function_menu.grid(row=2, column=0, columnspan=2, pady=10)

calculate_button = tk.Button(root, text="Tính toán", command=calculate_gcd_lcm)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
