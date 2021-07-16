#!/usr/bin/python
# -*- coding: utf-8 -*-
import pip

# Проверка библиотек
try:
    import time, random, datetime, asyncio, sys, wikipedia, logging, aiohttp, covid, pyrogram, os, wget
except ModuleNotFoundError:
    print("Установка дополнений...\n")
    pip.main(['install', 'tgcrypto'])
    pip.main(['install', 'pyrogram'])
    pip.main(['install', 'covid'])
    pip.main(['install', 'aiohttp'])
    pip.main(['install', 'wikipedia'])
    pip.main(['install', 'logging'])
    pip.main(['install', 'wget'])
    import os
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

# Проверка конфига
config = os.path.exists('config.ini')
if config == True:
    print("work...")
if config == False:
    with open("config.ini", "w+") as f:
        rep = """
[pyrogram]
api_id = 2860432
api_hash = 2fde6ca0f8ae7bb58844457a239c7214
app_version = 1.6.3.3
device_model = Terminal | By a9fm userbot | CLIP USERBOT |
"""
        repo = str(rep)
        f.write(repo)
        f.close()

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, ChatSendMediaForbidden
from pyrogram.types import Message
from time import sleep, perf_counter
from pyrogram.handlers import MessageHandler
from covid import Covid
from aiohttp import ClientSession
from google_trans_new import google_translator
from googletrans import LANGUAGES
import time, random, datetime, asyncio, sys, wikipedia, requests, googletrans

# Пноверка файла репутации
rep = os.path.exists('rep.txt')
if rep == True:
    print("work...")
else:
    with open("rep.txt", "w+") as f:
        rep = "0"
        repo = str(rep)
        f.write(repo)
        f.close()

# Очистка терминала
os.system('cls' if os.name == 'nt' else 'clear')

print("""
  ____ _     ___ _____
 / ___| |   |_ _|  _  |
| |   | |    | || |_) |
| |___| |___ | ||  ___|
 \____|_____|___|_|
    _       ___            _____   __  __
   / \     / _ \          |  ___| |  \/  |
  / _ \   | (_) |  _____  | |_    | |\/| |
 / ___ \   \__, | |_____| |  _|   | |  | |
/_/   \_\    /_/          |_|     |_|  |_|

Telegram Канал - @ArturDestroyerBot
Помощь - @Artur_destroyer

Логи:""")
# Спасибо всем кто помогал этому боту, а именно, Дентли, DragonBot, @frontcoder, Дима, a9fm


# Логи + Вход
app = Client("my_account")
import logging

# Вход в группу [Обновления]
with app:
         app.join_chat('ArturDestroyerBot') # Прошу, не убирайте эту строку

# Помощь | Инфа про юзербота
@app.on_message(filters.command("help" , prefixes=".") & filters.me)
async def info(client: Client, message: Message):
    await message.edit("""<b>UserBot CLIP [@ArturDestroyerBot]</b>

Версия 1.6.3.3
Создатель @artur_destroyer
<code>
КОММАНДЫ

Основные:
.help - Помощь | Информация | Проверка версии
.ping - Проверка Пинга бота [Качество полключения]
.restart - Перезагрузка [Ошибка, Баг в боте]
.update - Обновить

Мало временни:
.afk [Причина] - Ввойти в АФК [Не в сети]
.unafk - Выйти из АФК
.wiki [Слово] - Поиск в Википедии
.covid [Страна] - Статистика заражения вирусом covid-19 [Коронавирус]
.weather [Город] - Погода

Процент загрузки:
.hack - Взлом Пентагонна
.jopa - Взлом жопы
.mum - Поиск матери
.drugs - Принять 3aПрEщEHHblE BещECTBа

Спам:
.spam [Кол-во смс] [Текст сообщения]
.spamt - Спам Текстом
.spams - Спам стикерами
.stop - Стоп спам

Плюшки:
.type - Эффект Печати
.hide - Сообщения с Авто-удалением
.sw - Переключение расскладки [Если написали по типу ghbdtn]
.pin- Закрепить
.unpin - Открепить
.short [Ссылка] - сократитель ссылок
.tageall - Призыв всех участников
.truns - Смешная озвучка текста на английском
.id - Айди
.info - Информация

Администрация:
.ban - Бан
.unban - Разбан
.kick - Кик
.mute - Мут
.unmute - Размут
.kickall - Удаление всех с группы

[Репутация, для повышения попросите 2 человека написать вам в ответ сообщение "+"]
</code>
Если нужна помощь, пиши @artur_destroyer""")

