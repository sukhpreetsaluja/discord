import discord
from discord.ext import commands

class discord(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get the Official Sukhpreet Saluja's Discord Invite Link!")
    async def discord(self, ctx):
        await ctx.respond("Sukhpreet Saluja's Official Discord Server Invite Link is:\nhttps://sukh.gg/discord")

def setup(bot):
    bot.add_cog(discord(bot))
