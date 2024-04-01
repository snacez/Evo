def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Введите целое неотрицательное число для вычисления факториала: "))

if number < 0:
    print("Факториал определен только для неотрицательных чисел.")
elif number == 0:
    print("Факториал 0 равен 1.")
else:
    result = factorial(number)
    print(f"Факториал числа {number} равен {result}.")