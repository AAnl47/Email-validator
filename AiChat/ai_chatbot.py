from config import *
import telebot
from langchain_openai import ChatOpenAI

def ChatModel(prompt):
    chat = ChatOpenAI(openai_api_key=api_key)
    res=chat.invoke(prompt)
    print(res.content)
    return res.content


bot = telebot.TeleBot(BOT_API)

@bot.message_handler(['start'])
def start(message):
    bot.reply_to(message,"Hello, I'm your Assistant. How can I help you today?")

@bot.message_handler()
def chat(message):
    print(message.text)
    try:
        reply = ChatModel(message.text)
        bot.reply_to(message,reply)
    except:
        bot.reply_to(message,"Sorry, I didn't get that. Please try again.")

print("Bot started....")
bot.polling()