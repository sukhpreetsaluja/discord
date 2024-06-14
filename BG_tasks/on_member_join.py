import discord
from discord.ext import commands
import config as c

class member_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_member_join")
    async def on_member_join(self, member):
        print(f"{member} Joined!")
        general_channel = self.bot.get_channel(c.GENERAL_CHANNEL)
        default_role = member.guild.get_role(c.DEFAULT_ROLE_ID)
        chat_revive_role = member.guild.get_role(c.CHAT_REVIVE_ROLE_ID)
        giveaway_role = member.guild.get_role(c.GIVEAWAY_ROLE_ID)
        blog_role = member.guild.get_role(c.BLOG_ROLE_ID)
        await member.add_roles(default_role, chat_revive_role, giveaway_role, blog_role)
        await general_channel.send(f"Welcome {member.mention} Hope you will Enjoy Staying in our Server :)")
        try:
            await member.create_dm()
            await member.dm_channel.send('''Welcome to Our Official Discord Server!

This server is designed to be a gathering place for everyone who watches my content!

<#1039597156736180304> - Chat with Our Community!

<#1039793013372760094> - Post Your Arts Over Here!

<#1039792883571621990> If You Need Any Assistance From Our Community!

To Get Roles Go to <#1039597156736180295>

Make Sure to Read The rules Before Chatting :)

Our Server Invite Link:
<https://sukh.gg/dc>
<https://sukh.gg/discord>
https://discord.gg/ANV4nX5BNf''')
        except Exception:
            print("DM not Sent!")


def setup(bot):
    bot.add_cog(member_join(bot))