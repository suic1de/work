from logger import log, CloseApp
log(1, 'MAIN', 'Starting module imports')
from extraworker import exw
import os
import os.path
import re
import sys
import asyncio
import shutil
import requests
import urllib.request
import colorama
import os
import subprocess
colorama.init()
from fuzzywuzzy import fuzz
from tqdm import tqdm
from time import sleep
from os import system
from bs4 import BeautifulSoup
from colorstatscode import code
from settings import GetConfig, EditConfig
log(1, 'MAIN', 'Stage passed')

PATH = (os.path.abspath('.')+'/content')
HEADERS = {'user-agent': GetConfig("BASE", "useragent"), 'accept': '*/*'}

global NUM
NUM = 0

def call_upload(file):
    txtname = ('content/%s.txt' % file)
    videoname = ('content/%s.mp4' % file)
    exw(videoname, txtname)

if os.path.exists('content'):
    log(2, 'MAIN', 'Folder >content< already created')
    pass
else:
    os.mkdir("content")
    print(code.WARN, "Создана папка 'content' для хранения загруженных файлов.")
    log(2, 'MAIN', 'Folder >content< created')

if os.path.exists('content/Temp'):
    log(2, 'MAIN', 'Folder >Temp< already created')
    pass
else:
    os.mkdir("content/Temp")
    print(code.WARN, "Создана папка 'Temp' для хранения временных файлов.")
    log(2, 'MAIN', 'Folder >Temp< created')


try:
    with open(GetConfig("BASE", "parsefile"), "r", encoding="utf-8") as backfile:
        lines1 = backfile.readlines()
        log(1, 'MAIN', f'Number of lines:{len(lines1)}')
except FileNotFoundError:
        CloseApp(f'Файл >{GetConfig("BASE", "parsefile")}< не найден!')

def clear():
    _ = system('cls')
    sleep(3)
    if GetConfig("BASE", "getallurl") == 'True':
        massurls.get_urls(GetConfig("FILTER", "sitemap"))
    else:
        autoparse()

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

class massurls:
    def get_urls(url):
        EditConfig('BASE', 'getallurl', 'False')
        get = get_html(url)
        if get.status_code == 200:
            massurls.takethis(get.text)
        else:
            log(4, 'MAIN', f'Response: {get.status_code}')
            print(code.ERR, f'Что-то пошло не так, код ошибки: {get.status_code}')
            sleep(GetConfig("BASE", "pauseonerror"))
            onetwo()

    def takethis(get):
        print(123)
        i = 0
        soup = BeautifulSoup(get, 'html.parser')
        with open('temp.txt', 'w', encoding='utf-8') as g:
            for get in soup.find_all("loc", None):
                y = GetConfig("FILTER", "filterurl")
                print(get)
                g.write("%s\n" % get)
                i = i + 1
        if i == -1:
            CloseApp('Достигнут конец файла')
        else:
            try:
                r = open('temp.txt', encoding='utf-8').read().splitlines(1)
                with open(GetConfig("BASE", "parsefile"), 'w', encoding='utf-8') as f:
                    for tt in r:
                        tt = tt.replace(' ', '')
                        a = tt[5: -7]
                        f.write("%s\n" % a)
                        i = i - 1
            except FileNotFoundError:
                log(5, 'MAIN', 'File >temp.txt< not found')
                print(code.ERR, 'Временный файл не найден, подробнее в > report.log')
                sleep(GetConfig("BASE", "pauseonerror"))
                CloseApp('Временный файл не найден')
        f.close()
        try:
            os.remove('temp.txt')
        except OSError:
            pass


