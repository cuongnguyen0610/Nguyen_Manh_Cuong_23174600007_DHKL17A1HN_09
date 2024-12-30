import threading
import requests

def download_file(url, save_as):
    response = requests.get(url, stream=True)
    with open(save_as, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)

def main():
    files_to_download = [
        {'url': 'https://example.com/file1.txt', 'save_as': 'file1.txt'},
        {'url': 'https://example.com/file2.txt', 'save_as': 'file2.txt'},
    ]

    threads = []
    for file_info in files_to_download:
        thread = threading.Thread(
            target=download_file,
            args=(file_info['url'], file_info['save_as'])
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Tải xuống đã hoàn thành.")

if __name__ == "__main__":
    main()
