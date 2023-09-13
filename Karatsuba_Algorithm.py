def karatsuba(x, y):
    # Base case: If the numbers are small, use standard multiplication
    if x < 10 or y < 10:
        return x * y

    # Calculate the number of digits in the numbers
    n = max(len(str(x)), len(str(y)))
    n2 = n // 2

    # Split the input numbers into two halves
    a = x // 10**n2
    b = x % 10**n2
    c = y // 10**n2
    d = y % 10**n2

    # Recursively compute the three products required by Karatsuba
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    # Combine the results to get the final product
    result = ac * 10**(2 * n2) + (ad_bc * 10**n2) + bd
    return result

x = 12345678901234567890
y = 98765432109876543210
result = karatsuba(x, y)
print(result)

