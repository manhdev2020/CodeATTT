import random

def Miller_Rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # tìm s, r sao cho n - 1 = 2^s * r với r là số lẻ
    s = 0
    r = n - 1
    while r % 2 == 0:
        s += 1
        r //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        y = pow(a, r, n) # a^r mod n, nhân bình phương có lặp
        if (y != 1 and y != n-1):
            j = 1
            while (j <= s-1 and y != n-1):
                y = (y*y) % n
                if (y == 1):
                    return False
                j += 1
            if (y != n-1):
                return False
    return True


# Nhập giá trị a, b từ bàn phím
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

# Tạo mảng S1, S2 chứa các giá trị bình phương của các số nguyên
S1 = [x**2 for x in range(1, int(b**0.5) + 1)]
S2 = [x**2 for x in range(1, int(b**0.5) + 1)]

# Đếm số lượng tất cả các số nguyên tố nằm trong khoảng [a, b] sao cho số này cũng là tổng của hai số x, y thuộc S1, S2
data = {}
count = 0
for n in range(a, b+1):
    if Miller_Rabin(n):
        for x in S1:
            for y in S2:
                if x + y == n:
                    num_min = x if x < y else y
                    if num_min not in data:
                        count += 1
                        print(f"{x} + {y} = {n}")
                        data[num_min] = True
                        break


# In ra kết quả
print(
    f"Số lượng tất cả các số nguyên tố nằm trong khoảng [{a}, {b}] sao cho số này cũng là tổng của hai số x, y thuộc S1, S2 là: {count}")
