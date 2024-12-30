import threading

def print_even_numbers():
    for number in range(30, 51):
        if number % 2 == 0:
            print(f"Chẵn: {number}")

def print_odd_numbers():
    for number in range(30, 51):
        if number % 2 != 0:
            print(f"Lẻ: {number}")

def main():
    even_thread = threading.Thread(target=print_even_numbers)
    odd_thread = threading.Thread(target=print_odd_numbers)

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()

if __name__ == "__main__":
    main()
