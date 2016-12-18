#!/usr/bin/env python3

import collections
import config
import requests
import telebot

bot = telebot.TeleBot(config.token)

SICKIGRAM_BASE_URL = 'http://www.sickigram.com/'
SICKIGRAM_CATEGORIES = {
    2: "sex and shit",
    3: "racism",
    4: "religion",
    5: "politics",
    6: "sexism",
    7: "crime",
    12: "illness",
    8: "mortality",
    9: "news",
    15: "wordplay",
    16: "economics",
    13: "events",
    14: "celebrities",
    10: "sport",
    11: "tv",
    17: "nsfw af"
}


def _get_categories_hashtags(categories_list):
    result = ''
    if not isinstance(categories_list, collections.Iterable):
        return result
    for category_id in categories_list:
        if category_id in SICKIGRAM_CATEGORIES:
            hashtag = '#{} '.format(SICKIGRAM_CATEGORIES[category_id].replace(' ', '_'))
            result += hashtag
    return result

@bot.message_handler(commands=['joke'])
def get_best_random_joke_from_sgm(message):
    url = SICKIGRAM_BASE_URL + 'p/rand'
    args = {'c': 5, 'd': 0}
    result = requests.post(url, data=args).json()
    jokes = sorted(result['posts'], key=lambda x: x['score'], reverse=True)
    best_joke = jokes[0]
    joke = "{title}\n\n{text}".format(**best_joke)
    categories = _get_categories_hashtags(best_joke['categories'])
    if categories:
        joke += '\n\n{}'.format(categories)
    bot.send_message(message.chat.id, joke)

if __name__ == '__main__':
    bot.polling()
