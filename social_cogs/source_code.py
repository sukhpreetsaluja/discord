import discord
from discord.ext import commands

class source_code(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get the Source Code for this Bot")
    async def source_code(self, ctx):
        await ctx.respond("Saluja Army's Official Bot Source Code is Available here: <https://sukh.gg/discordbot/>")

def setup(bot):
    bot.add_cog(source_code(bot))
