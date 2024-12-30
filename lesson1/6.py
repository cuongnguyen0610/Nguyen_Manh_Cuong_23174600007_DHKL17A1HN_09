class Stack:
    def __init__(self, size):
        
        self.stack = [0.0] * size  
        self.top = -1  
        self.size = size  
    def isEmpty(self):
       
        return self.top == -1

    def isFull(self):
        
        return self.top == self.size - 1

    def push(self, value):
       
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
        else:
            self.top += 1
            self.stack[self.top] = value
            print(f"Đã đẩy {value} vào ngăn xếp.")

    def pop(self):
       
        if self.isEmpty():
            print("Ngăn xếp trống, không thể lấy phần tử.")
            return None
        else:
            popped_value = self.stack[self.top]
            self.top -= 1
            print(f"Đã lấy {popped_value} ra khỏi ngăn xếp.")
            return popped_value

    def count(self):
     
        return self.top + 1

    def print(self):
        
        if self.isEmpty():
            print("Ngăn xếp trống.")
        else:
            print("Nội dung ngăn xếp (từ đỉnh xuống đáy):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def __del__(self):
       
        print("Ngăn xếp đã bị hủy.")

if __name__ == "__main__":
    
    s = Stack(5)

    s.push(1.1)
    s.push(2.2)
    s.push(3.3)

    s.print()

    s.pop()

 
    s.print()

    del s