import random
import math


def Fermat(n, k):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for _ in range(1, k+1):
        a = random.randint(2, n-2)
        ucln = math.gcd(a, n)
        while(ucln != 1):
            ucln = math.gcd(a, n)

        r = pow(a, n-1, n)
        if (r != 1):
            return False
    return True


def main():
    n = int(input("Nhap so can kiem tra bang thuat toan Fermat: "))
    k = int(input("Nhap K: "))
    if (Fermat(n, k)):
        print("So nguyen to")
    else:
        print("Hop so")


if (__name__ == "__main__"):
    main()
