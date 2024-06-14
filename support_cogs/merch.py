import discord
from discord.ext import commands

class merch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Official Sukhpreet Saluja Merch")
    async def merch(self, ctx):
        await ctx.respond("Now you can REP yourself using Official Sukhpreet Saluja's Merch!\nBUY NOW: https://shop.sukh.gg/")

def setup(bot):
    bot.add_cog(merch(bot))
