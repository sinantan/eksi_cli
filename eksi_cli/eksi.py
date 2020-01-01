import sys
from termcolor import colored
from scraper import Scraper
import os


helpText="""
    _______  __  ___      _______. __       ______  __       __     ____    ____  __  
    |   ____||  |/  /     /       ||  |     /      ||  |     |  |    \   \  /   / /_ | 
    |  |__   |  '  /     |   (----`|  |    |  ,----'|  |     |  |     \   \/   /   | | 
    |   __|  |    <       \   \    |  |    |  |     |  |     |  |      \      /    | | 
    |  |____ |  .  \  .----)   |   |  |    |  `----.|  `----.|  |       \    /     | | 
    |_______||__|\__\ |_______/    |__|     \______||_______||__|        \__/      |_| 
                                                                                   

        Kullanım -> komut [ayar]
                Komutlar:
                gundem [başlık sayısı(opsiyonel)]
                ara [başlık veya kullanıcı flagi] [başlık veya kullanıcı adı]

                Ayarlar:
                    gundem:
                        başlık sayısı <int>
                    ara:
                        -b, -baslik
                        -k, -kullanici

                Örnek kullanım: Kullanıcı adı eksi olan kullanıcıyı ara.
                        ara -k eksi
        """

scraper=Scraper()


class Eksicli():

    def __init__(self):
        self.base_url="https://eksisozluk.com"
        self.profile_url = "https://eksisozluk.com/biri/"
        self.process = "" #kullanıcıdan alınacak girdi
        self.os_name = os.name
    
    def run(self):
        self.clear_console()
        self.process = input("ekşi cli >: ")
        self.command_filter(self.process) #gelen girdiyi işlemek için parçalıyoruz.
        

    def command_filter(self,process):
        splitted=process.split()
        if len(splitted)>1: #eğer girdi gundem veya help ise dizi boyutu 1 olacağından buraya girmiyor.
            search_type = splitted[1]
            if splitted[0] == "ara":    
                input_to_find = "-".join([i for i in splitted if splitted.index(i) >= 2 ]) #komutları içeren dizimizin içinden aranacak başlık veya kullanıcı adını bulup "-" ile ayırıyoruz.
                self.find_user(input_to_find) if search_type=="-k" or search_type == "kullanici" else None
                self.find_subject(input_to_find) if search_type=="-b" or search_type == "baslik" else None
            if splitted[0] == "gundem":
                self.list_feed(splitted[0],splitted[1])
        elif splitted[0]=="gundem":
            self.list_feed("gundem",25)
        elif splitted[0]=="help" or splitted[0]=="yardim":
            print(helpText)

        


    def list_feed(self,feed_type="gundem",limit=25):
        self.clear_console()
        scraper.feed(feed_type,limit)
        subject_number = input("Başlık numarası: ")
        self.show_subject(subject_number)

    def show_subject(self,row):
        self.clear_console()
        scraper.subject(type="selected",row=row)
        self.navigation()

    def find_subject(self,subject_name):
        self.clear_console()
        scraper.subject(type="searched",subject_name=subject_name)
        self.navigation()

    def find_user(self,username):
        self.clear_console()
        scraper.user(username)
        self.navigation()

    def navigation(self):
        choice = input("Başlıkları görüntüle (1), Ana menüye dön(2)\n>: ")
        self.list_feed() if choice=="1" else None
        self.run() if choice=="2" else None
        exit() if choice!="1" or choice!="2" else None

    def clear_console(self):
        os.system("cls") if self.os_name.find("nt") != -1 else os.system("clear") #os windows ise cmd'ye cls, unix-linux tabanlı ise clear yazıyor



if __name__=="__main__":
    eksicli=Eksicli()
    eksicli.run()
