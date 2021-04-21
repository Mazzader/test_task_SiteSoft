from celery import shared_task
from .models import Author, Post, Hab

import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


async def fetch(client, post):
    async with client.get(post) as resp:
        assert resp.status == 200
        return await resp.text()


async def main(post):
    async with aiohttp.ClientSession() as client:
        html = await fetch(client, post)
        return html


@shared_task()
def scrap_posts_from_hab():
    loop = asyncio.get_event_loop()
    habs = Hab.objects.all()
    for hab in habs:
        html = loop.run_until_complete(main(hab.link))
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a', class_='post__title_link')
        for post_link in links:
            link = get_or_none(Post, link=post_link.get('href'))
            if not link:
                try:
                    link = post_link.get('href')
                    html = loop.run_until_complete(main(post_link.get('href')))
                    soup = BeautifulSoup(html, 'html.parser')
                    title = soup.find('title').get_text()
                    date = soup.find('span', class_='post__time').get('data-time_published', None)
                    author = soup.find('span', class_='user-info__nickname').get_text()
                    author_link = soup.find('a', class_='post__user-info user-info').get('href')
                    model_author, created = Author.objects.get_or_create(nickname=author, link=author_link)
                    text = soup.find('div', class_='post__body post__body_full').get_text()
                    post = Post(title=title, pub_date=date, link=link, text=text, author=model_author)
                    post.save()
                except UnicodeDecodeError:
                    print(post_link.get('href'))
