import threading
import datetime
import time

def print_message(thread_name):
    for i in range(3):
        print(f"{thread_name}: Web {datetime.datetime.now().strftime('%b %d %H:%M:%S %Y')}")
        time.sleep(1)

    print(f"Exiting {thread_name}")

def main():
    print("Starting Main Thread")

    threads = []

    thread_names = ["Google", "Yahoo", "Facebook"]

    for name in thread_names:
        thread = threading.Thread(target=print_message, args=(name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Main Thread")
    print("Exiting")

if __name__ == "__main__":
    main()
