import discord
from discord.ext import commands
from discord import app_commands


class Poll(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    async def poll(
        self,
        interaction: discord.Interaction,
        question: str,
        option1: str,
        option2: str,
        option3: str = None,
        option4: str = None,
        option5: str = None,
        role: discord.Role = None,
    ):
        """Creates a Poll.

        Args:
            question (str): Add question for your poll.
            option1 (str): Create 1st option for your poll.
            option1 (str): Create 1st option for your poll.
            option2 (str): Create 2nd option for your poll.
            option3 (str): Create 3rd option for your poll.
            option4 (str): Create 4th option for your poll.
            option5 (str): Create 5th option for your poll.
            option6 (str): Create 6th option for your poll.
            option7 (str): Create 7th option for your poll.
            option8 (str): Create 8th option for your poll.
            option9 (str): Create 9th option for your poll.
            option10 (str): Create 10th option of your poll.
            role: Select a Role to mention for this Poll."""
        await interaction.response.defer(thinking=True)
        try:
            options = [option1, option2, option3, option4, option5]
            embed_options = []
            for o in options:
                if o != None:
                    embed_options.append(o)
            if role == None:
                if len(embed_options) == 2:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}",
                    )
                    msg = await interaction.followup.send(embed=embed)
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                elif len(embed_options) == 3:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}",
                    )
                    msg = await interaction.followup.send(embed=embed)
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                elif len(embed_options) == 4:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}\n4⃣ {embed_options[3]}",
                    )
                    msg = await interaction.followup.send(embed=embed)
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                    await msg.add_reaction("4⃣")
                elif len(embed_options) == 5:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}\n4⃣ {embed_options[3]}\n5⃣ {embed_options[4]}",
                    )
                    msg = await interaction.followup.send(embed=embed)
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                    await msg.add_reaction("4⃣")
                    await msg.add_reaction("5⃣")
            else:
                if len(embed_options) == 2:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}",
                    )
                    msg = await interaction.followup.send(
                        f"{role.mention}", embed=embed
                    )
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                elif len(embed_options) == 3:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}",
                    )
                    msg = await interaction.followup.send(
                        f"{role.mention}", embed=embed
                    )
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                elif len(embed_options) == 4:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}\n4⃣ {embed_options[3]}",
                    )
                    msg = await interaction.followup.send(
                        f"{role.mention}", embed=embed
                    )
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                    await msg.add_reaction("4⃣")
                elif len(embed_options) == 5:
                    embed = discord.Embed(
                        color=discord.Colour.random(),
                        title=f"{question}",
                        description=f"1⃣ {embed_options[0]}\n2⃣ {embed_options[1]}\n3⃣ {embed_options[2]}\n4⃣ {embed_options[3]}\n5⃣ {embed_options[4]}",
                    )
                    msg = await interaction.followup.send(
                        f"{role.mention}", embed=embed
                    )
                    await msg.add_reaction("1⃣")
                    await msg.add_reaction("2⃣")
                    await msg.add_reaction("3⃣")
                    await msg.add_reaction("4⃣")
                    await msg.add_reaction("5⃣")
            # await interaction.delete_original_response()
        except Exception as e:
            print(e)
            # await interaction.delete_original_response()
            await interaction.followup.send(
                "An error occured, try again later.", ephemeral=True
            )


async def setup(bot: commands.Bot):
    await bot.add_cog(Poll(bot))