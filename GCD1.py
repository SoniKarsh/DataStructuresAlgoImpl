# Better implementation of gcd algorithm.
# GCD Function


def gcd(n1, n2):
    # Divisor of n1 and n2
    fm = []
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            fm.append(i)

    # Return the rightmost element from the list
    return fm[-1]


m = int(input("Please Enter Number 1 \n"))
n = int(input("Please Enter Number 2 \n"))
print("gcd of these 2 number is ")
print(gcd(m, n))
