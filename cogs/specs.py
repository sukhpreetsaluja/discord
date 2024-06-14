import discord
from discord.ext import commands

class specs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get the Spec List of Sukhpreet Saluja's PC")
    async def specs(self, ctx):
        await ctx.respond("Sukhpreet Saluja's PC Specs are:\nCPU: AMD Ryzen 5 3600 (<https://amzn.to/4eeiU0m>)\nRam: 8GBX4 G.Skill Trident Z 3200Mhz (<https://amzn.to/45ldpZP>)\nMotherboard: Asrock B450 Steel Legend (<https://amzn.to/3XmepL6>)\nGPU: Nvidia GTX 1660 Super (<https://amzn.to/45nml0F>)")

def setup(bot):
    bot.add_cog(specs(bot))
