#------------------------------------------------------------------------------
# Створити функцію generator_numbers яка буде аналізувати текст, ідентифікувати
#   всі дійсні числа, які є частинами доходів і повертати їх як генератор.
# Реалізувати функцію sum_profit, яка буде використовувати generator_numbers
#   для підсумовування цих чисел і обчислення загального прибутку.
#------------------------------------------------------------------------------
import re
from decimal import Decimal
report = 'Загальний доход працівника складається з декілька частин: '\
        '1000.01 як основний дохід, доповнений додатковими надхожденнями '\
        '27.45 та 324.00 долларів'
pattern = r' \d+\.?\d* '
def generator_numbers(text):
    start_pos = 0
    while True:
        match = re.search(pattern, text[start_pos:])
        if match is None:
            yield None
        yield match.group().strip()
        start_pos += match.span()[1]
def sum_profit(text, func):
    gen = func(text)
    summ = 0
    while True:
        addon = next(gen)
        if addon is None:
            break
        summ += Decimal(addon)
    return summ
total_income = sum_profit(report, generator_numbers)
print(f'Загальний дохід: {total_income}')
