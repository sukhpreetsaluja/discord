import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class set_level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def set_level(self, ctx, level: discord.Option(int), xp: discord.Option(int), user_id: discord.Option(str)):
        await ctx.defer(ephemeral=True)

        async with self.bot.db.cursor() as cursor:
            await cursor.execute("UPDATE levels SET level = ?, XP = ? WHERE user = ?", (level, xp, user_id,))
            await self.bot.db.commit()
            user = await ctx.guild.fetch_member(user_id)
            await ctx.followup.send(f"Successfully Updated Levels of {user}")               

    @set_level.error
    async def set_level_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You don't have permission to use this Command!", ephemeral=True)

def setup(bot):
    bot.add_cog(set_level(bot))
