user_input = input("Введите строку: ").lower()
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
vowel_count = sum(1 for char in user_input if char in vowels)
consonant_count = sum(1 for char in user_input if char in consonants)
print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)