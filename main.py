
import asyncio
import re
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

import keyboard

bot = Bot("")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

class WithdrawalForm(StatesGroup):
    choosing_method = State()
    choosing_bank = State()
    choosing_crypto = State()
    entering_card_number = State()
    entering_crypto_address = State()
    sending_screenshot = State()
    entering_ton_address = State()
    confirming = State()

@dp.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Hamster Combat - продажа монет", reply_markup=keyboard.main_kb)

@dp.message(F.text == "Продажа монет 🐹")
async def sell_tokens(message: Message, state: FSMContext):
    await state.set_state(WithdrawalForm.choosing_method)
    await message.answer("Выберите способ вывода:", reply_markup=keyboard.sell_tokens)

@dp.message(F.text == "Ссылки")
async def sell_tokens(message: Message, state: FSMContext):
    await message.answer("Ссылка на канал:", reply_markup=keyboard.links_kb)
    await message.answer("Ваша реферальная ссылка для приглашения пользователей:\n<code>t.me/+d7qOqzXQLDw3ZjRi</code>", parse_mode=ParseMode.HTML)


@dp.message(WithdrawalForm.choosing_method, F.text == "Вывод на карты банков РФ 💳")
async def bank_withdrawal(message: Message, state: FSMContext):
    await state.set_state(WithdrawalForm.choosing_bank)
    await message.answer("Выберите банк:", reply_markup=keyboard.sell_tokens_bank)

@dp.message(WithdrawalForm.choosing_method, F.text == "Вывод в крипте 💰")
async def crypto_withdrawal(message: Message, state: FSMContext):
    await state.set_state(WithdrawalForm.choosing_crypto)
    await message.answer("Выберите криптовалюту:", reply_markup=keyboard.sell_tokens_crypto)

@dp.message(WithdrawalForm.choosing_bank)
async def process_bank_selection(message: Message, state: FSMContext):
    if message.text in ["Альфа-Банк", "СберБанк", "Т-Банк", "Юникредит банк"]:
        await state.update_data(selected_bank=message.text)
        await state.set_state(WithdrawalForm.entering_card_number)
        await message.answer(f"<b>Вывод на карту {message.text}</b>\nДля вывода средств на карту укажите ее номер:", parse_mode=ParseMode.HTML)
    elif message.text == "НАЗАД ⤵️":
        await state.set_state(WithdrawalForm.choosing_method)
        await message.answer("Выберите способ вывода:", reply_markup=keyboard.sell_tokens)
    else:
        await message.answer("Пожалуйста, выберите банк из предложенных вариантов или нажмите НАЗАД.")

@dp.message(WithdrawalForm.choosing_crypto)
async def process_crypto_selection(message: Message, state: FSMContext):
    if message.text in ["USDT (TRC20)", "USDT (TON)", "USDT (BEP20)", "USDC (BEP20)", "USDC (AVAXC)", "TON (TON)", "Solana (SOL)", "ETH (Optimism)", "NEAR (NEAR)"]:
        await state.update_data(selected_crypto=message.text)
        await state.set_state(WithdrawalForm.entering_crypto_address)
        await message.answer(f"<b>Вывод в {message.text}</b>\nУкажите адрес вашего криптокошелька для вывода:", parse_mode=ParseMode.HTML)
    elif message.text == "НАЗАД ⤵️":
        await state.set_state(WithdrawalForm.choosing_method)
        await message.answer("Выберите способ вывода:", reply_markup=keyboard.sell_tokens)
    else:
        await message.answer("Пожалуйста, выберите криптовалюту из предложенных вариантов")

@dp.message(WithdrawalForm.entering_card_number)
async def process_card_number(message: Message, state: FSMContext):
    if message.text == "НАЗАД ⬅️":
        await state.set_state(WithdrawalForm.choosing_bank)
        await message.answer("Выберите банк:", reply_markup=keyboard.sell_tokens_bank)
    elif re.match(r'^\d{16}$', message.text):
        await state.update_data(card_number=message.text)
        await state.set_state(WithdrawalForm.sending_screenshot)
        await message.answer("Отправьте скриншот баланса для подтверждения наличия у вас токенов")
    else:
        await message.answer("Пожалуйста, введите корректный номер карты (16 цифр без пробелов и других символов)")

