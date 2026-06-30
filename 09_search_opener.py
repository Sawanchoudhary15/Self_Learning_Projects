"""
Project: Search Opener (Google Search Opener — adapted to DuckDuckGo)
Concepts: sys.argv + requests + headers + bs4 CSS selectors + webbrowser

NOTE: Google and Bing both blocked scraping (403 errors), so we
switched to DuckDuckGo which is scraping-friendly.

Run from terminal like:
    python 09_search_opener.py cute cats
"""

import sys
import requests
import bs4
import webbrowser

searchWords = ' '.join(sys.argv[1:])
print(f'Searching for: {searchWords}')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

res = requests.get(
    f'https://duckduckgo.com/html/?q={searchWords}',
    headers=headers
)
res.raise_for_status()
print('Page downloaded! ✅')

soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElements = soup.select('a.result__a')
print(f'Found {len(linkElements)} links!')

# Open first 5 in browser tabs!
for link in linkElements[:5]:
    url = link.get('href')
    if url.startswith('//'):
        url = 'https:' + url
    print(f'Opening: {url}')
    webbrowser.open(url)

print('Done! ✅')
