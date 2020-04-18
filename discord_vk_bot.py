import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random
import post_creater
import article_id_sql
import sql_handlers



prefix = '!'
vkd_bot = commands.Bot(command_prefix=prefix)
vkd_bot.remove_command('help')

@vkd_bot.command()
async def help(ctx):
    emb = discord.Embed(title='Commands', colour=random.randint(0, 0xFFFF))
    emb.add_field(name='Use this for get a meme', value="{}meme".format(prefix))
    await ctx.send(embed=emb)

@vkd_bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Упс... Я не знаю такой команды. Используй !help для справки.')

@vkd_bot.command()
async def meme(ctx):
    if sql_handlers.fct_counts() == 0:
        sql_handlers.truncate_fct_used_article()
        post_raw = post_creater.create_post()
        article_id_sql.article_id_insert(post_raw)
        if post_raw[1] == '':
            emb = discord.Embed(colour=random.randint(0, 0xFFFF))
            emb.description = 'Источник: ['+post_raw[3]+']('+post_raw[3]+')'
            emb.set_image(url=post_raw[2])
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(colour=random.randint(0, 0xFFFF))
            emb.description = 'Источник: ['+post_raw[3]+']('+post_raw[3]+')\n\n```'+post_raw[1]+'```'
            emb.set_image(url=post_raw[2])
            await ctx.send(embed=emb)
    else:
        post_raw = post_creater.create_post()
        article_id_sql.article_id_insert(post_raw)
        if post_raw[1] == '':
            emb = discord.Embed(colour=random.randint(0, 0xFFFF))
            emb.description = 'Источник: ['+post_raw[3]+']('+post_raw[3]+')'
            emb.set_image(url=post_raw[2])  
            await ctx.send(embed=emb)
        else:
            emb = discord.Embed(colour=random.randint(0, 0xFFFF))
            emb.description = 'Источник: ['+post_raw[3]+']('+post_raw[3]+')\n\n```'+post_raw[1]+'```'
            emb.set_image(url=post_raw[2])  
            await ctx.send(embed=emb)


vkd_bot.run(open('token.txt', 'r').readline())