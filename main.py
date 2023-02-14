from telethon import TelegramClient, events, sync
#
from time import gmtime, strftime
from emoji import emojize
import asyncio

###
from emoji import emojize
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, aiocron, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User
#import pyfiglet
import zeus.client, zeus.test, zeus.bombs, zeus.helpp, zeus.loading, zeus.emoji, zeus.dump, zeus.sexy, zeus.type, zeus.magicrun, zeus.animation, zeus.animation2, zeus.chatinfo, zeus.mq, zeus.mute, zeus.nq, zeus.fuck, zeus.rev, zeus.tr, zeus.userinfo, zeus.base64, zeus.react, zeus.snow, zeus.ar, zeus.smsbomb
#
client = zeus.client.client
botClient = zeus.client.botClient
#
with client as friday:
	friday.add_event_handler(zeus.test.test) 
with client as friday:
	friday.add_event_handler(zeus.bombs.bombs)
with client as friday:
	friday.add_event_handler(zeus.helpp.help) 
with client as friday:
	friday.add_event_handler(zeus.loading.loading) 
with client as friday:
	friday.add_event_handler(zeus.emoji.itachi) 
with client as friday:
	friday.add_event_handler(zeus.dump.dump) 	
with client as friday:
	friday.add_event_handler(zeus.sexy.sexy) 
with client as friday:
	friday.add_event_handler(zeus.type.type) 
with client as friday:
	friday.add_event_handler(zeus.magicrun.magicrun) 	
with client as friday:
	friday.add_event_handler(zeus.animation.lul)
with client as friday:
	friday.add_event_handler(zeus.animation.snake)
with client as friday:
	friday.add_event_handler(zeus.animation.nothappy)
with client as friday:
	friday.add_event_handler(zeus.animation.clock)
with client as friday:
	friday.add_event_handler(zeus.animation.muah)
with client as friday:
	friday.add_event_handler(zeus.animation.heart)	
with client as friday:
	friday.add_event_handler(zeus.animation.gym)
with client as friday:
	friday.add_event_handler(zeus.animation.earth)
with client as friday:
	friday.add_event_handler(zeus.animation.moon)
with client as friday:
	friday.add_event_handler(zeus.animation.candy)
with client as friday:
	friday.add_event_handler(zeus.animation.smoon)
with client as friday:
	friday.add_event_handler(zeus.animation.tmoon)
with client as friday:
	friday.add_event_handler(zeus.animation.clown)
with client as friday:
	friday.add_event_handler(zeus.animation2.star)
with client as friday:
	friday.add_event_handler(zeus.animation2.boxs)		
with client as friday:
	friday.add_event_handler(zeus.animation2.rain)
with client as friday:
	friday.add_event_handler(zeus.animation2.clol)
with client as friday:
	friday.add_event_handler(zeus.animation2.odra)
with client as friday:
	friday.add_event_handler(zeus.animation2.fleaveme)		
with client as friday:
	friday.add_event_handler(zeus.animation2.loveu)
with client as friday:
	friday.add_event_handler(zeus.animation2.plane)
with client as friday:
	friday.add_event_handler(zeus.animation2.police)
with client as friday:
	friday.add_event_handler(zeus.animation2.jio)		
with client as friday:
	friday.add_event_handler(zeus.animation2.solarsystem)
with client as friday:
	friday.add_event_handler(zeus.chatinfo.info)
with client as friday:
	friday.add_event_handler(zeus.mq.mq)
with client as friday:
	friday.add_event_handler(zeus.mute.mute)		
with client as friday:
	friday.add_event_handler(zeus.nq.nq)	
with client as friday:
	friday.add_event_handler(zeus.fuck.fuck)					
with client as friday:
	friday.add_event_handler(zeus.rev.rev)										
with client as friday:
	friday.add_event_handler(zeus.tr.tr)
with client as friday:
	friday.add_event_handler(zeus.userinfo.userinfo)
with client as friday:
	friday.add_event_handler(zeus.base64.runb64)				
with client as friday:
	friday.add_event_handler(zeus.react.react)
with client as friday:
	friday.add_event_handler(zeus.snow.snow)
with client as friday:
	friday.add_event_handler(zeus.ar.runar)
#with client as brain:
#	brain.add_event_handler(zeus.brainrun.brainhandler)
#with client as moon:
#	moon.add_event_handler(zeus.moonrun.moonhandler)
#with client as ketdim:
#	ketdim.add_event_handler(zeus.ketdimrun.ketdimhandler)
#with client as tt:
#	tt.add_event_handler(zeus.tiktokrun.tiktokhandler)
#with client as ilove:
#	ilove.add_event_handler(zeus.iloverun.ilovehandler)
#with client as ir:
#	ir.add_event_handler(zeus.kissrun.kisshandler)
#with client as dr:
#	dr.add_event_handler(zeus.smilerun.smilehandler)
#with client as fr:
#	fr.add_event_handler(zeus.policerun.policehandler)
#with client as darkweb:
#	darkweb.add_event_handler(zeus.kick.kick)
#with client as darkweb:
#	darkweb.add_event_handler(zeus.calcubot.calcubot)
#dino
#with client as dakrweb:
#	darkweb.add_event_handler(zeus.dinorun.dinohandlers)
#rename
#with client as darkweb:
#	darkweb.add_event_handler(zeus.rename.rename)
#zipfile()


	
with client as friday:
	friday.add_event_handler(zeus.smsbomb.runj)					

	

client.start()
  
#result = pyfiglet.figlet_format("G O J O", font = "alligator" )
print("started")

client.run_until_disconnected()