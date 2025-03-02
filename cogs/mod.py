import discord
from discord.ext import commands
from discord import app_commands
from bot import MyBot


class Mod(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    # Clear Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def clear(self, interaction: discord.Interaction, amount: int):
        """Deletes any given amount of messages

        Args:
          amount (int): Enter the amount of messages which you want to delete"""
        embed = discord.Embed(
            description=f"Successfully Deleted {amount} messages",
            color=discord.Colour.random(),
        )
        await interaction.response.defer(thinking=True)

        await interaction.channel.purge(limit=amount + 1)
        await interaction.channel.send(embed=embed, delete_after=3)

    @clear.error
    async def clear_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        embed = discord.Embed(
            description="You don't have required permissions to use this command.",
            color=0xFF2B2B,
        )
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(embed=embed, delete_after=5)
        elif isinstance(error, app_commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

    # Warn Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_messages=True)
    @app_commands.checks.bot_has_permissions(manage_messages=True)
    async def warn(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = None,
    ):
        """Warns any Member

        Args:
          member: Choose member whom you want to warn
          reason (str): Enter Warning reason"""
        embed = discord.Embed(
            title=f"Warned {member}",
            description=f"{member} has been warned for {reason}",
            color=0xFC0313,
        )
        await interaction.response.send_message(embed=embed)

    @warn.error
    async def warn_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

    # Kick Command
    @app_commands.command()
    @app_commands.checks.has_permissions(kick_members=True)
    @app_commands.checks.bot_has_permissions(kick_members=True)
    async def kick(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = None,
    ):
        """Kicks any Member

        Args:
          member: Choose member whom you want to kick
          reason (str): Enter kicking reason"""
        await member.kick(reason=reason)
        embed = discord.Embed(
            title=f"Kicked {member}",
            description=f"{member} has been kicked for {reason}",
            color=0xFC0313,
        )
        await interaction.response.send_message(embed=embed)

    @kick.error
    async def kick_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

    # Ban Command
    @app_commands.command()
    @app_commands.checks.has_permissions(ban_members=True)
    @app_commands.checks.bot_has_permissions(ban_members=True)
    async def ban(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        reason: str = None,
    ):
        """Bans any Member

        Args:
          member: Choose member whom you want to ban
          reason (str): Enter banning reason"""
        await member.ban(reason=reason)
        embed = discord.Embed(
            title=f"Banned {member}",
            description=f"{member} has been     banned for {reason}",
            color=0xFC0313,
        )
        await interaction.response.send_message(embed=embed)

    @ban.error
    async def ban_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

    # addrole Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_roles=True)
    @app_commands.checks.bot_has_permissions(manage_roles=True)
    async def addrole(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        role: discord.Role,
    ):
        """Adds role to a Member

        Args:
          member: Choose a member whom you want to add the role
          role: Choose the role to add"""
        await member.add_roles(role)
        embed = discord.Embed(
            description=f"Successfully added {role.mention} role to {member.mention}.",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    @addrole.error
    async def addrole_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

    # removerole Command
    @app_commands.command()
    @app_commands.checks.has_permissions(manage_roles=True)
    @app_commands.checks.bot_has_permissions(manage_roles=True)
    async def removerole(
        self,
        interaction: discord.Interaction,
        member: discord.Member,
        role: discord.Role,
    ):
        """Removes role to a Member

        Args:
          member: Choose a member whom you want to add the role
          role: Choose the role to remove"""
        await member.remove_roles(role)
        embed = discord.Embed(
            description=f"Successfully removed {role.mention} role to {member.mention}.",
            color=discord.Colour.random(),
        )
        await interaction.response.send_message(embed=embed)

    @removerole.error
    async def removerole_error(
        self, interaction: discord.Interaction, error: commands.CommandError
    ):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message(
                "You don't have required permissions to use this command.",
                ephemeral=True,
            )
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message(
                "I don't have required permissions to perform this command",
                ephemeral=True,
            )

async def setup(bot: commands.Bot):
    await bot.add_cog(Mod(bot))