import json

def tinh_tong_nhan_vien(data):
    return sum([don_vi['so_nhan_vien'] for don_vi in data['don_vi']])

def in_thong_tin_cong_ty(data):
    print(f'Tên công ty: {data["ten_cong_ty"]}')
    print(f'Địa chỉ: {data["dia_chi"]}')

def in_thong_ke_don_vi(i, don_vi, tong_nhan_vien):
    ten_don_vi = don_vi['ten_don_vi']
    so_nhan_vien_don_vi = don_vi['so_nhan_vien']
    ty_le = (so_nhan_vien_don_vi / tong_nhan_vien) * 100

    print(f'{i}./ Tên đơn vị: {ten_don_vi}.')
    print(f'   - Số nhân viên: {so_nhan_vien_don_vi}')
    print(f'   - Tỷ lệ: {ty_le:.2f}%.\n')

def thong_ke_nhan_vien(data):
    # Tính tổng số nhân viên
    tong_nhan_vien = tinh_tong_nhan_vien(data)

    # In thông tin công ty
    in_thong_tin_cong_ty(data)
    print(f'Tổng số nhân viên: {tong_nhan_vien}')

    # In thống kê nhân viên theo đơn vị
    print('\n-----Thống kê nhân viên theo đơn vị------')
    for i, don_vi in enumerate(data['don_vi'], 1):
        in_thong_ke_don_vi(i, don_vi, tong_nhan_vien)

if __name__ == '__main__':
    # Đọc dữ liệu từ file JSON
    with open(r'C:\Users\DELL\Documents\lesson1 Data science\Nguyen_Manh_Cuong_23174600007_DHKL17A1HN\lesson2\du_lieu.json', 'r',encoding='utf-8') as file:
        du_lieu = json.load(file)

    # Gọi hàm thống kê nhân viên
    thong_ke_nhan_vien(du_lieu)
