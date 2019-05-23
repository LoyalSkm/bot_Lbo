import json
import poloniex
import random
from datetime import timedelta, datetime, date


# print(telegram.__version__)
from telegram.ext import Updater
updater = Updater(token='834879381:AAH0BaqokKCa0znrmnywNN7kV8yN76JLQ5E',
                  use_context=True)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def read_json():
    return json.load(open('users.json'))

def write_json(person_dict):
    json.dump(person_dict, open('users.json', 'w'), ensure_ascii=False, indent=6)


def reg(update, context):
    users = read_json()
    keys_all = users.keys()
    keys_main = str(update.message.chat_id) + " " + str(update.message.from_user.id) # начало кастыля, чтобы конктеризировать когото пишлось делать это

    if (keys_main) in keys_all:
        if users[keys_main]["registration"] == 1:
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text=update.message.from_user.first_name + " " + "ты играешь")
        elif users[keys_main]["registration"] == 0:
            users[keys_main]['registration'] = 1
            context.bot.send_message(chat_id=update.message.chat_id,
                                     text=update.message.from_user.first_name + " " + "ты снова в игре")
            write_json(users)
    elif (keys_main) not in keys_all:
        users[keys_main] = {
            'id': update.message.from_user.id,
            'first_name': update.message.from_user.first_name,
            'last_name': update.message.from_user.last_name,
            'username': "@" + update.message.from_user.username,
            'score': 0,
            'registration': 1,
            'data_time': "",
        }
        write_json(users)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=update.message.from_user.first_name + " " + "+")

def unreg(update, context):
    users = read_json()
    keys_all = users.keys()
    users[str(update.message.chat_id) + " " + str(update.message.from_user.id)]['registration'] = 0
    write_json(users)

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=update.message.from_user.first_name + " " + "-")

def users(update, context):
    users = read_json()

    for key, value in users.items():
        if str(update.message.chat_id) in key:
            if value['registration'] == 1:
                context.bot.send_message(chat_id=update.message.chat_id,
                                         text=value['first_name']+ " " + str(value['username'])+ " " + str(value['score']))
def rand(update, context):
    users = read_json()
    empt_list = [] #список учасников
    hunted_user = [] #рользователь который словил +1
    for key, value in users.items(): #поиск участников конкретной группы!!!!!< --- тут кастыль но я хз как по другому их искать
        if str(update.message.chat_id) in key: #поиск всех учасников по значению chat_id
            empt_list.append(key) #добавление всех зарегистрированных учасников
    for i in empt_list:
        if users[i]['data_time'] == str(date.today()):
            hunted_user.append(i) #пользователь у которого стоит егоднешняя дата в JSON
            break
    if hunted_user == []:
        rand = random.choice(empt_list)
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text=users[rand]['first_name'] + " " + "плюсанул +1")
        users[rand]['score'] += 1
        users[rand]['data_time'] = str(date.today())
        print(empt_list)
        write_json(users)
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                                 text="сегодня уже был победитель" + " " + users[hunted_user[0]]['first_name']+ " " + str(users[hunted_user[0]]['username']))


def cripta(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="BTC =" + " " + poloniex.get_btc("btc"))
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="ETH =" + " " + poloniex.get_btc("eth"))

from telegram.ext import CommandHandler
rand_handler = CommandHandler('rand', rand)
dispatcher.add_handler(rand_handler)
users_handler = CommandHandler('users', users)
dispatcher.add_handler(users_handler)
cripta_handler = CommandHandler('cripta', cripta)
dispatcher.add_handler(cripta_handler)
reg_handler = CommandHandler('reg', reg)
dispatcher.add_handler(reg_handler)
unreg_handler = CommandHandler('unreg', unreg)
dispatcher.add_handler(unreg_handler)

updater.start_polling()
