import os
import tldextract
from urllib.request import Request, urlopen
from urllib.parse import urlparse, unquote
import requests
import ssl
from bs4 import BeautifulSoup

from utils import favicon_domains, phishing_domains, \
    domains_fav_path, phishings_fav_path


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE


def get_icon_extension(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    file_extension = path.split(".")[-1]
    return file_extension


def download_favicon(url, save_path):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print('Success favicon downloading -', save_path, '\n')
    else: print('!!! ERROR favicon downloading\n')


def download_favicons_from_list(domains, download_path):
    os.makedirs(download_path, exist_ok=True)
    for i, domain in enumerate(domains, start=1):
        print(f'{i}.')
        try:
            req = Request(domain, headers=headers)
            print('Bank:', domain)
        except requests.HTTPError as e:
            print("HTTP Error:", e.response.status_code, e.response.reason)
        except requests.RequestException as e:
            print("Request Error:", str(e))
            
        html_content = urlopen(req, context=context).read()
        soup = BeautifulSoup(html_content, 'html.parser')
        link_el = soup.find("link", rel=lambda value: value and 'icon' in value.lower())
        
        if link_el:
            link_href = link_el.get('href')
            fav_url = link_href if bool(urlparse(link_href).netloc) else f'{domain}{link_href}'
            print('Fav Url:', fav_url)
            
            filename = f'{tldextract.extract(domain).registered_domain}.{get_icon_extension(fav_url)}'
            download_favicon(fav_url, os.path.join(download_path, filename))
        else:
            print("!!! favicon link element NOT FOUND\n")


print('Downloading domains favicons:')
download_favicons_from_list(favicon_domains, domains_fav_path)
print('Downloading phishing domains favicons:')
download_favicons_from_list(phishing_domains, phishings_fav_path)