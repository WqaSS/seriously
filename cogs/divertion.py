from discord.ext import commands
import discord

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hola", help="El bot te dice hola")
    async def hola(self, ctx):
        await ctx.send("Hola!")

    @commands.command(name='ping', description="Te da las diferentes latencias.")
    async def ping(self, ctx):
        embed = discord.Embed(title=f'Latencia del bot', color=discord.Color.random())
        embed.add_field(name=":ping_pong:", value=f"{round(self.bot.latency * 1000)} ms")
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))