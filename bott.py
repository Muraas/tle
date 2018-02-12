import conf
import json
import telebot
from telebot import types
bot = telebot.TeleBot(conf.token)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup.row('Лайки') 
markup.row('Опрос')

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
markup1.row('Отправить в канал')
markup1.row('Отменить')

@bot.message_handler(content_types=["photo"])
def repim(message):
	fid = message.photo[0].file_id
	bot.send_photo("@ruthsst", fid)
@bot.message_handler(content_types=["sticker"])
def repst(message):
	fid = message.sticker.file_id
	bot.send_sticker("@ruthsst", fid)
@bot.message_handler(content_types=["document"])
def repdoc(message):
	fid = message.document.file_id
	bot.send_document("@ruthsst", fid)

@bot.message_handler(content_types=["video"])
def repvid(message):
	fid = message.video.file_id
	bot.send_video("@ruthsst", fid)

@bot.message_handler(content_types=["text"])
def repeat(message):
	bot.send_message("@ruthsst", message.text, parse_mode="markdown", disable_web_page_preview = True)

if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			time.sleep(15)