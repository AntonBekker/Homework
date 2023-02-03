"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""
import sys
f_obj, name_emp, rate_emp, hours_emp = sys.argv
print(f_obj)

def calculate_salary(rate,hours):
    print(f'Сотрудник {name_emp} заработал {int(rate)*int(hours)} * 1.25')


calculate_salary(rate_emp,hours_emp)

