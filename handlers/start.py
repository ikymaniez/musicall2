# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""<b>Haii.. ππ» {message.from_user.first_name} Welcome To πVirtual Musicπ\n
πππ ππππππ πππ πππππ ππππππππ π πππ ππ ππππππππππ ππππ : [King](https://t.me/boyfriendnice)
πππππππ πππππ πππππππππππ πππ ππππππ πππ πππ πππππππππ ππ π ππππ πππππππ πππππ πππππππ π ππππ ππππ ππππππππ ππππππ ππππππ, ππππ πππ πππππππ ππππ ππππ πππππππ π.
βββββββββββββββ
β£ > πΌππππππ πππππ ππππππ ππππ.
β£ > π±πππ ππππ ππππ, πππππ ππππππ πππππππππ πππππ πππππ.
β£ > πΌππππππ πππ πππππππ ππππ πππππππ πππππ-πππππππ.
β£ > πΌππππππ ππππ ππππ πππ πππ πππππ ππππ ππππ πππππππ πππ.
βββββββββββββββ
π€΅ππ»π?πͺπ½π?π­ π«π : [King](https://t.me/boyfriendnice)
βοΈπ£π±πͺπ·π΄πΌ π―πΈπ» : [Grup Support](https://t.me/remaja_virtual62)
ββββββββββββββ
πππ πππππ : @Virtualsongbot - πππππππππ πππππ : @AsisstantMusicVirtual
 
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π€΅Owner Music", url="https://t.me/afterdaytoxic")
                  ],[
                    InlineKeyboardButton(
                        "π₯Official Group", url="https://t.me/captionanakmuda"
                    ),
                    InlineKeyboardButton(
                        "π’Official Channel", url="https://t.me/humangabutguys") 
                  ],[
                    InlineKeyboardButton(
                        "πInstagram", url="https://www.instagram.com/ikyyy_35"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aku sudah online, ayo kita joget ceria! πΆ**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π€΅Owner Music", url="https://t.me/afterdaytoxic"
                    )
                ],[
                    InlineKeyboardButton(
                        "β Yes!", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "β No!", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Klik tombol dibawah untuk melihat panduan menggunakan bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π¦ Cara Memakai Bot Music!", url="https://t.me/humangabutguys/91577"
                    )
                ]
            ]
        ),
    )
