import json
import random




def pilca(message):
    rand_pilca = random.randint(20, 30)
    user = message.from_user.username
    with open('pil.json', 'r') as file:
        data = json.load(file)
    # Проверяем, есть ли информация о пользователе в файле
    if user in data:
        # Увеличиваем количество использований команды на 1
        data[user] += rand_pilca
    else:
        # Добавляем информацию о пользователе
        if user is None:
            user = message.from_user.first_name
        data[user] = rand_pilca
        # Записываем обновленные данные в файл molitvi.json
    with open('pil.json', 'w') as file:
        json.dump(data, file)

def pilca10(message):
    rand_pilca = random.randint(200, 300)
    user = message.from_user.username
    with open('pil.json', 'r') as file:
        data = json.load(file)
    # Проверяем, есть ли информация о пользователе в файле
    if user in data:
        # Увеличиваем количество использований команды на 1
        data[user] += rand_pilca
    else:
        # Добавляем информацию о пользователе
        if user is None:
            user = message.from_user.first_name
        data[user] = rand_pilca
        # Записываем обновленные данные в файл molitvi.json
    with open('pil.json', 'w') as file:
        json.dump(data, file)

