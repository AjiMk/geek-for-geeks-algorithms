def mccarthy(n):
    if n>100:
        return n-10
    return mccarthy(mccarthy(n+11))

print(mccarthy(4))