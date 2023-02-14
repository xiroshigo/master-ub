from gpytranslate import Translator
from telethon import TelegramClient, events, sync 



@events.register(events.NewMessage(pattern=".tr ?(.*)"))
async def tr(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "en"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("`.tr LanguageCode` as reply to a message")
        return
    # text = emoji.demojize(text.strip()) # No need this.
    lan = lan.strip()
    translator = Translator()
    try:
        translated = await translator(text, targetlang=lan)

        after_tr_text = translated.text
        source_lan = await translator.detect(f'{translated.orig}')
        transl_lan = await translator.detect(f'{translated.text}')
        output_str = "Message lsnguage: **{}**\nTranslated: **{}**\n\nMessage: {}".format(
            source_lan,
            transl_lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))