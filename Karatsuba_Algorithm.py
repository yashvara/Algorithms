# According to this algorithm, we can represent any number of k digits as m = a*10k/2 + b,
# where k is the length of the number.
# a and b are decided based on the length of the number.

def karatsuba(m,n):
    if(m<10 or n<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)

        k = max(len(mstring), len(nstring))
        mid=int(k/2)
            #finding a and c i.e. the higher bits for each number
        a = int(mstring[:-mid])
        c = int(nstring[:-mid])

            #finding b and d i.e. the lower bits for each number
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])

            #finding ac, bd and ad_plus_bc
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd

print("Answer is:")
print(karatsuba(3425,2486))

