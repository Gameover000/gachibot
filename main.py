# Подключаем модуль случайных чисел 
import random
# Подключаем модуль для Телеграма
import telebot
# Указываем токен
bot = telebot.TeleBot('1900768441:AAGBTSeAjwyn1ku8M8KCKKrP3P5ySi6HNC8')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
# Заготовки для трёх предложений
first = ["Сегодня хороший день для fisting.","Вы найдете 300 bucks.","Сегодня вас похвалит Van."]
second = ["Но помните, что даже в этом случае нужно не забывать про своих slave.","Если поедете за город, заранее подумайте про ass.","Те, кто сегодня нацелен выполнить множество дел, должны помнить про dungeon master."]
third = [""]
@bot.message_handler(commands=['start'])
def start(message):


    markup = types.ReplyKeyboardMarkup()
    buttonA = types.KeyboardButton('Привет Master')
    buttonB = types.KeyboardButton('Master пришлите фото')
    buttonC = types.KeyboardButton('Музыка')
    buttonD = types.KeyboardButton("Играем")
    buttonE = types.KeyboardButton("Задонатьте мастеру")
    buttonF = types.KeyboardButton("Гачи видео")
    buttonG = types.KeyboardButton("Гачи Мемы")

    markup.row(buttonA, buttonB)
    markup.row(buttonC, buttonD)
    markup.row(buttonE, buttonF)
    markup.row(buttonG)

    bot.send_message(message.chat.id, 'Дарова,выбирай', reply_markup=markup)
# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Если написали «Привет»
    if message.text == "Привет Master":
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        # Показываем все кнопки сразу и пишем сообщение о выборе
        bot.send_message(message.from_user.id, text='Привет slave, сейчас я расскажу тебе гороскоп на сегодня,выбери свой знак зодиака.', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    elif message.text == "Master пришлите фото":
        bot.send_photo(message.from_user.id, open('photo/Screenshot_' + str(random.randint(1, 101)) + '.png', 'rb'))
    elif message.text == "Играем":
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_levo = types.InlineKeyboardButton(text='Налево', callback_data='game')
        keyboard.add(key_levo)
        key_pravo = types.InlineKeyboardButton(text='Направо', callback_data='game')
        keyboard.add(key_pravo)
        bot.send_message(message.from_user.id, text='Так уж быть,раз ты хочешь стать свободным,попробуй выбраться из gym', reply_markup=keyboard)
    elif message.text == "Задонатьте мастеру":
        bot.send_message(message.from_user.id, "https://oplata.qiwi.com/form?invoiceUid=ff9cd9dc-d562-4bea-aac1-94fe341c13fc")
    elif message.text == "Музыка":
        audio = open(r'C:/Users/Владимир/Desktop/MusicForBot/StandProud.mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
        audio = open(r'C:/Users/Владимир/Downloads/Za Warudo - DIO (vkusmp3.ru).mp3', 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(third)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "game":
        shans = random.randint(1, 20)
        if shans == 1:
            bot.send_message(call.message.chat.id, text = "Вы умерли")
            shans == 1
        else:
            bot.send_message(call.message.chat.id, text = "Куда дальше?")
            shans = random.randint(1, 7)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)