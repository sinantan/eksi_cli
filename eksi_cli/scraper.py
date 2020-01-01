from bs4 import BeautifulSoup   
import requests
from termcolor import colored
import os

class Scraper():

    def __init__(self):
        self.base_url="https://eksisozluk.com/"
        self.profile_url = "https://eksisozluk.com/biri/"
        self.gundem_url = "https://eksisozluk.com/basliklar/gundem"
        self.topics_fixed = list()
        self.topic_links=list()


    def request_eksisozluk(self,url):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        response = requests.get(url,headers=headers)
        soup=BeautifulSoup(response.text,'html.parser')
        return soup

    def feed(self,feed_type,limit):
        if feed_type=="gundem":
            url = 'https://eksisozluk.com/basliklar/gundem'
            topics = self.request_eksisozluk(url).find("ul",{'class':'topic-list'})
            rows = topics.find_all("li")
            
            for i in rows: #başlıkların url'lerini parçaladık.
                link = i.find('a')
                self.topic_links.append(link.get('href')) if link != None else None                
            
            all_topics = [i.text.replace('\n','') for i in rows if i.text.find('sponsored') != 0 or i.text.find('native') != 0 or i !='' ]   #çektiğimiz verideki gereksiz reklam verilerini dizimize almıyoruz.
            if 'NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});' in all_topics: all_topics.remove('NativeAdPub.push({ target: \'10924\' , id: \'nativespot-unit-10924\'});')

            self.topics_fixed = [i for i in all_topics if i!=''] #listedeki boş alanları feed'e dahil etmiyoruz.
            
            for i in range(int(limit)): #başlıkları yazdırıyoruz
                print(colored(str(i+1),'cyan'), self.topics_fixed[i], colored(self.topics_fixed[i].split()[-1],'green'))
                



    def user(self,username):
        url = self.profile_url + username
        data = self.request_eksisozluk(url)
        user_badge_div = data.find('ul',{'id':'user-badges'})
        user_badges = [i.text for i in user_badge_div.find_all('li')]
        print(*user_badges,sep=" - ")

    def subject(self,type="selected",row=None, subject_name=None):
        if row!=None: #eğer row verildiyse başlık listeden seçilmiş demektir.
            page_number = 1
            separator = 110 * "-"
            while True:
                try:
                    url = self.base_url + self.topic_links[int(row)-1].replace('?a=popular','')+'?p=' + str(page_number)
                    entry_div = self.request_eksisozluk(url).find("ul",{'id':'entry-item-list'})
                    entry = entry_div.find_all("li")

                    for i in entry:
                        print(i.find('div').text.strip())
                        print(colored(i.find('div',{'class':'info'}).text.strip(),'cyan'))
                        print(colored(separator,'green'))
                    page_number=page_number+1

                except AttributeError:
                    break
                
        elif(subject_name!=None): #subject name verildiyse başlık aranmış demektir.
            url = self.base_url + subject_name + "--0"
            entry_div = self.request_eksisozluk(url).find("ul",{'id':'entry-item-list'})
            
            if entry_div == None: 
                print(colored('HATA!','red')," Böyle bir başlık yok.")
            else:
                full_page = str(self.request_eksisozluk(url))
                econtent_id = full_page.index("'econtentid': ")
                url_suffix = full_page[econtent_id+15:econtent_id+20:1] #html sayfasının içinde aranacak başlığın url son ekini alıyoruz
                page_number = 1
                separator = 110 * "-"
                while True:
                    try:
                        new_url = url.replace('--0','--' +url_suffix) +'?p=' + str(page_number)
                        entry_div = self.request_eksisozluk(new_url).find("ul",{'id':'entry-item-list'})
                        entry = entry_div.find_all("li")

                        for i in entry:
                            print(i.find('div').text.strip())
                            print(colored(i.find('div',{'class':'info'}).text.strip(),'cyan'))
                            print(colored(separator,'green'))
                        page_number=page_number+1

                    except AttributeError:
                        break




        


