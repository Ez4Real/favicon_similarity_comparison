# Favicon Similarity Comparison
Data Schema Generator

## Overview
This project aims to compare the similarity between favicons of different websites. It provides a way to download favicons from a list of domains and then compares them using hash comparison and image similarity metrics.

## Technology Stack
- Python 3.10.0

## Features
- Download favicons from a list of domains.
- Compare the similarity between original and phishing favicons.
- Display the similarity index between pairs of favicons.
- Filter and identify similar favicons based on a similarity threshold.

## Project Setup
1. Clone the repository
2. Create a virtual environment (optional but recommended): ```python -m venv env```
3. Activate the virtual environment:
    ```source env/bin/activate```  # Linux/Mac
    ```env\Scripts\activate```     # Windows
4. Install the required packages: ```pip install -r requirements.txt```
5. Prepare the input files (**urls** folder):
    Fill in the files favicon_domains.txt and phishing_domains.txt with the list of domains whose favicon you want to compare, with each domain on a new line.
6. Download favicons from **urls** folder using ```prepare_favicons.py``` module.
7. Adjust the similarity threshold in ```image_similarity.py``` (**line 18**) to fine-tune the similarity comparison. The default threshold is set to 0.8, but you can modify it based on your requirements.

## Usage
- Now run ```hash_comparison.py``` to compare hashes and ```image_similarity.py``` to compare the similarity of favicons.

## Results 
- The script will display the similarity index between pairs of original and phishing favicons. If the similarity index exceeds the threshold, it will indicate a potential similarity.
- Additionally, the downloaded favicons will be stored in the ```favicons/domains_favicons``` and ```favicons/phishing_favicons``` directories.