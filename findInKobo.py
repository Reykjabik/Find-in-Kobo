#! python3

'''
The original idea was to do the requests in Amazon, but due to its bots making
scraping way more complex I decided to do the same on another book website.

AIM: Open all the product pages after searching a shopping site such as Kobo
'''

import sys, webbrowser, requests, bs4

if len(sys.argv) == 1:
    print('You need to input what you want to find in Kobo.')
else:
    print('Searching in Kobo...')

    baseURL = 'https://www.kobo.com/us/en/search?query='
    toSearch = '+'.join(sys.argv[1:])
    fullURL = baseURL + toSearch
    print(fullURL)
    req = requests.get(fullURL)

    try:
        req.raise_for_status()

        soup = bs4.BeautifulSoup(req.text, 'lxml')
        links = soup.select('a.synopsis')

        for i in range(min(7, (len(links)))):
            print(links[i].get('href'))
            webbrowser.open_new_tab(links[i].get('href'))

    except Exception as exc:
        print('There was a problem: %s' % (exc))
