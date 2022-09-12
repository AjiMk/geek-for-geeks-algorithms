import math
a = 1
b = -7
c = 10

a = 280
b = 399
c = 573

def roots(a, b, c):
    try:
        sqrt_formula = math.sqrt(b**2-4*(a*c))
    except:
        return -1
    # root_one = math.floor((-1 * b + sqrt_formula)/(2*a))
    # root_two = math.floor((-1 * b - sqrt_formula)/(2*a))

    # print(root_one, root_two)
    print(sqrt_formula)


# print( roots(a, b, c) )

ab = a, b
z = [-1]
zz = z
print( len(z) )
print( z[0]==-1 )
