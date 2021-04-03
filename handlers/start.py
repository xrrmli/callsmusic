from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Halo, {message.from_user.first_name}!</b>

Saya adalah bot Music yang dirancang khusus untuk menemani anda memutar musik dalam grup melalui obrolan suara.

Berikut dibawah ini adalah kontak owner bot dan cara menggunakannya.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Tutorial", url="https://telegra.ph/%F0%9D%95%B4%F0%9D%96%91%F0%9D%96%92%F0%9D%96%97-04-03-2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Grup", url="https://t.me/tongkrongannvirtual"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/painnhubbb"
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
