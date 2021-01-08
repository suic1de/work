#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logger
from logger import log, CloseApp
import configparser
import sys
# Auto generate by retUrn3d-Base

config = configparser.ConfigParser()
config.read("settings.ini")

def check():
    log(1, 'CHECK\\SETTINGS', 'Checking file integrity')
    try:
        with open('settings.ini', "r", encoding="utf-8") as None112:
            log(2, 'CHECK\\SETTINGS', 'settings.ini - OK')
    except Exception as f:
        log(5, 'CHECK\\SETTINGS', f'Failed to read file! > settings.ini - Failed. More details: {f}')
        CreateConfig()

    if config.sections() == ['BASE', 'FILTER', 'LOADER']:
        log(2, 'CHECK\\SETTINGS', f'All sections - OK > {config.sections()}')
    else:
        log(5, 'CHECK\\SETTINGS', f'Not all sections coincided! > {config.sections()}. Delete file >settings.ini< to create a new one at startup')
        CloseApp('Не все разделы совпали')
    log(1, 'CHECK\\SETTINGS', 'Successful')

def GetConfig(section = None, item = None):
    log(2, 'SETTINGS', f'№1 Requesting the settings file > {section}, {item}')
    ini = config[section][item]
    log(2, 'SETTINGS', f'№2 Response > {ini}')
    return ini

def EditConfig(part = None, section = None, item = None):
    log(2, 'SETTINGS', f'№1 Request to edit the settings file > {part}, {section}, {item}')
    try:
        config.set(part, section, item)
        with open("settings.ini", "w") as config_file:
            config.write(config_file)
    except Exception as e:
        log(4, 'SETTINGS', f'№2 Failed to edit the settings file. More details: {e}')
    log(2, 'SETTINGS', f'№2 Response > successfully')

def CreateConfig():
    log(3, 'SETTINGS', 'Create default file > settings.ini')
    config.add_section('BASE')
    config.set("BASE", "useragent", "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'")
    config.set("BASE", "parsefile", "parse.txt")
    config.set("BASE", "loglevel", "DEBUG")
    config.set("BASE", "pauseonerror", "5")
    config.set("BASE", "getallurl", "False")
    config.set("BASE", "getdialogs", "True")
    config.set("BASE", "forceupload", "True")
    config.add_section('FILTER')
    config.set("FILTER", "filtervid", "https://xxxmax.net/wp-content/plugins/clean-tube-player/public/player-x.php?")
    config.set("FILTER", "filterurl", "https://xxxmax.net")
    config.set("FILTER", "sitemap", "https://xxxmax.net/post-sitemap33.xml")
    config.set("FILTER", "studio", "")
    config.add_section('LOADER')
    config.set("LOADER", "apiid", "")
    config.set("LOADER", "apihash", "")
    config.set("LOADER", "channel", "")
    config.set("LOADER", "channel2", "")
    with open("settings.ini", "w") as config_file:
        config.write(config_file)
    CloseApp('Файл настроек был сброшен. Требуется его дополнение')


check()