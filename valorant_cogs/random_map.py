import discord
from discord.ext import commands
import random

Valorant_Maps = ['Bind',
                 'Haven',
                 'Split',
                 'Fracture',
                 'Breeze',
                 'Icebox',
                 'Pearl',
                 'Ascent',
                 'Lotus',
                 'Sunset',
                 'Abyss'
]

class random_map(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "It Will Give You Random Map For Valorant. It's Very Useful For Custom Games!")
    async def random_map(self, ctx):
        await ctx.respond("Random Valorant Map is:\n" + "**" + random.choice(Valorant_Maps) + "**")


def setup(bot):
    bot.add_cog(random_map(bot))
