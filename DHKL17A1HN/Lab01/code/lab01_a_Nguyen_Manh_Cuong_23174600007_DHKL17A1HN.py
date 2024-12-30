import json
class JSONReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def read_json(self):
        with open(self.file_path, 'r',encoding='utf-8') as file:
            self.data = json.load(file)
    def display_data(self):
        if self.data:
            for user in self.data:
                print(f"Name: {user['name']}, Age: {user['age']}, Address:{user['address']}")
# Sử dụng lớp JSONReader
path = 'C:/Users/DELL/Documents/lesson1 Data science/Nguyen_Manh_Cuong_23174600007_DHKL17A1HN/DHKL17A1HN/Lab02/data/users.json'
reader = JSONReader(path)
reader.read_json()
reader.display_data()