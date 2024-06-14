import discord
from discord.ext import commands

class upi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get UPI ID to Support Sukhpreet Saluja")
    async def upi(self, ctx):
        await ctx.respond("Now You can Support Sukhpreet Saluja using any Payment Method using this link\nhttps://sukh.gg/support")

def setup(bot):
    bot.add_cog(upi(bot))
