import sys
from termcolor import colored
import scraper


""" for i in range(1,11):
    number = str(i) + "."
    print(colored(number, 'green') + "Lorem ipsum dolor sit amet")
 """



class Eksicli():

    def __init__(self):
        self.base_url="https://eksisozluk.com"
        self.profile_url = "https://eksisozluk.com/biri/"

    def run(self):
        #print("deneme" + self.list_subject())
        print("""
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
        """)
        #command = input(">:")
        if sys.argv[1]=="gundem":
            print(self.find_subject(sys.argv[2]))
        

    def list_feed(self,feed="popular",limit=50):
        return feed

    def find_subject(self,subject_name):
        pass
    
    def find_user(self,username):
        pass

    


if __name__=="__main__":
    eksicli=Eksicli()
    eksicli.run()
