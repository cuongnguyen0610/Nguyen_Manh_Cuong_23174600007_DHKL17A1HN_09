import threading
import random

def tim_max(list_con, ket_qua):
    max_list_con = max(list_con)
    with ket_qua_lock:
        ket_qua.append(max_list_con)

def chia_list(list_lon, so_thread):
    kich_thuoc_list_con = len(list_lon) // so_thread
    list_con = [list_lon[i:i+kich_thuoc_list_con] for i in range(0, len(list_lon), kich_thuoc_list_con)]
    return list_con

def main():
    list_lon = [random.randint(0, 100) for _ in range(10)] 
    so_thread = 2
    list_con = chia_list(list_lon, so_thread)

    threads = []
    for i in range(so_thread):
        thread = threading.Thread(target=tim_max, args=(list_con[i], ket_qua))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    max_tat_ca = max(ket_qua)
    print("List:", list_lon)
    print("Số thread:", so_thread)
    print("Max của từng list con:")
    for i in range(so_thread):
        print(f"Thread {i + 1}: max = {ket_qua[i]}")
    print(f"Max của list: max = {max_tat_ca}")

if __name__ == "__main__":
    ket_qua = []
    ket_qua_lock = threading.Lock()
    main()
