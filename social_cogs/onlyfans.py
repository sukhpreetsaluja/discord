import discord
from discord.ext import commands

class onlyfans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get link of Offical Sukhpreet Saluja's OnlyFans!")
    async def onlyfans(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official OnlyFans Link is:\nhttps://sukh.gg/onlyfans/")

def setup(bot):
    bot.add_cog(onlyfans(bot))
