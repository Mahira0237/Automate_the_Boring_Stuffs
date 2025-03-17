#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
#Downloads only 5 instead, iff the page is updated

import requests, os, bs4, datetime, time
url = 'https://xkcd.com'               # starting url
os.makedirs('xkcd', exist_ok=True)    # store comics in ./xkcd
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
dt = datetime.datetime(2025, 3, 17, 12, 18, 0)
i=0
for n in range(1,10):
    while datetime.datetime.now() < dt + datetime.timedelta(days=n):
        time.sleep(1)
    if soup!=bs4.BeautifulSoup(res.text, 'lxml'):
        while not url.endswith('#') and i<5:
            # Download the page.
            print('Downloading page %s...' % url)
            res = requests.get(url)
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, 'lxml')

            # Find the URL of the comic image.
            comicElem = soup.select('#comic img')
            if comicElem == []:
                print('Could not find comic image.')
            else:
                comicUrl = 'https:' + comicElem[0].get('src')
                # Download the image.
                print('Downloading image %s...' % (comicUrl))
                res = requests.get(comicUrl)
                res.raise_for_status()

                # Save the image to ./xkcd.
                imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

            # Get the Prev button's url.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'https://xkcd.com' + prevLink.get('href')
            i+=1
    else: print("The page was not updated")

print('Done.')