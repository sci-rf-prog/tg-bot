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


def main():
	client.polling()


@client.message_handler(commands = ['get_start','start'])
def inlinebutton(message):
	client.send_message(message.chat.id, "инфа о НС")
	client.send_photo(message.chat.id, links['logo'])
	button(message)


@client.message_handler(content_types = ['new_chat_members'])
def hello(message):
	markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    	btn = types.KeyboardButton('Старт')
    	markup.add(btn)
	client.send_message(message.chat.id, text=f"Рад приветствовать, {message.from_user.first_name}!", reply_markup = markup)

@client.message_handler(content_types=['text'])
def start(message):
	if(message.text == 'Старт'):
		client.send_message(message.chat.id, "инфа о НС")
		client.send_photo(message.chat.id, links['logo'])
		button(message)

	
@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
bot.reply_to(message, text='hello')	

def button(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_prog = types.InlineKeyboardButton(text = "проги", callback_data = 'prog')
	item_robot = types.InlineKeyboardButton(text = "роботы", callback_data = 'robot')
	item_inf = types.InlineKeyboardButton(text = "просветительское", callback_data = 'inf') #ну и название у направеления

	markup_inline.add(item_prog,item_robot,item_inf)
	client.send_message(message.chat.id, "выберите инфу о направелении", reply_markup = markup_inline)


@client.callback_query_handler(func = lambda call: True)
def answerbutton(call):
	if call.data == 'prog':
		client.send_message(call.message.chat.id, prog_info)
	if call.data == 'robot':
		client.send_message(call.message.chat.id, 'Инфа о направелении роботов')
	if call.data == 'inf':
		client.send_message(call.message.chat.id, 'Инфа о направелении просветительское')
	client.answer_callback_query(callback_query_id=call.id)
	

@client.message_handler(content_types=["text"])
def get_mess(message):
	pass


if __name__ == "__main__":
	main()

