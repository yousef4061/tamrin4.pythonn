def is_factorial(n):
    fact = 1
    i = 1
    while fact < n:
        i += 1
        fact *= i
    return "yes" if fact == n else "no"

num = int(input("adad ra vared konid: "))
print(is_factorial(num))
# بررسی اعداد فاکتوریل