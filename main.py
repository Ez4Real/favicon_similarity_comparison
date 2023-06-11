import os
import re
import io 
import tldextract
from urllib.request import Request, urlopen
from urllib import error, request
from urllib.parse import urlparse, urlunparse, unquote
import requests
import ssl
import hashlib
from PIL import Image
import imagehash
from bs4 import BeautifulSoup, Comment
from skimage.metrics import structural_similarity as ssim


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

domains_fav_path = "favicons/domains_favicons"
phishings_fav_path = "favicons/phishing_favicons"


def get_icon_extension(url):
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    file_extension = path.split(".")[-1]
    return file_extension


def is_download_favicon_url(url):
    query_params = urlparse(url).query
    return query_params or 'time' in url

def compare_favicon_hashes(fav1, fav2):
    hash1 = imagehash.average_hash(fav1)
    hash2 = imagehash.average_hash(fav2)
    return hash1 == hash2

def download_favicon(url, save_path):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print('Success favicon downloading -', save_path, '\n')
    else: print('!!! ERROR favicon downloading\n')

def compare_favicon_similarity(fav1, fav2, similarity_threshold):
    img1 = fav1.convert('RGB')
    img2 = fav2.convert('RGB')
    similarity_index = ssim(img1, img2, multichannel=True)
    return similarity_index >= similarity_threshold


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
        
        link_el = soup.find("link", rel=lambda value: value and 'icon' in value)
            
        if link_el:
            link_href = link_el.get('href')
            
            fav_url = link_href if bool(urlparse(link_href).netloc) else f'{domain}{link_href}'
            print('Fav Url:', fav_url)
            
            filename = f'{tldextract.extract(fav_url).registered_domain}.{get_icon_extension(fav_url)}'
            
            download_favicon(fav_url, os.path.join(download_path, filename))
        else:
            print("!!! favicon link element NOT FOUND\n")


with open('urls/favicon_domains.txt', 'r') as file:
    favicon_domains = file.read().splitlines()
    # print('Favicon domains:', favicon_domains)
    
with open('urls/phishing_domains.txt', 'r') as file:
    phishing_domains = file.read().splitlines()
    # print('Phishing domains:', phishing_domains)


print('Downloading domains favicons:')
download_favicons_from_list(favicon_domains, domains_fav_path)
print('Downloading phishing domains favicons:')
download_favicons_from_list(phishing_domains, phishings_fav_path)

# favicon_url = f'https://{favicon_domain}/favicon.ico'
# favicon = download_favicon(favicon_url)


# for phishing_domain in phishing_domains:
#     phishing_url = f'https://{phishing_domain}/favicon.ico'
#     phishing_favicon = download_favicon(phishing_url)
    
#     # Module 1: 
#     if compare_favicon_hashes(favicon, phishing_favicon):
#         print(f"Exact match found: {favicon_domain} and {phishing_domain}")
        
#     # Module 2:
#     similarity_threshold = 0.8
#     if compare_favicon_similarity(favicon, phishing_favicon, similarity_threshold):
#         print(f"Similar match found: {favicon_domain} and {phishing_domain}")