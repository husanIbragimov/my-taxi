from aiogram import Router, F
from aiogram.types import Message, Contact
from filters import IsPrivateChat
from aiogram.filters import Command, StateFilter
from keyboards import builders, reply
from aiogram.fsm.context import FSMContext
from utils.states import UserGroup, DriverGroup


router = Router()
router.message.filter(IsPrivateChat())


@router.message(Command('register'))
async def register(message: Message, state: FSMContext):
    await state.set_state(DriverGroup.is_driver)
    print("register")
    await message.answer("Kim sifatida ro'yxatdan o'tmoqchisiz?", reply_markup=reply.is_driver)


@router.message(StateFilter(DriverGroup.is_driver))
async def is_driver(message: Message, state: FSMContext):
    text = message.text
    print(text)
    if text == "Haydovchi":
        await state.update_data(is_driver=True)
        await state.set_state(DriverGroup.first_name)
        await message.answer("Telefon raqamingizni kiriting")
    else:
        await state.update_data(is_driver=False)
        await state.set_state(UserGroup.first_name)
        await message.answer("Telefon raqamingizni kiriting")


@router.message(StateFilter(DriverGroup.first_name))
async def user_full_name(message: Message, state: FSMContext):
    name_lst = message.text.split()
    if len(name_lst) != 2:
        await message.answer("Bu yerga faqat ismingiz va familiyangizni kiriting.")
        return
    first_name, last_name = name_lst
    await state.update_data(first_name=first_name, last_name=last_name)
    await state.set_state(DriverGroup.phone_number)
    await message.answer("Telefon raqamingizni kiriting", reply_markup=builders.contact_keyboard())

@router.message(StateFilter(DriverGroup.phone_number))
async def user_phone_number(message: Contact, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    await state.set_state(DriverGroup.gender)
    await message.answer("Jinsingizni tanlang", reply_markup=reply.gender_btn)

@router.message(StateFilter(DriverGroup.gender))
async def user_gender(message: Message, state: FSMContext):
    gender = message.text
    if gender == "Erkak":
        await state.update_data(gender='male')
    else:
        await state.update_data(gender='female')
