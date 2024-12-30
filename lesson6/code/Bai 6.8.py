import threading
import random

def tinh_tong(list_con, ket_qua):
    tong = sum(list_con)
    with ket_qua_lock:
        ket_qua.append(tong)

def chia_list(list_lon, so_thread):
    kich_thuoc_list_con = len(list_lon) // so_thread
    list_con = [list_lon[i:i+kich_thuoc_list_con] for i in range(0, len(list_lon), kich_thuoc_list_con)]
    return list_con

def main():
    list_lon = [random.randint(0, 10) for _ in range(7)]  
    so_thread = 4
    list_con = chia_list(list_lon, so_thread)

    threads = []
    for i in range(so_thread):
        thread = threading.Thread(target=tinh_tong, args=(list_con[i], ket_qua))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    tong_tat_ca = sum(ket_qua)
    print("List:", list_lon)
    print("Số thread:", so_thread)
    print("Tổng từng list con:")
    for i in range(so_thread):
        print(f"Thread {i + 1}: {list_con[i]} = {ket_qua[i]}")
    print(f"Tổng list: {'+'.join(map(str, ket_qua))} = {tong_tat_ca}")

if __name__ == "__main__":
    ket_qua = []
    ket_qua_lock = threading.Lock()
    main()
