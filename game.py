from tokens import bot, consolee, chat_game, pers1, pers2, persh, persh2
from telebot import types
import time
import json
import datetime
import random
import sconsole




def send_help(message):
    with open('roli.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        helpa = data['help']
    bot.send_message(message.chat.id, helpa)


def achivment(message):
    bot.send_message(message.chat.id,
                           f"📋| Достижения:\nНовичок - имейте хотя-бы 1 крутку у себя на счету\nЩедрый - поделитесь крутками (пай @name число) 5 раз\nКрутильщик - Открутите 50 круток!\nКрутильщик 2 - открутите 200 круток!")
    sconsole.send_console(message)

def shop(message):

    keyboard = types.InlineKeyboardMarkup()
    top_button2 = types.InlineKeyboardButton("1", callback_data='товар2')
    top_button3 = types.InlineKeyboardButton("2", callback_data='товар3')
    top_button4 = types.InlineKeyboardButton("3", callback_data='товар4')
    top_button5 = types.InlineKeyboardButton("4", callback_data='товар5')
    keyboard.row(top_button2, top_button3, top_button4, top_button5)
    text = """
    ⚠️| *ATTENTION!* При нажатии инлайн кнопки внизу бот сразу оформляет вашу покупку!
    
🏪| *Выберите желаемый товар:*
👑 *Товар 1* = VIP статус. Цена - 20 круток
🅱️ *Товар 2* = буст (повышена вероятность  персов) на 3 часа. 
Цена - 15 круток (Работает на всех)
🌱 *Товар 3* = 1 крутка за пыльцу. Цена - 160 пыльцы
🌱 *Товар 4* = 10 Круток за пыльцу. Цена - 1600 пыльцы"""

    bot.send_message(message.chat.id, text, parse_mode='Markdown', reply_markup=keyboard)
    sconsole.send_console(message)
def vipferma(message):
    with open('vip.json', 'r') as file:
        vip_data = json.load(file)

    if message.from_user.username in vip_data and (
            datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[message.from_user.username]),
                                                                 "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(days=7):

        user_name = message.from_user.username

        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open('viptime.json', 'r') as file:
            timers = json.load(file)

        if str(user_name) in timers:
            last_time = datetime.datetime.strptime(timers[str(user_name)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time

            if time_difference.total_seconds() < 3600:
                remaining_time = datetime.timedelta(seconds=3600 - time_difference.total_seconds())
                bot.reply_to(message, f"❌ ОТКАЗ | фармить можно раз в час\nПопробуй еще раз через {remaining_time}")
                sconsole.send_console(message)
                return

        timers[str(user_name)] = current_time

        with open('viptime.json', 'w') as file:
            json.dump(timers, file)


        user_name = message.from_user.username
        krutki_file = 'krutki.json'
        timers_file = 'viptime.json'

        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        with open(timers_file, 'r') as file:
            timers_data = json.load(file)

        if user_name not in krutki_data:
            krutki_data[user_name] = 0

        krutki_count = random.randint(6, 10)
        krutki_data[user_name] += krutki_count

        with open(krutki_file, 'w') as file:
            json.dump(krutki_data, file)
        if message.chat.id == chat_game:
            bot.reply_to(message,
                         f"🥳| Вы получили {krutki_count} круток!\n💥| Текущее количество Ваших круток: {krutki_data[user_name]}\n❤️‍🔥| Профиль - Кто я")
        else:
            bot.reply_to(message,
                         f"🥳| Вы получили {krutki_count} круток!\n💥| Текущее количество Ваших круток: {krutki_data[user_name]}\n❤️‍🔥| Профиль - Кто я\nКРУТИТЬ В ГЕЙМ ЧАТЕ - https://t.me/+R_uQeMG26TVkYzQy")
        sconsole.send_console(message)
    else:
        bot.send_message(message.chat.id, "❌| У вас нет VIP статуса! Купить - магазин")
        sconsole.send_console(message)


def defferma(message):
    try:
        user_id = message.from_user.id
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('timers.json', 'r') as file:
            timers = json.load(file)
        if str(user_id) in timers:
            last_time = datetime.datetime.strptime(timers[str(user_id)], "%Y-%m-%d %H:%M:%S")
            time_difference = datetime.datetime.now() - last_time
            if time_difference.total_seconds() < 3600:
                remaining_time = datetime.timedelta(seconds=3600 - time_difference.total_seconds())
                bot.reply_to(message, f"❌ ОТКАЗ | фармить можно раз в час\nПопробуй еще раз через {remaining_time}")
                sconsole.send_console(message)
                return

        timers[str(user_id)] = current_time

        with open('timers.json', 'w') as file:
            json.dump(timers, file)
        user_name = message.from_user.username
        krutki_file = 'krutki.json'
        timers_file = 'timers.json'
        with open(krutki_file, 'r') as file:
            krutki_data = json.load(file)
        with open(timers_file, 'r') as file:
            timers_data = json.load(file)
        if user_name not in krutki_data:
            krutki_data[user_name] = 0
        krutki_count = random.randint(3, 6)
        krutki_data[user_name] += krutki_count
        with open(krutki_file, 'w') as file:
            json.dump(krutki_data, file)
        if message.chat.id == chat_game:
            bot.reply_to(message,
                         f"🥳| Вы получили {krutki_count} круток!\n💥| Текущее количество Ваших круток: {krutki_data[user_name]}\n❤️‍🔥| Профиль - Кто я")
        else:
            bot.reply_to(message,
                         f"🥳| Вы получили {krutki_count} круток!\n💥| Текущее количество Ваших круток: {krutki_data[user_name]}\n❤️‍🔥| Профиль - Кто я\nКРУТИТЬ В ГЕЙМ ЧАТЕ - https://t.me/+R_uQeMG26TVkYzQy")
        sconsole.send_console(message)
    except ConnectionError:
        bot.reply_to(message, 'Ошибка, попробуйте еще раз')


def peredacha(message):
    nazv = message.text.split("@")[1].split()[0]
    summa = int(message.text.split()[-1])
    igrok = message.from_user.username

    user = message.from_user.username
    krutki_file = 'krutki.json'
    with open(krutki_file, 'r') as file:
        krutki_data = json.load(file)
    if nazv not in krutki_data:
        krutki_data[nazv] = 0
    if igrok not in krutki_data:
        krutki_data[igrok] = 0
    if krutki_data[igrok] >= summa:
        krutki_data[igrok] -= summa
        krutki_data[nazv] += summa
        with open('krutki.json', 'w') as file:
            json.dump(krutki_data, file)
        msg = bot.send_message(message.chat.id, f"✅| @{igrok} перевёл @{nazv} {summa} круток!")
        with open('pay.json', 'r') as file:
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
        with open('pay.json', 'w') as file:
            json.dump(data, file)
    else:
        msg = bot.send_message(message.chat.id, f"❌| @{igrok} Недостаточно круток!")
    sconsole.send_console(message)


def kto_ti(message):
    nazv = message.text.split("@")[1]
    lico = random.randint(1, 3)
    user = message.from_user.username
    if lico == 1:
        kek = "👩🏿"
    elif lico == 2:
        kek = "👩🏻"
    elif lico == 3:
        kek = "👱🏻‍♂️"
    with open('VIP.json', 'r') as file:
        vip_data = json.load(file)
    if nazv in vip_data and (
            datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[nazv]),
                                                                 "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(days=7):
        remaining_time = datetime.timedelta(days=7) - (
                datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[nazv]),
                                                                     "%Y-%m-%d %H:%M:%S"))
        vip = f"👑vip - {remaining_time}"
    else:
        vip = '👑vip - нет'

    krutki_file = 'krutki.json'
    with open(krutki_file, 'r') as file:
        krutki_data = json.load(file)
    if nazv not in krutki_data:
        krutki_data[nazv] = 0
    with open('pil.json', 'r') as pilca:
        pil_data = json.load(pilca)
    if nazv not in pil_data:
        pil_data[nazv] = 0
    with open('molitvi.json', 'r') as file:
        mol_data = json.load(file)
    if nazv not in mol_data:
        mol_data[nazv] = 0
    if mol_data[nazv] >= 50:
        krut_dost = '✅'
    else:
        krut_dost = '❌'
    if mol_data[nazv] >= 200:
        krut_dost2 = '✅'
    else:
        krut_dost2 = '❌'
    with open('osebe.json', 'r', encoding='utf-8') as file:
        osebe = json.load(file)
    if nazv not in osebe:
        osebe[nazv] = 'описания пока нет'
    with open('pers.json', 'r', encoding='utf-8') as file:
        perss = json.load(file)
    if nazv not in perss:
        perss[nazv] = '0'
    with open('pers2.json', 'r', encoding='utf-8') as file:
        persss = json.load(file)
    if nazv not in persss:
        persss[nazv] = '0'
    krutki_file = 'krutki.json'
    with open(krutki_file, 'r', encoding='utf-8') as file:
        krutki_data = json.load(file)
    if nazv not in krutki_data:
        krutki_data[nazv] = 0
    if krutki_data[nazv] >= 1:
        novichek = '✅'
    else:
        novichek = '❌'
    with open(krutki_file, 'w', encoding='utf-8') as file:
        json.dump(krutki_data, file)
    with open('pay.json', 'r', encoding='utf-8') as file:
        datapay = json.load(file)
    if nazv not in datapay:
        datapay[nazv] = 0
    if datapay[nazv] >= 5:
        shedr = '✅'
    else:
        shedr = "❌"
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)
    user_clan = ''
    for clan_name, clan_info in clans.items():
        if nazv in clan_info['users']:
            user_clan = clan_name
            break
    bot.send_message(message.chat.id, f"{kek}| Информация о @{nazv}\n\n{vip}\n\n💬| О себе:\n{osebe[nazv]}\n\n🏰| Клан: {user_clan}\n\n🌱| Круток: {krutki_data[nazv]}\n✨| Пыльца: {pil_data[nazv]}\n🍓| Откручено круток: {mol_data[nazv]}\n\nВыбито персонажей:\n4️⃣⭐| {persss[nazv]}\n5️⃣⭐| {perss[nazv]}\n\n⭐| Достижения:\nНовичок - {novichek}\nЩедрый - {shedr}\nКрутильщик - {krut_dost}\nКрутильщик 2 - {krut_dost2}")
    sconsole.send_console(message)
