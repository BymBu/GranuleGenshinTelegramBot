import json
import sconsole
from tokens import bot
from telebot import types




def clanlist(message):
    sconsole.send_console(message)
    chat_id = message.chat.id
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)

    if clans:
        clans_list = '\n'.join(clans)
        bot.send_message(chat_id, f"🌱| Список кланов:\n{clans_list}")
    else:
        bot.send_message(chat_id, "💔| Кланов нет")


def send_my_clan(message):
    user = message.from_user.username
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)

    for clan_name in clans:
        clan = clans[clan_name]
        if user in clan['users']:
            owner = clan['users'][0]
            members_list = ', '.join([f"<a href='https://t.me/{member}'>{member}</a>" for member in clan['users']])
            kazna = clan.get('kazna', 0)
            if kazna < 20:
                level = 1
                attent = 'До следующего уровня должно быть  - 20'

            if kazna >= 20:
                level = 2
                attent = 'До следующего уровня должно быть  - 40'
            if kazna >= 40:
                level = 3
                attent = 'До следующего уровня должно быть  - 60'
            if kazna >= 60:
                level = 4
                attent = 'До следующего уровня должно быть  - 80'
            if kazna >= 80:
                level = 5
                attent = 'До следующего уровня должно быть  - 120'
            if kazna >= 120:
                level = 6
                attent = 'До следующего уровня должно быть  - 200'
            if kazna >= 200:
                level = 7
                attent = 'До следующего уровня должно быть  - 240'
            if kazna >= 240:
                level = 8
                attent = 'До следующего уровня должно быть  - 280'
            if kazna >= 280:
                level = 9
                attent = 'До следующего уровня должно быть  - 360'
            if kazna >= 360:
                level = 10
                attent = 'До следующего уровня должно быть  - 420'
            if kazna >= 420:
                level = 11
                attent = 'До следующего уровня должно быть  - 500'
            if kazna >= 500:
                level = 12
                attent = 'До следующего уровня должно быть  - 550'
            if kazna >= 550:
                level = 13
                attent = 'До следующего уровня должно быть  - 650'
            if kazna >= 650:
                level = 14
                attent = 'До следующего уровня должно быть  - 720'
            if kazna >= 720:
                level = 15
                attent = 'До следующего уровня должно быть  - 850'
            if kazna >= 850:
                level = 16
                attent = 'До следующего уровня должно быть  - 1000'
            if kazna >= 1000:
                level = 17
                attent = 'До следующего уровня должно быть  - 1200'
            if kazna >= 1200:
                level = 18
                attent = 'До следующего уровня должно быть  - 1500'
            if kazna >= 1500:
                level = 19
                attent = 'До следующего уровня должно быть  - 2000'
            if kazna >= 2000:
                level = 20
                attent = 'На данный момент у вас МАКС. ЛВЛ!'

            # Форматирование сообщения с помощью HTML
            response = f"💻| Вы состоите в клане '<b>{clan_name}</b>'.\n\n🍓| ЛВЛ - <b>{level}</b>\n✨| Казна - <b>{kazna}</b>\n💀| {attent}\n\n👑| Владелец - <a href='https://t.me/{owner}'>{owner}</a>\n🤷🏻| Участники - {members_list}"
            bot.reply_to(message, response, parse_mode='HTML', disable_notification=True, disable_web_page_preview=True)
            return

    bot.reply_to(message, "️❌| Вы не состоите ни в одном клане", disable_notification=True)


def add_to_kazna(message):
    sconsole.send_console(message)
    args = message.text.split(' ', 1)
    if len(args) < 2:
        bot.reply_to(message, "❌| Укажите сумму для добавления в казну.")
        return

    try:
        amount = int(args[1])
    except ValueError:
        bot.reply_to(message, "❌| Некорректная сумма. Введите целое число.")
        return

    user_username = message.from_user.username.replace('@', '')

    # Списываем средства у пользователя
    krutki_file = 'krutki.json'
    with open(krutki_file, 'r') as file:
        krutki_data = json.load(file)
    if user_username not in krutki_data:
        krutki_data[user_username] = 0

    if krutki_data[user_username] >= amount:
        krutki_data[user_username] -= amount
        with open(krutki_file, 'w') as file:
            json.dump(krutki_data, file)

    # Добавляем средства в казну клана
        with open('clans.json', 'r', encoding='utf-8') as f:
            clans = json.load(f)

        for clan_name, clan_info in clans.items():
            if user_username in clan_info['users']:
                clan_info['kazna'] = clan_info.get('kazna', 0) + amount
                with open('clans.json', 'w', encoding='utf-8') as f:
                    json.dump(clans, f, indent=4, ensure_ascii=False)
                bot.reply_to(message, f"✅| Сумма {amount} успешно добавлена в казну клана '{clan_name}'.")

                return
    else:
        bot.reply_to(message, f"❌| Недостаточно средств")
        return

    bot.reply_to(message, "❌| Вы не состоите в каком-либо клане.")



