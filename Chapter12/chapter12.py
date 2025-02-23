# import webbrowser
# webbrowser.open('https://inventwithpython.com/')

# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# print(res.status_code == requests.codes.ok)
# print(len(res.text))
# print(res.text[:250])

# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# print(res.raise_for_status())

# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# try:
#     res.raise_for_status()
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
#     print(playFile.write(chunk))

# playFile.close()

# import requests, bs4

# res = requests.get('https://nostarch.com')
# res.raise_for_status()
# noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(noStarchSoup))

# exampleFile = open('example.html')
# exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
# print(type(exampleSoup))

import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# elems = exampleSoup.select('#author')
# print(type(elems)) # elems is a list of Tag objects.
# print(len(elems))
# print(type(elems[0]))
# print(str(elems[0])) # The Tag object as a string.
# print(elems[0].getText())
# print(elems[0].attrs)

# pElems = exampleSoup.select('p')
# print(str(pElems[0]))
# print(pElems[0].getText())
# print(str(pElems[1]))
# print(pElems[1].getText())
# print(str(pElems[2]))
# print(pElems[2].getText())

import bs4
soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)