@dp.message(WithdrawalForm.entering_crypto_address)
async def process_crypto_address(message: Message, state: FSMContext):
    if message.text == "НАЗАД ⬅️":
        await state.set_state(WithdrawalForm.choosing_crypto)
        await message.answer("Выберите криптовалюту:", reply_markup=keyboard.sell_tokens_crypto)
    elif re.match(r'^[a-zA-Z0-9\-_]{28,}$', message.text):
        await state.update_data(crypto_address=message.text)
        await state.set_state(WithdrawalForm.sending_screenshot)
        await message.answer("Отправьте скриншот баланса для подтверждения наличия у вас токенов")
    else:
        await message.answer("Пожалуйста, введите корректный адрес криптокошелька")

@dp.message(WithdrawalForm.sending_screenshot)
async def process_screenshot(message: Message, state: FSMContext):
    if message.text == "НАЗАД ⬅️":
        user_data = await state.get_data()
        if 'card_number' in user_data:
            await state.set_state(WithdrawalForm.entering_card_number)
            await message.answer(f"<b>Вывод на карту {user_data['selected_bank']}</b>\nДля вывода средств на карту укажите ее номер:", parse_mode=ParseMode.HTML)
        elif 'crypto_address' in user_data:
            await state.set_state(WithdrawalForm.entering_crypto_address)
            await message.answer(f"<b>Вывод в {user_data['selected_crypto']}</b>\nУкажите адрес вашего криптокошелька для вывода:", parse_mode=ParseMode.HTML)
    elif message.photo:
        await state.set_state(WithdrawalForm.entering_ton_address)
        await message.answer("<b>Отправьте подключенный адрес кошелька TON:</b>\n как подключить ton кошелек к hamster kombat ГАЙД:\nhttps://teletype.in/@homyakcombocards/SSYNesbQRjy", parse_mode=ParseMode.HTML)
    else:
        await message.answer("Пожалуйста, отправьте скриншот баланса (изображение)")

@dp.message(WithdrawalForm.entering_ton_address)
async def process_ton_address(message: Message, state: FSMContext):
    if message.text == "НАЗАД ⬅️":
        await state.set_state(WithdrawalForm.sending_screenshot)
        await message.answer("Отправьте скриншот баланса для подтверждения наличия у вас токенов")
    elif re.match(r'^[a-zA-Z0-9\-_]{32,}$', message.text):
        await state.update_data(ton_address=message.text)
        await state.set_state(WithdrawalForm.confirming)
        await message.answer(
            "Адрес крипто биржи для вывода монет (наша комиссия за вывод 3.5%):\n"
            "<code>Доступно в день листинга токенов</code>\n"
            "вставьте этот адрес в приложении hamster kombat",
            parse_mode=ParseMode.HTML,
            reply_markup=keyboard.agree_kb
        )
    else:
        await message.answer("Пожалуйста, отправьте корректный адрес кошелька TON")

@dp.message(WithdrawalForm.confirming)
async def confirm_withdrawal(message: Message, state: FSMContext):
    if message.text == "НАЗАД ⬅️":
        await state.set_state(WithdrawalForm.entering_ton_address)
        await message.answer("<b>Отправьте подключенный адрес кошелька TON:</b>\n как подключить ton кошелек к hamster kombat ГАЙД:\nhttps://rbkgames.com/publications/articles/kak-podklyuchit-koshelek-v-hamster-kombat/", parse_mode=ParseMode.HTML)
    elif message.text == "Подтвердить вывод ✅":
        user_data = await state.get_data()
        await state.clear()
        if 'card_number' in user_data:
            await message.answer(f"Спасибо! Ваш запрос на вывод средств на карту {user_data['selected_bank']} (номер карты: {user_data['card_number']}) принят\nСредства поступят на ваш счет в течении 24 часов", reply_markup=keyboard.main_kb)
        elif 'crypto_address' in user_data:
            await message.answer(f"Спасибо! Ваш запрос на вывод средств в {user_data['selected_crypto']} (адрес: {user_data['crypto_address']}) принят\nСредства поступят на ваш счет в течении 24 часов", reply_markup=keyboard.main_kb)
    else:
        await message.answer("Пожалуйста, подтвердите вывод или нажмите НАЗАД.")

@dp.message(F.text.in_({"НАЗАД ↩️", "НАЗАД ⤵️", "НАЗАД ⬅️"}))
async def handle_back(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == WithdrawalForm.choosing_method:
        await state.clear()
        await message.answer("Главное меню", reply_markup=keyboard.main_kb)
    elif current_state in [WithdrawalForm.choosing_bank, WithdrawalForm.choosing_crypto]:
        await state.set_state(WithdrawalForm.choosing_method)
        await message.answer("Выберите способ вывода:", reply_markup=keyboard.sell_tokens)
    # Другие состояния обрабатываются в соответствующих хендлерах

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
