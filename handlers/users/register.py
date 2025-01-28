from aiogram import Router, F
from aiogram.types import Message
from filters import IsPrivateChat
from aiogram.filters import Command
from keyboards import builders, reply
from aiogram.fsm.context import FSMContext
from utils.states import UserGroup, DriverGroup


router = Router()
router.message.filter(IsPrivateChat())


# @router.message(Command('profile'))
