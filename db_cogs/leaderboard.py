import discord
from discord.ext import commands
import datetime
import config as c

class leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Find Out Who are the Top 10 Chatters of Saluja Army!")
    async def leaderboard(self, ctx):
        print("leaderboard")
        await ctx.defer()
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("SELECT level, xp, user FROM levels WHERE guild = ? ORDER BY level DESC, xp DESC LIMIT 10", (ctx.guild.id,))
            data = await cursor.fetchall()
            print(data)
            if data:
                em = discord.Embed(title="Level Leaderboard of Saluja Army!", timestamp=datetime.datetime.now(), url="https://www.sukhpreetsaluja.com")
                count = 0
                for table in data:
                    print(count)
                    count += 1
                    user = await ctx.guild.fetch_member(table[2])
                    em.add_field(name=f"{count}. {user}", value=f"Level: **{table[0]}** | XP: **{table[1]}**", inline=False)
                em.set_footer(text="Saluja Army",)
                print("done")
                await ctx.respond(embed=em)

def setup(bot):
    bot.add_cog(leaderboard(bot))