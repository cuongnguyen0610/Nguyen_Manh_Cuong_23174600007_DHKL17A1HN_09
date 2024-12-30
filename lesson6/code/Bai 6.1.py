import threading
import time

def print_thread_name():
    thread_name = threading.current_thread().name
    print(f"Thread name: {thread_name}")

def main():
    num_threads = 5

    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=print_thread_name, name=f"Thread-{i+1}")
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
