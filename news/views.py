from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.
import requests
from bs4 import BeautifulSoup

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footer links

toi_news = []

for th in toi_headings:
	toi_news.append(th.text)



#Getting news from Crypto yahoo search

ht_r = requests.get("https://sg.news.search.yahoo.com/search;_ylt=AwrXgCOhldBgdwkAACgo4gt.;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=crpyto&fr=uh3_news_web_gs&fr2=piv-web&b=11&pz=10&xargs=0")
ht_soup = BeautifulSoup(ht_r.content, 'html.parser')
ht_headings = ht_soup.findAll('h4')
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)

def index(req):

	return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})