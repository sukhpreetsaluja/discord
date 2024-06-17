import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
import datetime


class update_birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @commands.has_permissions(administrator=True)
    async def update_birthday(self, ctx, user_id, date):
        await ctx.defer()
        try:
            datetime.datetime.strptime(date, "%d-%m-%Y")
        except ValueError:
            await ctx.followup.send("Invalid birthday format. Please use DD-MM-YYYY.")
            return
        
        async with self.bot.db.cursor() as cursor:
            check = await cursor.execute(
            "SELECT birthday FROM birthdays WHERE user_id = ?", (ctx.author.id,)
        )
            row = await cursor.fetchone()

            if row:
                await cursor.execute(
                    "INSERT OR REPLACE INTO birthdays (user_id, birthday) VALUES (?, ?)",
                    (ctx.author.id, date,),
                )
                await self.bot.db.commit()
                await ctx.followup.send(f"Birthday of User {user_id} is Updated to {date}")
            else:
                await ctx.followup.send(f"User Doesn't Exsists!")




    @update_birthday.error
    async def update_birthday_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.respond("You don't have permission to use this Command!", ephemeral=True)

def setup(bot):
    bot.add_cog(update_birthday(bot))