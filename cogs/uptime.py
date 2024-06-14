import discord
import time
from discord.ext import commands
import datetime

class uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        global start_time
        start_time = time.time()

    @discord.slash_command(description = "Check the Uptime of the Bot")
    async def uptime(self, ctx):
        current_time = time.time()
        uptime_diff = int(round(current_time-start_time))
        uptime = str(datetime.timedelta(seconds=uptime_diff))
        await ctx.respond(f"My Uptime is {uptime}")

def setup(bot):
    bot.add_cog(uptime(bot))
