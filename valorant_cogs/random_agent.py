import discord
from discord.ext import commands
import random

Valorant_Agents = ['Brimstone',
                   'Phoenix',
                   'Sage',
                   'Sova',
                   'Viper',
                   'Cypher',
                   'Reyna',
                   'Killjoy',
                   'Harbor',
                   'Breach',
                   'Omen',
                   'Jett',
                   'Raze',
                   'Skye',
                   'Yoru',
                   'Astra',
                   'Kay/O',
                   'Chamber',
                   'Neon',
                   'Fade',
                   'Gekko',
                   'Deadlock',
                   'ISO',
                   'Clove'
]

class random_agent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "It Will Give You Random Agent Of Valorant!")
    async def random_agent(self, ctx):
        await ctx.respond("Random Valorant Agent is:\n" + "**" + random.choice(Valorant_Agents) + "**")

def setup(bot):
    bot.add_cog(random_agent(bot))
