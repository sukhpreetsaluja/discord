import discord
from discord.ext import commands

class coc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Clan Link for Official Sukhpreet Saluja's COC Clans!")
    async def coc(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Clash of Clans Clan Link is:\nhttps://sukh.gg/coc/")

def setup(bot):
    bot.add_cog(coc(bot))
