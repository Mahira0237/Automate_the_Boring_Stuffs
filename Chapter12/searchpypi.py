#! python3
# searchpypi.py  - Opens several search results.
#Does not work

import requests, sys, webbrowser, bs4
print('Searching...')    # display text while downloading the search result page
res = requests.get('https://www.britannica.com/animal/cat')
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'lxml')
# Open a browser tab for each result.
linkElems = soup.select('#content a')
print(linkElems)

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://www.britannica.com/animal/cat' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)

# <a class="w-100 link-gray-900" href="/animal/cat#ref374452">Identifying cats</a>