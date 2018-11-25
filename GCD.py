# Simplest implementation of gcd algorithm.
# GCD Function


def gcd(n1, n2):
    # Factors of m
    fm = []
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            fm.append(i)

    # Factors of n
    fn = []
    for j in range(1, n2 + 1):
        if n2 % j == 0:
            fn.append(j)

    # Common factors from fm and fn
    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    # Return the rightmost element from the list
    return cf[-1]


m = input("Please Enter Number 1 \n")
n = input("Please Enter Number 2 \n")
print("gcd of these 2 number is ")
print(gcd(m, n))
