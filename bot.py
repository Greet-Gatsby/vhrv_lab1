import config
import telebot

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')

def start(update, context):
"""Send a message when the command /start is issued."""
update.message.reply_text('Hi!')

def help(update, context):
"""Send a message when the command /help is issued."""
update.message.reply_text('Help!')

def echo(update, context):
"""Echo the user message."""
update.message.reply_text(update.message.text)

def error(update, context):
"""Log Errors caused by Updates."""
logger.warning('Update "%s" caused error "%s"', update, context.error)

def echo(update, context):
"""Echo the user message."""
update.message.reply_text(update.message.text)
bot.polling(none_stop=True)
