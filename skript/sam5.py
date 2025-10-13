def add_score(scores, player, score):
    new_record = (player, score)
    scores.append(new_record)
    return scores

def get_top_players(scores, n=3):
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return sorted_scores[:n]

def get_player_scores(scores, player):
    player_records = [record for record in scores if record[0] == player]
    return player_records

records = [("Alice", 150), ("Bob", 200), ("Charlie", 180), ("Alice", 170)]

print("Начальные рекорды:")
for record in records:
    print(record)

# Тест 1: Добавление нового рекорда
print("\n--- Тест 1: Добавление нового рекорда ---")
records = add_score(records, "David", 190)
print("После добавления рекорда Дэвида:")
for record in records:
    print(record)

# Тест 2: Получение топ-2 игроков
print("\n--- Тест 2: Получение топ-2 игроков ---")
top_players = get_top_players(records, 2)
print("Топ-2 игрока:")
for player in top_players:
    print(f"{player[0]}: {player[1]} очков")

# Тест 3: Получение всех результатов Alice
print("\n--- Тест 3: Получение всех результатов Alice ---")
alice_scores = get_player_scores(records, "Alice")
print("Все результаты Alice:")
for score in alice_scores:
    print(f"{score[0]}: {score[1]} очков")