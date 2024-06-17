import discord
from discord.ext import commands
import datetime


class birthday(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Set your Birthday!")
    async def birthday(self, ctx, date):
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
                await ctx.followup.send(f"Your birthday was already set to `{row[0]}`!")
            else:
                await cursor.execute(
                    "INSERT INTO birthdays (user_id, birthday) VALUES (?, ?)",
                    (ctx.author.id, date,),
                )
                await self.bot.db.commit()
                await ctx.followup.send(f"Your birthday has been set to {date}.")

def setup(bot):
    bot.add_cog(birthday(bot))