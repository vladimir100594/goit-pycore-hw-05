def caching_fibonacci ():
    # Створюємо порожній словник для кешу
    cache = {}

    # Внутрішня функція, яка обчіслює чісло фібоначчі
    def fibonacci(n):
        # якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # якщо n == 1, повертаємо 1
        if n == 1:
            return 1
        # Якщо вже обчислювали це число, повертаємо з кешу
        if n in cache:
            return cache[n]
        # Інакше обчислюємо рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  
print(fib(15)) 