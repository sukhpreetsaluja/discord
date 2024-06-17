import discord
import aiosqlite
import config as c


bot = discord.Bot(intents=discord.Intents().all())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(
        name='This Server', url='https://www.twitch.tv/sukhpreetsaluja'))
    setattr(bot, "db", await aiosqlite.connect('main.db'))
    async with bot.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS afk (user INTEGER, guild INTEGER, reason TEXT)")
        await cursor.execute("CREATE TABLE IF NOT EXISTS levels (level INTEGER, xp INTEGER, user INTEGER, guild INTEGER)")
        await cursor.execute("CREATE TABLE IF NOT EXISTS image_gen (user_id INTEGER, number INTEGER)")
        await cursor.execute("CREATE TABLE IF NOT EXISTS birthdays (user_id INTEGER PRIMARY KEY, birthday TEXT NOT NULL)")
        await bot.db.commit()
    print("Bot is Ready")

'''test_cog = [
    'birthday'
]'''

cogs_list = [
    'ai',
    'uptime',
    'about',
    'bored',
    'meme',
    'ping',
    'specs',
    'weather',
    'quote'
]

db_cogs = [
    'afk',
    'leaderboard',
    'rank',
    'birthday'
]

social_cogs = [
    'coc',
    'discord',
    'onlyfans',
    'twitch',
    'twitter',
    'whatsapp',
    'x',
    'youtube',
    'game_ids',
    'help',
    'socials',
    'source_code'
]

support_cogs = [
    'upi',
    'support',
    'merch'
]

valorant_cogs = [
    'random_agent',
    'random_map',
    'valorant_id',
    'register'
]

BG_tasks = [
    'leveling_system',
    'on_member_join',
    'check_links',
    'member_left',
    'birthday_wish'
]


admin_cmds = [
    'shut_down',
    'remove_user',
    'add_user',
    'set_level',
    'update_birthday'
]

'''for cog in test_cog:
    bot.load_extension(f'cogs.{cog}')
    print(f"{cog} Loaded")'''


for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')
    print(f"{cog} Loaded")

for db_cog in db_cogs:
    bot.load_extension(f'db_cogs.{db_cog}')
    print(f"{db_cog} Loaded")

for social_cogs in social_cogs:
    bot.load_extension(f'social_cogs.{social_cogs}')
    print(f"{social_cogs} Loaded")

for support_cog in support_cogs:
    bot.load_extension(f'support_cogs.{support_cog}')
    print(f"{support_cog} Loaded")

for valo_cog in valorant_cogs:
    bot.load_extension(f'valorant_cogs.{valo_cog}')
    print(f"{valo_cog} Loaded")

for BG_Tasks in BG_tasks:
    bot.load_extension(f'BG_tasks.{BG_Tasks}')
    print(f"{BG_Tasks} Loaded")

for admin_cog in admin_cmds:
    bot.load_extension(f'admin_cmds.{admin_cog}')
    print(f"{admin_cog} Loaded")

bot.run(c.FINAL_TOKEN)