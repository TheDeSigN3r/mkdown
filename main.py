import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types

TOKEN = 'YOUR TOKEN' # محل توکن شما 
bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query.split()) == 1) #query Text 
def qq(q):
    text = q.query
    bold = types.InlineQueryResultArticle('1', 'Bold', types.InputTextMessageContent('*{}*'.format(text), parse_mode="Markdown"))
    code = types.InlineQueryResultArticle('2', 'Code', types.InputTextMessageContent('```{}```'.format(text), parse_mode="Markdown"))
    italic = types.InlineQueryResultArticle('3', 'Italic', types.InputTextMessageContent('_{}_'.format(text), parse_mode="Markdown"))
                

    bot.answer_inline_query(q.id, [bold, code, italic], cache_time=1)
    
    
bot.polling(True)

#new Update Soon
