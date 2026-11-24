#1
a = input("Введите число: ")
print("Тип данных после ввода:", type(a))
b = int(a)
print("Тип после int():", type(b))
c = str(b)
print("Тип после str():", type(c))
#2
a = float(input("Введите число: "))
if a > 0:
    a = -a
print("Результат:", a)
#3
cap = int(input("Вместимость автобуса: "))
on = int(input("Уже в автобусе: "))
wait = int(input("Ожидают посадки: "))
a = max(0, wait - (cap - on))
print("Осталось ожидать:", a)
#4
name = input("Введите ваше имя: ")
print("Привет", name)
#5
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Произведение:", a * b)