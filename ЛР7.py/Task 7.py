def count_vowels_and_consonants(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = sum(1 for char in s if char in consonants)
    return vowel_count, consonant_count

user_input = input("Введите строку для подсчета гласных и согласных букв: ")

vowels, consonants = count_vowels_and_consonants(user_input)
print(f"Количество гласных букв: {vowels}")
print(f"Количество согласных букв: {consonants}")