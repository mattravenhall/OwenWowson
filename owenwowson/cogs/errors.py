#!/usr/bin/env python3

import random
import sys
import traceback

from discord.ext import commands


class CogErrHandler(commands.Cog):
    """Handle exceptions and unknown commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            confused_response = random.choice([
                f"\"{ctx.message.content}\"? What Are You Talking About?",
                f"This is the first time, for me, in the \"{ctx.message.content}\" universe",
                f"I've never heard of \"{ctx.message.content}\" before",
            ])
            await ctx.send(confused_response)
        else:
            print(f"Ignoring exception in command {ctx.command}:", file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(CogErrHandler(bot))
