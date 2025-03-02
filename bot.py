import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

exts = ("cogs.mod", "cogs.utility", "cogs.poll")


class MyBot(commands.Bot):

    def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)

    async def setup_hook(self) -> None:

        for ext in exts:
            await self.load_extension(ext)

        print("Loaded all Cogs.")

        await self.tree.sync()

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, name="Your Server"
            )
        )
        print("Bot is Online")


if __name__ == "__main__":
    intents = discord.Intents.all()
    bot = MyBot(command_prefix=">", intents=intents)
    load_dotenv()
    bot.run(os.getenv("TOKEN"))