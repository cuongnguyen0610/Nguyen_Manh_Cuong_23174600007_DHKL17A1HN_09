import threading
import datetime

def google():
    for i in range(3):
        print("Google: Web", datetime.datetime.now())

def yahoo():
    for i in range(3):
        print("Yahoo: Web", datetime.datetime.now())

def facebook():
    for i in range(3):
        print("Facebook: Web", datetime.datetime.now())

def main():
    t1 = threading.Thread(target=google)
    t2 = threading.Thread(target=yahoo)
    t3 = threading.Thread(target=facebook)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
