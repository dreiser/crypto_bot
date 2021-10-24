from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/fetch_price')
b2 = KeyboardButton('/pairs20')
b3 = KeyboardButton('/out_of_ideas')


kb_particapent = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_particapent.add(b1).add(b2).add(b3)