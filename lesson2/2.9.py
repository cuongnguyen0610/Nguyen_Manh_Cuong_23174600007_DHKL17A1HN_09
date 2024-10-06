import json

if __name__ == "__main__":
    # Đối tượng từ điển Python mẫu
    python_dict = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "is_student": False,
        "grades": [95, 89, 78]
    }

    # Sắp xếp các khóa và chuyển đổi đối tượng từ điển thành chuỗi JSON
    json_string = json.dumps(python_dict, indent=4, sort_keys=True)

    # In ra các thành viên với mức thụt lề 4
    print(f"Chuỗi JSON sau khi chuyển đổi:\n{json_string}")