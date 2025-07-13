
import telebot
import os

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ FXGroupForexBot è attivo e funzionante!")

bot.polling()