def ktoya(message):
    user_name = message.from_user.username
    lico = random.randint(1, 7)
    user = message.from_user.username
    if lico == 1:
        kek = "👩🏿"
    elif lico == 2:
        kek = "👩🏻"
    elif lico == 3:
        kek = "👱🏻‍♂️"
    elif lico == 4:
        kek = "👴🏼️"
    elif lico == 5:
        kek = "👨‍🦲️"
    elif lico == 6:
        kek = "👹️"
    elif lico == 7:
        kek = "👱🏿‍♀️"
    with open('VIP.json', 'r') as vipka:
        vip_data = json.load(vipka)
    if message.from_user.username in vip_data and (
            datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[message.from_user.username]),
                                                                 "%Y-%m-%d %H:%M:%S")) < datetime.timedelta(days=7):
        remaining_time = datetime.timedelta(days=7) - (
                datetime.datetime.now() - datetime.datetime.strptime(str(vip_data[message.from_user.username]),
                                                                     "%Y-%m-%d %H:%M:%S"))
        vip = f"👑vip - {remaining_time}"
    else:
        vip = '👑vip - нет'
    krutki_file = 'krutki.json'
    with open(krutki_file, 'r') as krutki:
        krutki_data = json.load(krutki)
    if user_name not in krutki_data:
        krutki_data[user_name] = 0
    with open('pil.json', 'r') as pilca:
        pil_data = json.load(pilca)
    if user_name not in pil_data:
        pil_data[user_name] = 0
    with open('molitvi.json', 'r') as molitv:
        data = json.load(molitv)
    if user_name not in data:
        data[user_name] = 0
    if data[user_name] >= 50:
        krut_dost = '✅'
    else:
        krut_dost = '❌'
    if data[user_name] >= 200:
        krut_dost2 = '✅'
    else:
        krut_dost2 = '❌'
    with open('osebe.json', 'r', encoding='utf-8') as opis:
        osebe = json.load(opis)
    if user_name not in osebe:
        osebe[user_name] = 'описания пока нет'
    with open('pers.json', 'r', encoding='utf-8') as chetr:
        perss = json.load(chetr)
    if user_name not in perss:
        perss[user_name] = '0'
    with open('pers2.json', 'r', encoding='utf-8') as legi:
        persss = json.load(legi)
    if user_name not in persss:
        persss[user_name] = '0'
    krutki_file = 'krutki.json'
    with open(krutki_file, 'r', encoding='utf-8') as file:
        krutki_data = json.load(file)
    if user_name not in krutki_data:
        krutki_data[user_name] = 0
    if krutki_data[user_name] >= 1:
        novichek = '✅'
    else:
        novichek = '❌'
    with open('pay.json', 'r', encoding='utf-8') as file:
        datapay = json.load(file)
    if user_name not in datapay:
        datapay[user_name] = 0
    if datapay[user_name] >= 5:
        shedr = '✅'
    else:
        shedr = "❌"
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)
    user_clan = ''
    for clan_name, clan_info in clans.items():
        if user_name in clan_info['users']:
            user_clan = clan_name
            break
    user_name = message.from_user.username
    bot.send_message(message.chat.id, f"{kek}| Информация о @{user_name}\n\n{vip}\n\n💬| О себе:\n{osebe[user_name]}\n\n🏰| Клан: {user_clan}\n\n🌱| Круток: {krutki_data[user_name]}\n✨| Пыльца: {pil_data[user_name]}\n🍓| Откручено круток: {data[user]}\n\nВыбито персонажей:\n4️⃣⭐| {persss[user_name]}\n5️⃣⭐| {perss[user_name]}\n\n⭐| Достижения:\nНовичок - {novichek}\nЩедрый - {shedr}\nКрутильщик - {krut_dost}\nКрутильщик 2 - {krut_dost2}")
    sconsole.send_console(message)


def top(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("🌱Крутки", callback_data='select_top: крутки')
    btn2 = types.InlineKeyboardButton("🍓Откр. Крутки", callback_data='select_top: откр. крутки')
    btn3 = types.InlineKeyboardButton("✨Леги", callback_data='select_top: леги')
    btn4 = types.InlineKeyboardButton("💻Кланы", callback_data='select_top: кланы')
    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(message.chat.id, "Выберите желаемый ТОП-10:", reply_markup=markup)
    sconsole.send_console(message)


def krytki(message):
    a = pers1
    b = pers2
    bot.send_message(message.chat.id,
                          f"ГЕЙМЕРСКОЕ ОТДЕЛЕНИЕ (ТАМ КРУТИТЬ ПЕРСОНАЖЕЙ) https://t.me/+R_uQeMG26TVkYzQy \n😈 Правила просты. Тебе нужно выбрать между\nактуальными 💥Баннерами, кого ты хочешь.\nДля круток используй команды\n• Крутить {a} (1 или 10)\n• Крутить {b} (1 или 10)\n• Крутить стандарт (1 или 10)\n• Крутить оружейный (1 или 10)")
    sconsole.send_console(message)








