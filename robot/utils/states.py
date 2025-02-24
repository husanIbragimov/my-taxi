from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()


class UserGroup(StatesGroup):
    name = State()
    phone = State()
    is_user = State()
    birthdate = State()


class DriverGroup(UserGroup):
    car = State()
    car_color = State()
    car_photo = State()
    car_number = State()
    experience = State()
