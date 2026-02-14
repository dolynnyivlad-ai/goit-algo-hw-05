import re
from typing import Callable

text = '''
    Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
    доповнений додатковими надходженнями 27.45 і 324.00 доларів. 
'''


def generator_numbers(text: str):
    pattern = r'\d+\.?\d+'
    numb = re.findall(pattern, text)

    for num in numb:
        yield float(num)


def sum_profit(text: str, func: Callable):
    x = sum([i for i in func(text)])
    return x


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
