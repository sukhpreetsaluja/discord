import discord
from discord.ext import commands

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Gives you the commands that can be used with this Bot!")
    async def help(self, ctx):
        await ctx.respond("You can get All Commands That can Be Used Here:\nhttps://sukhpreetsaluja.com/botcmd/")

def setup(bot):
    bot.add_cog(help(bot))
