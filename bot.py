import conf
import telebot
from telebot import types
import my_model
import cloud


bot = telebot.TeleBot(conf.TOKEN)  # создаем экземпляр бота
database = {}
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    button_new = types.InlineKeyboardButton(text="Я новенький", callback_data="newbie")
    button_old = types.InlineKeyboardButton(text="Я уже смешарик", callback_data="keep_history")
    keyboard.add(button_new, button_old)
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, который ноет и больше (почти) ничего не умеет!")
    bot.send_message(message.chat.id, "Для того, чтобы продолжить начатую беседу, нажмите соответствующую кнопку. Если хотите очистить историю диалога, соврите (ну нажмите Я новенький)",reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard_exit = types.InlineKeyboardMarkup()
    button_exit = types.InlineKeyboardButton(text="Выпей чаю, все будет хорошо :)", callback_data="button_exit")
    keyboard_exit.add(button_exit)
    keyboard_start = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Послушать нытье!!!", callback_data="button1")
    keyboard_start.add(button1)
    if call.message:
        if call.data == "newbie":
            database[call.message.chat.id] = []
            bot.send_message(call.message.chat.id, "Ура, можно начинать!",reply_markup=keyboard_start)
        if call.data == "keep_history":
            try:
                database[call.message.chat.id] = database[call.message.chat.id]
            except:
                database[call.message.chat.id] = []
                bot.send_message(call.message.chat.id, "Вы еще не смешарик...Не торопитесь")
            bot.send_message(call.message.chat.id, "Ура, можно начинать!",reply_markup=keyboard_start)
        if call.data == "button1":
            bot.send_message(call.message.chat.id, "WARNING: Бот тоже человек! Пока он печатает Вам ответ, он плачет, шмыгает, проклинает маленькую клавиатуру и Т9. Следовательно, его ответ займет некоторое время, до пяти минут.")
            bot.send_message(call.message.chat.id, "Отправьте любую Вашу мысль, оставьте бота на пару минут, заварите чай и возвращайтесь за порцией негатива! Можете отправлять сколько угодно сообщений; чтобы успокоить бота, нажмите на соответствующую кнопку.",reply_markup=keyboard_exit)
        if call.data == "button_exit":
            keyboard_cloud = types.ReplyKeyboardMarkup(row_width=1)
            button_yes = types.KeyboardButton("Даааа")
            keyboard_cloud.add(button_yes)
            button_no = types.KeyboardButton("Не трать мое время.")
            keyboard_cloud.add(button_no)
            bot.send_message(call.message.chat.id, "Вы успокоили бота. Большое Вам спасибо!")
            bot.send_message(call.message.chat.id, "Не хотите ли построить облако слов для Вашего диалога?",reply_markup=keyboard_cloud)
            
@bot.message_handler(func=lambda m: True)
def send_len(message):
    if message.text not in ['Даааа', 'Не трать мое время.']:
        keyboard_exit = types.InlineKeyboardMarkup()
        button_exit = types.InlineKeyboardButton(text="Выпей чаю, все будет хорошо :)", callback_data="button_exit")
        keyboard_exit.add(button_exit)
        database[message.chat.id].append(message.text)
        #bot_response = my_model.get_text(message.text)
        bot_response = 'У ля ля конфеты парки бабалайка'
        bot.send_message(message.chat.id, bot_response ,reply_markup=keyboard_exit)
        database[message.chat.id].append(bot_response)
        #bot.send_message(message.chat.id, 'БЛАБЛА',reply_markup=keyboard_exit)
    elif message.text == "Даааа":
        try:
            history = ' '.join(database[message.chat.id])
            cloud.get_cloud(history)
            photo = open("wordcloud.png", 'rb')
            bot.send_photo(message.chat.id, photo)
            bot.send_message(message.chat.id, "До свидания! Если хотите, чтобы бот снова поистерил....... Нажмите /start")
        except:
            bot.send_message(message.chat.id, "Слишком мало поговорили... Будьте общительнее!")
            bot.send_message(message.chat.id, "До свидания! Если хотите, чтобы бот снова поистерил....... Нажмите /start")
    else:
        bot.send_message(message.chat.id, "До свидания! Если хотите, чтобы бот снова поистерил....... Нажмите /start")
        
    
    
if __name__ == '__main__':
    bot.polling(none_stop=True)