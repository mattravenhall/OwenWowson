#!/usr/bin/env python3

from discord import FFmpegPCMAudio
from discord.ext import commands
from discord.channel import VoiceChannel
import requests


class CogWow(commands.Cog):
    """Deal out them wows"""
    def __init__(self, bot):
        self.bot = bot
        self._endpoint = "https://owen-wilson-wow-api.onrender.com/wows/random"

    def text_response(self, endpoint: str) -> str:
        return message

    @commands.command(name="wow")
    async def random_wow(self, ctx):
        print(f"Responding to wow command")

        response = requests.get(self._endpoint)

        # Handle failures
        if response.status_code != 200:
            await ctx.channel.send("Oops, looks like the API is down...")
        else:
            # Parse wow
            resp = response.json()[0]

            # Send text response
            message = '\n'.join([
                f"{resp['video']['480p']}",
                f"Wow number {resp['current_wow_in_movie']} of {resp['total_wows_in_movie']} from \"{resp['movie']}\" ({resp['year']})",
                f"\"{resp['full_line']}\"",
            ])
            await ctx.channel.send(message)

            # Send audio response, if in a voice channel
            for voice_client in self.bot.voice_clients:
                if voice_client.guild == ctx.guild:
                    break
            else:
                print(f"No activate voice channel")
                return
            voice_client.play(FFmpegPCMAudio(resp['audio']))

    @commands.command(name="join")
    async def join_channel(self, ctx):
        print(f"Responding to join command")

        if len(ctx.message.content.split()) == 1:
            await ctx.channel.send("Join what? You forgot to provide a voice channel!")
        else:

            destination = ctx.message.content.split()[1]

            voice_channels = {
                channel.name: channel for channel in ctx.guild.channels
                if isinstance(channel, VoiceChannel)
            }

            if destination in voice_channels.keys():
                await ctx.channel.send("On my way!")
                await voice_channels[destination].connect()
            else:
                await ctx.channel.send(f"Couldn't find a voice channel called '{destination}'")

    @commands.command(name="joinme")
    async def summon(self, ctx):
        print(f"Responding to joinme command")
        if hasattr(ctx.author.voice, 'channel'):
            await ctx.channel.send("On my way!")
            await ctx.author.voice.channel.connect()
        else:
            await ctx.channel.send(f"You're not in a voice channel!")


async def setup(bot):
    await bot.add_cog(CogWow(bot))
