#!/usr/bin/env python3

import asyncio
import os
import random
import sys
import traceback

from discord import Embed, FFmpegPCMAudio, Intents
from discord.channel import VoiceChannel
from discord.ext import commands
import requests
import yaml

from utils import LOGGER, valid_filepath


class OwenWowson(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True

        super().__init__(
            intents=intents,
            command_prefix='!',
            case_insensitive=True,
        )
        self.initial_extensions = [
            'cogs.errors',
            'cogs.health',
            'cogs.wows',
        ]

    async def on_ready(self):
        n_connected = len(self.guilds)
        guild_names = [f"{guild.name}:{guild.id}" for guild in self.guilds]
        LOGGER.debug(f"Successfully logged into {n_connected} server{'s' if n_connected > 1 else ''}: {', '.join(sorted(guild_names))}")

    async def on_message(self, message):
        # Prevent bot responding to itself
        if message.author == self.user:
            return

        LOGGER.debug(f"Spotted message: {message.content}")

        # Process as a command
        await bot.process_commands(message)


async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    async with bot:
        await load_extensions()
        await bot.start(input("Please provide your token: "))


if __name__ == '__main__':
    bot = OwenWowson()
    asyncio.run(main())
