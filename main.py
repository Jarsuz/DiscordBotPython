Prefix = '?'

Token = ""

Embed_Color = 3447003







### DO NOT EDIT THIS BELOW UNLESS YOU KNOW WHAT YOU ARE DOING ###
from discord.ext import commands
import datetime, re
import json
import discord
import asyncio
import time
import datetime
import random
import aiohttp
import os
import logging
import json
import requests
start_time = time.time()


embed_color = Embed_Color
ver = "0.1"
description = "Discord Self Bot"
bot = commands.Bot(command_prefix='?', description=description, pm_help=None, self_bot=False)


@bot.event
async def on_ready():
	print("Logged in!")
	idle = discord.Status.idle
	print("Changed the status to: Idle")
	await bot.change_presence(activity=discord.Game(name='Fortnite'), status = idle, afk = False)

@bot.command(pass_context = True)
async def stats(ctx):
	second = time.time() - start_time
	minute, second = divmod(second, 60)
	hour, minute = divmod(minute, 60)
	day, hour = divmod(hour, 24)
	week, day = divmod(day, 7)
	embed = discord.Embed(color = embed_color)
	embed.add_field(name="Version", value=ver, inline=False)
	embed.add_field(name="Uptime", value="Weeks: %d, Days: %d, Hours: %d, Minutes: %d"% (week, day, hour, minute), inline=False)
	embed.add_field(name="Prefix", value=Prefix, inline=False)
	embed.set_footer(text="Discord self bot made by Kyousei#8357")
	await ctx.send(embed = embed)


@bot.command(pass_context = True)
async def shutdown(ctx):
	print("Bot shutting down!")
	await bot.logout()

@bot.command(pass_context = True)
async def heart(ctx):
    hearts1 = ["❤", "💞", "💗", "💟", "❣", "♥", "💕", "💓", "💝", "❤💞", "💗💟", "❣♥", "💕💓", "❤💞💗", "💟❣♥", "❤💕💓"]
    hearts2 = ["❤", "💞", "💗", "💟", "❣", "♥", "💕", "💓", "💝", "❤💞", "💗💟", "❣♥", "💕💓", "❤💞💗", "💟❣♥", "❤💕💓"]
    hearts3 = ["❤", "💞", "💗", "💟", "❣", "♥", "💕", "💓", "💝", "❤💞", "💗💟", "❣♥", "💕💓", "❤💞💗", "💟❣♥", "❤💕💓"]
    embed = discord.Embed(description = random.choice(hearts3) + random.choice(hearts2) + random.choice(hearts1), color = embed_color)
    await ctx.send(embed = embed)


@bot.command(pass_context = True)
async def ping(ctx):
	pingtime = time.time()
	pingms = await ctx.send("Pinging...")
	ping = (time.time() - pingtime) * 1000
	await bot.edit_message(pingms, ":ping_pong: The ping time is `%dms`" % ping)


@bot.command(pass_context = True)
async def ud(ctx, *, msg):
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    response = requests.get(api, params=[("term", word)]).json()
    embed = discord.Embed(description = "No results found!", color = 0xFF0000)
    if len(response["list"]) == 0: return await client.say(embed = embed)
    
    embed = discord.Embed(title = "Word", description = word, color = embed_color)
    embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
    embed.add_field(name = "Examples:", value = response['list'][0]["example"])
    embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
    await ctx.send(embed = embed)

@bot.command(pass_context = True)
@commands.has_role('ROLE')
async def setgame(ctx, *, game: str):
	try:
		await bot.change_presence(activity=discord.Game(name=game), status=ctx.message.guild.me.status)
		logging.info("Set game to " + str(game))
		await ctx.channel.send("New game was succesfully set!")
	except Exception as e:
		print("Failed to set game: {}".format(str(e)) + "\n lol")


@bot.command(pass_context = True, aliases=['rg'])
@commands.has_role('ROLE')
async def resetgame(ctx):
	await bot.change_presence(activity=discord.Game(name='PornHub.com'), status=ctx.message.guild.me.status)
	await ctx.channel.send("The status was succesfully reseted!")

@bot.command(pass_context = True)
async def embed(ctx, *, desc: str):
	embed = discord.Embed(description = desc, color = embed_color)
	await ctx.send(embed = embed)


@bot.event
async def on_member_join(member):
  guild = member.guild
  await member.create_dm()
  await member.dm_channel.send(
    f'Hi {member.name}, welcome to {guild.name}!')

bot.run('',bot=False)
