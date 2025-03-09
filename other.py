from tokens import bot, chat_shop, chat_id
from telebot import types
import time
import json
import datetime
import sconsole


def send_inst(message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.row(
        types.InlineKeyboardButton(text='пон', callback_data='page2'),
    )
    with open('roli.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        instructions = data['inst']
        instructions2 = data['inst2']

    message_text = f"Глава 1\n{instructions}"
    mess = f'Глава 2\n{instructions2}'
    bot.send_message(message.chat.id, message_text, reply_markup=inline_keyboard)
    bot.send_message(message.chat.id, mess, reply_markup=inline_keyboard)




def gamehelp(message, help):

    message_text = f"{help}"
    bot.send_message(message.chat.id, message_text)



def bottyt(message):
    bot.send_message(message.chat.id, '✅| На месте')
    sconsole.send_console(message)


def opisanie(message):

    user_name = message.from_user.username
    description = message.text.replace('+описание', '')

    with open('osebe.json', 'r') as file:
        data = json.load(file)

    if str(user_name) not in data:
        data[str(user_name)] = []

    data[str(user_name)] = description[:50]

    with open('osebe.json', 'w') as file:
        json.dump(data, file)

    bot.reply_to(message, '✅ Описание сохранено!')
    sconsole.send_console(message)


def newmemb(message, instructions, help):
    if message.chat.id == chat_id:
        for member in message.new_chat_members:
            chat = message.chat.id
            voice_path = "voice/приветствие.ogg"

            with open(voice_path, "rb") as voice:
                bot.send_voice(chat, voice)
            send_inst(message, instructions)
            sconsole.send_newmemb(message)
    else:
        for member in message.new_chat_members:
            chat = message.chat.id

            voice_path = "voice/приветствие.ogg"

            with open(voice_path, "rb") as voice:
                bot.send_voice(chat, voice)
            gamehelp(message, help)
            sconsole.send_newmemb(message)

def selectop(call):
    chat_id = call.message.chat.id

    if call.data == 'select_top: крутки':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🌱Крутки", callback_data='select_top: крутки')
        btn2 = types.InlineKeyboardButton("🍓Откр. Крутки", callback_data='select_top: откр. крутки')
        btn3 = types.InlineKeyboardButton("✨Леги", callback_data='select_top: леги')
        btn4 = types.InlineKeyboardButton("💻Кланы", callback_data='select_top: кланы')
        markup.add(btn1, btn2, btn3, btn4)
        with open('krutki.json', 'r') as json_file:
            data = json.load(json_file)

        # Сортировка данных по убыванию
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        total_count = sum(data.values())
        result_message = "📱| Топ 10 пользователей по КРУТКАМ:\n"
        top_10 = sorted_data[:10]
        for i, item in enumerate(top_10):
            result_message += f"{i + 1}. @{item[0]} — {item[1]}\n"
        tc = str(total_count)
        result_message += f'🥵| Сумма всех круток — {tc}'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=result_message, reply_markup=markup)
    elif call.data == 'select_top: откр. крутки':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🌱Крутки", callback_data='select_top: крутки')
        btn2 = types.InlineKeyboardButton("🍓Откр. Крутки", callback_data='select_top: откр. крутки')
        btn3 = types.InlineKeyboardButton("✨Леги", callback_data='select_top: леги')
        btn4 = types.InlineKeyboardButton("💻Кланы", callback_data='select_top: кланы')
        markup.add(btn1, btn2, btn3, btn4)
        with open('molitvi.json', 'r') as json_file:
            moldata = json.load(json_file)
        sorted_data2 = sorted(moldata.items(), key=lambda x: x[1], reverse=True)
        total_count2 = sum(moldata.values())
        result_message = "📱| Топ 10 пользователей\nпо ОТКРУЧЕННЫМ КРУТКАМ:\n"
        top_10 = sorted_data2[:10]
        for i, item in enumerate(top_10):
            result_message += f"{i + 1}. @{item[0]} — {item[1]}\n"
        tc2 = str(total_count2)
        result_message += f'🥵| Сумма всех открученных круток — {tc2}'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=result_message, reply_markup=markup)
    elif call.data == 'select_top: леги':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🌱Крутки", callback_data='select_top: крутки')
        btn2 = types.InlineKeyboardButton("🍓Откр. Крутки", callback_data='select_top: откр. крутки')
        btn3 = types.InlineKeyboardButton("✨Леги", callback_data='select_top: леги')
        btn4 = types.InlineKeyboardButton("💻Кланы", callback_data='select_top: кланы')
        markup.add(btn1, btn2, btn3, btn4)
        with open('pers.json', 'r') as json_file:
            moldata = json.load(json_file)
        sorted_data2 = sorted(moldata.items(), key=lambda x: x[1], reverse=True)
        total_count2 = sum(moldata.values())
        result_message = "📱| Топ 10 пользователей\nпо ЛЕГЕНДАРКАМ:\n"
        top_10 = sorted_data2[:10]
        for i, item in enumerate(top_10):
            result_message += f"{i + 1}. @{item[0]} — {item[1]}\n"
        tc2 = str(total_count2)
        result_message += f'🥵| Сумма всех Легендарок — {tc2}'
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=result_message, reply_markup=markup)
    elif call.data == 'select_top: кланы':
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🌱Крутки", callback_data='select_top: крутки')
        btn2 = types.InlineKeyboardButton("🍓Откр. Крутки", callback_data='select_top: откр. крутки')
        btn3 = types.InlineKeyboardButton("✨Леги", callback_data='select_top: леги')
        btn4 = types.InlineKeyboardButton("💻Кланы", callback_data='select_top: кланы')
        markup.add(btn1, btn2, btn3, btn4)
        with open('clans.json', 'r', encoding='utf-8') as f:
            clans = json.load(f)

        if not clans:
            result_message = "🌟| Топ 10 кланов по уровню:\n\n"
            result_message += "💔 Пусто 💔"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=result_message)
            return

        # Создаем список кланов
        clan_list = []
        for clan_name, clan_info in clans.items():
            kazna = clan_info.get('kazna', 0)
            level = None
            if kazna < 20:
                level = 1

            if kazna >= 20:
                level = 2

            if kazna >= 40:
                level = 3

            if kazna >= 60:
                level = 4

            if kazna >= 80:
                level = 5

            if kazna >= 120:
                level = 6

            if kazna >= 200:
                level = 7

            if kazna >= 240:
                level = 8

            if kazna >= 280:
                level = 9

            if kazna >= 360:
                level = 10

            if kazna >= 420:
                level = 11

            if kazna >= 500:
                level = 12

            if kazna >= 550:
                level = 13

            if kazna >= 650:
                level = 14

            if kazna >= 720:
                level = 15

            if kazna >= 850:
                level = 16

            if kazna >= 1000:
                level = 17

            if kazna >= 1200:
                level = 18

            if kazna >= 1500:
                level = 19

            if kazna >= 2000:
                level = 20

            if level is not None:
                clan_list.append((clan_name, level))

        # Сортируем список по уровню
        sorted_clans = sorted(clan_list, key=lambda x: x[1], reverse=True)

        # Создаем сообщение с топ-10 кланами
        result_message = "🌟| Топ 10 кланов по уровню:\n\n"
        for i, (clan_name, level) in enumerate(sorted_clans[:10]):
            result_message += f"{i + 1}. {clan_name} – {level} уровень\n"

        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=result_message, reply_markup=markup)
    elif call.data == 'товар2':
        # VIP
        user_username = call.from_user.username
        shopil = user_username
        with open('VIP.json', 'r') as vipka:
            vip_data = json.load(vipka)

        if call.from_user.username in vip_data and (
                datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[call.from_user.username]),
                                                                     "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(days=7):
            remaining_time = datetime.timedelta(days=7) - (
                    datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[call.from_user.username]),
                                                                         "%Y-%m-%d %H:%M:%S"))
            bot.answer_callback_query(call.id,
                             text=f'❌| @{shopil} у Вас уже есть Вип! Осталось - {remaining_time}')

        else:

            user_username = call.from_user.username
            shopil = user_username
            krutki_file = 'krutki.json'
            with open(krutki_file, 'r') as file:
                krutki_data = json.load(file)
            if shopil not in krutki_data:
                krutki_data[shopil] = 0

            if krutki_data[shopil] >= 20:
                krutki_data[shopil] -= 20
                with open('krutki.json', 'w') as file:
                    json.dump(krutki_data, file)
                bot.answer_callback_query(call.id,
                                 text=f'✅| Покупка успешно оплачена! @{shopil} с Вашего счёта снято 20 круток!\nВаш VIP статус уже красуется в "Кто я"!')
                response = f"👩🏻‍🦱| @{shopil} купил VIP статус 7дней!"
                bot.send_message(chat_shop, response)

                with open('vip.json', 'r') as file:
                    vip_data = json.load(file)
                if shopil not in vip_data:
                    vip_data[shopil] = 0

                vip_data[call.from_user.username] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                with open('vip.json', 'w') as file:
                    json.dump(vip_data, file, indent=4)
            else:
                user_username = call.from_user.username
                shopil = user_username
                bot.answer_callback_query(call.id,
                                          text=f'❌| Покупка не оплачена! @{shopil} на Вашем балансе недостаточно круток\nФарми = "ферма"')

    elif call.data == 'товар3':
        # VIP
        user_username = call.from_user.username
        shopil = user_username
        krutki_file = 'krutki.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        if shopil not in krutki_data:
            krutki_data[shopil] = 0
        if krutki_data[shopil] >= 15:
            krutki_data[shopil] -= 15
            with open('krutki.json', 'w') as file:
                json.dump(krutki_data, file)
            bot.answer_callback_query(call.id,
                             text=f'✅| Покупка успешно оплачена! @{shopil} с Вашего счёта снято 15 круток!\nБуст на повышенный шанс активирован на 3 часа!')
            response = f"👩🏻‍🦱| @{shopil} купил буст на 3 часа"
            bot.send_message(chat_shop, response)
            main = 'main'
            with open('byst.json', 'r') as file:
                vip_ddata = json.load(file)
            if main not in vip_ddata:
                vip_ddata[main] = 0
            vip_ddata[main] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open('byst.json', 'w') as file:
                json.dump(vip_ddata, file, indent=4)

        else:
            user_username = call.from_user.username
            shopil = user_username
            bot.answer_callback_query(call.id,
                             text=f'❌| Покупка не оплачена! @{shopil} на Вашем балансе недостаточно круток\nФарми = "ферма"')
    elif call.data == 'товар4':
        # VIP
        user_username = call.from_user.username
        shopil = user_username

        with open('pil.json', 'r') as file:
            pil_data = json.load(file)
        if shopil not in pil_data:
            pil_data[shopil] = 0
        if pil_data[shopil] >= 160:
            pil_data[shopil] -= 160
            with open('pil.json', 'w') as file:
                json.dump(pil_data, file)
            bot.answer_callback_query(call.id,
                             text=f'✅| Покупка успешно оплачена! @{shopil} с Вашего счёта снято 160 пыльцы!\nВам выдана 1 крутка!')
            response = f"👩🏻‍🦱| @{shopil} купил 1 крутку за 160 пыльцы"
            bot.send_message(chat_shop, response)

            with open('krutki.json', 'r') as file:
                krut_data = json.load(file)
            if shopil not in krut_data:
                krut_data[shopil] = 1
            krut_data[shopil] += 1

            with open('krutki.json', 'w') as file:
                json.dump(krut_data, file, indent=4)

        else:
            user_username = call.from_user.username
            shopil = user_username
            bot.answer_callback_query(call.id,
                             text=f'❌| Покупка не оплачена! @{shopil} на Вашем балансе недостаточно пыльцы')
    elif call.data == 'товар5':
        # VIP
        user_username = call.from_user.username
        shopil = user_username

        with open('pil.json', 'r') as file:
            pil_data = json.load(file)
        if shopil not in pil_data:
            pil_data[shopil] = 0
        if pil_data[shopil] >= 1600:
            pil_data[shopil] -= 1600
            with open('pil.json', 'w') as file:
                json.dump(pil_data, file)
            bot.answer_callback_query(call.id,
                             text=f'✅| Покупка успешно оплачена! @{shopil} с Вашего счёта снято 1600 пыльцы!\nВам выдана 10 круток!')
            response = f"👩🏻‍🦱| @{shopil} купил 10 круток за 1600 пыльцы"
            bot.send_message(chat_shop, response)

            with open('krutki.json', 'r') as file:
                krut_data = json.load(file)
            if shopil not in krut_data:
                krut_data[shopil] = 1
            krut_data[shopil] += 10

            with open('krutki.json', 'w') as file:
                json.dump(krut_data, file, indent=4)

        else:
            user_username = call.from_user.username
            shopil = user_username
            bot.answer_callback_query(call.id,
                             text=f'❌| Покупка не оплачена! @{shopil} на Вашем балансе недостаточно пыльцы')
    elif call.data == 'delete_yes':
        user = call.message.from_user.username
        with open('clans.json', 'r') as f:
            clans = json.load(f)

        for clan, members in clans.items():
            if user == members[0]:
                del clans[clan]
                with open('clans.json', 'w') as f:
                    json.dump(clans, f, indent=4)
                bot.answer_callback_query(call.id, "Клан успешно удален")
                break   

        else:
            bot.answer_callback_query(call.id, "Вы не являетесь владельцем клана")

    elif call.data == 'delete_no':
        bot.answer_callback_query(call.id, "Удаление клана отменено")











