def calc_stat(listened):
    total_songs = len(listened)
    total_duration = sum(listened)
    return f'Вы прослушали {total_songs} песен общей продолжительностью {total_duration} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))
 