from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    Lasiya = InlineKeyboardMarkup([
        
        [InlineKeyboardButton("Youtube โค", url="https://www.youtube.com/channel/UCHyseVcfusXkOClpwja00yg")],
        [InlineKeyboardButton(
            "Report Bugs ๐", url="https://t.me/Danuma_admin_bot")],
        [InlineKeyboardButton(
            "Bot channel ๐งช",url="https://t.me/danumabots")]
    ])
    thumbnail_url = "https://telegra.ph/file/69a96df53932f1cd2174f.jpg"
    await message.reply_photo(thumbnail_url, caption=f"Hi<b>{message.from_user.first_name}</b>\n\n<b>Instructions for use..</b>\nโข Type /help to get instructins.\nโข Type /tute for make a bot like me.\nโโโโโ โ **Lets Play** โ โโโโโ\n ", reply_markup=Lasiya)
    raise StopPropagation
