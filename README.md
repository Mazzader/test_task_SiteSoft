# Тестовое задание для SiteSoft
Быстрый старт проекта:

```
Клонируем проект
docker-compose build
docker-compose up
```

### Описание скрипта парсинга хабра
Скрипт парсинга хабра лежит в файле tasks.py и работает через celery как запланированная задача каждые 10 минут, внутри скрипта присутсвуют ассинхронные запросы через aiohttp к хабру.


### Структура моделей в б.д.
Author:
```
nickname = Charfield(max_length=300, unique=True) # никнейм пользователя
link = Charfield(max_length=1000, unique=True) # ссылка на аккаунт пользователя
```

Hab:
```
title = Charfield(max_length=300) # название хаба
link = Charfield(max_length=1000, unique=True) # Ссылка на хаб на гитхабе
```

Post:
```
title = CharField(max_length=300) # заголовок поста
pub_date = DateTimeField() # Дата публикации
link = CharField(max_length=1000, unique=True) # Ссылка на пост
text = TextField() # Текст поста
author = ForeignKey(to=Author) # Свзавыем пост и автора, при удалении заполниям нулями
hab = ForeignKey(to=Hab) # Связываем пост и хаб, при удалении удалем все посты связанные с хабом
```

### Стек:
```
Django
RabbitMQ
Celery
aiohttp
asyncio
postgresql
docker
nginx
gunicorn
```
