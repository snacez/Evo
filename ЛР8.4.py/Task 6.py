import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    if friend in DATABASE:
        city = DATABASE[friend]
        if city in UTC_OFFSET:
            offset = dt.timedelta(hours=UTC_OFFSET[city])
            current_time = dt.datetime.utcnow() + offset
            return current_time.strftime("%H:%M")
        else:
            return "Поправка к UTC для этого города не найдена"
    else:
        return "Информации о друге с таким именем нет в базе данных"

print(what_time('Соня'))
