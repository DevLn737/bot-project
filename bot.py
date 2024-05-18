import os
import platform
import config
import disnake
from disnake.ext import commands
from utils.logger import logger


class DiscordBot(commands.Bot):
    def __init__(self) -> None:
        intents = disnake.Intents.all()
        super().__init__(
            # test_guilds=[1039982973153464340],
            command_prefix=commands.when_mentioned_or(config.BOT_PREFIX),
            intents=intents,
            case_insensitive=True,
            help_command=None,
            allowed_mentions=disnake.AllowedMentions(
                everyone=False, users=True, roles=False
            ),
        )

    # Загружаем команды(в disnake нет поддержки ассинхронной загрузки)
    def load_cogs(self) -> None:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                try:
                    self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Расширение {filename} успешно загружено")
                except Exception as e:
                    print(f"Не удалось загрузить {filename} | {e}")

    # Запускается при первом запуске бота
    async def on_ready(self) -> None:
        logger.info(f"Запущен как {self.user.name}")
        logger.info(f"discord.py API версия: {disnake.__version__}")
        logger.info(f"Версия Python: {platform.python_version()}")
        logger.info(
            f"Запущено на: {platform.system()} {platform.release()} ({os.name})"
        )
        logger.info("-------------------")
        self.load_cogs()
        logger.info(f"Всего загружено {len(self.cogs)} команд")

    # Запускается при каждом успешном запуске команды
    async def on_message(self, message: disnake.Message):
        if message.author.bot or message.author.id == self.user.id:
            return

    # Запускается после успешного выполнения команды
    async def on_slash_command_completion(
        self, interaction: disnake.ApplicationCommandInteraction
    ):
        logger.info(f"{interaction.author} выполнил команду '{interaction.data.name}'")

    async def on_command_error(
        self,
        interaction: disnake.ApplicationCommandInteraction,
        error: commands.CommandError,
    ):
        logger.error(f"{interaction.author} выполнил команду '{interaction.data.name}'")
        logger.error(error)


bot = DiscordBot()
bot.run(config.SECRET_TOKEN)


# @bot.slash_command(description="Multiplies the number by 7")
# async def multiply(inter, number: int):
#     await inter.response.send_message(number * 7)
# Загрузка py файлов без использования директорий
# def load_cogs() -> None:
#     for filename in os.listdir("./cogs"):
#         if filename.endswith(".py"):
#             try:
#                 bot.load_extension(f"cogs.{filename[:-3]}")
#                 print(f"Расширение {filename} успешно загружено")
#             except Exception as e:
#                 print(f"Не удалось загрузить {filename} | {e}")

# Загрузка py файлов c использованием директорий
# def load_cogs() -> None:
#     for foldername in os.listdir("./cogs"):
#         if os.path.isdir(os.path.join("./cogs", foldername)):
#             for filename in os.listdir(os.path.join("./cogs", foldername)):
#                 if filename.endswith(".py"):
#                     try:
#                         bot.load_extension(f"cogs.{foldername}.{filename[:-3]}")
#                         print(f"Расширение {filename} успешно загружено")
#                     except Exception as e:
#                         print(f"Не удалось загрузить {filename} | {e}")
