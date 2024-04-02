num = int(input("Введите целое число больше 1: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "является простым числом.")
else:
    print(num, "не является простым числом.")