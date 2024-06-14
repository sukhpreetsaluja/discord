import discord
from discord.ext import commands

class socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Link of Every Single Official Sukhpreet Saluja's Socials!")
    async def socials(self, ctx):
        await ctx.respond("Sukhpreet Saluja's All Social Media Handler Links:\nYoutube: <https://sukh.gg/youtube>\nTwitch: <https://sukh.gg/twitch>\nX: <https://sukh.gg/x>\nWhatsapp: <https://sukh.gg/whatsapp>\nDiscord: <https://sukh.gg/discord>")

def setup(bot):
    bot.add_cog(socials(bot))
