list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
players_count = len(list_players)
# Разделите участников на две команды

tim_players_1 = list_players[:int(players_count/2)]
tim_players_2 = list_players[int(players_count/2):]
print(tim_players_1)
print(tim_players_2)