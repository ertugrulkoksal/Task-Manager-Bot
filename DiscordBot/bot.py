import discord
from discord.ext import commands
import commands as bot_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command(name='add_task')
async def add_task(ctx, *, description):
    task_id = bot_commands.add_task(description)
    await ctx.send(f'Yeni Görevinde Başarılar. Görev ID: {task_id}')


@bot.command(name='delete_task')
async def delete_task(ctx, task_id: int):
    bot_commands.delete_task(task_id)
    await ctx.send(f'Görev Silindi. Silinen Görev ID: {task_id}')


@bot.command(name='show_tasks')
async def show_tasks(ctx):
    tasks = bot_commands.show_tasks()
    if tasks:
        response = '\n'.join([f"{task['id']}: {task['description']} - {'Görev Tamamlandı' if task['completed'] else 'Görev Devam Ediyor'}" for task in tasks])
    else:
        response = "Hiç görevin yok."
    await ctx.send(response)

@bot.command(name='complete_task')
async def complete_task(ctx, task_id: int):
    bot_commands.complete_task(task_id)
    await ctx.send(f'Görev Başarıyla Tamamlandı. Tebrikler :) Tamamlanan Görev ID: {task_id}')

#Enter discord token here
bot.run('DISCORD_TOKEN')
