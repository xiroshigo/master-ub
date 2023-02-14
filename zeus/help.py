from telethon import TelegramClient, events, sync
import zeus.client
client = zeus.client.client
@events.register(events.NewMessage(pattern=".help"))
async def help(event):
	await event.edit("""

ZEUS-USERBOT ~~HELP~~ MENU

[01] Bombs - Animation emojise — .bombs
[02] Help - Help menu — .help
[03] Loading  - Animation loading — .loading
[04] Emoji  -  Emoji text editor - .emoji <here text>
[05] Dump - Candy dump animate - .dump
[06] Sexy - Animation porno - .sexy
[07] Typer - Animation write text - .type <here text>
[08] Lul - animatsia lul - .lul
[09] Snake - Snake animation - .snake 
[10] Nothappy - Abimation Nothappy - .nothappy
[11] Clock - animation clock - .clock
[12] Muah - animation - .muah
[13] Heart - animation - .heart
[14] Gym - animation gymnastic - .gym
[15] Earth - animation globus - .earth
[16] Moon - animation - .moon
[17] Candy - Animatiln - .candy
[18] Smoon - animation - .smoon
[19] Tmoon - animation - .tmoon
[20] Clown - animation - .clown
[21] Star - batterfly and star animation - .star
[22] Boxs - Color animation - .boxs
[23] Rain - water animation - .rain
[24] Clol - "What?" snimation - .clol
[25] Odra - Animation - .odra 
[26] Fleaveme - animation - .fleaveme
[27] Loveu - love animation - .loveu
[28] Plane - animation - .plane
[29] Police - animation sirena - .police
[30] Jio - animation - .jio
[31] Solarsystem - animation - .solarsystem
[32] Chatinfo - function scan chatinfo - .chatinfo  
[33] M.Q - Memocyte Quote - .mq <reply text>
[34] Mute - Admin function - .mute (m, h, d )
[35] N.Q - Nedo Quote - .nq <reply text>
[36] Fuck - Fuck you - .fuck
[37] Rev - reverse - .rev
[38] Tr - Translator - .tr <language code > <reply message>
[39] Userinfo - Username information - .userinfo <reply>
[40] Base64 - encode and decode  text messages - .b64 en <reply text> .b64 de <reply encoded message>
[41] React - reactions - .react help
[42] Snow - animation snow - .snow
[43] Tts - text to voice - .tts <lang code> reply text message
[44] Itp - image to pdf - .itp reply to image

News: @ub_zeus
""")
	