from tokens import bot, consolee


def send_console(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id
    chat_type = message.chat.type
    chat_name = message.chat.title
    location = message.location
    command = message.text.split()[0]
    response = f"‼️Пользователь @{username} использовал команду {command}!"
    response += f"\n👩🏻‍🦱| ID пользователя: {user_id}"
    response += f"\n👕| Имя пользователя: {username}"
    response += f"\n📛| Имя: {first_name}"
    response += f"\n📛| Фамилия: {last_name}"
    response += f"\n💻| ID чата: {chat_id}"
    response += f"\n📦| Тип чата: {chat_type}"
    response += f"\n✅| Название чата: {chat_name}"
    response += f"\n🗺️| Локация: {location}"

    bot.send_message(consolee, response)

def send_newmemb(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    chat_id = message.chat.id
    chat_type = message.chat.type
    chat_name = message.chat.title
    location = message.location
    response = f"🔥️Пользователь @{username} присоединился к {chat_name}!"
    response += f"\n👩🏻‍🦱| ID пользователя: {user_id}"
    response += f"\n👕| Имя пользователя: {username}"
    response += f"\n📛| Имя: {first_name}"
    response += f"\n📛| Фамилия: {last_name}"
    response += f"\n💻| ID чата: {chat_id}"
    response += f"\n📦| Тип чата: {chat_type}"
    response += f"\n✅| Название чата: {chat_name}"
    response += f"\n🗺️| Локация: {location}"

    bot.send_message(consolee, response)