import discord
from discord.ext import commands
import config as c
import aiohttp

class weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Latest Weather Condition of any City!")
    async def weather(self, ctx, city: discord.Option(str)):
        await ctx.defer()
        api = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": c.WEATHER_API_KEY,
            "q": city
        }

        async with aiohttp.ClientSession() as session:
            async with session.get(api, params=params) as res:
                data = await res.json()
                try:
                    location = data["location"]["name"]
                    temp_c = data["current"]["temp_c"]
                    temp_f = data["current"]["temp_f"]
                    humidity = data["current"]["humidity"]
                    wind_kph = data["current"]["wind_kph"]
                    wind_mph = data["current"]["wind_mph"]
                    condition = data["current"]["condition"]["text"]
                    image_url = "http:" + data["current"]["condition"]["icon"]

                    embed = discord.Embed(title=f"Weather For {location}", description=f"The Condition in `{location}` is `{condition}`")
                    embed.add_field(name="Temprature", value=f"C: {temp_c} | F: {temp_f}")
                    embed.add_field(name="Humidity", value=f"{humidity}")
                    embed.add_field(name="Wind Speed", value=f"KPH: {wind_kph} | MPH: {wind_mph}")
                    embed.set_thumbnail(url=image_url)

                    await ctx.followup.send(embed=embed)
                except KeyError:
                    await ctx.followup.send(f"Unable to Find the City Named `{city}`")

def setup(bot):
    bot.add_cog(weather(bot))