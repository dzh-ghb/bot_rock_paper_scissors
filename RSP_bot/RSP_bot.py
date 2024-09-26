# -*- coding: cp1251 -*-
import random #импорт библиотеки random
import telebot #импорт библиотеки telebot
from telebot import types #импорт объекта types из библиотеки telebot (содержит функционал для создания клавиатур)
from config import TOKEN #импорт токена (личный идентификатор) созданного tlg-бота из файла config.py в директории с исходной программой

bot = telebot.TeleBot(TOKEN)

game = ['Камень', 'Ножницы', 'Бумага']

@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.send_message(message.chat.id, "Игра \"Камень-Ножницы-Бумага\"")
  send_mess = bot.send_message(message.chat.id, 'Как тебя зовут?')
  bot.register_next_step_handler(send_mess, handle_name)

def handle_name(message):
  name = message.text
  keyboard = types.ReplyKeyboardMarkup(True)  #создание клавиатуры, значение True фиксирует размер кнопки
  btn1 = types.KeyboardButton('Камень')  #создание кнопок
  btn2 = types.KeyboardButton('Бумага')
  btn3 = types.KeyboardButton('Ножницы')
  keyboard.add(btn1, btn2, btn3)  #добавление кнопок
  bot.send_message(message.chat.id, 'Привет, ' + name + '!')
  bot.send_message(message.chat.id, 'Удачной игры!', reply_markup=keyboard) #reply_markup=keyboard - доп. параметр для вывода клавиатуры

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  random_answer = random.choice(game) #выбор бота

  if (message.text == 'Камень' and random_answer == 'Бумага') or (
      message.text == 'Ножницы' and random_answer == 'Камень') or (
          message.text == 'Бумага'
          and random_answer == 'Ножницы'): #message.text - сообщ. юзера
    result = 'Ты проиграл!'
  elif (message.text == 'Камень' and random_answer == 'Ножницы') or (
      message.text == 'Ножницы'
      and random_answer == 'Бумага') or (message.text == 'Бумага'
                                         and random_answer == 'Камень'):
    result = 'Ты выиграл!'
  else:
    result = 'Ничья!'
  bot.reply_to(message, random_answer)
  bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)