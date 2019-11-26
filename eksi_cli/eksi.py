import sys
from termcolor import colored
import cli


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


         Komutlar:
         komut [ayarlar]
         gundem [başlık sayısı(opsiyonel)]
         ara [başlık veya kullanıcı flagi] [başlık veya kullanıcı adı]

         Ayarlar:
            gundem:
                başlık sayısı <int>
            ara:
                -b, -baslik
                -k, -kullanici

        Örnek: Kullanıcı adı eksi olan kullanıcıyı ara.
                ara -k eksi
        """)
        #command = input(">:")
        if sys.argv[1]=="gundem":
            print(self.list_subject(sys.argv[2]))
        
    def input(self):
        pass

    def list_subject(self,feed="popular",limit=50):
        return feed

    def get_subject(self,queue,page=1):
        pass
    
    def get_user(self,username):
        pass

    


if __name__=="__main__":
    eksicli=Eksicli()
    eksicli.run()
