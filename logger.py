#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import sys
from time import sleep
from colorstatscode import code


logging.basicConfig(level=logging.DEBUG, filename='report.log', filemode='w', format='%(asctime)s | %(levelname)s <> %(message)s.')
logging.debug('[LOGGER] LOGGING > STARTED')

def log(level, module, message):

    if level == 1:
        logging.debug(f'[{module}] {message}')
    elif level == 2:
        logging.info(f'[{module}] {message}')
    elif level == 3:
        logging.warning(f'[{module}] {message}')
    elif level == 4:
        logging.error(f'[{module}] {message}')
    elif level == 5:
        logging.critical(f'[{module}] {message}')
    else:
        logging.error(f'[LOGGER] Level >{level}< not found')

def CloseApp(arg):
    print(code.WARN,f'Автоматическое завершение программы по причине: {arg}, подробнее в > report.log')
    log(3, 'END', arg)
    sleep(6)
    sys.exit(1)

