import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class remove_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def remove_user(self, ctx, user_id: discord.Option(str)):
        await ctx.defer(ephemeral=True)
        async with self.bot.db.cursor() as cursor:     
            user = await ctx.guild.fetch_member(user_id)
            await cursor.execute("SELECT userid FROM admin_user WHERE userid = ?", (user_id,))
            check = await cursor.fetchall()
            check = len(check)
            if check >= 1:
                await cursor.execute("DELETE FROM admin_user WHERE userid = ?", (user_id,))
                await self.bot.db.commit()
                await ctx.followup.send(f"User {user} has been removed from Admin List!", ephemeral=True)
            else:
                await ctx.followup.send(f"{user} Doesn't Exist in Admin List!", ephemeral=True)                

    @remove_user.error
    async def remove_user_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You don't have permission to use this Command!", ephemeral=True)

def setup(bot):
    bot.add_cog(remove_user(bot))
