import discord
from discord.ext import commands
import requests
import textwrap
from PIL import Image, ImageDraw, ImageFont

class quote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(description = "Make a Quote with Message Link!")
    async def quote(self, ctx, message_link):
        await ctx.defer()
        if message_link[0:28] == "https://discord.com/channels":
            try:
                channel_id = int(message_link.split("/")[-2])
                message_id = int(message_link.split("/")[-1])
                channel = self.bot.get_channel(channel_id)
                message = await channel.fetch_message(message_id)

                text = message.content
                text_author = message.author 
                author_avatar = message.author.display_avatar
            
            except AttributeError:
                await ctx.respond(f"Message should be in Official Saluja Army's Discord Server!")
                return
            except ValueError:
                await ctx.respond(f"Message link not Valid!")
                return
            except Exception as e:
                await ctx.respond(f"Error Occured!\nError: `{e}`")
                return
            image = author_avatar     
            print(image)
            response = requests.get(image)
            if response.status_code == 200:
                with open("avatar.png", "wb") as f:
                    f.write(response.content)
            
            avatar = Image.open("avatar.png")
            quote_bg = Image.open("quote.png")
            new_height = 1024
            avatar = avatar.resize((int(1024 * 1.07), int(new_height * 1.07)))
            combined_img = Image.new('RGBA', (1920, 1080))
            combined_img.paste(avatar, (-150,0))
            combined_img.paste(quote_bg, mask=quote_bg)        

            draw = ImageDraw.Draw(combined_img)
            font = ImageFont.truetype("font.TTF", 84)
            author_font = ImageFont.truetype("font.TTF", 40)
            if len(text) > 100:
                text = text[:175] + "..."
            text = textwrap.wrap(text, width=20)
            x = combined_img.width*0.47
            y = 530
            final_text = ''
            for text in text:
                final_text = final_text + text + "\n"
                y -= 43
            draw.multiline_text((x,y), final_text, fill = (255,255,255), font=font, align="center")
            author_name = f"~ {text_author}"
            draw.text((620,1000), author_name, fill = (255,255,255), font=author_font)
            combined_img.save("Final_Quote_BG.png")

            await ctx.followup.send(f"[Jump to Original Message]({message_link})", file=discord.File('Final_Quote_BG.png'))
        else:
            await ctx.followup.send(f"Only Message links are supported!")

def setup(bot):
    bot.add_cog(quote(bot))