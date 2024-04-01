number = int(input("Введите число, для которого нужно вывести таблицу умножения: "))

print(f"Таблица умножения для числа {number}:")
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")