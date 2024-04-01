def reverse_order(n):
    if n < 1:
        return
    print(n, end=' ')
    reverse_order(n - 1)

number = int(input("Введите натуральное число n: "))
print(f"Числа от {number} до 1 в обратном порядке:")
reverse_order(number)