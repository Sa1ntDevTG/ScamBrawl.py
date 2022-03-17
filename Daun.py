#Слито в @smoke_software
# -*- coding: utf-8 -*-
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.handlers import MessageHandler
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
import logging, time, math, random
from datetime import datetime
import json
from urllib.request import urlopen

times = 300 # Время сна (в секундах)
Chat = "" # Юзернейм скам чата
Token = "5174417833:AAHPXQn-dD7JWJ07jjE4wstx03s1EpQ-Mq0"
Admin = "5006820524" # Айди (юзерка) для админа, для логов
app = Client("my_session", api_id=2860432, api_hash="2fde6ca0f8ae7bb58844457a239c7214") # При запуске заходим на любой настоящий аккаунт!

start = 666
with app:
    while start != 0: # Бесконечный цикл
        iii = app.get_history(Chat)  # Чтение чата
        app.delete_messages(Chat, iii[0].message_id)  # Удаление последнего сообщения в чате (прошлого конкурса)
        url = f"https://api.telegram.org/bot{Token}/getChatMembersCount?chat_id=@{Chat}" # Получение кол-ва участников
        with urlopen(url) as f:
            resp = json.load(f)
        sub = resp['result']
        subscribers = int(sub)
        global acccu
        acccu = 0
        acccu += random.randint(1, 10)
        needsubes = int(subscribers / 100)
        needsubs = int((math.ceil(needsubes) + 1) * 100)
        # Отправка фото с фейк конкурсом
        app.send_photo(Chat, f"https://t.me/smoke_software", f"Конкурс на данный аккаунт\nКто больше всех добавит до {needsubs} участников, Получит этот акк\nГруппа @{Chat}\nНа данный момент: {subscribers} участников")
        # Логи админу
        app.send_message(Admin, f"Бравл\nНужно {needsubs}\nЕсть {subscribers}")
        # Сон
        time.sleep(times)
        
app.run()
#Слито в @smoke_software