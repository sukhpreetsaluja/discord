import discord
from discord.ext import commands
import psutil
import time
import datetime

class about(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        global start_time
        global cpu_usage
        global ram_usage
        start_time = time.time()
        cpu_usage = psutil.cpu_percent(4)
        ram_usage = psutil.virtual_memory()[2]

    @discord.slash_command(description = "Bot will tell you some facts about itself")
    async def about(self, ctx):
        current_time_about_me = time.time()
        uptime_difference_about_me = int(round(current_time_about_me - start_time))
        uptime_about_me = str(datetime.timedelta(seconds=uptime_difference_about_me))
        await ctx.respond(f"I'm a Bot Created by Sukhpreet Singh Saluja For the official Discord Server of Saluja Army.\nI was Created on 2nd of Januray 2021 For the Purpose of Moderation but now I am Also Being used Commands and Fun as well!\nSome __**Interesting Stats**__ About me:\n> Ping: {round(self.bot.latency * 1000)}ms\n> Uptime: {uptime_about_me}\n> CPU Usage: {cpu_usage}%\n> Ram Usage: {ram_usage}%")

def setup(bot):
    bot.add_cog(about(bot))