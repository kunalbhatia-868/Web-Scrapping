from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

for article in soup.find_all('article'):
    heading = article.header.h2.text
    entry_content = article.find('div', class_='entry-content')
    text = entry_content.p.text
    yt_link = None
    try:
        video_url = entry_content.span.iframe["src"]
        vid_id = video_url.split('/')[4].split('?')[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except AttributeError:
        pass

    print(heading)
    print(text)
    print(yt_link)
    print()
    csv_writer.writerow([heading, text, yt_link])

csv_file.close()
