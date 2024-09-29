class TS:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Toán: {self.diem_toan}, Lý: {self.diem_ly}, Hóa: {self.diem_hoa}, Tổng điểm: {self.tinh_tong_diem()}")

def nhap_danh_sach_ts():
    danh_sach = []
    so_luong = int(input("Nhập số lượng thí sinh: "))
    for i in range(so_luong):
        ho_ten = input("Nhập họ tên thí sinh: ")
        diem_toan = float(input("Nhập điểm Toán: "))
        diem_ly = float(input("Nhập điểm Lý: "))
        diem_hoa = float(input("Nhập điểm Hóa: "))
        ts = TS(ho_ten, diem_toan, diem_ly, diem_hoa)
        danh_sach.append(ts)
    return danh_sach

def in_danh_sach_trung_tuyen(danh_sach, diem_chuan):
    ds_trung_tuyen = [ts for ts in danh_sach if ts.tinh_tong_diem() >= diem_chuan]
    ds_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)
    
    print(f"Danh sách thí sinh trúng tuyển (Điểm chuẩn: {diem_chuan}):")
    for ts in ds_trung_tuyen:
        ts.in_thong_tin()


if __name__ == "__main__":
    danh_sach = nhap_danh_sach_ts()
    diem_chuan = 20
    in_danh_sach_trung_tuyen(danh_sach, diem_chuan)
