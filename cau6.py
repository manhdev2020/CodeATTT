def tongUoc(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result


def main():
    n = int(input("Hãy nhập n: "))
    for i in range(1,n):
        soThuNhat = i
        soThuHai  = tongUoc(soThuNhat)
        if soThuHai > soThuNhat and tongUoc(soThuHai) == soThuNhat:
            print(soThuNhat, soThuHai)

if __name__ == '__main__':
    main()
