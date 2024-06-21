 random

def computer_throw():
    return random.random() <= 0.7def user_throw():
    return random.random() <= 0.7

def play_game    computer_score = 0
    user_score = 0
    
    while True        # Ход компьютера
        if computer_throw():
            print("Компьютер бросает вам мяч.")
            answer = input(" ловите мяч? (Да/Нет): ")
            
            answer.lower() == "да":
                print("Вы поймали мяч                user_score += 1
            else:
                print("Вы пропули мяч.")
                break
            
        else:
            print("Компью бросает вам мяч.")
            print("Компьютер Я думаю...")
            print("Компьютер: Математика - это интересно!")
            
        
        #Ход пользователя
        if user_throw():
            question = input("Бросайтене мяч! Задайте вопрос: ")
            
            print(fВы задали вопрос: {question}")
            
        else:
            computer_response "Я думаю..."
            
       # Подсчет очков
_score += 1
        
       # Вывод текущего счета
      (f"Текущий счет - Компьютер: {computer_score}, Вы: {user_score}")
    
    
    # Вывод общего счета после оконания игры    
    if computer_score > user_score:
         winner = "Кпьютер"
     elif user_score > computer_score:
         winner = "Вы"
     else:
         winner = "Ничья"
     
     print(f"\n Игра окончена! Победитель - {winner}!\n")
 
 
# Запуск игры   
play_game()
