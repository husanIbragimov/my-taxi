from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()
    sex = State()
    about = State()
    photo = State()


class UserGroup(StatesGroup):
    first_name = State()
    last_name = State()
    phone_number = State()
    gender = State()
    photo = State()
    is_driver = State()


class DriverGroup(UserGroup):
    experience = State()
    license_number = State()
    license_expiry_date = State()
    license_image = State()
    make = State()
    model = State()
    car_color = State()
    car_year = State()
    car_photo = State()


class OrderGroup(StatesGroup):
    content = State()
    price = State()
    when = State()
    where = State()
    location = State()
