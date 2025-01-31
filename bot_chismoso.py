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

lista=[]

cartas=[]

#fichero=open("cartas.txt","wb")
#pickle.dump(cartas,fichero)
#fichero.close()

ayuda="1-Para enviar mensajes al canal se usan los siguientes comandos: \n/enviar 'mensaje a enviar'\n*Ejemplo: \n/enviar Te tengo un chisme nuevo \n2-Para enviar una cancion 🎧 o foto 📸 se utiliza el mismo comando, ademas se puede responder una foto o cancion con el comando /enviar *'Mensaje a enviar' \n*Ejemplo: \n(responde una foto o cancion y luego escribe en el chat) \n/enviar *Aqui mando una cancion para mi persona especial \n3-Tambien puedes enviar encuestas solo creandola en el chat del bot. \n4-Para enviar una carta al buzon para el 14 de febrero se usa el comando /carta seguido del texto de la carta y al final 'Para:' tal persona\n*Ejemplo:\n/carta Hola, seguro no te esperabas recibir una carta por aqui, te quiero mucho y estoy enamorado de ti. Para:Fulanita de Matematica\n5-Si tienes alguna queja o sugerencia usa el comando /feedback, funciona igual que /enviar\n6-Para unirte al canal usa el comando /canal"

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
        await client.send_message(chat, message=ayuda)
        
    elif(mesage[0:8] == "/enviar "):
        if(event.message.media):
            if isinstance(event.message.media, MessageMediaPhoto):
                index=mesage.find(" ")
                text=mesage[index+1:]
                text=text.replace("pinga","p*nga")
                text=text.replace("cojone","coj*ne")
                text=text.replace("bollo","b*llo")
                text=text.replace("negga","n*gga")
                text=text.replace("singao","s*ngao")
                text=text.replace("singar","s*ngar")
                await client.send_message("@Leonardo2004", file=event.message.media.photo, message=text)
                await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                user={"id":event.sender.id,"mess":text}
                lista.append(user)
            
            elif isinstance(event.message.media, MessageMediaDocument):
                index=mesage.find(" ")
                text=mesage[index+1:]
                text=text.replace("pinga","p*nga")
                text=text.replace("cojone","coj*ne")
                text=text.replace("bollo","b*llo")
                text=text.replace("negga","n*gga")
                text=text.replace("singao","s*ngao")
                text=text.replace("singar","s*ngar")
                await client.send_message("@Leonardo2004", file=event.message.media.document, message=text)
                await event.reply("Cancion y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                user={"id":event.sender.id,"mess":text}
                lista.append(user)
        
        elif(mesage[0:9] == "/enviar *" and event.message.reply_to):
                reply_to_msg_id = event.message.reply_to.reply_to_msg_id
                reply_to_peer_id = event.message.reply_to.reply_to_peer_id
                original_message = await client.get_messages(reply_to_peer_id, ids=reply_to_msg_id)
                text=original_message.message
                index=mesage.find("*")
                if(original_message.media):
                    if isinstance(original_message.media, MessageMediaPhoto):
                        await client.send_message("@Leonardo2004", file=original_message.media.photo, message=mesage[index+1:])
                        await event.reply("Foto y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                        user={"id":event.sender.id,"mess":mesage[index+1:]}
                        lista.append(user)
                    elif isinstance(original_message.media, MessageMediaDocument):
                        await client.send_message("@Leonardo2004", file=original_message.media.document, message=mesage[index+1:])
                        await event.reply("Cancion y mensaje enviado al administrador 🚀 si es aprobado se enviara al canal 😉")
                        user={"id":event.sender.id,"mess":mesage[index+1:]}
                        lista.append(user)
                else:
                    await client.send_message("@Leonardo2004", text)
                    await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
                    user={"id":event.sender.id,"mess":text}
                    lista.append(user)
             
        else:
            index=mesage.find(" ")
            text=mesage[index+1:]
            text=text.replace("pinga","p*nga")
            text=text.replace("cojone","coj*ne")
            text=text.replace("bollo","b*llo")
            text=text.replace("negga","n*gga")
            text=text.replace("singao","s*ngao")
            text=text.replace("singar","s*ngar")
            await client.send_message("@Leonardo2004", text)
            await event.reply("Mensaje enviado al administrador 🚀, si es aprobado se enviara al canal 😉")
            user={"id":event.sender.id,"mess":text}
            lista.append(user)
            
    elif(event.message.poll):
        await event.reply("Encuesta recibida y enviada al administrador 🚀 , si es aprobada se enviara al canal 😉")
        await client.send_message("@Leonardo2004" , file=event.poll , message="" )
        
    elif(mesage[0:7]== "/carta "):
        index=mesage.find("Para:")
        if(index>20):
            fichero=open("cartas.txt","rb")
            cartas=pickle.load(fichero)
            fichero.close()
            cartas.append(mesage[7:])
            fichero2=open("cartas.txt","wb")
            pickle.dump(cartas,fichero2)
            fichero2.close()
            await event.reply("Carta enviada 🚀, se guardara hasta el 14 de febrero y luego sera abierta")
        else:
            await event.reply("Texto de carta muy corto o no se ha encontrado el 'Para:'")
            
    elif(mesage == "/abrir" and sender.id == 968663996):
        await event.reply("Se ha abierto el buzon, se enviaran todas las cartas al canal")
        fichero=open("cartas.txt","rb")
        cartas=pickle.load(fichero)
        fichero.close()
        for carta in cartas:
            await client.send_message(chanel, message=carta)
            
    elif(mesage=="/num"):
        fichero=open("cartas.txt","rb")
        cartas=pickle.load(fichero)
        fichero.close()
        await event.reply("En este momento se encuentran " + str(len(cartas)) + " cartas en el buzon")
            
    elif(mesage=="/start"):
        await client.send_message(chat,"Hola! escribe /help para obtener ayuda de como enviar mensajes al canal")
        
    elif(mesage=="/canal"):
        await event.reply("Link del canal de Secretos y Confesiones 🤫: https://t.me/+FOTbPY4sSpw2ODMx")
        
    elif(mesage=="/done" and event.message.reply_to and sender.id == 968663996):
        reply_to_msg_id = event.message.reply_to.reply_to_msg_id
        reply_to_peer_id = event.message.reply_to.reply_to_peer_id
        original_message = await client.get_messages(reply_to_peer_id, ids=reply_to_msg_id)
        text=original_message.message
        if(original_message.media):
            if isinstance(original_message.media, MessageMediaPhoto):
                await client.send_message(chanel , file=original_message.media.photo , message=text)
                await event.reply("Foto enviada al canal")
            elif isinstance(original_message.media, MessageMediaDocument):
                await client.send_message(chanel , file=original_message.media.document , message=text)
                await event.reply("Cancion enviada al canal")
            elif (original_message.poll):
                await client.send_message(chanel, file=original_message.poll , message="")
                await event.reply("Encuesta enviada al canal")
        else:
            await client.send_message(chanel,original_message.message)
            await event.reply("Mensaje enviado al canal")
        
    elif(mesage[0:10] == "/feedback "):
        index=mesage.find(" ")
        text="Mensaje de feedback: "
        text=text + mesage[index+1:]
        await client.send_message("@Leonardo2004", text )
        await event.reply("Mensaje enviado al administrador, gracias por la sugerencia 😁")
        
    elif(mesage[0:4] == "/no " and event.message.reply_to and sender.id == 968663996 ):
        reply_to_msg_id = event.message.reply_to.reply_to_msg_id
        reply_to_peer_id = event.message.reply_to.reply_to_peer_id
        original_message = await client.get_messages(reply_to_peer_id, ids=reply_to_msg_id)
        text=original_message.message
        index=mesage.find(" ")
        mensage="El mensaje: '" + text + "' no ha sido enviado porque: " + mesage[index+1:]
        for user in lista:
            if(user["mess"]==text):
                id=user["id"]
                await client.send_message(id,mensage)
                await event.reply("Mensaje enviado")
                lista.remove(user)
        
    else:
        if not isinstance(chat,Channel):
            await client.send_message(chat,"Formato del mensaje incorrecto, si tiene dudas presione /help")
         
with client:
    client.run_until_disconnected()


