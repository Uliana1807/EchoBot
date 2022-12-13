import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5736760041:AAE6Tlc9d2PnvCUewowcLncyUVj16Oj14Fc'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Привет!\nЯ эхо-юот!")


@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)