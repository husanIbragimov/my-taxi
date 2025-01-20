from aiogram import Bot, Dispatcher, types
from funcs import get_user_info, start_answer, help_answer
from aiogram.filters import Command
from asyncio import run

dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(663153232, "Bot started")


async def shutdown_answer(bot: Bot):
    await bot.send_message(663153232, "Bot stopped")


async def echo(message: types.Message, bot: Bot):
    print(message)
    print(dir(message))
    await message.copy_to(chat_id=message.chat.id)


async def start():
    dp.startup.register(startup_answer)

    dp.message.register(start_answer, Command("start"))
    dp.message.register(help_answer, Command("help"))
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7833141218:AAEl0rm6vcNkivxtmvoFP3WIazGSlYSY3Kg")
    await bot.set_my_commands(
        [
            types.BotCommand(
                command="start", description="Botni ishga tushirish"
            ),
            types.BotCommand(
                command="help", description="Yordam"
            ),
            types.BotCommand(
                command="info", description="Foydalanuvchi haqida ma'lumot"
            )
        ]
    )
    await dp.start_polling(bot, polling_timeout=1)


run(start())
