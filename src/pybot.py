import os
import telebot
import json
from telebot import types
from dotenv import dotenv_values

CURR_PATH = os.path.dirname(__file__)
with open(os.path.join(CURR_PATH, '../static/links.json')) as json_file:
    links = json.load(json_file)

env = dotenv_values(os.path.join(CURR_PATH, '../.env'))
client = telebot.TeleBot(env['TOKEN'])

with open(os.path.join(CURR_PATH, '../static/prog.txt'), 'r') as txt_file:
	prog_info = txt_file.read()
with open(os.path.join(CURR_PATH, '../static/razv.txt'), 'r') as txt_file:
	razv_info = txt_file.read()
with open(os.path.join(CURR_PATH, '../static/rob.txt'), 'r') as txt_file:
	robot_info = txt_file.read()
with open(os.path.join(CURR_PATH, '../static/scipo.txt'), 'r') as txt_file:
	scipo_info = txt_file.read()
with open(os.path.join(CURR_PATH, '../static/inf.txt'), 'r') as txt_file:
	sinf_info = txt_file.read()


def main():
	client.polling()

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
bot.reply_to(message, text='Привет')

@client.message_handler(commands = ['get_start','start'])
def inlinebutton(message):
	client.send_photo(message.chat.id, links['logo'],caption = inf)
	button(message)


def button(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_prog = types.InlineKeyboardButton(text = "Программирование", callback_data = 'prog')
	item_robot = types.InlineKeyboardButton(text = "Робототехника", callback_data = 'robot')
	item_inf = types.InlineKeyboardButton(text = "Развлекательный", callback_data = 'razv')
	item_inf = types.InlineKeyboardButton(text = "Научно-популярное", callback_data = 'scipo')

	markup_inline.add(item_prog,item_robot,item_inf)
	client.send_message(message.chat.id, "Выберите направление о котором хотели бы узнать больше", reply_markup = markup_inline)


@client.callback_query_handler(func = lambda call: True)
def answerbutton(call):
	if call.data == 'prog':
		client.send_message(call.message.chat.id, prog_info)
	if call.data == 'robot':
		client.send_message(call.message.chat.id, robot_info)
	if call.data == 'razv':
		client.send_message(call.message.chat.id, inf_info)
	if call.data == 'scipo':
		client.send_message(call.message.chat.id, scipo_info)
	client.answer_callback_query(callback_query_id=call.id)
	

@client.message_handler(content_types=["text"])
def get_mess(message):
	pass


if __name__ == "__main__":
	main()

