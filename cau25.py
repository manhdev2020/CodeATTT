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


def find_prime_sum(n, m, prime_list):
    if m == 1:
        if n in prime_list:
            return [n]
        else:
            return None
    else:
        for p in prime_list:
            result = find_prime_sum(n - p, m - 1, prime_list)
            if result is not None:
                return [p] + result
        return None


def main():
    # Lấy giá trị của M và N từ người dùng
    N = int(input("Nhập giá trị của N: "))
    M = int(input("Nhập giá trị của M: "))

    # Tạo danh sách các số nguyên tố
    prime_list = []
    for i in range(2, N + 1):
        if Miller_Rabin(i):
            prime_list.append(i)

    # Gọi hàm find_prime_sum để tìm các số nguyên tố có tổng bằng N và số lượng bằng M
    result = find_prime_sum(N, M, prime_list)

    # Kiểm tra kết quả
    if result is not None:
        print(f"{N} có thể được phân tích thành tổng của {M} số nguyên tố: {result}")
    else:
        print(f"{N} không thể được phân tích thành tổng của {M} số nguyên tố")


if __name__ == "__main__":
    main()
