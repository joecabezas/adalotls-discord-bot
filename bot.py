import os
import json

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType
from dotenv import load_dotenv

from adalotl import Adalotl

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

adalotls_command_options = create_option(
        name = "number",
        description = "This is the the Adalotl number, for example, for Adalotl 007, this will be '007'",
        option_type = SlashCommandOptionType.INTEGER,
        required = True
        )

@slash.slash(name="adalots", options=[adalotls_command_options])
async def _adalots(ctx: SlashContext, number):
    await ctx.defer()

    if (number < 1 or number > 888):
        await ctx.send('Hey!, that adalotl does not exist! :<')
        return

    number = f"{number:03}"

    adalotl = None
    try:
        adalotl = Adalotl(number)
    except TypeError as e:
        await ctx.send('Adalotl not found or not minted yet')
        return

    embed = discord.Embed(title=f"Adalotl {number}")
    #embed.add_field(name="Name", value=json.dumps(metadata, indent=4))
    embed.set_image(url=adalotl.image_url)

    await ctx.send(embeds=[embed])

bot.run(DISCORD_TOKEN)