def create_clan(message):
    sconsole.send_console(message)
    user = message.from_user.username
    with open('clans.json', 'r') as f:
        clans = json.load(f)

    for clan, members in clans.items():
        if user in members:
            bot.reply_to(message, "❌| Вы уже состоите в клане")
            return

    # Проверяем, состоит ли пользователь в других кланах
    for clan in clans.values():
        if user in clan['users']:
            bot.reply_to(message, "❌| Вы уже состоите в другом клане")
            return

    name = message.text.split("клан")[1].strip()
    if not name:
        bot.reply_to(message, "❌| Пожалуйста, укажите имя клана после команды")
        return

    krutki = 0

    krutki_file = 'krutki.json'
    with open(krutki_file, 'r') as file:
        krutki_data = json.load(file)
    if user not in krutki_data:
        krutki_data[user] = 0

    if krutki_data[user] >= 15:
        krutki_data[user] -= 15
        with open('krutki.json', 'w') as file:
            json.dump(krutki_data, file)

        user_username = message.from_user.username
        with open('clans.json', 'r', encoding='utf-8') as f:
            clans = json.load(f)

        if name in clans:
            bot.reply_to(message, "❌| Клан с таким названием уже существует.")
            return

        clan = {name: {'users': [user_username], 'krutki': krutki}}
        clans.update(clan)

        with open('clans.json', 'w', encoding='utf-8') as f:
            json.dump(clans, f, indent=4)

        bot.reply_to(message, f"✅| Клан {name} успешно создан! Вы являетесь его создателем")
    else:
        bot.reply_to(message, '❌| Недостаточно средств. Стоимость - 15 круток')

def delete_clan(message):
    sconsole.send_console(message)
    user = message.from_user.username
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)

    # Поиск клана, в котором пользователь является владельцем
    clan_name = None
    for name, info in clans.items():
        if info['users'][0] == user:
            clan_name = name
            break

    if not clan_name:
        bot.reply_to(message, "❌| Вы не являетесь владельцем ни одного клана.")
        return

    # Удаление клана
    del clans[clan_name]
    with open('clans.json', 'w', encoding='utf-8') as f:
        json.dump(clans, f, indent=4, ensure_ascii=False)

    bot.reply_to(message, f"✅| Клан {clan_name} успешно удален.")


def invite_to_clan(message):
    sconsole.send_console(message)
    args = message.text.split(' ', 2)
    if len(args) < 2:
        bot.reply_to(message, "❌| Укажите пользователя для приглашения.")
        return

    user_username = args[1].replace('@', '')
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)

    for clan_name, clan_info in clans.items():
        if clan_info['users'][0] == message.from_user.username:
            if user_username == message.from_user.username:
                bot.reply_to(message, "❌| Вы уже являетесь участником клана.")
                return

            if user_username in clan_info['users']:
                bot.reply_to(message, "❌| Пользователь уже состоит в этом клане.")
                return

            for other_clan_name, other_clan_info in clans.items():
                if user_username in other_clan_info['users']:
                    bot.reply_to(message, f"❌| Пользователь уже состоит в клане '{other_clan_name}'.")
                    return

            clan_info['users'].append(user_username)
            with open('clans.json', 'w', encoding='utf-8') as f:
                json.dump(clans, f, indent=4, ensure_ascii=False)
            bot.reply_to(message, f"✅| Пользователь @{user_username} успешно добавлен в клан '{clan_name}'.")
            return

    bot.reply_to(message, "❌| Вы не являетесь владельцем ни одного клана.")


def remove_from_clan(message):
    sconsole.send_console(message)
    args = message.text.split(' ', 2)
    if len(args) < 2:
        bot.reply_to(message, "❌| Укажите пользователя для удаления из клана.")
        return

    user_username = args[1].replace('@', '')
    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)

    for clan_name, clan_info in clans.items():
        if clan_info['users'][0] == message.from_user.username:
            if user_username == message.from_user.username:
                bot.reply_to(message, "❌| Вы не можете удалить себя из клана.")
                return

            if user_username not in clan_info['users']:
                bot.reply_to(message, "❌| Пользователь не состоит в этом клане.")
                return

            clan_info['users'].remove(user_username)
            with open('clans.json', 'w', encoding='utf-8') as f:
                json.dump(clans, f, indent=4, ensure_ascii=False)
            bot.reply_to(message, f"✅| Пользователь @{user_username} успешно удален из клана '{clan_name}'.")
            return

    bot.reply_to(message, "❌| Вы не являетесь владельцем ни одного клана.")

def leave_clan(message):
    user_username = message.from_user.username.replace('@', '')

    with open('clans.json', 'r', encoding='utf-8') as f:
        clans = json.load(f)
    sconsole.send_console(message)
    for clan_name, clan_info in clans.items():
        if user_username in clan_info['users']:
            if user_username == clan_info['users'][0]:
                bot.reply_to(message, "⚠️| Вы являетесь владельцем клана. Если вы хотите удалить клан, воспользуйтесь командой 'Удалить клан'.")
                return

            clan_info['users'].remove(user_username)
            with open('clans.json', 'w', encoding='utf-8') as f:
                json.dump(clans, f, indent=4, ensure_ascii=False)
            bot.reply_to(message, f"✅| Вы успешно покинули клан '{clan_name}'.")
            return

    bot.reply_to(message, "❌| Вы не состоите в каком-либо клане.")
