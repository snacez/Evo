num = int(input("Введите целое неотрицательное число: "))
factorial = 1

if num < 0:
    print("Факториал отрицательного числа не определен.")
elif num == 0:
    print("Факториал 0 равен 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Факториал числа", num, "равен", factorial)