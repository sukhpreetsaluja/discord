import discord
from discord.ext import commands

class whatsapp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link for Official Sukhpreet Saluja's Whatsapp Community Link!")
    async def whatsapp(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Whatsapp Community Link is:\nhttps://sukh.gg/whatsapp/")

def setup(bot):
    bot.add_cog(whatsapp(bot))
