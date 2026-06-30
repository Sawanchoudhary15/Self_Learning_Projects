"""
Project: XKCD Comic Downloader
Concepts: requests + iter_content (binary download) + bs4 + Path + while loop

Downloads every XKCD comic, walking backward from the latest comic
to the very first one, using the "Prev" link on each page.
"""

import requests
import bs4
from pathlib import Path

# Create folder to save comics
Path('xkcd_comics').mkdir(exist_ok=True)

url = 'https://xkcd.com'

while True:
    print(f'Downloading page {url}')

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Find the comic image
    comic = soup.select('#comic img')

    if comic:
        src = comic[0].get('src')
        if src.startswith('//'):
            src = 'https:' + src

        imageName = Path(src).name
        print(f'Downloading image {src}')

        imageRes = requests.get(src)
        imageRes.raise_for_status()

        with open(Path('xkcd_comics') / imageName, 'wb') as f:
            for chunk in imageRes.iter_content(100000):
                f.write(chunk)

        print(f'Saved {imageName} ✅')

    # Find the Prev button
    prevLink = soup.select('a[rel="prev"]')

    if not prevLink:
        print('No more comics! Done! ✅')
        break

    url = 'https://xkcd.com' + prevLink[0].get('href')
