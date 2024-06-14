import discord
from discord.ext import commands

class valorant_id(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Want to Play with Sukhpreet Saluja?")
    async def valorant_id(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Valorant ID is\nRiot ID: **Sukhpreet Saluja**\nTagline: **#NUB**")


def setup(bot):
    bot.add_cog(valorant_id(bot))
