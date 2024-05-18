import disnake
from disnake.ext import commands
from g4f.client import AsyncClient
from g4f.Provider import ReplicateImage, DuckDuckGo

client = AsyncClient(
    provider=DuckDuckGo,
    image_provider=ReplicateImage,
)


class ChatCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="chat", description="Общение с ai чат ботом")
    async def chat(
        self,
        inter: disnake.ApplicationCommandInteraction,
        message: str = commands.Param(description="Текст запроса для общения"),
    ):
        if not message:
            return await inter.response.send_message(
                content="Пожалуйста, введите сообщение для диалога", ephemeral=True
            )

        # Ждём завершения выполнения команды, предотвращаем TIMEOUT ошибку
        await inter.response.defer()
        response = await client.chat.completions.create(
            model="",
            messages=[{"role": "user", "content": f"{message}"}],
        )
        content = response.choices[0].message.content
        await inter.edit_original_response(content=content)

    @commands.slash_command(
        name="draw", description="Попросить ai нарисовать изображение по запросу"
    )
    async def draw(
        self,
        inter: disnake.ApplicationCommandInteraction,
        prompt: str = commands.Param(
            description="Текст того, что необходимо нарисовать"
        ),
    ):
        if not prompt:
            return await inter.response.send_message(
                content="Пожалуйста, выведите, что вы хотите нарисовать", ephemeral=True
            )

        # Ждём завершения выполнения команды, предотвращаем TIMEOUT ошибку
        await inter.response.defer(with_message="Изображает что-то прекрасное 🎨...")
        response = await client.images.generate(
            model="",
            prompt=prompt,
        )
        url = response.data[0].url
        await inter.edit_original_response(content=url)


def setup(bot: commands.Bot):
    bot.add_cog(ChatCommands(bot))
