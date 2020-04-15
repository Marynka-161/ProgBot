# -*- coding: utf-8 -*-

import telebot
import string
from telebot import types


TOKEN = '1062622209:AAHn8837uftD4Gnfrmx2LqK_38tb-6tmwJY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler ( commands= ['start'])
def send_welcome ( message): 
	bot.send_message  (message.from_user.id, "Тебе вітає Java Training Bot! Я допоможу тобі у вивченні такої мови програмування як Java. Після проходження кожного розділу можна пройти загальний тест. Успіхів тобі!")
	keyboard = types.InlineKeyboardMarkup()
	key_bas = types.InlineKeyboardButton(text='Основні поняття', callback_data='basic')
	keyboard.add(key_bas)
	key_loo = types.InlineKeyboardButton(text='Умовні оператори та цикли', callback_data='loops')
	keyboard.add(key_loo)
	key_arr = types.InlineKeyboardButton(text='Масиви', callback_data='array')
	keyboard.add(key_arr)
	key_cla = types.InlineKeyboardButton(text='Класи та об\'єкти', callback_data='сlasses')
	keyboard.add(key_cla)
	key_mor = types.InlineKeyboardButton(text='Більше про класи', callback_data='moreclasses')
	keyboard.add(key_mor)
	key_oth = types.InlineKeyboardButton(text='Виключення, списки, протоколи та файли', callback_data='other')
	keyboard.add(key_oth)
	bot.send_message  (message.from_user.id, "Отже, яку із тем ти хочеш вибрати? Я б порокомендував тобі почати з самого початку, якщо ти новачок в програмуванні на мові Java.", reply_markup = keyboard)
	
@bot.message_handler ( commands= ['help'])
def send_welcome ( message): 
	bot.send_message  (message.from_user.id, "Для того щоб розпочати навчання натисніть /start.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
	if call.data =='basic':
		keyboard1 = types.InlineKeyboardMarkup()
		key_int = types.InlineKeyboardButton(text='Введення в Java', callback_data='introduction')
		keyboard1.add(key_int)
		key_fir = types.InlineKeyboardButton(text='Програма \"Hello World\"', callback_data='first')
		keyboard1.add(key_fir)
		key_com = types.InlineKeyboardButton(text='Коментарі в Java', callback_data='comment')
		keyboard1.add(key_com)
		key_var = types.InlineKeyboardButton(text='Змінні', callback_data='variables')
		keyboard1.add(key_var)
		key_ope = types.InlineKeyboardButton(text='Примітивні оператори', callback_data='operator')
		keyboard1.add(key_ope)
		key_inc = types.InlineKeyboardButton(text='Інкремент та декримент', callback_data='incdec')
		keyboard1.add(key_inc)
		key_lin = types.InlineKeyboardButton(text='Рядки', callback_data='lines')
		keyboard1.add(key_lin)
		key_inp = types.InlineKeyboardButton(text='Зчитування користувацького вводу', callback_data='input')
		keyboard1.add(key_inp)
		key_t1 = types.InlineKeyboardButton(text='Тест', callback_data='test1')
		keyboard1.add(key_t1)
		bot.send_message  (call.from_user.id, "Вибери підрозділ", reply_markup = keyboard1)

	elif call.data =='introduction':
		text =  open( 't1.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Програма \"Hello World\"\" ', callback_data='first')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='first':
		text =  open( 't2.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Коментарі в Java\" ', callback_data='comment')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Введення в Java\"', callback_data='introduction')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='comment':
		text =  open( 't3.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Змінні\" ', callback_data='variables')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Програма \"Hello World\"\"', callback_data='first')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='variables': 
		text =  open( 't4.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Примітивні оператори\" ', callback_data='operator')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Коментарі в Java\"', callback_data='comment')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='operator': 
		text =  open( 't5.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Інкремент та декримент\" ', callback_data='incdec')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Змінні\"', callback_data='variables')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='incdec':
		text =  open( 't6.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Рядки\" ', callback_data='lines')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Примітивні оператори\"', callback_data='operator')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='lines':
		text =  open( 't7.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до підрозділа \"Зчитування користувацького вводу\" ', callback_data='input')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Інкремент та декримент\"', callback_data='incdec')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='input':
		text =  open( 't8.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_forward = types.InlineKeyboardButton(text='Перейти до тесту ', callback_data='test1')
		keyboard.add(key_forward)
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Рядки\"', callback_data='lines')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='test1':
		text =  open( 't9.txt', 'rb')
		keyboard = types.InlineKeyboardMarkup()
		key_menu = types.InlineKeyboardButton(text='Перейти на головне меню', callback_data='basic')
		keyboard.add(key_menu)
		key_back = types.InlineKeyboardButton(text='Повернутися до подрозділа \"Зчитування користувацького вводу\"', callback_data='input')
		keyboard.add(key_back)
		bot.send_message  (call.from_user.id, text.read(), reply_markup = keyboard)
	elif call.data =='3':
		bot.send_message(call.message.chat.id, 'Привильно')
		text =  open( 't10.txt', 'rb')
		bot.send_message(call.from_user.id, text.read())
	elif call.data =='2' or '1':
		bot.send_message(call.message.chat.id, 'Неправильно, спробуй ще')

	@bot.message_handler(content_types = ['text'])
	def send_text( message):
		if message.text.lower().replace(' ', '') == 'int,+,sum':
			bot.send_message(message.chat.id, 'Привильно')
			keyboard = types.InlineKeyboardMarkup()
			key_1 = types.InlineKeyboardButton(text='...повинно бути оголошено щонайменше дві змінні.', callback_data='1')
			keyboard.add(key_1)
			key_2 = types.InlineKeyboardButton(text='...всі рядки повинні бути цілими числами.', callback_data='2')
			keyboard.add(key_2)
			key_3 = types.InlineKeyboardButton(text='...там повинен бути метод, званий "main".', callback_data='3')
			keyboard.add(key_3)
			bot.send_message  (message.from_user.id, "2. У кожній програмі Java...", reply_markup = keyboard)
		elif message.text.lower().replace(' ', '') == 'string,system,name':
			bot.send_message(message.chat.id, 'Привильно')
			bot.send_message(message.chat.id, 'Ви успішно прошли цей тест. Вітаю!')
		else:
			bot.send_message(message.chat.id, 'Неправильно, спробой ще')

bot.polling(none_stop = True)
