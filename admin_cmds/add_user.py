import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions

class add_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def add_user(self, ctx, user_id: discord.Option(str)):
        await ctx.defer(ephemeral=True)
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("SELECT userid FROM admin_user WHERE userid = ?", (user_id,))
            check = await cursor.fetchall()
            check = len(check)
            user = await ctx.guild.fetch_member(user_id)
            if check >= 1:
                await ctx.followup.send(f"{user} is already in Admin List!", ephemeral=True)
            else:
                await cursor.execute("INSERT INTO admin_user (userid) VALUES (?)", (user_id,))
                await self.bot.db.commit()
                await ctx.followup.send(f"User {user} has been added to Admin List!", ephemeral=True)

    @add_user.error
    async def add_user_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You don't have permission to use this Command!", ephemeral=True)

def setup(bot):
    bot.add_cog(add_user(bot))
