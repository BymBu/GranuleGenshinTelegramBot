from tokens import chat_game, bot, standart, fourpers, ls , test, fiveweap, fourweap, pers2, pers1, chat_id
import datetime
import json
import random
import time
import forKrutki
import sconsole










def standart1(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user = message.from_user.username
        user_name = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return
        timers[str(game)] = current_time
        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0
        if krutki_data[user_name] > 0:
            krutki_data[user_name] -= 1
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)
            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)
            with open('molitvi.json', 'r') as file:
                data = json.load(file)
            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 1
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 1
                # Записываем обновленные данные в файл molitvi.json


            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca(message)

                # Отправляем подтверждение пользователю
            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(standart) - 1)
                    random_element = standart[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                if randomizer == 22 or randomizer == 2:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(standart) - 1)
                    random_element = standart[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')


def standart10(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user = message.from_user.username


        user_name = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return
        timers[str(game)] = current_time
        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0
        if krutki_data[user_name] >= 10:
            krutki_data[user_name] -= 10
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)
            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")
            randomizer = random.randint(0, 23)
            print(randomizer)
            with open('molitvi.json', 'r') as file:
                data = json.load(file)
            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 10
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 10
                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca10(message)


                # Отправляем подтверждение пользователю
            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15 or randomizer == 10:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(standart) - 1)
                    random_element = standart[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15 or randomizer == 14:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                print('буст не робит')
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(standart) - 1)
                    random_element = standart[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')



def oryj1(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user = message.from_user.username
        user_name = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return

        timers[str(game)] = current_time

        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        if krutki_data[user_name] > 0:
            krutki_data[user_name] -= 1
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)

            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)

            with open('molitvi.json', 'r') as file:
                data = json.load(file)

            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 1
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 1

                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca(message)
                # Отправляем подтверждение пользователю

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fiveweap) - 1)
                    random_element = fiveweap[random_index]
                    time.sleep(1.5)

                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourweap) - 1)
                    random_element = fourweap[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                if randomizer == 22 or randomizer == 2:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fiveweap) - 1)
                    random_element = fiveweap[random_index]
                    time.sleep(1.5)

                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourweap) - 1)
                    random_element = fourweap[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')


def oryj10(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user_name = message.from_user.username
        user = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return
        timers[str(game)] = current_time
        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0
        if krutki_data[user_name] >= 10:
            krutki_data[user_name] -= 10
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)
            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")
            randomizer = random.randint(0, 23)
            print(randomizer)
            with open('molitvi.json', 'r') as file:
                data = json.load(file)
             # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 10
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 10
                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)
                # Отправляем подтверждение пользователю

            forKrutki.pilca10(message)

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15 or randomizer == 10:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fiveweap) - 1)
                    random_element = fiveweap[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15 or randomizer == 14:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourweap) - 1)
                    random_element = fourweap[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                              text=f"🥳| Поздравляем! Ты выбилЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1,2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                              text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                print('буст не робит')
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:
                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fiveweap) - 1)
                    random_element = fiveweap[random_index]
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)
                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1
                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    random_index = random.randint(0, len(fourweap) - 1)
                    random_element = fourweap[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")
                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')








def persone(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user_name = message.from_user.username
        user = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return

        timers[str(game)] = current_time

        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        if krutki_data[user_name] > 0:
            krutki_data[user_name] -= 1
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)

            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)

            with open('molitvi.json', 'r') as file:
                data = json.load(file)

            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 1
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 1

                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca(message)

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {pers1}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")

                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 10:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                print('бут Не робит')
                if randomizer == 22 or randomizer == 2:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {pers1}‼️\n@{user}| Откручено круток - {data[user]}")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')



def persone10(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user = message.from_user.username
        user_name = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return

        timers[str(game)] = current_time

        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        if krutki_data[user_name] >= 10:
            krutki_data[user_name] -= 10
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)

            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)

            with open('molitvi.json', 'r') as file:
                data = json.load(file)

            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 10
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 10

                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca10(message)

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15 or randomizer == 1 or randomizer == 3:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ты выбил {pers1}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n Ты выбил {rare}")
            else:
                print("буст Не робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ты выбил {pers1}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ты выбил {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")

        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')




def perstwo(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не туда...")
    else:
        user_name = message.from_user.username
        user = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return

        timers[str(game)] = current_time

        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        if krutki_data[user_name] > 0:
            krutki_data[user_name] -= 1
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)

            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)

            with open('molitvi.json', 'r') as file:
                data = json.load(file)

            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 1
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 1

                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca(message)

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! Ты выбил {pers2}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 10:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}\n🛒|Буст длится ещё - {remaining_time}")
            else:
                print('бут Не робит')
                if randomizer == 22 or randomizer == 2:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {pers2}‼️\n@{user}| Откручено круток - {data[user]}")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")
        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')




