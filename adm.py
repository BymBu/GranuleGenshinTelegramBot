import json

from tokens import bot, ls, chat_id, tanya, chat_game, consolee




def get_id(message):
    if message.from_user.id == ls:
        chat = message.chat.id


        chatid = message.chat.id
        user_id = message.from_user.id
        user_name = message.from_user.username
        response = f"📌{user_id} ({user_name}) использовал команду /айди"
        bot.send_message(consolee, response)
        bot.send_message(chatid, f"ID вашего чата: {chat_id}")

'''                                  АДМИН КОМАНДЫ ДЛЯ GRANULE                                               '''

def compins(message):
    if message.from_user.id == ls:
        try:
            comp_value = int(message.text.split()[1])  # Extract the compensation value from the message
        except (IndexError, ValueError):
            bot.reply_to(message, "Пожалуйста, введите число после команды 'компенсация'.")
            return

        # Load the JSON file
        with open('krutki.json', 'r') as file:
            data = json.load(file)

        # Increase each value by the compensation value
        for key in data:
            data[key] += comp_value

        # Write the updated data back to the JSON file
        with open('krutki.json', 'w') as file:
            json.dump(data, file)

        bot.reply_to(message, f"Компенсация {comp_value} была успешно добавлена каждому пользователю.")



def give(message):
    nazv = message.text.split("@")[1].split()[0]
    summa = int(message.text.split()[-1])
    igrok = message.from_user.username

    chat = message.chat.id

    if message.from_user.id == ls:
        user_id = message.from_user.id

        user_namee = message.from_user.username
        response = f"📌{user_id} ({user_namee}) Выдал @{nazv} {summa} круток"
        bot.send_message(consolee, response)
        user = message.from_user.username

        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if nazv not in krutki_data:
            krutki_data[nazv] = 0
        if igrok not in krutki_data:
            krutki_data[igrok] = 0

        if krutki_data[igrok] > 0 or krutki_data[igrok] == 0:
            krutki_data[nazv] += summa
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)




        msg = bot.send_message(message.chat.id, f"✅| @{igrok} выдал @{nazv} {summa} круток!")
def snyat(message):
    nazv = message.text.split("@")[1].split()[0]
    summa = int(message.text.split()[-1])
    igrok = message.from_user.username

    chat = message.chat.id

    if message.from_user.id == ls:
        user_id = message.from_user.id

        user_namee = message.from_user.username
        response = f"📌{user_id} ({user_namee}) Снял @{nazv} {summa} круток"
        bot.send_message(consolee, response)
        user = message.from_user.username

        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if nazv not in krutki_data:
            krutki_data[nazv] = 0
        if igrok not in krutki_data:
            krutki_data[igrok] = 0

        if krutki_data[igrok] > 0 or krutki_data[igrok] == 0:
            krutki_data[nazv] -= summa
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)




        msg = bot.send_message(message.chat.id, f"✅| @{igrok} снял у @{nazv} {summa} круток!")


'''                                      ДЛЯ БЕСЕДЫ ЗАПИСЬ В JSON                      '''








def write_commands(message):
    chat = message.chat.id


    if message.from_user.id == ls or message.from_user.id == tanya:
        user_id = message.from_user.id
        user_name = message.from_user.username
        respons1e = f"📌{user_id} ({user_name}) использовал команду /записать команды"
        bot.send_message(consolee, respons1e)
    # Проверяем, является ли сообщение командой "записать роли"
        if message.text.lower().startswith('/записать_команды'):
        # Получаем текст после команды
            text = message.text[len('/записать_команды'):].strip()

            if len(text) > 0:
            # Записываем текст в файл roli.json
                with open('commands.json', 'w') as file:
                    data = {
                        'command': text
                    }
                    json.dump(data, file)

                response = 'Текст успешно записан в commands.json!'
                newtxt = "📌 Новый текст для 'команды' успешно записан"
                bot.send_message(consolee, newtxt)
            else:
                response = 'Вы не ввели текст для записи в commands.json'
        else:
            response = 'Неизвестная команда'

        bot.reply_to(message, response)

def write_rest(message):
    if message.from_user.id == ls or message.from_user.id == tanya:
        user_id = message.from_user.id
        user_name = message.from_user.username
        respons1e = f"📌{user_id} ({user_name}) использовал команду /записать ресты"
        bot.send_message(consolee, respons1e)
    # Проверяем, является ли сообщение командой "записать роли"
        if message.text.lower().startswith('/записать_ресты'):
        # Получаем текст после команды
            text = message.text[len('/записать_ресты'):].strip()
            if len(text) > 0:
            # Записываем текст в файл roli.json
                with open('resti.json', 'w') as file:
                    data = {
                        'rest': text
                    }
                    json.dump(data, file)
                response = 'Текст успешно записан в resti.json!'
                newtxt = "📌 Новый текст для 'ресты' успешно записан"
                bot.send_message(consolee, newtxt)
            else:
                response = 'Вы не ввели текст для записи в resti.json'
        else:
            response = 'Неизвестная команда'
        bot.reply_to(message, response)

def write_roles(message):
    if message.from_user.id == ls or message.from_user.id == tanya:
        user_id = message.from_user.id
        user_name = message.from_user.username
        respons1e = f"📌{user_id} ({user_name}) использовал команду /записать роли"
        bot.send_message(consolee, respons1e)
    # Проверяем, является ли сообщение командой "записать роли"
        if message.text.lower().startswith('/записать_роли'):
        # Получаем текст после команды
            text = message.text[len('/записать_роли'):].strip()
            if len(text) > 0:
            # Записываем текст в файл roli.json
                with open('roles.json', 'w') as file:
                    data = {
                        'role': text
                    }
                    json.dump(data, file)
                response = 'Текст успешно записан в roles.json!'
                newtxt = "📌 Новый текст для 'роли' успешно записан"
                bot.send_message(consolee, newtxt)
            else:
                response = 'Вы не ввели текст для записи в roles.json'
        else:
            response = 'Неизвестная команда'
        bot.reply_to(message, response)