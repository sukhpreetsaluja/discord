import discord
from discord.ext import commands
import DiscordUtils
import resend
import re
import config as c

email_check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
mobile_check = r'(0|91)?[6-9][0-9]{9}'
valorant_id_check = r'\b[\w\d ]{4,32}#[\w\d ]{3,5}\b'

class register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    class MyModal(discord.ui.Modal):
        def __init__(self, bot, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.bot = bot

            self.fullname = discord.ui.InputText(label="Full Name", required=True, placeholder="Enter your Full Name | Example: Sukhpreet Saluja")
            self.add_item(self.fullname)
            self.mobilenumber = discord.ui.InputText(label="Mobile Number", min_length=10, max_length=10 ,required=True, placeholder="Enter Your Mobile Number (Without Country Code) | Example: 9779400646")
            self.add_item(self.mobilenumber)
            self.email = discord.ui.InputText(label="Email Address", required=True, placeholder="Enter your Email ID | Example: contact@sukhpreetsaluja.com")
            self.add_item(self.email)
            self.Valorant_ID = discord.ui.InputText(label="Valorant ID", required=True, placeholder="Enter your Valorant ID | Example: Sukhpreet Saluja#NUB")
            self.add_item(self.Valorant_ID)

        async def callback(self, interaction: discord.Interaction):
            print(self.fullname.value)
            print(self.mobilenumber.value)
            print(self.email.value)
            print(self.Valorant_ID.value)
            await interaction.response.defer()
            if (re.fullmatch(email_check, self.email.value)):
                if (re.fullmatch(mobile_check, self.mobilenumber.value)):
                    if (re.fullmatch(valorant_id_check, self.Valorant_ID.value)):
                        resend.api_key = c.RESEND_API
                        sukh_dm = await self.bot.fetch_user(788436892512944200)
                        await sukh_dm.create_dm()
                        await sukh_dm.send(f"Name: `{self.fullname.value}`\nMobile Number: `{self.mobilenumber.value}`\nEmail: `{self.email.value}`\nValorant ID: `{self.Valorant_ID.value}`")
                        resend.Contacts.create({
                            "email": self.email.value,
                            "first_name": self.fullname.value,
                            "unsubscribed": False,
                            "audience_id": '504f6753-5bf0-4fb5-8f39-20dc0f2dd1a3',
                        })
                        email_params = {
                            "from": "Sukhpreet Saluja <contact@sukhpreetsaluja.com>",
                            "to": self.email.value,
                            "subject": "Confirmation: Registration for Sukhpreet Saluja's Official Valorant Event",
                            "html": f'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html dir="ltr" lang="en">

    <body style="font-family:-apple-system, BlinkMacSystemFont, &#x27;Segoe UI&#x27;, &#x27;Roboto&#x27;, &#x27;Oxygen&#x27;, &#x27;Ubuntu&#x27;, &#x27;Cantarell&#x27;, &#x27;Fira Sans&#x27;, &#x27;Droid Sans&#x27;, &#x27;Helvetica Neue&#x27;, sans-serif;font-size:1.0769230769230769em;min-height:100%;line-height:155%">
        <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation" style="align:center;padding-left:0px;padding-right:0px;h-padding:0px;width:auto;max-width:600px;font-family:-apple-system, BlinkMacSystemFont, &#x27;Segoe UI&#x27;, &#x27;Roboto&#x27;, &#x27;Oxygen&#x27;, &#x27;Ubuntu&#x27;, &#x27;Cantarell&#x27;, &#x27;Fira Sans&#x27;, &#x27;Droid Sans&#x27;, &#x27;Helvetica Neue&#x27;, sans-serif">
        <tbody>
            <tr>
            <td>
                <h2 style="margin:0;padding:0;font-size:2.25em;line-height:1.44em;padding-top:0.389em;font-weight:600;text-align:left"><span>Hello </span>{self.fullname.value}<span>,</span></h2>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"><span>We are pleased to notify you that your registration for </span><span><strong>Sukhpreet Saluja&#x27;s Official Valorant Event</strong></span><span> our upcoming valorant event, has been accepted and validated! We&#x27;re very happy to have you on board, and we hope you will participate.</span></p>
                <table align="center" width="100%" border="0" cellPadding="0" cellSpacing="0" role="presentation">
                <tbody style="width:100%">
                    <tr style="width:100%">
                    <td align="left" data-id="__react-email-column"><img src="https://resend-attachments.s3.amazonaws.com//KyyOreEZPGN0psm" style="display:block;outline:none;border:none;text-decoration:none;max-width:100%;border-radius:8px" width="100%" /></td>
                    </tr>
                </tbody>
                </table>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"><span>Your registration ensures that you&#x27;ll be at the event and guarantees your place in the action. We&#x27;re sure that this will be a great chance for you to show off your Valorant Skills and make new friends among the players in our community.</span></p>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"><span>Please contact the undersigned if you have any queries or require any further information prior to the event. We want you to have a wonderful experience, so we&#x27;re here to help in any way we can.</span></p>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"><span>Thank you once more for signing up for Sukhpreet Saluja&#x27;s Official Valorant Event. We&#x27;re excited to see you there and hope everything goes well for you!</span></p>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"><span>Regards,</span><br /><span>Sukhpreet Saluja</span><br /><span>+91 97794-00646</span></p>
                <p style="margin:0;padding:0;font-size:1em;padding-top:0.5em;padding-bottom:0.5em;text-align:left"></p>
            </td>
            </tr>
        </tbody>
        </table>
    </body>

    </html>'''
                        }
                        email = resend.Emails.send(email_params)
                        print(email)
                        return await interaction.followup.send("Your Registeration for the Event was Successful :D")
                    else:
                        return await interaction.followup.send("Your Registeration Failed!\nReason: `Invalid Valorant ID`")
                else:
                    return await interaction.followup.send("Your Registeration Failed!\nReason: `Invalid Mobile Number`")
            else:
                return await interaction.followup.send("Your Registeration Failed!\nReason: `Invalid Email Address`")


    @discord.slash_command(description="Use this Command to Register Yourself for the Upcoming Event!")
    async def register(self, ctx: discord.ApplicationContext):
        modal = self.MyModal(self.bot, title="Event Registeration")
        await ctx.send_modal(modal)

def setup(bot):
    bot.add_cog(register(bot))