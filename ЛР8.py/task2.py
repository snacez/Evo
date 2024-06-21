def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_numbers(numbers):
    reversed_numbers = []
    for num in numbers:
        reversed_num = reverse_number(num)
        if is_palindrome(num):
            print(f"Число {num} является палиндромом!")
        reversed_numbers.append(reversed_num)
    return reversed_numbers

# Пример использования функций
numbers = [123, 121, 456, 787, 987]
reversed_list = process_numbers(numbers)
print("Новый список с перевернутыми числами:")
print(reversed_list)
