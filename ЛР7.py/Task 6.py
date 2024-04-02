user_input = input("Введите строку: ").lower().replace(" ", "").replace(",", "").replace(".", "")
if user_input == user_input[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")