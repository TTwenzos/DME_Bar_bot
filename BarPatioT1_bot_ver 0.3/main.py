from constans import bot
from config import *
from menu import Time, Reply_menu_keyboard
from handlers import Reply_markup_handlers, Password_handler
import os

try:
    
    @bot.message_handler(commands=['start'])
    def main(message):
        bot.send_message(message.chat.id, Time.greeting(Time.get_hour()), reply_markup=Reply_menu_keyboard.main_reply_keyboard())
        bot.register_next_step_handler(message, request_handler)

    @bot.message_handler(commands=['getenv'])
    def main(message):
        bot.send_message(message.chat.id, str(os.environ["SUPERUSER_RIGHT"]))

    @bot.message_handler(commands=['exit'])
    def main(message):
        bot.send_message(message.chat.id, 'Chao!')
        bot.stop_bot()
        exit(0)
    @bot.message_handler(commands=["admin"])
    def admin(message):
        bot.send_message(message.chat.id, 'Введите пароль админа')
        bot.register_next_step_handler(message, Password_handler.root_handler)
    @bot.message_handler(content_types=['text'])

    def request_handler(message):
        Reply_markup_handlers.reply_keyboard_handler(message)
    if __name__ == '__main__':
        bot.infinity_polling()
    else: Exception_logger(__name__, 'Бот запущен не из файла "mein.py"', "i")

except Exception as e:
    Exception_logger(__name__, e, "C")
