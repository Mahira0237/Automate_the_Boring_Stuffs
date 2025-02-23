#! python3
# searchpypi.py  - Opens several search results.
#Does not work

import requests, sys, webbrowser, bs4
print('Searching...')    # display text while downloading the search result page
res = requests.get("https://www.google.com/search?sca_esv=a6857920e5190db0&sxsrf=AHTn8zrU09r5qndyFzkEL2Pv0VNKTjpl2g:1740293229838&q=automate+the+boring+stuff&spell=1&sa=X&ved=2ahUKEwj41ZO-mdmLAxWs-TgGHTlkDuoQBSgAegQIBxAB&biw=967&bih=850&dpr=1.13" + " ".join(sys.argv[1:]))
print(res.raise_for_status())

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# Open a browser tab for each result.
linkElems = soup.select('jjYud')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)