# cogs/information.py
from discord.ext import commands
import discord
import datetime

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='userinfo', help='Muestra información sobre un usuario')
    async def userinfo(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        embed = discord.Embed(title=f'Información de {member.name}', color=discord.Color.blue())
        embed.add_field(name='ID', value=member.id, inline=False)
        embed.add_field(name='Nombre', value=member.display_name, inline=True)
        embed.add_field(name='Creado el', value=member.created_at.strftime('%d/%m/%Y'), inline=True)
        embed.add_field(name='Se unió el', value=member.joined_at.strftime('%d/%m/%Y'), inline=True)
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command(name='serverinfo', help='Muestra información sobre el servidor')
    async def serverinfo(self, ctx):
        server = ctx.guild
        embed = discord.Embed(title=f'Información de {server.name}', color=discord.Color.green())
        embed.add_field(name='Miembros', value=server.member_count, inline=True)
        embed.add_field(name='Canales', value=len(server.channels), inline=True)
        embed.add_field(name='Creado el', value=server.created_at.strftime('%d/%m/%Y'), inline=True)
        embed.set_thumbnail(url=server.icon.url)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Information(bot))