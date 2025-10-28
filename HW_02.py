import re
from typing import Callable

def generator_numbers (text: str):
    # Знаходимо всі дійсні числа, які відокремлені пробілами
    # \d+ - одна або більше цифр
    # \. - крапка
    # \d+ - одна або більше цифр після крапки
    # Регулярний вираз шукає числа типу 123.45
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit (text: str, func: Callable):
    # Викликаємо генератор і складаємо всі числа
    return sum(func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 50.00 і 350.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") 
