class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        print("Hình chữ nhật có:")
        print("  - Chiều dài:", self.dai)
        print("  - Chiều rộng:", self.rong)
        print("  - Chu vi:", self.tinh_chu_vi())
        print("  - Diện tích:", self.tinh_dien_tich())
dai = float(input("Nhập chiều dài: "))
rong = float(input("Nhập chiều rộng: "))
hinh_chu_nhat = HinhChuNhat(dai, rong)
hinh_chu_nhat.in_thong_tin()