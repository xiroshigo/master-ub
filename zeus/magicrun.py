from telethon import TelegramClient, events
import zeus.client
from zeus.magic import Magic
import time
magic = Magic()
client = zeus.client.client
@events.register(events.NewMessage)
async def magicrun(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)