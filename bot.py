#!/usr/bin/env python3

import config
import telebot

import requests

bot = telebot.TeleBot(config.token)


# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#
#     bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['time'])
def get_utc_time(message):
    utc_time = requests.get('http://www.timeapi.org/utc/now').content
    bot.send_message(message.chat.id, utc_time)

if __name__ == '__main__':
    bot.polling()
