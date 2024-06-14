import discord
from discord.ext import commands

class twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link for Official Sukhpreet Saluja's Twitter/X Accoount!")
    async def twitter(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Twitter Handler Link is:\nhttps://sukh.gg/twitter/")

def setup(bot):
    bot.add_cog(twitter(bot))
