
import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

@app.on_message(
    command(["سورس مين","سورس","السورس","سورسي", "shark"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cde2b51203fbdab57fac5.jpg",
        caption=f"""╭═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊 ⌝](https://t.me/L_H_V)⧽⌯⊶★═╮\n★‹ [⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊 ⌝𝐀](https://t.me/L_H_V)\n★‹ [𝐎𝐌𝐀𝐑](https://t.me/T_3_A)\n★‹ [𝐻𝐴𝑆𝑆𝐴𝑁](https://t.me/QF_QG)\n★‹ \n╰═★⊷⌯⧼[⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊 ⌝](https://t.me/L_H_V)⧽⌯⊶★═╯\n ⍟ Welcome to source shark""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐌𝐀𝐑༄►", url=f"https://t.me/T_3_A"), 
                ],[
                    InlineKeyboardButton(
                        "⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊 ⌝⚡️", url=f"https://t.me/L_H_V"),
                ],[
                    InlineKeyboardButton(
                        "𝐀𝐃𝐃 𝐌𝐄💞", url=f"https://t.me/SuPeRaDs1bot?startgroup=true"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )



