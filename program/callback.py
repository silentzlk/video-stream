# Copyright (C) 2021 By VeezMusicProject

from driver.queues import QUEUE
from pyrogram import Client, filters
from program.utils.inline import menu_markup
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f"""Hello ð \n\nI'm Video Stream Bot \n\nTest me @binarysongslk \n\nPowered by @binary_lk""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Add me to your Group â",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("HELP", callback_data="hcbowtouse")],
                [
                    InlineKeyboardButton("Commands", callback_data="cbcmds"),
                ],
                [
                    InlineKeyboardButton(
                        "Official Group", url=f"https://t.me/Binary_bots_Support"
                    ),
                    InlineKeyboardButton(
                        "Official Channel", url=f"https://t.me/binary_lk"
                    ),
                ],
               
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""Read the  below ! ð

 ðð»I'm stream Films on @binarysongslk 
 ðð»I can download youtube videos mp4 & mp3 too.ð»
 ðð»Add me to u'r grp and promote to admin and type /userbotjoin


`- END, EVERYTHING HAS BEEN SETUP -`
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""Hello ð [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !

Â» **press the button below to read the available commands !ð **

__Powered by @binary_lk""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("All Commands Here", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("ð Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f"""Here is the basic commands:

Â» /play (song name/link) - play music on video chat
Â» /vplay (video name/link) - play video on video chat
Â» /vstream - play live video from yt live/m3u8
Â» /playlist - show you the playlist
Â» /video (query) - download video from youtube
Â» /song (query) - download song from youtube
Â» /lyric (query) - scrap the song lyric
Â» /search (query) - search a youtube video link

Â» /ping - show the bot ping status
Â» /speedtest - run the bot server speedtest
Â» /uptime - show the bot uptime status
Â» /alive - show the bot alive info (in group)

Here is the admin commands:

Â» /pause - pause the stream
Â» /resume - resume the stream
Â» /skip - switch to next stream
Â» /stop - stop the streaming
Â» /vmute - mute the userbot on voice chat
Â» /vunmute - unmute the userbot on voice chat
Â» /volume `1-200` - adjust the volume of music (userbot must be admin)
Â» /reload - reload bot and refresh the admin data
Â» /userbotjoin - invite the userbot to join group
Â» /userbotleave - order userbot to leave from group

Here is the sudo commands:

Â» /rmw - clean all raw files
Â» /rmd - clean all downloaded files
Â» /sysinfo - show the system information
Â» /update - update your bot to latest version
Â» /restart - restart your bot
Â» /leaveall - order userbot to leave from all group


__Powered by @binary_lk""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    user_id = query.message.from_user.id
    buttons = menu_markup(user_id)
    chat = query.message.chat.title
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"âï¸ **Settings of** {chat}\n\nâ¸ : pause stream\nâ¶ï¸ : resume stream\nð : mute userbot\nð : unmute userbot\nâ¹ : stop stream",
              reply_markup=InlineKeyboardMarkup(buttons),
          )
    else:
        await query.answer("â nothing is currently streaming", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button !", show_alert=True)
    await query.message.delete()
