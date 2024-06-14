import discord
from discord.ext import commands

class youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link for Official Sukhpreet Saluja's Youtube Channel!")
    async def youtube(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Youtube Channel Link is:\nhttps://sukh.gg/youtube/")

def setup(bot):
    bot.add_cog(youtube(bot))
