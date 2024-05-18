import disnake
from disnake.ext import commands


class FunCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.slash_command(
        name="ping", description="Пинг! Возвращает задержку бота до хоста"
    )
    async def ping(self, inter: disnake.ApplicationCommandInteraction) -> None:
        """Get the bot's current websocket latency."""
        embed = disnake.Embed(
            title="🏓 Pong!",
            description=f"Задержка до бота {round(self.bot.latency * 1000)}мс",
            color=0xBEBEFE,
        )

        # Ждём завершения выполнения команды, предотвращаем TIMEOUT ошибку
        await inter.response.defer()
        await inter.edit_original_response(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(FunCommands(bot))
