from tokens import chat_id, bot, consolee, ls
import time
from telebot import types
import json
def send_instructions(message):
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

def instr(message):
    if message.chat.id == chat_id or message.chat.id == ls:
        send_instructions(message)


def rests(message):
    if message.chat.id == chat_id or message.chat.id == ls:
        sticker_id = 'CAACAgIAAxkBAAEJ69pkzQdkwvrc2lAFt64-a9tmvHh0qgACmjEAAltXaUpknhQ3hgEsJS8E'
        bot.send_sticker(message.chat.id, sticker_id)
        with open('resti.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        bot.reply_to(message, f"{data['rest']}")

def fludcommands(message):
    if message.chat.id == chat_id or message.chat.id == ls:
        with open('commands.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        bot.reply_to(message, f"{data['command']}")

def rolies(message):
    if message.chat.id == chat_id or message.chat.id == ls:
        with open('roles.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        bot.reply_to(message, f"{data['role']}")
