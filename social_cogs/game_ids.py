import discord
from discord.ext import commands

class game_id(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Every Single in-game ID of Sukhpreet Saluja")
    async def game_id(self, ctx):
        await ctx.respond('''Sukhpreet Saluja's In Game ID For all the Games:\n\n
                        **__Riot Games__**\nRiot ID: Sukhpreet Saluja\nTagline: #NUB\n
                        **__Epic Games__**\nEpic ID/Creator Code: SukhpreetSaluja\n
                            **__Steam__**\nSteam ID: sukhpreetsaluja\n
                         **__Battle.net__**\nBattle Tag: SukhpreetSS#1756\n
                             **__Xbox__**\nGamertag: SukhpreetSaluja''')
def setup(bot):
    bot.add_cog(game_id(bot))
