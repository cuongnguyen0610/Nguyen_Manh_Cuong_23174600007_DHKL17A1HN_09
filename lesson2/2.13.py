import requests

def hien_thi_sach_noi_bat(api_url):
    try:
        # Gửi yêu cầu GET đến API
        response = requests.get(api_url)

        # Kiểm tra xem yêu cầu có thành công hay không (status code 200)
        if response.status_code == 200:
            data = response.json()
            hien_thi_thong_tin_sach_noi_bat(data)
        else:
            print(f"Không thể kết nối đến API. Mã lỗi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Lỗi kết nối: {e}")

def hien_thi_thong_tin_sach_noi_bat(data):
    # In danh sách bài post nổi bật
    print("Danh sách các bài post nổi bật:\n")

    # Hiển thị thông tin của mỗi bài post (giới hạn chỉ hiển thị 3 bài đầu)
    for i, post in enumerate(data[:3], 1):
        print(f"Bài Post {i}:")
        print(f"   - Name: {post['name']}")
        print(f"   - Email: {post['email']}")
        print(f"   - Body: {post['body']}\n")

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/comments?postId=1"

    print("Đang tải thông tin sách nổi bật từ API...\n")
    hien_thi_sach_noi_bat(api_url)
