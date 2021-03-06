import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.utils import friday_on_cmd


@friday.on(friday_on_cmd(pattern="spd ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@SpotifyMusicDownloaderBot"
    await event.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await event.edit("`Downloading music taking some times,  Stay Tuned...`")
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=752979930)
            )
            await bot.send_message(chat, link)
            respond = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock bot and try again```")
            return
        await event.delete()
        await bot.forward_messages(event.chat_id, respond.message)


@friday.on(friday_on_cmd(pattern="netease ?(.*)"))
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await netase.edit("`Downloading...Please wait`")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await netase.reply("```Please unblock Bot and try again```")
            return
        await netase.edit("`Sending Your Music...`")
        await asyncio.sleep(3)
        await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await netase.delete()


@friday.on(friday_on_cmd(pattern="dzd ?(.*)"))
async def DeezLoader(Deezlod):
    if Deezlod.fwd_from:
        return
    d_link = Deezlod.pattern_match.group(1)
    if ".com" not in d_link:
        await Deezlod.edit("` I need a link to download something pro.`**(._.)**")
    else:
        await Deezlod.edit("**Initiating Download!**")
    chat = "@DeezLoadBot"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            response = await conv.get_response()
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            song = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await Deezlod.edit("**Error:** `unblock` bot `and retry!`")
            return
        await bot.send_file(Deezlod.chat_id, song, caption=details.text)
        await Deezlod.client.delete_messages(
            conv.chat_id, [msg_start.id, response.id, r.id, msg.id, details.id, song.id]
        )
        await Deezlod.delete()


CMD_HELP.update(
    {
        "song": "**Song**\
        \n\n**Syntax : **`.spd <song name>`\
        \n**Usage :** downloads the song from Spotify and uploades it.\
        \n\n**Syntax : **`.netease <song name>`\
        \n**Usage :** downloads the song from internet and uploades it.\
        \n\n**Syntax : **`.dzd <song name>`\
        \n**Usage :** downloads the song from Deezer and uploades it."
    }
)
