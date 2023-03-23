import telebot
from telebot import types
import openai
openai.api_key = "open Ai key"
api = 'Telegram bot API'
bot = telebot.TeleBot(api)

def resp(question):
    respon = "Q: {qst}\nA:".format(qst=question)
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=respon,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Silahkan bertanya sesuka hati :)")

@bot.message_handler(func=lambda message: True) 
def echo_message(message):
 msg = message.text
 response = resp(msg)
 bot.send_message(message.chat.id, response)
    
print('bot start running')
bot.polling()