# Перезагрузка
@app.on_message(filters.command("restart" , prefixes=".") & filters.me)
async def restart(client: Client, message: Message):
    await message.edit("<b>Перезагрузка бота...</b>")
    await message.edit("<b>Бот перезапущен!</b>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

@app.on_message(filters.command("update" , prefixes=".") & filters.me)
async def info(client: Client, message: Message):
    await message.edit("<b>Обновление бота...</b>")
    os.remove("bot.py")
    url = 'https://raw.githubusercontent.com/A9FM/ClipUserbot/main/bot.py'
    wget.download(url, '')
    await message.edit("<b>Бот обновлён...</b>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

# Репутация
@app.on_message(filters.text & filters.incoming & filters.regex('^\-$') & filters.reply)
async def rep(client: Client, message: Message):
    if message.reply_to_message.from_user.is_self:
        with open("rep.txt", "r+") as f:
            data = f.read()
            data = int(data)
            num = 1
            rep = data - num
            repo = str(rep)
            f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "💔 Вы понизили мою репутацию 💔\n🔝 Репутация " + str(repo) + " 🔝"
            await message.reply_text(text)
@app.on_message(filters.text & filters.incoming & filters.regex('^\+$') & filters.reply)
async def rep(client: Client, message: Message):
    if message.reply_to_message.from_user.is_self:
        with open("rep.txt", "r+") as f:
            data = f.read()
            data = int(data)
            num = 1
            rep = data + num
            repo = str(rep)
            f.close()
        with open("rep.txt", "w+") as f:
            repo = str(rep)
            f.write(repo)
            f.close()
            text = "❤️ Вы повысили мою репутацию ❤️\n🔝 Репутация " + str(repo) + " 🔝"
            await message.reply_text(text)

# Айди
@app.on_message(filters.command('id', prefixes='.') & filters.me)
async def spam(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.edit(f"Твой айди: {message.chat.id}")
    else:
        id = f"Твой айди: {message.reply_to_message.from_user.id}\n\nАйди группы: {message.chat.id}"
        await message.edit(id)

# спам
@app.on_message(filters.command('spam', prefixes='.') & filters.me)
async def spam(client: Client, message: Message):
        if not message.text.split('.spam', maxsplit=1)[1]:
                await message.edit('<i>Нету аргументов.</i>')
                return
        count = message.command[1]
        text = ' '.join(message.command[2:])
        count = int(count)
        await message.delete()
        for _ in range(count):
                await app.send_message(message.chat.id, text)
                await asyncio.sleep(0.2)

# Призыв всех
@app.on_message(filters.command("tagall", prefixes=".") & filters.me)
async def tagall(client, message):
    args = ' ! '
    if len(message.text.split()) >= 2:
        args = message.text.split('.tagall ', maxsplit=1)[1]
    await message.delete()
    chat_id = message.chat.id
    string = ""
    limit = 1
    members = client.iter_chat_members(chat_id)
    async for member in members:
        tag = member.user.username
        if limit <= 9:
            list = ['ᅠ', 'ᅠ']
            if tag != None:
                w = random.choice(list)
                string += f"<a href='https://t.me/{tag}'>{w}</a> "
            else:
                w = random.choice(list)
                string += f"<a href='tg://user?id={member.user.id}'>{w}</a> "
            limit += 1
        else:
            text = f"{args}{string}"
            await client.send_message(chat_id, text, disable_web_page_preview=1)
            limit = 1
            string = ""
            await asyncio.sleep(2)

# Удалить смс
@app.on_message(filters.command("del" , prefixes=".") & filters.me)
async def del_msg(client: Client, message: Message):
    if message.reply_to_message:
        message_id = message.reply_to_message.message_id
        await message.delete()
        await client.delete_messages(message.chat.id, message_id)

# Пурдж
@app.on_message(filters.command('purge', prefixes='.') & filters.me)
async def purge(client: Client, message: Message):
        if message.reply_to_message:
                r = message.reply_to_message.message_id
                m = message.message_id
                msgs = []
                await message.delete()
                v = m - r
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                r = message.reply_to_message.message_id
                msgs = []
                while r != m:
                        msgs.append(int(r))
                        r += 1
                await client.delete_messages(message.chat.id, msgs)
                await app.send_message(message.chat.id, f'<b>Удалено > {v} сообщений!</b>')
        else:
                        await message.edit('<i>А где реплай?</i>')

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
async def type(client: Client, message: Message):
    orig_text = message.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            sleep(0.10)
        except FloodWait as e:
            sleep(e.x)

# Удаление всех с группы (200 уч лимит)
@app.on_message(filters.command('kickall', '.') & filters.me & ~filters.private)
def kickall(client: Client, message: Message):
    num = 0
    for all in client.iter_chat_members(message.chat.id):
       try:
           num =+ 1
           client.kick_chat_member(message.chat.id, all.user.id, 0)
       except:
           pass

# Бан
@app.on_message(filters.command("ban", prefixes=".") & filters.me & ~filters.private)
async def ban(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.kick_chat_member(message.chat.id, reply.from_user.id)
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> забанен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

# Кик
@app.on_message(filters.command("kick", prefixes=".") & filters.me & ~filters.private)
async def kick(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.kick_chat_member(message.chat.id, reply.from_user.id)
        await app.unban_chat_member(message.chat.id, reply.from_user.id)
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> кикнут!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

# Мут
@app.on_message(filters.command("mute", prefixes=".") & filters.me & ~filters.private)
async def mute(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=False))
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> замучен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

# Размут
@app.on_message(filters.command("unmute", prefixes=".") & filters.me & ~filters.private)
async def unmute(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=False, can_invite_users=True, can_pin_messages=False))
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> размучен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

# Разбан
@app.on_message(filters.command("unban", prefixes=".") & filters.me & ~filters.private)
async def unban(client: Client, message: Message):
    try:
        if not message.reply_to_message:
            await message.edit('<i>А где реплай?</i>')
            return
        reply = message.reply_to_message
        await app.restrict_chat_member(message.chat.id, reply.from_user.id, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_polls=True, can_send_other_messages=True, can_add_web_page_previews=True, can_change_info=False, can_invite_users=True, can_pin_messages=False))
        await message.edit(f'<b><a href="tg://user?id={reply.from_user.id}">{reply.from_user.first_name}</a> разбанен!</b>')
    except:
        await message.edit('<i>У меня недостаточно прав.</i>')

# Инфо
@app.on_message(filters.command("info", prefixes=".") & filters.me & ~filters.private)
async def unban(client: Client, message: Message):
    if message.reply_to_message:
        username = message.reply_to_message.from_user.username
        id = message.reply_to_message.from_user.id
        first_name = message.reply_to_message.from_user.first_name
        user_link = message.reply_to_message.from_user.mention
    else:
        username = message.from_user.username
        id = message.from_user.id
        first_name = message.from_user.first_name
        user_link = message.from_user.mention
    if username:
        username = f"@{username}"
        text = f"""
<b>Информация</b>:
Айди: <code>{id}</code>
Имя: {first_name}
Юзернейм: {username}
Ссылка: {user_link}"""
    else:
        text = f"""
<b>Информация</b>:
Айди: <code>{id}</code>
Имя: {first_name}
Ссылка: {user_link}"""
    await message.edit(text, parse_mode="HTML")

# Трунслэйт озвучка
@app.on_message(filters.command("truns", prefixes=".") & filters.me)
async def switch(client: Client, message: Message):
    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"""
    en_keys = """eicykengшщzh_fiwaproldgeiчsmit_bu.E"№;%:?ICYKENGШЩZH_FIWAPROLDGEIЧSMIT_BU,"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit('No text for switch')
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

# Пинг
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def ping(client: Client, message: Message):
    start = perf_counter()
    await message.edit('Pong')
    end = perf_counter()
    ping2 = end - start
    ping = ping2 * 1000

    if 0 <= ping <= 199:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟢Качество соединение: Стабильное🟢')
    if 199 <= ping <= 400:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🟠Качество соединения: Хорошее🟠')
    if 400 <= ping <= 600:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n🔴Качество соединения: Не стабильное🔴')
    if 600 <= ping:
        await message.edit(f'<b>🏓 Понг\n📶</b> {round(ping)} мс\n⚠Качество соединения: Перепады связи⚠')

# Covid
@app.on_message(filters.command("covid", prefixes=".") & filters.me)
async def covid_local(client: Client, message: Message):
    region = ' '.join(message.command[1:])
    await message.edit('<code>Загрузка...</code>')
    covid = Covid(source="worldometers")
    try:
        local_status = covid.get_status_by_country_name(region)
        await message.edit("<b>=======🦠 COVID-19 STATUS 🦠=======</b>\n" +
                           f"<b>Регион [Страна]</b>: <code>{local_status['country']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>🤧 Новые заражения</b>: <code>{local_status['new_cases']}</code>\n" +
                           f"<b>😷 Новые смерти</b>: <code>{local_status['new_deaths']}</code>\n" +
                           "<b>====================================</b>\n" +
                           f"<b>😷 Подтверждённые</b>: <code>{local_status['confirmed']}</code>\n" +
                           f"<b>❗️ Активные [Заражённые]:</b> <code>{local_status['active']}</code>\n" +
                           f"<b>⚠️ Критически</b>: <code>{local_status['critical']}</code>\n" +
                           f"<b>💀 Смертей</b>: <code>{local_status['deaths']}</code>\n" +
                           f"<b>🚑 Спасенно [Вылеченно]</b>: <code>{local_status['recovered']}</code>\n")
    except ValueError:
        await message.edit(f'<code>There is no region called "{region}"</code>')

# Сократитель линков
linkToken = '6c2ac1846a1c1A2d5f88A3E5fbf0e14fcf96d7d0'
async def link_short(link: str):
    async with ClientSession(
        headers={
            'Authorization': f'API-Key {linkToken}'
        }
    ) as ses:
        async with ses.post(
            'https://api.waa.ai/v2/links',
            json={'url': link}
        ) as resp:
            return await resp.json()

@app.on_message(filters.command("short", prefixes=".") & filters.me)
async def shorten_link_command(client: Client, message: Message):
    if message.reply_to_message:
         link = message.reply_to_message.text
    else:
        try:
            link = message.command[1]
        except IndexError:
            return await message.delete()
    output = (await link_short(link))["data"]
    await message.edit(f'Сокращенная ссылка: {output["link"]}')

# Закреп
@app.on_message(filters.command("pin", prefixes=".") & filters.me)
async def pin(client: Client, message: Message):
    try:
        message_id = message.reply_to_message.message_id
        await client.pin_chat_message(message.chat.id, message_id)
        await message.edit('<code>Закрепленно! </code>')
    except:
        await message.edit('<b>Сделайте реплай сообщению</b>')

@app.on_message(filters.command("unpin", prefixes=".") & filters.me)
async def pin(client: Client, message: Message):
    try:
        message_id = message.reply_to_message.message_id
        await client.unpin_chat_message(message.chat.id, message_id)
        await message.edit('<code>Открепленно! </code>')
    except:
        await message.edit('<b>Сделайте реплай сообщению</b>')
# Википедия
@app.on_message(filters.command("wiki", prefixes=".") & filters.me)
async def wiki(client: Client, message: Message):
    lang = message.command[1]
    user_request = ' '.join(message.command[2:])
    await message.edit('<b>Ищем инфу</b>')
    if user_request == '':
        wikipedia.set_lang("ru")
        user_request = ' '.join(message.command[1:])
    try:
        if lang == 'en':
            wikipedia.set_lang("en")

        result = wikipedia.summary(user_request)
        await message.edit(f'''<b>Слово:</b>
<code>{user_request}</code>

<b>Значение:</b>
<code>{result}</code>''')
    except Exception as exc:
        await message.edit(f'''<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>''')
# Переклюяение раскладки
@app.on_message(filters.command("sw", prefixes=".") & filters.me)
async def switch(client: Client, message: Message):
    text = ' '.join(message.command[1:])
    ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
    en_keys = """`qwertyuiop[]asdfghjkl;'zxcvbnm,./~@#$%^&QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?"""
    if text == '':
        if message.reply_to_message:
            reply_text = message.reply_to_message.text
            change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
            reply_text = str.translate(reply_text, change)
            await message.edit(reply_text)
        else:
            await message.edit('Текст отсутствует')
            await asyncio.sleep(3)
            await message.delete()
    else:
        change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
        text = str.translate(text, change)
        await message.edit(text)

# Погода
def get_pic(city):
    file_name = f'{city}.png'
    with open(file_name, 'wb') as pic:
        response = requests.get('http://wttr.in/{citys}_2&lang=en.png', stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            pic.write(block)
        return file_name

@app.on_message(filters.command("weather", prefixes=".") & filters.me)
async def weather(client: Client, message: Message):
    city = message.command[1]
    await message.edit("```Загрузка...```")
    r = requests.get(f"https://wttr.in/{city}?m?M?0?q?T&lang=rus")
    await message.edit(f"```City: {r.text}```")
    await client.send_document(chat_id=message.chat.id, document=get_pic(city), reply_to_message_id=message.message_id)
    os.remove(f'{city}.png')

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
async def hack(client: Client, message: Message):
    perc = 0
    while(perc < 100):
        try:
            text = "👮 Взлом пентагона в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    text = "✅ Пентагон успешно взломан!"
    await message.edit(str(text))
    sleep(3)
    perc = 0
    while(perc < 100):
        try:
            text = "⬇️ Скачивание данных ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
        text = "🐓Нашли файты что ты петух!"
        await message.edit(text)

# Команда Взлома жопы
@app.on_message(filters.command("jopa", prefixes=".") & filters.me)
async def jopa(client: Client, message: Message):
    perc = 0
    while(perc < 100):
        try:
            text = "🍑 Взлом жопы в процессе ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    text = "✅ Жопа взломана"
    await message.edit(str(text))
    sleep(3)
    text = "🔍 Поиск Сливов ..."
    await message.edit(str(text))
    perc = 0
    sleep(3)
    while(perc < 100):
        try:
            text = "⬇️ Скачивание сливов ..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 4)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    text = "✅ Сливы были найдены"
    await message.edit(str(text))
    perc = 0
    sleep(5)
    while(perc < 100):
        try:
            text = "⬆️ Продажа сливов барыге..." + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)

    text = "✅ Проданно"
    await message.edit(str(text))
    sleep(2)
    rand =+ random.randint(100, 5000)
    bal = rand
    text = "💸 Вы заработали " + str(bal) + " ₽"
    await message.edit(text)

# Наркота
@app.on_message(filters.command("drugs", prefixes=".") & filters.me)
async def drugs(client: Client, message: Message):
    perc = 0
    result = 0
    while(perc < 100):
        try:
            text = "🍁Поиск запрещённых препаратов " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    text = "Найдено 3 кг шпекса🍪💨"
    await message.edit(str(text))
    sleep(3)
    text = "Оформляем вкид 🌿⚗️"
    await message.edit(str(text))
    sleep(5)
    result += random.randint(1, 4)

    if result == 1:
        text = "🔥😳 Вас успешно откачали, пожалуйста, больше не принимайте запрещённые препараты 😳🔥"
        await message.edit(str(text))
    if result == 2:
        text = "🥴Вы пожилой наркоман, вас не берёт одна доза, вам необходимо больше, попробуйте  ещё раз оформить вкид🥴"
        await message.edit(str(text))
    if result == 3:
        text = "😖Сегодня не ваш день, вы хоть и пожилой, но приняли слишком много. Окончательная причина смерти - передоз😖"
        await message.edit(str(text))
    if result == 4:
        text = "😌Вы оформили вкид, Вам понравилось)😌"
        await message.edit(str(text))

# Оскорбление мамки
@app.on_message(filters.command("mum" , prefixes=".") & filters.me)
async def mum(client: Client, message: Message):
    text = "🔍 Поиск твоей мамки начался..."
    await message.edit(str(text))
    sleep(3.0)
    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Ищем твою мамашу на Авито... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 3)
            sleep(0.75)
        except FloodWait as e:
            sleep(e.x)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))
    sleep(3.0)

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамаши на свалке... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            sleep(0.75)
        except FloodWait as e:
            sleep(e.x)
    text = "❌ Мамаша не найденна"
    await message.edit(str(text))

    perc = 0
    while(perc < 100):
        try:
            text = "🔍 Поиск твоей мамки в канаве... " + str(perc) + "%"
            await message.edit(str(text))
            perc += random.randint(1, 5)
            sleep(0.75)
        except FloodWait as e:
            sleep(e.x)
    text = "✅ Мамка найдена... Она в канаве"
    await message.edit(str(text))