def perstwo10(message):
    if message.chat.id == chat_id:
        msg = bot.send_message(message.chat.id, "Не тут...")
    else:
        user = message.from_user.username
        user_name = message.from_user.username
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        game = "main"
        with open('timers2.json', 'r') as file:
            timers = json.load(file)
        if str(game) in timers:
            last_time = datetime.datetime.strptime(timers[str(game)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 5:
                remaining_time = datetime.timedelta(seconds=5 - time_difference.total_seconds())
                pass
                return

        timers[str(game)] = current_time

        with open('timers2.json', 'w') as file:
            json.dump(timers, file)
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        if krutki_data[user_name] >= 10:
            krutki_data[user_name] -= 10
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)

            user_id = message.from_user.id
            user_name = message.from_user.username
            print(f"📌{user_id} ({user_name}) использовал команду /крутить")
            msg = bot.send_message(message.chat.id, "Оп-оп полетела!")

            randomizer = random.randint(0, 23)
            print(randomizer)

            with open('molitvi.json', 'r') as file:
                data = json.load(file)

            # Проверяем, есть ли информация о пользователе в файле
            if user in data:
                # Увеличиваем количество использований команды на 1
                data[user] += 10
            else:
                # Добавляем информацию о пользователе
                if user is None:
                    user = message.from_user.first_name
                data[user] = 10

                # Записываем обновленные данные в файл molitvi.json
            with open('molitvi.json', 'w') as file:
                json.dump(data, file)

            forKrutki.pilca10(message)

            with open('byst.json', 'r') as bystik:
                byst = json.load(bystik)
            boost = 'main'
            if boost in byst and (
                    datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                         "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(
                hours=3):
                remaining_time = datetime.timedelta(hours=3) - (
                        datetime.datetime.now() - datetime.datetime.strptime(str(byst[boost]),
                                                                             "%Y-%m-%d %H:%M:%S"))
                print("буст робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15 or randomizer == 1 or randomizer == 3:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {pers2}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n😊| При 10 крутках просто увеличиваются шансы!")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n🛒|Буст длится ещё - {remaining_time}\n Ты выбил {rare}")
            else:
                print("буст Не робит")
                if randomizer == 22 or randomizer == 2 or randomizer == 4 or randomizer == 15:

                    with open('pers.json', 'r') as file:
                        ddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in ddata:
                        # Увеличиваем количество использований команды на 1
                        ddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        ddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers.json', 'w') as file:
                        json.dump(ddata, file)

                    sticker_id = 'CAACAgIAAxkBAAEJ275kxpPl2Y458MnEoXbQ_XbtmjuUnAACZDcAAiCUMUo0OeEanlI2cy8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {pers2}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")


                elif randomizer == 21 or randomizer == 20 or randomizer == 19 or randomizer == 18 or randomizer == 17 or randomizer == 16 or randomizer == 15:
                    with open('pers2.json', 'r') as file:
                        dddata = json.load(file)

                    # Проверяем, есть ли информация о пользователе в файле
                    if user in dddata:
                        # Увеличиваем количество использований команды на 1
                        dddata[user] += 1
                    else:
                        # Добавляем информацию о пользователе
                        if user is None:
                            user = message.from_user.first_name
                        dddata[user] = 1

                        # Записываем обновленные данные в файл molitvi.json
                    with open('pers2.json', 'w') as file:
                        json.dump(dddata, file)
                    sticker_id = 'CAACAgIAAxkBAAEJ3Ylkx5H2Devt0zMmMiB_JNh6I3yV5AACcy8AAj25OEqlwksKSEoXlS8E'
                    bot.send_sticker(message.chat.id, sticker_id)

                    random_index = random.randint(0, len(fourpers) - 1)
                    random_element = fourpers[random_index]
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"🥳| Поздравляем! ТЫ ВЫБИЛ {random_element}‼️\n@{user}| Откручено круток - {data[user]}\n😊| При 10 крутках просто увеличиваются шансы!")


                else:
                    sticker_id = 'CAACAgIAAxkBAAEJ27xkxpN7rp9VUbGzcRPRIqW5p-sJJAACeTYAAsrJOUpVlV9yyWrnsi8E'
                    bot.send_sticker(message.chat.id, sticker_id)
                    time.sleep(1.5)

                    aboba = random.randint(1, 2)
                    if aboba == 1:
                        rare = 'Меч Драконьей Крови ⚔️'
                    elif aboba == 2:
                        rare = 'Лук Ворона 🏹'
                    bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id,
                                          text=f"Ты не выбил(а) легу😿\n@{user}| Откручено круток - {data[user]}\n Ты выбил {rare}")

        else:
            bot.reply_to(message, '❌ Недостаточно круток! Фарми - "ферма"')







