import discord
from discord.ext import commands, tasks
import datetime
import pytz
import asyncio
import config as c

class birthday_wish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.birthday_wish.start()

    @tasks.loop(minutes=1)
    async def birthday_wish(self):
        ist_timezone = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.now(ist_timezone)
        if now.hour == 0 and now.minute == 0:
            today = now.strftime("%d-%m")

            async with self.bot.db.cursor() as cursor:
                cursor = await cursor.execute(
                    "SELECT user_id FROM birthdays WHERE birthday LIKE ?", (today + "%",)
                )
                rows = await cursor.fetchall()

            if rows:
                for user_id in rows:
                    member = self.bot.get_guild(c.DISCORD_SERVER_ID).get_member(user_id[0])
                    if member:
                        general_channel = self.bot.get_channel(c.GENERAL_CHANNEL)
                        await general_channel.send(f"Happy Birthday, {member.mention} :birthday:!")

    @birthday_wish.before_loop
    async def before_birthday_wish(self):
        await self.bot.wait_until_ready()
        print("About to Start!")
        await asyncio.sleep(10)
        
def setup(bot):
    bot.add_cog(birthday_wish(bot))
