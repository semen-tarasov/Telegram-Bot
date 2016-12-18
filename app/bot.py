#!/usr/bin/env python3

import requests
import telebot

from app import config

bot = telebot.TeleBot(config.token)

SICKIGRAM_BASE_URL = 'http://www.sickigram.com/'

# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
#
#     bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=['joke'])
def get_best_random_joke_from_sgm(message):
    url = SICKIGRAM_BASE_URL + 'p/rand'
    args = {'c': 5, 'd': 0}
    result = requests.post(url, data=args).json()
    jokes = sorted(result['posts'], key=lambda x: x['score'], reverse=True)
    best_joke = jokes[0]
    joke = "{title}\n\n{text}".format(**best_joke)
    bot.send_message(message.chat.id, joke)


@bot.message_handler(commands=['time'])
def get_utc_time(message):
    utc_time = requests.get('http://www.timeapi.org/utc/now').content
    bot.send_message(message.chat.id, utc_time)

if __name__ == '__main__':
    bot.polling()
