"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
""""Решение 1:""""
def my_func():
    agr1 = int(input("Ведите первое число: "))
    arg2 = int(input("Ведите второе число: "))
    arg3 = int(input("Ведите третье число: "))
    my_list = [agr1,arg2,arg3]
    my_list.sort(reverse=True)
    return my_list
listgoal = my_func()
print(listgoal[0]+listgoal[1])

""""Решение 2:""""
def my_func():
    agr1 = int(input("Ведите первое число: "))
    arg2 = int(input("Ведите второе число: "))
    arg3 = int(input("Ведите третье число: "))
    my_list = [agr1,arg2,arg3]
    return my_list
listgoal = my_func()
goal = sum(listgoal) - min(listgoal)
print(goal)

