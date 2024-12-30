import threading

def print_even(limit):
    for i in range(2, limit + 1, 2):
        print(f"Even: {i}")

def print_odd(limit):
    for i in range(1, limit + 1, 2):
        print(f"Odd: {i}")

if __name__ == "__main__":
    threshold = 10

    even_thread = threading.Thread(target=print_even, args=(threshold,))
    odd_thread = threading.Thread(target=print_odd, args=(threshold,))

    even_thread.start()
    odd_thread.start()

    even_thread.join()
    odd_thread.join()
