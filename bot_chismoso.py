import asyncio
from telethon import TelegramClient, events, sync, types
from telethon import functions
from telethon.tl.types import *
import time
import pickle

# Use your own values from my.telegram.org
api_id = 29068923
api_hash = '72035fc7d10fc5bd2847e23ecad1a850'
bot_token = "7969883361:AAGSbuVfeHdje5QVcSy3_2eloD6zKaIcHX8"
client = TelegramClient("bot",api_id,api_hash).start(bot_token=bot_token)

print("Iniciando")

@client.on(events.NewMessage)
async def handle_new_message(event):
    sender = await event.get_sender()
    chat = await event.get_chat()
    mesage=event.message.message
    canal=-1002488977043
    chanel=await client.get_entity(PeerChannel(canal))
    #print(sender.id)
    #print(chat)
    
    if(mesage=="/help"):
        await event.reply("Escribe en este formato el nuevo mensaje que vas a enviar: '/enviar Te tengo un chisme buenooo' , por favor recuerda el ' ' (espacio) despues del enviar, si tiene sugerencias use el comando /feedback , funciona exactamente igual que /enviar 😁")
    elif(mesage[0:8] == "/enviar "):
        index=mesage.find(" ")
        text=mesage[index+1:]
        text=text.replace("pinga","p*nga")
        text=text.replace("cojone","coj*ne")
        text=text.replace("bollo","b*llo")
        text=text.replace("negga","n*gga")
        text=text.replace("singao","sing*o")
        await client.send_message("@Leonardo2004", text)
        await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
    elif(mesage=="/start"):
        await client.send_message(chat,"Hola! escribe /help para obtener ayuda de como enviar mensajes al canal")
    elif(mesage=="/canal"):
        await event.reply("Link del canal de chismes y secretos 🤫: https://t.me/+FOTbPY4sSpw2ODMx")
    elif(mesage=="/done" and event.message.reply_to and sender.id == 968663996):
        reply_to_msg_id = event.message.reply_to.reply_to_msg_id
        reply_to_peer_id = event.message.reply_to.reply_to_peer_id
        original_message = await client.get_messages(reply_to_peer_id, ids=reply_to_msg_id)
        await client.send_message(chanel,original_message.message)
        await event.reply("Mensaje enviado al canal")
    elif(mesage[0:10] == "/feedback "):
        index=mesage.find(" ")
        text=mesage[index+1:]
        await client.send_message("@Leonardo2004", text )
        await event.reply("Mensaje enviado al administrador, gracias por la sugerencia 😁")
    else:
        await client.send_message(chat,"Formato del mensaje incorrecto")
         
with client:
    client.run_until_disconnected()


