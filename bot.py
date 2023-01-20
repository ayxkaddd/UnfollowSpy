import telebot
from telebot import types
from colorama import init, Fore

init(autoreset=True)

import config
from main import Inst_Tools

token = f"{config.bot_token}"
admins_id = config.admins_id
username=f"{config.ig_username}"
password=f"{config.ig_password}"
ig_account_id = f"{config.ig_account_id}"


bot = telebot.TeleBot(token)
app = Inst_Tools(username, password, ig_account_id)


@bot.message_handler(commands=["start"])
def start(message):
    print(f"{Fore.CYAN}localhost@{Fore.MAGENTA}{message.from_user.first_name}: {Fore.WHITE}{message.text}")
    if message.from_user.id in admins_id:
        bot.send_message(message.from_user.id, "haai")
        markup = types.ReplyKeyboardMarkup(row_width=1)
        itembtn1 = types.KeyboardButton('/total_followers')
        itembtn2 = types.KeyboardButton('/check_if_follow')
        itembtn3 = types.KeyboardButton('/check_if_unfollow')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.from_user.id, "commands:", reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, "bye")


@bot.message_handler(commands=["total_followers"])
def total_followes(message):
    print(f"{Fore.CYAN}localhost@{Fore.MAGENTA}{message.from_user.first_name}: {Fore.WHITE}{message.text}")
    total_followers = app.total_followers()
    bot.send_message(message.from_user.id, f"you have {total_followers} followers")


@bot.message_handler(commands=["check_if_follow"])
def check_if_follow(message):
    print(f"{Fore.CYAN}localhost@{Fore.MAGENTA}{message.from_user.first_name}: {Fore.WHITE}{message.text}")
    follow = app.check_if_follow(message.text.split(" ")[-1])
    if follow:
        bot.send_message(message.from_user.id, f"{message.text.split(' ')[-1]} follow you")
    else:
        bot.send_message(message.from_user.id, f"{message.text.split(' ')[-1]} does not follow you")


@bot.message_handler(commands=["check_if_unfollow"])
def check_if_unfollow(message):
    print(f"{Fore.CYAN}localhost@{Fore.MAGENTA}{message.from_user.first_name}: {Fore.WHITE}{message.text}")
    bot.send_message(message.from_user.id, "wait a minute... ")
    bot.send_chat_action(message.from_user.id, "typing", 60)
    unfollow_list = app.get_followers()
    if unfollow_list:
        for i in unfollow_list:
            for adm_id in admins_id:
                bot.send_message(adm_id, f"https://www.instagram.com/{i}/")  
            print(f"\n{Fore.RED}https://www.instagram.com/{i}/")
    else:
        bot.send_message(message.from_user.id, "no one has unsubscribed")


@bot.message_handler(content_types=["text"])
def commands(message):
    print(f"{Fore.CYAN}localhost@{Fore.MAGENTA}{message.from_user.first_name}: {Fore.WHITE}{message.text}")
    bot.send_message(message.from_user.id, "meow")


bot.infinity_polling()