from bs4 import BeautifulSoup   
import requests


class Scraper():

    def __init__(self):
        self.base_url="https://eksisozluk.com/"
        self.profile_url = "https://eksisozluk.com/biri/"
        self.gundem_url = "https://eksisozluk.com/basliklar/gundem"
        self.topics_fixed = list()
        self.topic_links=list()


    def feed(self,feed_type,limit):
        if feed_type=="gundem":
            url = 'https://eksisozluk.com/basliklar/gundem'
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
            response = requests.get(url,headers=headers)
            soup=BeautifulSoup(response.text,'html.parser')
            topics = soup.find("ul",{'class':'topic-list'})
            rows = topics.find_all("li")
            
            for i in rows: #başlıkların url'lerini parçaladık.
                link = i.find('a')
                self.topic_links.append(link.get('href')) if link != None else None                
            
            all_topics = [i.text.replace('\n','') for i in rows if i.text.find('sponsored') != 0 or i.text.find('native') != 0 or i !='' ]   #çektiğimiz verideki gereksiz reklam verilerini dizimize almıyoruz.
            if 'NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});' in all_topics: all_topics.remove('NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});')

            self.topics_fixed = [i for i in all_topics if i!=''] #listedeki boş alanları feed'e dahil etmiyoruz.
            
            for i in range(int(limit)): #başlıkları yazdırıyoruz
                print(i+1 ,self.topics_fixed[i])
                



    def user(self,username):
        pass

    def subject(self,row):
        #buradan print et.
        print(self.topic_links[int(row)-1])
        print(self.topics_fixed[int(row)-1])


