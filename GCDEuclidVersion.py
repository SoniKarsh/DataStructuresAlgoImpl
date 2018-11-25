# Euclid's implementation of gcd algorithm.
# GCD Function


def gcd(n1, n2):
    if n2 > n1:
        (n1, n2) = (n2, n1)

    if int(n1) % int(n2) == 0:
        return n2
    else:
        diff = n1 - n2
        return gcd(max(n2, diff), min(n2, diff))


m = int(input("Please Enter Number 1 \n"))
n = int(input("Please Enter Number 2 \n"))
print("gcd of these 2 number is ")
print(gcd(m, n))
