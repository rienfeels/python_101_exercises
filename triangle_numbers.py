def triangle_number(n):
    return n * (n + 1) // 2

for i in range(1, 101):
    print(triangle_number(i))
