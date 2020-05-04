import sys
import requests
from bs4 import BeautifulSoup


class CaptchaException(Exception):
    pass


class NineAnime:

    def __init__(self, portal_url):
        self.portal_url = portal_url  # https://9anime.to
        self._servers_api = portal_url + '/ajax/film/servers?id='

        self.user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0"
        self.waf_token = ''


    def get_episode_urls(self, anime_id, provider_hint=''):
        """
        Args:
            provider_hint (str): Episode id of one of the episodes. Determines which server to choose.
        """
        url = self._servers_api + anime_id
        cookies = {'waf_token': self.waf_token}
        headers = {"User-Agent": self.user_agent}

        r = requests.get(url, headers=headers, cookies=cookies)

        if '<title>WAF</title>' in r.text:
            raise CaptchaException("Set the 'waf_token' attribute to the 'waf_token' cookie value and try again.")

        soup = BeautifulSoup(r.json()['html'], features='html5lib')
        srvs = soup.find_all('div', class_='server')

        # use that provider/server which contains the provider_hint
        for server in srvs:
            hrefs = [self.portal_url + a.attrs['href'] for a in server.find_all('a')]
            contains_hint = any(provider_hint in href for href in hrefs)
            if contains_hint or not provider_hint:
                return hrefs
        return None


if __name__ == '__main__':
    anime = NineAnime('https://9anime.to')

    anime.waf_token = input('waf_token: ')

    urls = anime.get_episode_urls('6q67', '022plxr')
    [print(url) for url in urls]
