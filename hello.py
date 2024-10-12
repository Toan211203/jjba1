# print_numbers_extended.py

# Hàm để in các số từ 1 đến 10
def print_numbers():
    # Vòng lặp từ 1 đến 10
    for i in range(1, 11):
        # Kiểm tra xem số có phải là số chẵn hay lẻ
        if i % 2 == 0:
            print(f"Số {i} là số chẵn")
        else:
            print(f"Số {i} là số lẻ")

# Thông báo bắt đầu chương trình
print("Chương trình bắt đầu")

# Gọi hàm in số
print_numbers()

# Thông báo kết thúc chương trình
print("Chương trình kết thúc")
