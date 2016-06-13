import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types

TOKEN = '216162835:AAH3z6Pb4F9-dDFWJYlHwjuS-VlTHy5D_SU' # محل توکن شما 
bot = telebot.TeleBot(TOKEN)

@bot.inline_handler(lambda query: len(query.query.split()) == 0)
@bot.inline_handler(lambda query: len(query.query.split()) == 1)
@bot.inline_handler(lambda query: len(query.query.split()) == 2)
@bot.inline_handler(lambda query: len(query.query.split()) == 3)
@bot.inline_handler(lambda query: len(query.query.split()) == 4)
@bot.inline_handler(lambda query: len(query.query.split()) == 5)
@bot.inline_handler(lambda query: len(query.query.split()) == 6)
@bot.inline_handler(lambda query: len(query.query.split()) == 7)
@bot.inline_handler(lambda query: len(query.query.split()) == 8)
@bot.inline_handler(lambda query: len(query.query.split()) == 9)
@bot.inline_handler(lambda query: len(query.query.split()) == 10)
@bot.inline_handler(lambda query: len(query.query.split()) == 11)
@bot.inline_handler(lambda query: len(query.query.split()) == 12)
@bot.inline_handler(lambda query: len(query.query.split()) == 13)
@bot.inline_handler(lambda query: len(query.query.split()) == 14)
@bot.inline_handler(lambda query: len(query.query.split()) == 15)
@bot.inline_handler(lambda query: len(query.query.split()) == 16)
@bot.inline_handler(lambda query: len(query.query.split()) == 18)
@bot.inline_handler(lambda query: len(query.query.split()) == 19)
@bot.inline_handler(lambda query: len(query.query.split()) == 20)
def qq(q):
    text = q.query
    thumbb = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-asap-b.jpg'
    thumbc = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-forque-c.jpg'
    thumbi = 'http://lettergenerator.net/alphabetletters/bold/printable-letter-newtown-i.jpg'
    bold = types.InlineQueryResultArticle('1', 'Bold', types.InputTextMessageContent('*{}*'.format(text), parse_mode="Markdown"), description='{}'.format(text), thumb_url=thumbb, thumb_width=20, thumb_height=20)
    code = types.InlineQueryResultArticle('2', 'Code', types.InputTextMessageContent('```{}```'.format(text), parse_mode="Markdown"), description='{}'.format(text), thumb_url=thumbc, thumb_width=20, thumb_height=20)
    italic = types.InlineQueryResultArticle('3', 'Italic', types.InputTextMessageContent('_{}_'.format(text), parse_mode="Markdown"), description='{}'.format(text), thumb_url=thumbi, thumb_width=20, thumb_height=20)
    bot.answer_inline_query(q.id, [bold, code, italic], cache_time=1)
    
    
bot.polling(True)

#new Update Soon
