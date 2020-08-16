import telebot
import test
import time
bot = telebot.TeleBot("TOKEN")

@bot.message_handler(content_types=['sticker'])
def welcome(message):
	try:
		if message.from_user.id == 293490416:
			time.sleep(0.0000001)
		else:
			stik = str(message.sticker.set_name)
			f = open('stickers.txt', 'r')
			test = f.read()
			if stik in test:
				bot.delete_message(message.chat.id, message.message_id)
			f.close()
	except Exception as e:
		time.sleep(0.0000001)

@bot.message_handler(commands=['remember'])
def welcome2(message):
	try:
		if message.from_user.id == 293490416:
			msg = bot.send_message(message.chat.id, 'Пришлите мне стикер из того набора, который будет автоудаляться')
			bot.register_next_step_handler(msg, remember)
		else:
			msg = bot.send_message(message.chat.id, 'Извините у вас нет доступа к этой команде')
			time.sleep(0.0000001)
	except Exception as e:
		time.sleep(0.0000001)


def remember(message):
	try:
	    if message.from_user.id == 293490416:
		    msg = bot.send_message(message.chat.id, 'Я запомнил этот набор\nЕсли кто-то кроме вас будет им пользоваться я буду его удалять)')

		    f = open('stickers.txt', 'a')
		    f.write(str(message.sticker.set_name)+'\n')
		    f.close()
		else:
            time.sleep(0.0000001)
	except Exception as e:
		time.sleep(0.0000001)



if __name__ == '__main__':
    bot.polling(none_stop=True)
