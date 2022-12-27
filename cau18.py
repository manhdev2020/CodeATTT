import math

# Tách về dạng mảng (A[3], A[2], A[1], A[0])
# a = 2^((t-1)*w)A[t-1] + ... + 2^(2w)A[2] + 2^(w)A[1] + A[0]

# Chuyển số về dạng mảng
def conver_to_array(n, w, t):
    A = []

    for i in range(t-1, -1, -1):
        value = n // (math.pow(2, i * w))
        n = n - value * (math.pow(2, i * w))
        A.append(int(value))

    return A

# Chuyển mảng về dạng số
def convert_to_number(e, arr, w, t):
    total = 0
    index = 0
    for i in range(t-1, -1, -1):
        total += arr[index] * math.pow(2, i * w)
        index += 1
    return int(total)

# Cộng
def addition(a, b, w, t):
    C = []
    e = 0  # bit nhớ

    A = conver_to_array(a, w, t)
    B = conver_to_array(b, w, t)

    lenA = len(A)

    for i in range(lenA - 1, -1, -1):
        value = int((A[i] + B[i] + e) % math.pow(2, w))
        if (value != A[i] + B[i] + e):
            e = 1
        else:
            e = 0
        C.append(value)

    C = C[::-1]
    print(f'({e}, {C})')
    print(convert_to_number(e, C, w, t))


def main():
    w = 8
    p = 2147483647
    t = math.ceil(math.log2(p) / w)

    a = int(input('Nhap a: '))
    b = int(input('Nhap b: '))

    addition(a, b, w, t)


if __name__ == '__main__':
    main()
