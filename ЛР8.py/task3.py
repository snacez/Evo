def calculate_investment_amount(principal, interest_rate, years):
    amount = principal * (1 + interest_rate) ** years
    return amount

# Ввод данных от пользователя
principal = float(input("Введите начальную сумму: "))
interest_rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = int(input("Введите количество лет: "))

# Расчет и вывод итоговой суммы
result = calculate_investment_amount(principal, interest_rate, years)
print(f"Через {years} лет ваша инвестиция вырастет до: {result:.2f}")
