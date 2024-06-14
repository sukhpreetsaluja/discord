import discord
from discord.ext import commands

class twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link of Official Sukhpreet Saluja's Twitch Channel!")
    async def twitch(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Twitch Channel Link is:\nhttps://sukh.gg/twitch/")

def setup(bot):
    bot.add_cog(twitch(bot))
