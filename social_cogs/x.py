import discord
from discord.ext import commands

class x(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link for Official Sukhpreet Saluja's X/Twitter Account!")
    async def x(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official X Handler Link is:\nhttps://sukh.gg/x/")

def setup(bot):
    bot.add_cog(x(bot))
