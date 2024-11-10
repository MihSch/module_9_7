def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        k = 0
        for i in range(2, a // 2 + 1):
            if (a % i == 0):
                k = k + 1
        if (k <= 0):
            return f'Простое\n{a}'
        else:
            return f'Составное\n{a}'

    return wrapper


@is_prime
def sum_three(a, b, c):
    sum_= a + b + c
    return sum_

result = sum_three(2, 3, 6)
print(result)