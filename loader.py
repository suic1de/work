#! /usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import time
import sys
import os
import utils
from telethon.client.telegramclient import TelegramClient
from logger import log, CloseApp
from settings import GetConfig
from telethon import events
from utils import progress, humanbytes, time_formatter, convert_from_bytes




api_id = GetConfig("LOADER", 'apiid')#'1926838'#keyline[0]
api_hash = GetConfig("LOADER", 'apihash')#'bd5be9e930902b2a02f0396932dddabb'#keyline[1]

try:
    client = TelegramClient('loader', api_id, api_hash)
except Exception as ap:
    sys.exit(1)

async def uploader(nameclip, nametxttoload, namecliptoload):

    await client.start()

    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print("%s - %s" % (dialog.name, dialog.entity.id))

    chat_id = GetConfig("LOADER", "channel")
    chat_id2 = GetConfig("LOADER", "channel2")

    #nameclip = 'rr.mp4'
    #nametxttoload = 'Task-1.txt'
    #namecliptoload = 'Temp\\5a746c60-1acf-4c62-9fc8-20d7ee0de6c9done.mp4'
    #chat_id = '1213129356'
    #chat_id2 = '1266958853'

    entity = None
    entity2 = None
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        id = str(dialog.entity.id)
        if id == chat_id:
            entity = dialog.entity
            break
    if not entity:
        sys.exit(1)

    dialogs1 = await client.get_dialogs()
    for dialog1 in dialogs1:
        id1 = str(dialog1.entity.id)
        if id1 == chat_id2:
            entity2 = dialog1.entity
            break
    if not entity:
        sys.exit(1)

    start = time.time()
    async for message1 in client.iter_messages(entity2, limit=1):
        print('TAKE1')
        print('Gat it:', message1.id)
    async for message1 in client.iter_messages(entity2, limit=1):
        print('TAKE2')
        print('Gat it:', message1.id)
    try:
        with open(nametxttoload, "r", encoding="utf-8") as t1:
            t11 = t1.readlines()[0:4]
            print('STAGE1')
            try:
                async for message1 in client.iter_messages(entity2, limit=1):
                    print('TAKE3')
                    print('Gat it:', message1.id)
                await client.send_file(entity, nameclip, video_note=True, supports_streaming=True,caption="".join(t11), filename=nameclip, timeout=1200)
                await asyncio.sleep(4)
                async for message in client.iter_messages(entity2, limit=1):
                    print('TAKE4')
                    print('Gat it:', message.id)
                await client.send_file(entity2, namecliptoload, reply_to=message.id, video_note=True, supports_streaming=True, filename=nameclip)
                async for message1 in client.iter_messages(entity2, limit=1):
                    print('TAKE5')
                    print('Gat it:', message1.id)
            except Exception as e:
                await client.send_message(entity, f"[UPLOADER] Произошла ошибка во время загрузки\n\n**Ошибка:** {e}")
    except Exception as e:
        await client.send_message(entity, f"[UPLOADER] Произошла ошибка во время загрузки\n\n**Ошибка:** {e}")


    await client.disconnect()

    try:
        os.remove(nameclip)
        os.remove(namecliptoload)
        sys.exit(0)
    except Exception:
        sys.exit(1)


