import discord
from discord.ext import commands
import random
import config as c
from discord.utils import get

class leveling_system(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def leveling_system(self, message):
        if message.author.bot:
            return
        author = message.author
        guild = message.guild
        spam_channel = self.bot.get_channel(1039597157130440723)
        if message.channel == spam_channel:
            print("No XP Given")
        else:
            async with self.bot.db.cursor() as cursor:
                await cursor.execute("SELECT xp FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
                xp = await cursor.fetchone()
                await cursor.execute("SELECT level FROM levels WHERE user = ? AND guild = ?", (author.id, guild.id,))
                level = await cursor.fetchone()
                if not xp or not level:
                    await cursor.execute("INSERT INTO levels (level, xp, user, guild) VALUES (?,?,?,?)", (0, 0, author.id, guild.id))
                    await self.bot.db.commit()
                    
                try:
                    xp = xp[0]
                    level = level[0]
                except TypeError:
                    xp = 0
                    level = 0
                if get(author.roles, id=c.MEMBER_ONLY_ROLE_ID):
                    print(f"{author} have this role!")
                    random_level = random.randint(2, 6)
                    print(random_level)
                    if level < 5:
                        await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp+random_level, author.id, guild.id))
                    else:
                        rand = random.randint(1, int(level/2))
                        if rand == 1:
                            xp = xp + random.randint(2, 6)
                            await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))
                else:
                    print(f"{author} Does not have this role!")
                    random_level = random.randint(1, 3)
                    print(random_level)
                    if level < 5:
                        await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp+random_level, author.id, guild.id))
                    else:
                        rand = random.randint(1, level)
                        if rand == 1:
                            xp = xp + random.randint(1, 3)
                            await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (xp, author.id, guild.id))

                if xp >= 100:
                    level += 1
                    await cursor.execute("UPDATE levels SET level = ? WHERE user = ? AND guild = ?", (level, author.id, guild.id))
                    await cursor.execute("UPDATE levels SET xp = ? WHERE user = ? AND guild = ?", (0, author.id, guild.id))
                    rank_channel = self.bot.get_channel(1054366900513157164)
                    
                    await rank_channel.send(f'Congratulations {author.mention}, You Just Leveled up to **{level}**!')
            await self.bot.db.commit()
            if level >= 100:
                sukh_id = ['Sukhpreet Saluja#4646', 'sukhpreetsaluja#0']
                if str(message.author) in sukh_id:
                    return
                else:
                    message_channel = message.channel.id
                    await message_channel.send(f"Congratulations, {author.mention} For Reaching Level 100. It was your Hard Work and Dedication to our Community! You can Claim your Gift by Opening a Support Ticket :D")
                if level >= 75:
                    member = message.author
                    level_75_role_id = 1039597154404147253
                    level_75_role = discord.utils.get(guild.roles, id=level_75_role_id)
                    await  member.add_roles(level_75_role)
                    if level >= 50:
                        member = message.author
                        level_50_role_id = 1039597154378989667
                        level_50_role = discord.utils.get(guild.roles, id=level_50_role_id)
                        await  member.add_roles(level_50_role)
                        if level >= 30:
                            member = message.author
                            level_30_role_id = 1039597154358005779
                            level_30_role = discord.utils.get(guild.roles, id=level_30_role_id)
                            await  member.add_roles(level_30_role)
                            if level >= 20:
                                member = message.author
                                level_20_role_id = 1039597154358005775
                                level_20_role = discord.utils.get(guild.roles, id=level_20_role_id)
                                await  member.add_roles(level_20_role)
                                if level >= 15:
                                    member = message.author
                                    level_15_role_id = 1039597154337038403
                                    level_15_role = discord.utils.get(guild.roles, id=level_15_role_id)
                                    await  member.add_roles(level_15_role)                                
                                    if level >= 10:
                                        member = message.author
                                        level_10_role_id = 1039597154337038402
                                        level_10_role = discord.utils.get(guild.roles, id=level_10_role_id)
                                        await  member.add_roles(level_10_role)
                                        if level >= 5:
                                            member = message.author
                                            level_5_role_id = 1039597154337038399
                                            level_5_role = discord.utils.get(guild.roles, id=level_5_role_id)
                                            await  member.add_roles(level_5_role)
                                        else:
                                            pass



def setup(bot):
    bot.add_cog(leveling_system(bot))
