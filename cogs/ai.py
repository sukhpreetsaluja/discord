import discord
from discord.ext import commands
import config as c
import google.generativeai as genai
import requests
import os
import PIL

genai.configure(api_key=c.GEMINI_API)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 16384,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

class ai(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description = "Get Response from AI")
    async def ai(self, ctx, prompt: discord.Option(str), image: discord.Option(str, "Enter Link", required = False, default = None)):
        await ctx.defer()
        try:
            if image == None:
              response = model.generate_content(prompt)
              if len(response.text) > 1800:
                  with open("ai_response.txt", "w") as n:
                      n.write(response.text)
                  file = discord.File("ai_response.txt")
                  await ctx.followup.send("Response is Greater than 2000 Characters, So I uploaded it as a text file instead!\nNote: Response is Limited to 13000 Characters!", file=file)
              else:
                  await ctx.followup.send(f"{response.text}")
            else:
              download_dir = os.getcwd()
              response = requests.get(image)
              response.raise_for_status()

              file_name = os.path.basename(image)
              input = 'input'

              content_type = response.headers.get('Content-Type', '')
              if content_type == 'image/jpeg':
                  extension = '.jpg'
              elif content_type == 'image/png':
                  extension = '.png'
              elif content_type == 'video/mp4':
                  await ctx.followup.send("Support for Videos coming soon!")
                  return
              else:
                  await ctx.followup.send("I can only take `.jpg`, `.png` and `.mp4` Formats!")
                  return
              input = input + extension
              response = requests.get(image)
              response.raise_for_status()
              file_path = os.path.join(download_dir, input)
              with open(file_path, 'wb') as file:
                file.write(response.content)
              image = PIL.Image.open(input)
              print(image)
              response = model.generate_content([image, prompt])
              if len(response.text) > 1800:
                  with open("ai_response.txt", "w") as n:
                      n.write(response.text)
                  file = discord.File("ai_response.txt")
                  await ctx.followup.send("Response is Greater than 2000 Characters, So I uploaded it as a text file instead!\nNote: Response is Limited to 13000 Characters!", file=file)
              else:
                  await ctx.followup.send(f"{response.text}")
        except Exception as e:
            await ctx.respond(f"Due to Error Reponse was not Generated\nError Occured: `{e}`")

def setup(bot):
    bot.add_cog(ai(bot))