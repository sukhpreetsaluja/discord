import discord
from discord.ext import commands

class afk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener("on_message")
    async def afk_msg(self, message):
        if message.author.bot:
            return
        async with self.bot.db.cursor() as afk:
            await afk.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?", (message.author.id, message.guild.id))
            data = await afk.fetchone()
            if data:
                await message.channel.send(f"{message.author.mention}, Welcome Back From AFK!")
                await afk.execute("DELETE FROM afk WHERE user = ? AND guild = ?", (message.author.id, message.guild.id))
            if message.mentions:
                for mention in message.mentions:
                    await afk.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?", (mention.id, message.guild.id))
                    data2 = await afk.fetchone()
                    if data2 and mention.id != message.author.id:
                        await message.channel.send(f"{mention.name} is Currently AFK!\nReason: `{data2[0]}`")
        await self.bot.db.commit()
        await self.bot.process_application_commands(message)
            
    @discord.slash_command(description = "Set AFK Status")
    async def afk(self, ctx, *, reason = None):
        if reason == None:
            reason = "No Reason Provided!"
        async with self.bot.db.cursor() as cursor:
            await cursor.execute("SELECT reason FROM afk WHERE user = ? AND guild = ?", (ctx.author.id, ctx.guild.id))
            data = await cursor.fetchone()
            if data:
                if data[0] == reason:
                    return await ctx.respond("You are Already AFK with the Same Reason!", ephemeral=True)
                await cursor.execute("UPDATE afk SET reason = ? WHERE user = ? AND guild = ?", (reason, ctx.author.id, ctx.guild.id))
            else:
                await cursor.execute("INSERT INTO afk (user, guild, reason) VALUES(?, ?, ?)", (ctx.author.id, ctx.guild.id, reason))
                await ctx.respond(f"You are now AFK for `{reason}`", ephemeral=True)
            await self.bot.db.commit()


def setup(bot):
    bot.add_cog(afk(bot))