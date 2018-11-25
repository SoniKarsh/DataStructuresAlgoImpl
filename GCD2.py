# Better implementation of gcd algorithm.
# GCD Function


def gcd(n1, n2):
    global mocn
    for i in range(1, min(n1, n2)):
        if n1 % i == 0 and n2 % i == 0:
            # Maximum of common numbers.
            mocn = i

    return mocn


m = int(input("Please Enter Number 1 \n"))
n = int(input("Please Enter Number 2 \n"))
print("gcd of these 2 number is ")
print(gcd(m, n))
