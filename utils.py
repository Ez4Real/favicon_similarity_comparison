import os
import glob
from PIL import Image

domains_fav_path = "favicons/domains_favicons"
phishings_fav_path = "favicons/phishing_favicons"


with open('urls/favicon_domains.txt', 'r') as file:
    favicon_domains = file.read().splitlines()

with open('urls/phishing_domains.txt', 'r') as file:
    phishing_domains = file.read().splitlines()
    
original_favicons = []
for favicon_file in glob.glob(os.path.join(domains_fav_path, "*")):
    favicon = Image.open(favicon_file)
    original_favicons.append(favicon)

# Load the phishing favicons
phishing_favicons = []
for favicon_file in glob.glob(os.path.join(phishings_fav_path, "*")):
    favicon = Image.open(favicon_file)
    phishing_favicons.append(favicon)