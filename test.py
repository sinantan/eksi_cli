from bs4 import BeautifulSoup   
import requests

url = 'https://eksisozluk.com/basliklar/gundem'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
response = requests.get(url,headers=headers)

soup=BeautifulSoup(response.text,'html.parser')

topics = soup.find("ul",{'class':'topic-list'})

rows = topics.find_all("li")
all_topics = []

all_topics = [i.text.replace('\n','') for i in rows if i.text.find('sponsored') != 0 or i.text.find('native') != 0 or i !='' ]   #çektiğimiz verideki gereksiz reklam verilerini dizimize almıyoruz.
if 'NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});' in all_topics: all_topics.remove('NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});')



all_topics_fixed = [i for i in all_topics if i!='']

counter=1
for i in range(1,20):
    print(i,all_topics_fixed[i])
    counter+= 1