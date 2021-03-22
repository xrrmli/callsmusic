from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo, {message.from_user.first_name}!</b>
Saya adalah bot music voice call group!
Dirancang khusus untuk menemanimu di obrolan suara.
Berikut dibawah ini adalah kontak owner bot.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ OWNER BOT", url="https://t.me/boiii999"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "INSTAGRAM", url="https://www.instagram.com/aipmarvelous/"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "CARA MEMAKAINYA", url="https://telegra.ph/Cara-Menggunakan-BoI-Music-Bot-boimusic-bot-03-09"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "Hai, apakah anda ingin memainkan sebuah lagu?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "Tidak ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
