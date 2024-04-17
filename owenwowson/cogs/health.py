#!/usr/bin/env python3

from discord.ext import commands


class CogHealth(commands.Cog, name='Healthcheck Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="healthcheck")
    async def adhoc_play(self, ctx):
        print(f"Heard command healthcheck")
        await ctx.send(f"All good!")


async def setup(bot):
    await bot.add_cog(CogHealth(bot))
