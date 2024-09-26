# -*- coding: cp1251 -*-
import random #������ ���������� random
import telebot #������ ���������� telebot
from telebot import types #������ ������� types �� ���������� telebot (�������� ���������� ��� �������� ���������)
from config import TOKEN #������ ������ (������ �������������) ���������� tlg-���� �� ����� config.py � ���������� � �������� ����������

bot = telebot.TeleBot(TOKEN)

game = ['������', '�������', '������']

@bot.message_handler(commands=['start'])
def handle_start(message):
  bot.send_message(message.chat.id, "���� \"������-�������-������\"")
  send_mess = bot.send_message(message.chat.id, '��� ���� �����?')
  bot.register_next_step_handler(send_mess, handle_name)

def handle_name(message):
  name = message.text
  keyboard = types.ReplyKeyboardMarkup(True)  #�������� ����������, �������� True ��������� ������ ������
  btn1 = types.KeyboardButton('������')  #�������� ������
  btn2 = types.KeyboardButton('������')
  btn3 = types.KeyboardButton('�������')
  keyboard.add(btn1, btn2, btn3)  #���������� ������
  bot.send_message(message.chat.id, '������, ' + name + '!')
  bot.send_message(message.chat.id, '������� ����!', reply_markup=keyboard) #reply_markup=keyboard - ���. �������� ��� ������ ����������

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  random_answer = random.choice(game) #����� ����

  if (message.text == '������' and random_answer == '������') or (
      message.text == '�������' and random_answer == '������') or (
          message.text == '������'
          and random_answer == '�������'): #message.text - �����. �����
    result = '�� ��������!'
  elif (message.text == '������' and random_answer == '�������') or (
      message.text == '�������'
      and random_answer == '������') or (message.text == '������'
                                         and random_answer == '������'):
    result = '�� �������!'
  else:
    result = '�����!'
  bot.reply_to(message, random_answer)
  bot.send_message(message.chat.id, result)

bot.polling(none_stop=True)