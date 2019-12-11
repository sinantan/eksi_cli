from bs4 import BeautifulSoup   
import requests


class Scraper():

    def __init__(self):
        self.base_url="https://eksisozluk.com"
        self.profile_url = "https://eksisozluk.com/biri/"
        self.gundem_url = "https://eksisozluk.com/basliklar/gundem"

    def feed(self,feed_type,limit):
        if feed_type=="gundem":
            response = requests.get(self.gundem_url)
            soup = BeautifulSoup(response.text,"html.parser")

            topics = soup.find_all('ul',{'class':'topic-list'})
            for topic in topics:
                print(topic.text)



    def user(self,username):
        pass

    def subject(self,subject_name):
        pass


