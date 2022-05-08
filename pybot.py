import telebot
import conf 
from telebot import types


client = telebot.TeleBot(conf.config['token'])

@client.message_handler(commands = ['get_start','start'])
def inlinebutton(message):
	client.send_message(message.chat.id, "инфа о НС")
	client.send_photo(message.chat.id, 'https://vk.com/feed?section=likes&z=photo-157823267_457278575%2Fdef88df5f2c4808795')
	button(message)

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
		client.send_message(call.message.chat.id, 'Инфа о направелении прог')
	if call.data == 'robot':
		client.send_message(call.message.chat.id, 'Инфа о направелении роботы')
	if call.data == 'inf':
		client.send_message(call.message.chat.id, 'Инфа о направелении просветительское')
	client.answer_callback_query(callback_query_id=call.id)
	

@client.message_handler(content_types=["text"])
def get_mess(message):
	pass
client.polling()
