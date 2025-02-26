from aiogram import Bot
from aiogram.types import Message


async def get_user_info(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photo = await message.from_user.get_profile_photos()

    text = (
        f"{message.from_user.mention_html('USER')} INFO:\n\n"
        f"Ism-familiya: {message.from_user.full_name}\n"
        f"ID: {message.from_user.id}\n"
        f"Username: @{user.username}\n"
    )
    if user.bio: text += f"Bio: <i>{user.bio}</i>\n"
    if user.username: text += f"Username: @{user.username}\n"
    if user_photo.photos:
        await message.answer_photo(photo=user_photo.photos[0][-1].file_id, caption=text, parse_mode="HTML")
    else:
        await message.answer(text, parse_mode="HTML")


async def start_answer(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Salom, {message.from_user.mention_html(f'{message.from_user.full_name}')}!\n", parse_mode="HTML")


async def help_answer(message: Message, bot: Bot):
    text = f"""
    <b>Yordam</b>
    /start - Botni ishga tushirish
    /help - Yordam
    /info - Foydalanuvchi haqida ma'lumot
    """
    await bot.send_message(message.from_user.id, text, parse_mode="HTML")


