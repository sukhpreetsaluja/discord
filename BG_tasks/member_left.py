import discord
from discord.ext import commands
import config as c

class member_left(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_member_remove")
    async def on_member_remove(self, member):
        goodbye_channel = self.bot.get_channel(c.GOODBYE_CHANNEL)
        await goodbye_channel.send(f"{member.name} Left the Server!")

def setup(bot):
    bot.add_cog(member_left(bot))