import datetime as dt

# Введите дату и время начала прохождения курса
start_moment = dt.datetime(2023, 9, 1, 8, 3, 0)  # Например, 1 сентября 2023 года в 8:30 утра
current_moment = dt.datetime.now()  # Текущее время

total_time = current_moment - start_moment

print("Время, затраченное на прохождение курса:", total_time)
