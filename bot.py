import os
import json

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType

from adalotl import Adalotl

from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
slash = SlashCommand(bot, sync_commands=True)

adalotl_command_options = create_option(
        name = "number",
        description = "This is the the Adalotl number, for example, for Adalotl 007, this will be '007'",
        option_type = SlashCommandOptionType.INTEGER,
        required = True
        )

@slash.slash(name="adalotl", options=[adalotl_command_options])
async def _adalotl(ctx: SlashContext, number):
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

    embed_image = discord.Embed(title=f"Adalotl {number}")
    embed_image.set_image(url=adalotl.image_url)

    embed_attributes = discord.Embed(title='Attributes')
    for attribute in adalotl.attributes:
        embed_attributes.add_field(
                name='\u200b',
                value=f"```{attribute}```",
                inline=True
                )

    await ctx.send(embeds=[embed_image, embed_attributes])

bot.run(DISCORD_TOKEN)
