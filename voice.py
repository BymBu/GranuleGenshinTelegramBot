

from tokens import bot, ls, chat_id, tanya, chat_game
import os
import random
import sconsole
import time


def random_voice(message):

    chat = message.chat.id
    music_folder = "musicrand"  # Укажите путь к папке с музыкой
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    chat = message.chat.id
    with open(music_path, 'rb') as music:
        bot.send_audio(chat, music)
    sconsole.send_console(message)

def lox(message):

    chat = message.chat.id
    sent_message = bot.send_message(chat, "☑️")
    time.sleep(0.3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=sent_message.message_id,
                          text="✅")
    time.sleep(1)
    # Удаляем сообщение
    bot.delete_message(chat, sent_message.message_id)
    voice_path = "voice\лох жизнь выбрал.ogg"  # здесь указывается путь к голосовому файлу
    with open(voice_path, "rb") as voice:
        bot.send_voice(chat, voice)
    sconsole.send_console(message)

def tilt(message):

    chat = message.chat.id
    music_folder = "depres"  # Укажите путь к папке с музыкой
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    chat = message.chat.id
    with open(music_path, 'rb') as music:
        bot.send_audio(chat, music)
    user_id = message.from_user.id
    user_name = message.from_user.username
    sconsole.send_console(message)

def trash(message):

    music_folder = "jtrash"  # Укажите путь к папке с музыкой
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    chat = message.chat.id
    with open(music_path, 'rb') as music:
        bot.send_audio(chat, music)
    user_id = message.from_user.id
    user_name = message.from_user.username
    sconsole.send_console(message)

def phonki(message):

    music_folder = "phonk"  # Укажите путь к папке с музыкой
    music_files = os.listdir(music_folder)
    random_music = random.choice(music_files)
    music_path = os.path.join(music_folder, random_music)
    chat = message.chat.id
    with open(music_path, 'rb') as music:
        bot.send_audio(chat, music)
    user_id = message.from_user.id
    user_name = message.from_user.username
    sconsole.send_console(message)