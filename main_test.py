import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode



import keyboard

bot = Bot("7449823563:AAF7uOmhDNrLdoJl5jM7EgljedrdqZGHt0U") #, parse_mode="HTML"

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Hamster Combat - продажа монет", reply_markup=keyboard.main_kb)


@dp.message()
async def echo(message: Message):
    msg = message.text

    if msg == "Продажа монет 🐹":
        await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens)

    elif msg == "Ссылки":
        await message.answer("Ссылка на канал:", reply_markup=keyboard.links_kb)
        await message.answer("Ваша реферальная ссылка для приглашения пользователей:\n<code>t.me/+d7qOqzXQLDw3ZjRi</code>", parse_mode=ParseMode.HTML)

    elif msg == "Вывод на карты банков РФ 💳":
        await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens_bank)
        
    elif msg == "Вывод в крипте 💰":
        await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens_crypto)

    elif msg == "НАЗАД ↩️":
        await message.answer("Назад", reply_markup=keyboard.main_kb)
    elif msg == "НАЗАД ⤵️":
        await message.answer("Назад", reply_markup=keyboard.sell_tokens)
    elif "Альфа-Банк" or "СберБанк" or "Т-Банк" or "Юникредит банк" or "USDT (TRC20)" or "USDT (TON)" or "USDT (BEP20)" or "USDC (BEP20)" or "USDC (AVAXC)" or "TON (TON)" or "Solana (SOL)" or "ETH (Optimism)" or "NEAR (NEAR)":
        await message.answer("Пока не доступно для вывода средств\nP.S. Доступ будет открыт в день листинга токенов", parse_mode=ParseMode.HTML)



'''
    match msg:
        case "Продажа монет 🐹":
            await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens)
        case "Ссылки":
            await message.answer("Ссылка на канал:", reply_markup=keyboard.links_kb)
            await message.answer("Ваша реферальная ссылка для приглашения пользователей:\n<code>t.me/+d7qOqzXQLDw3ZjRi</code>", parse_mode=ParseMode.HTML)

        case "Вывод на карты банков РФ 💳":
            await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens_bank)
        case "Вывод в крипте 💰":
            await message.answer("Продажа монет 🐹", reply_markup=keyboard.sell_tokens_crypto)
        case "НАЗАД ↩️":
            await message.answer("Назад", reply_markup=keyboard.main_kb)
        case "НАЗАД ⤵️":
            await message.answer("Назад", reply_markup=keyboard.sell_tokens)
        elif "Альфа-Банк" or "СберБанк" or "Т-Банк" or "Юникредит банк" or "USDT (TRC20)" or "USDT (TON)" or "USDT (BEP20)" or "USDC (BEP20)" or "USDC (AVAXC)" or "TON (TON)" or "Solana (SOL)" or "ETH (Optimism)" or "NEAR (NEAR)":
            await message.answer("Пока не доступно для вывода средств\nP.S. Доступ будет открыт в день листинга токенов", parse_mode=ParseMode.HTML)
'''

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())