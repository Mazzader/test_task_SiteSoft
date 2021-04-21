import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup


async def fetch(client, post):
    async with client.get(post) as resp:
        assert resp.status == 200
        return await resp.text()


async def main(post):
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, post)
        return html

habs = ['https://habr.com/ru/hub/programming/', 'https://habr.com/ru/hub/infosecurity/', 'https://habr.com/ru/hub/electronics/']

loop = asyncio.get_event_loop()
for hab in habs:
    html = loop.run_until_complete(main(hab))
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', class_='post__title_link')
    for post_link in links:
        try:
            html = loop.run_until_complete(main(post_link.get('href')))
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('title').get_text()
            link = post_link.get('href')
            date = soup.find('span', class_='post__time').get('data-time_published', None)
            author = soup.find('span', class_='user-info__nickname').get_text()
            author_link = soup.find('a', class_='post__user-info user-info').get('href')
            text = soup.find('div', class_='post__body post__body_full').get_text()
            print('Пост: {}, автор: {}, дата публикации: {}\n'
                  'Ссылка на пост: {}\n'
                  'Ссылка на автора: {}\n'.format(title, author, date, link, author_link))
            print(text)
        except UnicodeDecodeError:
            print(post_link.get('href'))