import discord
from discord.ext import commands
import time
import datetime

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        global start_time
        start_time = time.time()

    @discord.slash_command(description = "This Will Give you The Latency of The Bot")
    async def ping(self, ctx):
        current_time_ping = time.time()
        uptime_difference_ping = int(round(current_time_ping - start_time))
        uptime_ping = str(datetime.timedelta(seconds=uptime_difference_ping))
        await ctx.respond(f"Pong! \nBot Response Time: {round(self.bot.latency * 1000)}ms\nMy Uptime is {uptime_ping}")

def setup(bot):
    bot.add_cog(ping(bot))
