import discord
from discord.ext import commands
import json
from urllib.request import Request, urlopen

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description="It will give you a random meme from Reddit!")
    async def meme(self, ctx):
        await ctx.defer()
        api_url = "https://meme-api.com/gimme"
        request_site = Request(api_url, headers={"User-Agent": "Mozilla/5.0"})
        memeapi = urlopen(request_site)
        memedata = json.load(memeapi)

        memeurl = memedata['url']
        memeposter = memedata['author']
        memesub = memedata['subreddit']
        memelink = memedata['postLink']

        embed = discord.Embed(title="Sukhpreet Saluja", url="https://www.sukhpreetsaluja.com/support")
        embed.set_image(url=memeurl)
        embed.set_footer(text=f"Meme By: {memeposter} | Subreddit: {memesub}")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(meme(bot))