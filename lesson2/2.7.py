import json

def json_to_python(json_data):
    try:
        # Sử dụng hàm json.loads để chuyển đổi JSON thành đối tượng Python
        python_obj = json.loads(json_data)
        return python_obj
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

if __name__ == "__main__":
    # Dữ liệu JSON mẫu
    json_data = '{"name": "John", "age": 30, "city": "New York"}'

    # Chuyển đổi dữ liệu JSON thành đối tượng Python
    python_object = json_to_python(json_data)

    # In đối tượng Python
    if python_object is not None:
        print("Đối tượng Python sau khi chuyển đổi:")
        print(python_object)