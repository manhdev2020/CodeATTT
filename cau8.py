def check(n):
    d = 0
    for i in range(2, (int)(n/2)+1):
        if n % i == 0:
            d += 1
    if d == 1: # Đã tính 1 và n
        return True
    else:
        return False


def main():
    n = int(input("Nhập n: "))
    result = []
    for i in range(1, n + 1):
        if check(i):
            result.append(str(i))
    if len(result) == 0:
        print(f"Nhỏ hơn hoặc bằng {n} không có số T-Prime")
    else:
        print(f"Các số T-Prime nhỏ hơn {n} là: {(', ').join(result)}")


if __name__ == "__main__":
    main()
