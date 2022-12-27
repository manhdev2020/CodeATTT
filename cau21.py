def sangNT(n):
    a = [1]*(n+1)
    a[0] = a[1] = 0
    result = []
    for i in range(2, n+1):
        t = (int)(n/i)
        for j in range(2, t+1):
            a[i*j] = 0
    for i in range(2, n+1):
        if a[i]:
            result.append(i)
    return result


def process(a, b):
    arrayNT = sangNT(b)
    result = []
    for i in range(a, b+1):
        if i in arrayNT: 
            index = arrayNT.index(i) # in ra vị trí của giá trị i
            if index in arrayNT: # index đại diện cho só các số nguyên tố
                for z in range(index):
                    print(arrayNT[z], end=' ')
                result.append(str(i))
                print(f'| {i}')
    return result


def main():
    a = int(input("Nhập A: "))
    b = int(input("Nhập B: "))
    print(
        f'Các số siêu nguyên tố từ {a} đến {b} là: {(", ").join(process(a, b))}')


if __name__ == '__main__':
    main()
