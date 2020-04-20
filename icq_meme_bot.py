from bot.bot import Bot
from bot.handler import CommandHandler, HelpCommandHandler, StartCommandHandler, UnknownCommandHandler
import post_creater
import article_id_sql
import sql_handlers


TOKEN = "..."


bot = Bot(token=TOKEN)


def unknown_command_cb(bot, event):
    user = event.from_chat
    (command, command_body) = event.data["text"].partition(" ")[::2]
    bot.send_text(
        chat_id=user,
        text="Неизвестная команда '{message}' от '{source}'. Используйте /meme".format(
            source=user, message=command[1:], command_body=command_body
        )
    )


def start_command(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Привет! Я бот с мемами :3 Используй /meme")


def help_command(bot, event):
    bot.send_text(chat_id=event.from_chat, text="Для того, чтобы получить мем используй /meme")


def meme_sender(bot, event):
    if  sql_handlers.fct_counts() == 0:
        sql_handlers.truncate_fct_used_article()
        post_raw = post_creater.create_post()
        article_id_sql.article_id_insert(post_raw)
        bot.send_text(chat_id=event.from_chat , text=post_raw[1] +'\n\n'+ post_raw[2]+'\n\n'+'Источник: '+post_raw[3])
    else: 
        post_raw = post_creater.create_post()
        article_id_sql.article_id_insert(post_raw)
        bot.send_text(chat_id=event.from_chat , text=post_raw[1] +'\n\n'+ post_raw[2]+'\n\n'+'Источник: '+post_raw[3])
      

bot.dispatcher.add_handler(UnknownCommandHandler(callback=unknown_command_cb))
bot.dispatcher.add_handler(StartCommandHandler(callback=start_command))
bot.dispatcher.add_handler(HelpCommandHandler(callback=help_command))
bot.dispatcher.add_handler(CommandHandler(command="meme", callback=meme_sender))
bot.start_polling()
bot.idle()