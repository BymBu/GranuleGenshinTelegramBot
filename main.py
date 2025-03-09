import clans
import flud
import krytku
import sconsole

NUMBERS_ROWS = 40

import atexit

import telebot
from telebot import types
import os
import json
import psutil
import requests
import time
import random
import datetime

# МОДУЛИ

import adm
from tokens import bot, consolee
import voice
import flud
import game
import other
import krytku
import clans
import sconsole
from tokens import pers1, pers2, ls, chat_id, chat_game, chat_shop
context = {}


likes = 0
dislikes = 0


def on_start():
    print("Бот успешно запущен")
    response = f"📌Бот запущен"
    bot.send_message(consolee, response)

on_start()


def on_stop():
    print("Бот успешно выключен")
    response = f"📌Бот выключен"
    bot.send_message(consolee, response)




@atexit.register
def exit_handler():
    on_stop()








with open('roli.json', 'r', encoding="utf-8") as file:
    data = json.load(file)
    instructions = data['inst']
    instructions2 = data['inst2']
    help = data['help']










bot.skip_pending = True




@bot.message_handler(func=lambda message: message.text.lower() == 'инструктаж')
def handle_instructions_command(message):
    flud.instr(message)


@bot.message_handler(commands='start')
def handle_instructions_command(message):
    game.send_help(message)

@bot.message_handler(commands='help')
def handle_instructions_command(message):
    game.send_help(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'помощь')
def handle_instructions_command(message):
    game.send_help(message)






'''                                                     GRANULE GAME                                                                '''

@bot.message_handler(func=lambda message: message.text.startswith('компенсация'))
def compensate(message):
    adm.compins(message)





@bot.message_handler(func=lambda message: message.text.lower() == f'крутить оружейный')
def roles(message):
    krytku.oryj1(message)
@bot.message_handler(func=lambda message: message.text.lower() == f'крутить оружейный 10')
def roles(message):
    krytku.oryj10(message)

@bot.message_handler(func=lambda message: message.text.lower() == f'крутить оружейку')
def roles(message):
    krytku.oryj1(message)
@bot.message_handler(func=lambda message: message.text.lower() == f'крутить оружейку 10')
def roles(message):
    krytku.oryj10(message)

@bot.message_handler(func=lambda message: message.text.lower() == f'крутить стандарт')
def roles(message):
    krytku.standart1(message)
@bot.message_handler(func=lambda message: message.text.lower() == f'крутить стандарт 10')
def roles(message):
    krytku.standart10(message)

@bot.message_handler(func=lambda message: message.text.lower() == f'крутить {pers1}')
def roles(message):
    krytku.persone(message)
@bot.message_handler(func=lambda message: message.text.lower() == f'крутить {pers1} 10')
def roles(message):
    krytku.persone10(message)

@bot.message_handler(func=lambda message: message.text.lower() == f'крутить {pers2}')
def roles(message):
    krytku.perstwo(message)
@bot.message_handler(func=lambda message: message.text.lower() == f'крутить {pers2} 10')
def roles(message):
    krytku.perstwo10(message)










@bot.message_handler(func=lambda message: message.text.lower() == 'ферма')
def send_krutki(message):
    game.defferma(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'вип ферма')
def farm_plus(message):
    game.vipferma(message)

@bot.message_handler(func=lambda message: message.text.startswith('пай'))
def handle_kto(message):
    game.peredacha(message)

@bot.message_handler(func=lambda message: message.text.startswith('Выдать'))
def handle_kto(message):
    adm.give(message)

@bot.message_handler(func=lambda message: message.text.startswith('Снять'))
def handle_kto(message):
    adm.snyat(message)

@bot.message_handler(func=lambda message: message.text.startswith('Пай'))
def handle_kto(message):
    game.peredacha(message)

@bot.message_handler(func=lambda message: message.text.startswith('кто ты'))
def handle_kto(message):
    game.kto_ti(message)

@bot.message_handler(func=lambda message: message.text.startswith('Кто ты'))
def handle_kto(message):
    game.kto_ti(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'кто я')
def roles(message):
    game.ktoya(message)

@bot.message_handler(func=lambda message: message.text.startswith('+описание'))
def save_description(message):
    other.opisanie(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'топ')
def roles(message):
    game.top(message)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    other.selectop(call)

@bot.message_handler(func=lambda message: message.text.lower() == 'крутки')
def roles(message):
    game.krytki(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'достижения')
def send_info(message):
    game.achivment(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'магазин')
def rest(message):
    game.shop(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'бот')
def get_chat_id(message):
    other.bottyt(message)




'''                                               Кланы                                                                   '''


@bot.message_handler(func=lambda message: message.text.startswith('создать клан'))
def handle_message(message):
    clans.create_clan(message)
@bot.message_handler(func=lambda message: message.text.startswith('Создать клан'))
def handle_message(message):
    clans.create_clan(message)

@bot.message_handler(func=lambda message: message.text.startswith('пригласить'))
def handle_message(message):
    clans.invite_to_clan(message)
@bot.message_handler(func=lambda message: message.text.startswith('Пригласить'))
def handle_message(message):
    clans.invite_to_clan(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'удалить клан')
def handle_message(message):
    clans.delete_clan(message)

@bot.message_handler(func=lambda message: message.text.startswith('Удалить'))
def handle_message(message):
    clans.remove_from_clan(message)
@bot.message_handler(func=lambda message: message.text.startswith('удалить'))
def handle_message(message):
    clans.remove_from_clan(message)

@bot.message_handler(func=lambda message: message.text.startswith('Казна'))
def handle_message(message):
    clans.add_to_kazna(message)
@bot.message_handler(func=lambda message: message.text.startswith('казна'))
def handle_message(message):
    clans.add_to_kazna(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'выйти с клана')
def handle_message(message):
    clans.leave_clan(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'кланы')
def handle_message(message):
    clans.clanlist(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'мой клан')
def handle_message(message):
    clans.send_my_clan(message)
@bot.message_handler(func=lambda message: message.text.lower() == 'клан')
def handle_message(message):
    clans.send_my_clan(message)









'''                                                Flud                                                                   '''
@bot.message_handler(func=lambda message: message.text.lower() == 'лох')
def handle_message(message):
    voice.lox(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'рандом')
def send_random_music(message):
    voice.random_voice(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'тильт')
def send_random_music(message):
    voice.tilt(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'треш')
def send_random_music(message):
    voice.trash(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'фонк')
def send_random_music(message):
    voice.phonki(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'айди')
def get_chat_id(message):
    adm.get_id(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'роли')
def roles(message):
    flud.rolies(message)


@bot.message_handler(func=lambda message: message.text.lower() == 'ресты')
def rest(message):
    flud.rests(message)

@bot.message_handler(func=lambda message: message.text.lower() == 'команды')
def rest(message):
    flud.fludcommands(message)

@bot.message_handler(commands=['записать_ресты'])
def write_roles_handler(message):
    adm.write_rest(message)

@bot.message_handler(commands=['записать_команды'])
def write_roles_handler(message):
    adm.write_commands(message)

@bot.message_handler(commands=['записать_роли'])
def write_roles_handler(message):
    adm.write_roles(message)




'''                                              Bot message                                                                '''



@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def greet_new_members(message):
    other.newmemb(message, instructions, help)











if __name__ == '__main__':
    bot.delete_webhook(drop_pending_updates=True)
    bot.infinity_polling()