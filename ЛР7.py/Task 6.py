def is_palindrome(s):
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]

user_input = input("Введите строку для проверки на палиндром: ")

if is_palindrome(user_input):
    print("Введенная строка является палиндромом.")
else:
    print("Введенная строка не является палиндромом.")