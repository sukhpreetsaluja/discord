import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class shut_down(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def shut_down(self, ctx):
        await ctx.respond("Bot Shutting Down!")
        await self.bot.db.close()
        await ctx.bot.close()

    @shut_down.error
    async def shut_down_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You don't have permission to use this Command!", ephemeral=True)

def setup(bot):
    bot.add_cog(shut_down(bot))
