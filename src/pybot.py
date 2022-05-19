import os
import telebot
import json
from telebot import types
from dotenv import dotenv_values
from static import prog_info, razv_info, robot_info, scipo_info, inf_info

CURR_PATH = os.path.dirname(__file__)
with open(os.path.join(CURR_PATH, '../static/links.json')) as json_file:
    links = json.load(json_file)

env = dotenv_values(os.path.join(CURR_PATH, '../.env'))
client = telebot.TeleBot(env['TOKEN'])


def main():
	client.polling()


@client.message_handler(content_types = ['new_chat_members'])
def hello(message):
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
	btn = types.KeyboardButton('Узнать о НС!')
	markup.add(btn)
	client.send_message(message.chat.id, text=f"Рад приветствовать, {message.from_user.first_name}! Жми Кнопку!", reply_markup = markup)


@client.message_handler(commands = ['get_start','start'])
def inlinebutton(message):
	client.send_photo(message.chat.id, links['logo'],caption = inf_info)
	button(message)


@client.message_handler(content_types=['text'])
def start(message):
	if(message.text == 'Узнать о НС!'):
		rem = types.ReplyKeyboardRemove()
		client.send_photo(message.chat.id, links['logo'],caption = inf_info)
		button(message)


def button(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_prog = types.InlineKeyboardButton(text = "Прога", callback_data = 'prog')
	item_robot = types.InlineKeyboardButton(text = "Робототехника", callback_data = 'robot')
	item_razvl = types.InlineKeyboardButton(text = "Развлекательное", callback_data = 'razv')
	item_inf = types.InlineKeyboardButton(text = "Научно-популярное", callback_data = 'scipo')

	markup_inline.add(item_prog, item_robot, item_razvl, item_inf)
	client.send_message(message.chat.id, "Выберите направление о котором хотели бы узнать больше", reply_markup = markup_inline)


@client.callback_query_handler(func = lambda call: True)
def answerbutton(call):
	if call.data == 'prog':
		client.send_message(call.message.chat.id, prog_info)
	if call.data == 'robot':
		client.send_message(call.message.chat.id, robot_info)
	if call.data == 'razv':
		client.send_message(call.message.chat.id, razv_info)
	if call.data == 'scipo':
		client.send_message(call.message.chat.id, scipo_info)
	client.answer_callback_query(callback_query_id=call.id)
	

@client.message_handler(content_types=["text"])
def get_mess(message):
	pass


if __name__ == "__main__":
	main()

