import discord
from discord.ext import commands
import datetime
import random


rank_cmd_random_tip = [ '**Tip:** If you want to increase your level FASTTTTT Then be active in <#498395996531982340> :)',
                        'Dhooooop', 'Briyani OP', 'WoooooooooW', 'Sukh OP', 'Shoutout to Every Single Supporter!',
                        'I Wonder what is the age of Sukh?', 'How do I Apply for King Role?', 'What da Dog Doin\'?',
                        'Love you💖', 'Sukh Haggu', 'I Wonder What\'s C4Ruler is Upto🤔', 'Is Jaskaran Ded?',
                        'I Want to Reach Radiant Someday', '6969 Ophieee', 'What\'s the Next Member Only Sneak? I Wonder....',
                        'Instagram Sucks', 'RIP Prince86🪦', 'Yash Shah Came in Clutch!', 'It\'s Not Yuvi It\'s Yubi Remember That!',
                        'Haggu Vapis Kabh Ayega?', 'When will Sukh Haggu Next part will Come? I Wonder....', '150 Rupiya Dega!',
                        'Jett FTW', 'Can I Be Your Pocket Sage❣️', 'Team Flash Incoming.... Opponent Reyna: Uno Reverse Card',
                        'Facecam Kabh?', 'Aap toh Bahut Gyani ho baba... aapke jaise kaun?',
                        'Think You can keep up?', 'Whole Team Saves this round. Meanwhile Jett with Ultimate: I Don\'t Have Such Weaknesses!',
                        'Ha vai agya swaad?', 'Better Luck Next Time!', 'SHOP.SUKH.GG is the Best Merch You would ever find :D']


class rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Find out your Rank in Saluja Army!")
    async def rank(self, ctx):
        member = ctx.author
        if member is None:
            member = ctx.author
        #try:
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
            xp = await cursor.fetchone()
            await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (member.id, ctx.guild.id))
            level = await cursor.fetchone()

            if not xp or not level:
                await cursor.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?,?,?,?)", (0, 0, member.id, ctx.guild.id))
                await self.bot.db.commit()
                await self.bot.process_application_commands()

            try:
                xp = xp[0]
                level = level[0]
            except TypeError:
                xp = 0
                level = 0
            userAvatar = member.display_avatar

            em = discord.Embed(title=f"{member.name}'s Rank in Saluja Army!", description=f"Level: **{level}**\n XP: **{xp}/100**\n", timestamp=datetime.datetime.now(), url="https://www.sukhpreetsaluja.com")
            em.add_field(name="\u200b", value=random.choice(rank_cmd_random_tip))
            em.set_footer(text="Saluja Army",)
            em.set_thumbnail(url=userAvatar.url)
            await ctx.respond(embed=em)
        #except AttributeError:
         #   await ctx.respond("This Command is only usable in Official Server of Saluja Army!\nJoining Link: <https://sukh.gg/discord>")

def setup(bot):
    bot.add_cog(rank(bot))