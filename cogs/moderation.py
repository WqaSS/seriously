# cogs/moderation.py
from this import d
from discord.ext import commands
import discord

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ban', help='Banea a un usuario del servidor')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.name} ha sido baneado. Razón: {reason or "No especificada"}')

    @commands.command(name='kick', help='Expulsa a un usuario del servidor')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} ha sido expulsado. Razón: {reason or "No especificada"}')

    @commands.command(name="cls")
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: str = None):
        """
        Purge command to delete messages in a channel.
        Usage: !cls <amount> or !cls all
        """
        # Check if no attribute is provided
        if amount is None:
            await ctx.send("Error: Please provide a number of messages to delete or use 'all'.")
            return

        # Check if the amount is 'all'
        if amount.lower() == "all":
            try:
                await ctx.channel.purge()
                await ctx.send("All messages have been deleted.", delete_after=5)
                return
            except discord.Forbidden:
                await ctx.send("Error: The bot lacks permission to delete messages.")
                return

        # Check if the input is a valid integer
        try:
            amount = int(amount)
        except ValueError:
            await ctx.send("Error: Invalid attribute. Please provide a valid number or 'all'.")
            return

        # Check if the amount is less than 0
        if amount <= 0:
            await ctx.send("Error: The number of messages to delete cannot be negative.")
            return

        # Perform the purge
        try:
            await ctx.channel.purge(limit=amount + 1)  # +1 to include the command message
            await ctx.send(f"Deleted {amount} message(s).", delete_after=5)
        except discord.Forbidden:
            await ctx.send("Error: The bot lacks permission to delete messages.")
        except discord.HTTPException:
            await ctx.send("Error: Failed to delete messages due to an API error.")

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Error: You lack the 'Manage Messages' permission to use this command.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Error: The bot lacks the 'Manage Messages' permission.")

async def setup(bot):
    await bot.add_cog(Moderation(bot))