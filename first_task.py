def caching_fibonacci():  # Вертає функцію fibonacci
    cash = {}

    def fibonacci(n):
        # print(f"Викликаємо fibonacci({n}), кеш: {cash}")

        if n <= 1:
            return n
        if n in cash:
            return cash[n]

        cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cash[n]

    return fibonacci


def main():
    fib = caching_fibonacci()  # Отримуємо функцію fibonacci
    f10 = fib(10)  # Викликаємо fibonacci з аргументом 10
    f15 = fib(15)
    return f10, f15


if __name__ == '__main__':
    result = main()
    print(result)
