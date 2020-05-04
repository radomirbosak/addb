# -*- coding: utf-8 -*-

import datetime

from .nineanime import NineAnime, CaptchaException


def get_now_utc():
    nowdate = datetime.datetime.utcnow()
    return nowdate.replace(tzinfo=datetime.timezone.utc)


def get_min_utc():
    mindate = datetime.datetime.min
    return mindate.replace(tzinfo=datetime.timezone.utc)


def get_max_utc():
    mindate = datetime.datetime.max
    return mindate.replace(tzinfo=datetime.timezone.utc)


def update_episode_urls(anime):
    if '9anime.to' not in anime.get('watch_url'):
        print(f'Portals other than 9anime.to are not supported.')
        return

    watch_url_parts = anime['watch_url'].split('/')
    anime_id = watch_url_parts[-2].split('.')[-1]
    episode_id = watch_url_parts[-1]

    nineanime = NineAnime('https://9anime.to')
    nineanime.waf_token = input('Enter the 9anime "waf_token" cookie: ')
    try:
        urls = nineanime.get_episode_urls(anime_id, episode_id)
    except CaptchaException:
        print('Failed captcha. Urls not updated.')
        return

    if urls:
        anime['episode_url'] = urls
