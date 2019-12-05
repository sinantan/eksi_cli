import sys
from termcolor import colored
from scraper import Scraper


""" for i in range(1,11):
    number = str(i) + "."
    print(colored(number, 'green') + "Lorem ipsum dolor sit amet")
 """

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

class Eksicli():

    def __init__(self):
        self.base_url="https://eksisozluk.com"
        self.profile_url = "https://eksisozluk.com/biri/"

    def run(self):
        if len(sys.argv)>1:
            if sys.argv[1]=="gundem":
                if len(sys.argv)>2:
                    print(self.list_feed(sys.argv[2]))
                else:
                    print(self.list_feed())
            elif sys.argv[1]=="ara":
                if sys.argv[2]=="-b" or sys.argv[2]=="-baslik":
                    print(self.find_subject(sys.argv[3]))
                elif sys.argv[2]=="-k" or sys.argv[2]=="-kullanici":
                    print(self.find_user(sys.argv[3]))
                else:
                    print("Geçersiz komut.")
            elif sys.argv[1]=="help" or sys.argv[1]=="yardim":
                print(helpText)
            else:
                print("Geçersiz komut.")
        else:
            print("Lütfen parametre giriniz.")

    def list_feed(self,feed="popular",limit=50):
        return feed

    def find_subject(self,subject_name):
        return subject_name
    
    def find_user(self,username):
        return username

    


if __name__=="__main__":
    eksicli=Eksicli()
    eksicli.run()