# СПАМ
@app.on_message (filters.command("spamt" , prefixes=".") & filters.me)
async def spamt(client: Client, message: Message):
    global spam
    spam = 0
    while(spam < 1000000):
        try:
            await message.reply_text("Спам!!!")
            spam += 1
        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("spams", prefixes=".") & filters.me)
async def spams(client: Client, message: Message):
    global spam
    spam = 0
    while(spam < 1000000):
        try:
            await message.reply_text("😡")
            spam += 1
        except FloodWait as e:
            sleep(e.x)

# Стоп спам
@app.on_message (filters.command("stop" , prefixes=".") & filters.me)
async def stam(client: Client, message: Message):
        global spam
        spam = 0
        await message.reply_text("Стоп спам...")
        spam += 1000000

# AFK
async def afk_handler(client: Client, message: Message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        if message.from_user.is_bot is False:
            await message.reply_text(f"<b>Я АФК уже {afk_time}</b>\n"
                                     f"<b>Причина:</b> <i>{reason}</i>")
    except NameError:
        pass

@app.on_message (filters.command("afk" , prefixes=".") & filters.me)
async def afk(client: Client, message: Message):
    global start, end, handler, reason
    start = datetime.datetime.now().replace(microsecond=0)
    handler = client.add_handler(MessageHandler(afk_handler, (filters.private & ~filters.me)))
    if len(message.text.split()) >= 2:
        reason = message.text.split(" ", maxsplit=1)[1]
    else:
        reason = "Неизвестно"
    await message.edit(f"<b>Теперь я АФК</b>\n"
                       f"<b>Причина:</b> <i>{reason}</i>")

# No AFK
@app.on_message (filters.command("unafk" , prefixes=".") & filters.me)
async def unafk(client: Client, message: Message):
    try:
        global start, end
        end = datetime.datetime.now().replace(microsecond=0)
        afk_time = (end - start)
        await message.edit(f"<b>Я теперь не АФК.\nБыл в афк {afk_time}</b>")
        client.remove_handler(*handler)
    except NameError:
        await message.edit("<b>Я не был в АФК</b>")
        await asyncio.sleep(3)
        await message.delete()

# Автоудаление сообщений
@app.on_message(filters.command("hide", prefixes=".") & filters.me)
async def hide(client: Client, message: Message):
    orig_text = message.text.split(".hide ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"
    while(tbp != orig_text):
        try:
            joper = tbp + typing_symbol
            await message.edit(str(joper))
            sleep(0.10)
            tbp = tbp + text[0]
            text = text[1:]
            await message.edit(str(tbp))
            sleep(0.10)
        except FloodWait as e:
            sleep(e.x)

    sleep(1.25)
    await message.delete()

@app.on_message(filters.command("a9fm", prefixes=".") & filters.me)
async def stap(client: Client, message: Message):
    perc = 0
    while(perc < 25):
        try:
            await message.edit("ArturDestroyer")
            sleep(0.75)
            await message.edit("Hacker")
            sleep(0.75)
            await message.edit("A9FM")
            sleep(0.75)
            await message.edit("Anonymous")
            sleep(0.75)
            await message.edit("Python developer")
            sleep(0.75)
            await message.edit("Destroyer")
            sleep(0.75)
            await message.edit("Rox Tigers Top")
            sleep(0.75)
            await message.edit("Create UserBot_Clip")
            sleep(0.75)
            await message.edit("Vzlom Jopi")
            sleep(0.75)
            await message.edit("Hack You")
            sleep(0.75)
            await message.edit("Слит клоун")
            sleep(0.75)
            await message.edit("Пруфы, чучало")
            sleep(0.75)
            await message.edit("I am use CLIP UserBot")
            sleep(0.75)
            perc += 1
        except FloodWait as e:
            sleep(e.x)
    await message.edit("@artur_destroyer")

app.run()
