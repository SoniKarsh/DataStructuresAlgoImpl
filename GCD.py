# Simplest implementation of gcd algorithm.
def gcd(m, n):
    fm = []
    for i in range(1, m + 1):
        if m % i == 0:
            fm.append(i)

    fn = []
    for j in range(1, n + 1):
        if n % j == 0:
            fn.append(j)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)

    return cf[-1]

m = input("Please Enter Number 1 \n")
n = input("Please Enter Number 2 \n")
print("gcd of these 2 number is ")
print(gcd(m, n))
