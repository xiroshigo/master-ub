from telethon import TelegramClient, events, sync

@events.register(events.NewMessage(pattern=".hello"))
async def test(event):
	await event.edit("test")
	