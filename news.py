import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import time

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"lxml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
   time.sleep(0.5)
   link = news.select_one('title')    
   print(link.text)
   print(link.next_sibling.next_sibling)
   print(news.pubDate)
   print("-"*60)
