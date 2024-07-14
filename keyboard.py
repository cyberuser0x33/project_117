from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Продажа монет 🐹"),
            KeyboardButton(text="Ссылки")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Меню",
    selective=True
)


sell_tokens = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вывод на карты банков РФ 💳") 
        ],
        [
            KeyboardButton(text="Вывод в крипте 💰")
        ],
        [
            KeyboardButton(text="НАЗАД ↩️")
        ]

    ],
    resize_keyboard=True,
    selective=True
)

sell_tokens_bank = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Альфа-Банк"),
            KeyboardButton(text="СберБанк")
        ],
        [
            KeyboardButton(text="Т-Банк"),
            KeyboardButton(text="Юникредит банк")
        ],
        [
            KeyboardButton(text="НАЗАД ⤵️")
        ]
    ]
)

sell_tokens_crypto = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="USDT (TRC20)"),
            KeyboardButton(text="USDT (TON)"),
            KeyboardButton(text="USDT (BEP20)")
        ],
        [
            KeyboardButton(text="USDC (BEP20)"),
            KeyboardButton(text="USDC (AVAXC)"),
            KeyboardButton(text="TON (TON)")
        ],
        [
            KeyboardButton(text="Solana (SOL)"),
            KeyboardButton(text="ETH (Optimism)"),
            KeyboardButton(text="NEAR (NEAR)")
        ],
        [
            KeyboardButton(text="НАЗАД ⤵️")
        ]
    ]
)

agree_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
           KeyboardButton(text="Подтвердить вывод ✅") 
        ],
        [
            KeyboardButton(text="НАЗАД ⬅️")
        ]
    ]
)

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=sell_hamster_combat")
            
        ]   
    ]
)