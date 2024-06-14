import discord
from discord.ext import commands

class support(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Want to Support Sukhpreet Saluja?")
    async def support(self, ctx):
        await ctx.respond("You can Support Sukhpreet Saluja using this link:\n<https://sukh.gg/support>\nYoutube Membership: <https://sukh.gg/join>")

def setup(bot):
    bot.add_cog(support(bot))
