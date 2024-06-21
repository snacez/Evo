import random

def open_lootbox():
    items = []
    for _ in range(20):
        rand = random.random()
        if rand < 0.7:
            items.append("обычный")
        elif rand < 0.9:
            items.append("редкий")
        elif rand < 0.95:
            items.append("эпический")
        else:
            items.append("легендарный")
    
    counts = {"обычный": items.count("обычный"), "редкий": items.count("редкий"), "эпический": items.count("эпический"), "легендарный": items.count("легендарный")}
    
    luck_message = ""
    if counts["эпический"] > 3:
        luck_message = "(Удача!)"
    if counts["легендарный"] > 1:
        luck_message = "(Большая удача!)"

    print(f"Обычные: {counts['обычный']}, Редкие: {counts['редкий']}, Эпические: {counts['эпический']}, Легендарные: {counts['легендарный']} {luck_message}")
    
    for item in items:
        if item == "обычный":
            print(f"\033[0m{item}", end=" ")
        elif item == "редкий":
            print(f"\033[94m{item}", end=" ")
        elif item == "эпический":
            print(f"\033[95m{item}", end=" ")
        else:
            print(f"\033[93m{item}", end=" ")

# Открытие лутбоксов
open_lootbox()