def get_content(get):
    soup = BeautifulSoup(get, 'html.parser')
    log(2, 'MAIN', 'Filtering the received content')
    print(code.LOG,'Фильтруем полученный контент')
    i = 0

    for get in soup.find_all("meta"):
        if get.get("itemprop", None) == "name":
            name = get.get("content", None)
            file1 = get.get("content", None)
            name = name.replace('–', '\nНазвание:')
            try:
                with open(PATH+'//'+file1+'.txt', "r", encoding="utf-8") as check:
                    log(2, 'MAIN', f'File already exists > {file1}')
                    a = GetConfig("BASE", "forceupload")
                    if a == 'True':
                        if exists(PATH+'//'+file1+'.mp4') == True:
                            print(code.LOG, 'Обнаружен незагруженный файл, вызван мастер загрузки.\nЭто может занять некоторое время...')
                            call_upload(file1)
                            onetwo()
                        else:
                            print(code.WARN, "Файл уже существует и был загружен ранее, пропускаем.")
                            log(3, 'MAIN', 'Additional content by filters is written to a file')
                            onetwo()
                    else:
                        print(code.WARN, "Файл уже существует!")
                        onetwo()
            except FileNotFoundError:
                pass


        elif get.get("itemprop", None) == "uploadDate":
            uploaddate = get.get("content", None)
            f = open(PATH + '//' + file1 + '.txt', 'a', encoding='utf-8')
            if len(GetConfig("FILTER", "studio")) > 3:
                log(2, 'MAIN', 'Studio filter enable, check settings.ini for change')
                if fuzz.partial_ratio(GetConfig("FILTER", "studio"), name) > 93:
                    f.write("Студия: #%s\n" % name)
                    f.write("Актеры: ")
                    print(code.INF,'Дополнительный контент по фильтрам записан в файл.')
                    log(2, 'MAIN', 'Additional content by filters is written to a file')
                else:
                    f.close()
                    try:
                        os.remove(PATH+'//'+file1+'.txt')
                        log(2, 'MAIN', 'File %s deleted' % PATH+'//'+file1+'.txt')
                        print(code.LOG, 'Студия не совпадает с указанной в фильтре, пропускаем.')
                        log(2, 'MAIN', 'Studio does not match in filter, skip')
                        onetwo()
                    except Exception as f:
                        log(4, 'MAIN', f'Error with >> %s. {f}' % PATH + '//' + file1 + '.txt')
                        print(code.ERR,'Произошла ошибка при попытке удаления файла, подробнее в > report.log')
                        sleep(GetConfig("BASE", "pauseonerror"))
                        onetwo()
            else:
                log(2, 'MAIN', 'Studio filter disable, check settings.ini for change')
                f.write("Студия: #%s\n" % name)
                f.write("Актеры: ")
                f.close()
                print(code.INF, 'Дополнительный контент по фильтрам записан в файл.')
                log(2, 'MAIN', 'Additional content by filters is written to a file')

    for get in soup.find_all("div", class_="tags-list"):
        y = '<a class ="label" href="https://xxxmax.net/actor/'
        tag = get #Вроде костыль а удобно
        for tag in soup.find_all('a', href=True, title=True):
            if fuzz.partial_ratio(tag, y) > 97:
                with open(PATH + '//' + file1 + '.txt', 'a', encoding='utf-8') as g:
                    name1 = tag.get("title").replace(' ','_')
                    g.write("#%s, " % name1)



    for get in soup.find_all("iframe"):
        if get.get("src", None):
            urlll = get.get("src", None)
            y = GetConfig("FILTER", "filtervid")
            if fuzz.partial_ratio(urlll, y) == 100:
                print(code.LOG,'Отловили ссылку к ролику, пытаемся скачать.')
                video = get_html(urlll)
                print(code.LOG,'Статус:',video.status_code)
                log(2, 'MAIN', f'Response: {video.status_code}')
                sleep(1)
                soup = BeautifulSoup(video.text, 'html.parser')
                for video in soup.find_all("source"):
                    if video.get("src", None):
                        with open(PATH + '//' + file1 + '.txt', 'a', encoding='utf-8') as file:
                            file.write("\nДата загрузки: %s" % uploaddate[0:10])
                        link = video.get("src", None)
                        log(2, 'MAIN', f'Download started: {link}, {file1}')
                        download_url(link, file1+'.mp4', file1)

                    else:
                        log(4, 'MAIN', f'Failed to start download video. More details: {file1}, RESP:{video.status_code}.')
                        print(code.ERR,'Не удалось начать загрузку видео.')
                        sleep(GetConfig("BASE", "pauseonerror"))
                        onetwo()

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, filename, file):
    try:
        with DownloadProgressBar(unit='B', unit_scale=True,
                                 miniters=1, desc=filename) as t:
            urllib.request.urlretrieve(url, filename=filename, reporthook=t.update_to)
            try:
                shutil.move(os.path.abspath('.')+'//'+filename, PATH+'//'+filename)
                log(2, 'MAIN', 'Download - Done. File moved to folder')
                print('\n',code.LOG,'Вызван мастер загрузки. Это может занять некоторое время...')
                call_upload(file)
                sleep(4)
                onetwo()
            except FileNotFoundError:
                log(4, 'MAIN', f'FileNotFoundError >{filename}< - shutil.move in download_url')
                print(code.ERR,'Ошибка при перемещении загруженного видео в папку, подробнее в > report.log')
                sleep(GetConfig("BASE", "pauseonerror"))
                onetwo()
    except urllib.error.URLError:
        log(4, 'MAIN', 'Failed to start download, it may not be possible to access the file')
        print(code.ERR,'Не удалось начать скачивание, возможно нету доступа к файлу.')
        sleep(GetConfig("BASE", "pauseonerror"))
        onetwo()

def onetwo():
    global NUM
    NUM = NUM + 1
    sleep(1)
    clear()

def autoparse():
    if len(lines1) == NUM:
        CloseApp('Достигнут конец файла')
    else:
        print(code.INF, f'Загружено {NUM} из {len(lines1)}')
        log(2, 'MAIN', f'Uploaded {NUM} of {len(lines1)}')
        with open(GetConfig("BASE", "parsefile"), "r", encoding="utf-8") as RLL:
            URL = RLL.readlines()[NUM]
            print(URL)
            y = GetConfig("FILTER", "filterurl")
            if fuzz.partial_ratio(URL, y) > 90:
                get = get_html(URL)
                if get.status_code == 200:
                    get_content((get.text))
                else:
                    log(4, 'MAIN', f'Response: {get.status_code}')
                    print(code.ERR, f'Что-то пошло не так, код ошибки: {get.status_code}')
                    sleep(GetConfig("BASE", "pauseonerror"))
                    onetwo()
            else:
                log(4, 'MAIN', f'Over 90% link match was expected. The entered one matches only on {fuzz.partial_ratio(URL, y)}%')
                print(code.ERR,f'Ожидалось совпадение ссылки более 90%. Введенная совпадает лишь на {fuzz.partial_ratio(URL, y)}%')
                sleep(GetConfig("BASE", "pauseonerror"))
                onetwo()

clear()