import json
from datetime import datetime

def ghi_vao_tap_tin(du_lieu):
    ngay_hien_tai = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ten_tap_tin = f'{ngay_hien_tai}.json'

    with open(ten_tap_tin, 'w') as file:
        json.dump(du_lieu, file, indent=2)
    
    print(f'Dữ liệu đã được ghi vào tập tin: {ten_tap_tin}')

def quan_ly_giao_dich():
    danh_sach_giao_dich = []

    while True:
        print("1. Thêm giao dịch tiền")
        print("2. Thêm giao dịch vàng")
        print("0. Kết thúc")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            giao_dich_tien = input("Nhập thông tin giao dịch tiền: ")
            danh_sach_giao_dich.append({"Loai": "Tien", "Thong tin": giao_dich_tien})
        elif lua_chon == '2':
            giao_dich_vang = input("Nhập thông tin giao dịch vàng: ")
            danh_sach_giao_dich.append({"Loai": "Vang", "Thong tin": giao_dich_vang})
        elif lua_chon == '0':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

    return danh_sach_giao_dich

if __name__ == '__main__':
    du_lieu_giao_dich = quan_ly_giao_dich()

    ghi_hoac_khong = input("Bạn muốn ghi vào tập tin? (1: Có, 0: Không): ")

    if ghi_hoac_khong == '1':
        ghi_vao_tap_tin(du_lieu_giao_dich)
    else:
        print("Dữ liệu không được ghi vào tập tin.")
