import threading
import requests

def make_request(url):
    response = requests.get(url)
    print(f"URL: {url}, Status Code: {response.status_code}")

def main():
    urls = [
        'https://www.example.com',
        'https://www.example.org',
        'https://www.example.net',
    ]

    threads = []
    for url in urls:
        thread = threading.Thread(target=make_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Các yêu cầu HTTP đã hoàn thành.")

if __name__ == "__main__":
    main()
