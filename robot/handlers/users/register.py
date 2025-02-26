from aiogram import Router, F
from aiogram.types import Message
from filters import IsPrivateChat
from aiogram.filters import Command
from keyboards import builders, reply
from aiogram.fsm.context import FSMContext
from utils.states import UserGroup, DriverGroup


router = Router()
router.message.filter(IsPrivateChat())


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(UserGroup.name)
    await message.answer('Ismingizni kiriting: ', reply_markup=builders.profile(message.from_user.full_name))