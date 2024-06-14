import discord
from discord.ext import commands
import re

class check_links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.Cog.listener("on_message")
    async def on_message(self, message):
        if message.author.bot:
            return
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("SELECT userid FROM admin_user WHERE userid = ?", (message.author.id,))
            row = await cursor.fetchone()
            if row is not None:
                pass
            else:
                regex = (r'^((http|https)://)?(?!(?:\w+\.)?(?:tenor\.com|giphy\.com|sukhpreetsaluja\.com|sukh\.gg|gurpreetsaluja\.com|gsfs\.link))(?=[a-zA-Z0-9])([a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}(?:/[^#?]*\?[^#]*)?$')
                print(message.content)

                if re.match(regex, message.content.lower().replace(' ', '').replace(')', '').replace('(', '').replace('/', '').replace('-', '')) is not None:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention}, Links are not Allowed!")

def setup(bot):
    bot.add_cog(check_links(bot))
