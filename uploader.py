#! /usr/bin/env python
# -*- coding: utf-8 -*-
from logger import log, CloseApp
import asyncio
import time
import sys
import os
import utils
from telethon.client.telegramclient import TelegramClient
from settings import GetConfig
from utils import progress, humanbytes, time_formatter, convert_from_bytes


async def uploader(file = None):


	if file == None:
		log(3, 'UPLOADER', 'Download call came empty > None')
		pass
	else:
		txtname = ('content\\%s.txt' % file)
		videoname = ('content\\%s.mp4'% file)
		filename = ('%s.mp4' % file)
