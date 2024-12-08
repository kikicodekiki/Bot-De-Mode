import telebot
from telebot import types

bot = telebot.TeleBot(token = '')

to_send = """, and welcome to my Python project for the Introduction to programming with Python course.
             This bot is designed to simplify how you keep up with fashion trends. It provides real-time insights 
             into the popularity of styles and items, analyzing data from platforms like Pinterest and Instagram.

            <b>Features:</b>

            -> Daily Trend Updates: Receive automated notifications on the latest fashion trends.
            -> Keyword Stats: Get tailored analytics and visuals for specific styles or categories 
               (e.g., "streetwear," "eco-fashion").
            -> Trend Alerts: Stay ahead with notifications about rising hashtags and keywords.
            -> Personalized Content: Customize updates based on your favorite styles, colors, or brands.
            -> Easy Navigation: User-friendly commands and interactive buttons for seamless exploration.
    Bot de Mode streamlines the overwhelming world of fashion data, making it easier to stay stylish in the 
    fast-paced realm of influencers and rapid trends.  """

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, f"<b>Hello, dear {message.from_user.first_name}</b>" + to_send, parse_mode='html')
    # create the inline buttons
    markup = types.InlineKeyboardMarkup()
    notification_button = types.InlineKeyboardButton(text='Daily Trend Updates', callback_data='trend_updates')
    help_button = types.InlineKeyboardButton(text='Help', callback_data='help')
    markup.row(notification_button, help_button)
    bot.send_message(message.chat.id, 'Available commands: ', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'trend_updates':
        bot.answer_callback_query(callback.id)

bot.polling(non_stop=True)
