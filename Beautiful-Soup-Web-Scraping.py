import requests as r
from bs4 import BeautifulSoup as soup

webpages=[]
#you can change the number in range to reflect the number of total pages in a text
#this loop loops through all the pages in the subdirectory
for i in range(1,10):
    root_url = 'https://zh.wikisource.org/wiki/[insert url subdirectory]'+ str(i)
    webpages.append(root_url)
headers = {'User-Agent': 'Mozilla/5.0'}

#this loop downloads the plain text, finds the titles of the texts, and names the downloaded file with the titles
with r.Session() as s:

    for item in webpages:

        data = r.get(item, headers=headers)
        data.encoding = 'utf-8'
        page_soup = soup(data.text, 'html5lib')
        headlines = page_soup.find_all(class_='mw-headline')

        with open(r'sample.txt', 'a', encoding='utf-8') as file:

            for headline in headlines:
                headline_text = headline.get_text()
                paras = page_soup.find_all('p')
                text = ''
                for para in paras:
                    p_text = para.get_text()
                    text+= p_text
                text = headline_text + text
                file.write(text)

