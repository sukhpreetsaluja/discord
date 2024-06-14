import discord
from discord.ext import commands
import aiohttp
import json

class bored(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Bot will give you a Fun Activity to Do!")
    async def bored(self, ctx):
        await ctx.defer()
        try:
            api = "http://www.boredapi.com/api/activity?participants=1&price=0"
            async with aiohttp.ClientSession() as session:
                async with session.get(api) as res:
                    data = await res.json()
                    activity = data["activity"]
                    await ctx.followup.send(f"{activity}")
        except Exception as e:
            await ctx.followup.send(f"Error Occured!\nError Code: `{e}`")

def setup(bot):
    bot.add_cog(bored(bot))