import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import pytz


class Utility(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Say commands
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def say(self, interaction: discord.Interaction, message: str):
        """Says Anything

        Args:
          message (str): Enter the text which you want to say"""
        await interaction.response.defer(thinking=True)
        await interaction.channel.send(message)
        await interaction.delete_original_response()

    @say.error
    async def say_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # Embed Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def embed(
        self,
        interaction: discord.Interaction,
        message: str,
        title: str = None,
        thumbnail: str = None,
        image: str = None,
    ):
        """Embeds your Text

        Args:
          message (str): Enter the text which you want to embed
          title (str): Enter the title for your embed
          thumbnail: Link of your thmbanail image"""
        embedvar = discord.Embed(
            title=title, description=message, color=discord.Colour.random()
        )
        if image is not None:
            embedvar.set_image(url=image)
        if thumbnail is not None:
            embedvar.set_thumbnail(url=thumbnail)
        await interaction.response.send_message(embed=embedvar)

    @embed.error
    async def embed_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # Avatar Command
    @app_commands.command()
    async def avatar(
        self, interaction: discord.Interaction, member: discord.Member = None
    ):
        """Gives the member's avatar

        Args:
          member: Choose the member to see his/her avatar"""
        author = interaction.user
        member = author if not member else member
        embed = discord.Embed(
            title="Here is " + member.name + "'s Avatar", color=discord.Colour.random()
        )
        embed.set_image(url=member.avatar.url)
        await interaction.response.send_message(embed=embed)

    # DM Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def dm(
        self, interaction: discord.Interaction, member: discord.Member, message: str
    ):
        """DM any Member

        Args:
          member: Choose member whom you want to DM
          message (str): Enter message to send in member's DM"""
        await member.send(message)
        embed = discord.Embed(
            title=f"DM Sent to {member}",
            description=f"Sent {message} to {member}",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    @dm.error
    async def dm_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # lock command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.bot_has_permissions(manage_channels=True)
    async def lock(self, interaction: discord.Interaction):
        """Locks the channel for @everyone Role"""
        await interaction.channel.set_permissions(
            interaction.guild.default_role, send_messages=False
        )
        embed = discord.Embed(
            description=f"{interaction.channel.mention} has been locked.",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    @lock.error
    async def lock_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # unlock command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_channels=True)
    @app_commands.checks.bot_has_permissions(manage_channels=True)
    async def unlock(self, interaction: discord.Interaction):
        """Unlocks the channel for @everyone Role"""
        await interaction.channel.set_permissions(
            interaction.guild.default_role, send_messages=True
        )
        embed = discord.Embed(
            description=f"{interaction.channel.mention} has been unlocked.",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    @unlock.error
    async def unlock_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # AFK command
    @app_commands.command()
    async def afk(self, interaction: discord.Interaction, reason: str = None):
        """Sets your AFK status

        Args:
          reason (str): Give reason for your AFK"""

        with open("./afkdata.json", "r") as f:
            records = json.load(f)

        records[str(interaction.user.id)] = reason
        with open("./afkdata.json", "w") as f:
            json.dump(records, f)

        embed = discord.Embed(
            title="Success!",
            description=f"{interaction.user.mention}, your AFK has been set. Reason: {reason}",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    # Check if user is AFK
    @commands.Cog.listener()
    async def on_message(self, message):
        with open("./afkdata.json", "r") as f:
            records = json.load(f)
            if not message.author.bot:
                # Check if user is AFK and handle mentions
                if str(message.author.id) in records:
                    reason = records[str(message.author.id)]
                    embed = discord.Embed(
                        title="Success!",
                        description=f"Welome back {message.author.mention}, your AFK has been removed!",
                        color=discord.Colour.random(),
                    )
                    await message.reply(embed=embed, delete_after=10)
                    # Remove user's AFK status when they send a message
                    del records[str(message.author.id)]
                    with open("./afkdata.json", "w") as f:
                        json.dump(records, f)
                elif message.mentions:
                    for user in message.mentions:
                        if str(user.id) in records:
                            reason = records[str(user.id)]
                            embed = discord.Embed(
                                title="Success!",
                                description=f"{user.mention} is currently AFK. Reason: {reason}",
                                color=discord.Colour.random(),
                            )
                            await message.reply(embed=embed, delete_after=10)

                # Check if message is a reply to an AFK user
                elif (
                    message.reference
                    and message.reference.message_id in records.values()
                ):
                    for user_id, reason in records.items():
                        if message.reference.message_id == reason:
                            user = message.guild.get_member(int(user_id))
                            if user:
                                embed = discord.Embed(
                                    title="Success!",
                                    description=f"{user.mention} is currently AFK. Reason: {reason}",
                                    color=discord.Color.random(),
                                )
                                await message.reply(embed=embed, delete_after=10)

    # Default Role

    @app_commands.command()
    @app_commands.checks.has_permissions(manage_roles=True)
    @app_commands.checks.bot_has_permissions(manage_roles=True)
    async def autorole(self, interaction: discord.Interaction, role: discord.Role):
        """Sets a role which will autoassign to new members.

        Args:
          role: Select a role to autoassign to new members."""
        data = {}
        data["guild_id"] = str(interaction.guild.id)
        data["default_role_id"] = str(role.id)
        with open("default_role.json", "w") as f:
            json.dump(data, f)
        embed = discord.Embed(
            description=f"{role.mention} is successfully set as your AutoRole.",
            color=0x03FC52,
        )
        await interaction.response.send_message(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        with open("default_role.json", "r") as f:
            data = json.load(f)
        if str(member.guild.id) == data["guild_id"]:
            role = discord.utils.get(
                member.guild.roles, id=int(data["default_role_id"])
            )
            await member.add_roles(role)

    @autorole.error
    async def autorole_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command.",
                ephemeral=True,
            )

    # userinfo command
    @app_commands.command()
    async def userinfo(
        self, interaction: discord.Interaction, member: discord.Member = None
    ):
        """Shows some information about the user.

        Args:
          role: Select the user which you'd like to view information."""
        if not member:
            member = interaction.user
        roles = [role for role in member.roles if role != member.guild.default_role]
        embed = discord.Embed(title=f"{member.name}'s Info", colour=member.colour)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="ID:", value=member.id, inline=False)
        embed.add_field(name="Display Name:", value=member.display_name, inline=False)
        created_at = member.created_at.astimezone(pytz.timezone("Asia/Kolkata"))
        embed.add_field(
            name="Joined Discord:",
            value=created_at.strftime("%a, %#d %B %Y, %I:%M %p IST"),
            inline=False,
        )
        joined_at = member.joined_at.astimezone(pytz.timezone("Asia/Kolkata"))
        embed.add_field(
            name="Joined Server:",
            value=joined_at.strftime("%a, %#d %B %Y, %I:%M %p IST"),
            inline=False,
        )
        embed.add_field(
            name=f"Roles ({len(roles)})",
            value=" ".join([role.mention for role in roles]),
            inline=False,
        )
        embed.set_footer(
            text=f"Requested by {interaction.user}",
            icon_url=interaction.user.avatar.url,
        )
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Utility(bot))