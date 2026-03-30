import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.filters import Command

TOKEN = "8291260233:AAGuU7qhz5QXDQvOXPUTQZavvNowd7_5zWU"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🚗 Testni boshlash",
            web_app=WebAppInfo(url="https://avtotest-911.vercel.app/")
        )]
    ])
    await message.answer("Avtotestni boshlash uchun tugmani bosing 👇", reply_markup=keyboard)

@dp.message()
async def get_data(message: types.Message):
    if message.web_app_data:
        data = message.web_app_data.data
        await message.answer(f"Natijangiz: {data}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())