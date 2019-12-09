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
        self.process = "" #kullanıcıdan alınacak girdi

    
    def run(self):
        print("ekşi komut satırı arayüzüne hoş geldiniz.")
        self.process = input("Ekşi cli >: ")
        self.command_filter(self.process) #gelen girdiyi işlemek için parçalıyoruz.

    def command_filter(self,process):
        splitted=process.split()
        if len(splitted)>1: #eğer girdi gundem veya help ise dizi boyutu 1 olacağından buraya girmiyor.
            search_type = splitted[1]
            if splitted[0] == "ara":    
                input_to_find = "-".join([i for i in splitted if splitted.index(i) >= 2 ]) #komutları içeren dizimizin içinden aranacak başlık veya kullanıcı adını ayırıyoruz.
                self.find_user(input_to_find) if search_type=="-k" or search_type == "kullanici" else None
                self.find_subject(input_to_find) if search_type=="-b" or search_type == "baslik" else None
            if splitted[0] == "gundem":
                self.list_feed(splitted[0],splitted[1])
        elif splitted[0]=="gundem":
            self.list_feed()
        elif splitted[0]=="help" or splitted[0]=="yardim":
            print(helpText)

        


    def list_feed(self,feed="gundem",limit=50):
        print(colored(" 1- ", 'cyan') + "Lorem ipsum dolor sit amet " + colored("(252)", 'red'))
        print(colored(" 2- ", 'cyan') + "Lorem ipsum dolor sit amet " + colored("(98)", 'yellow'))
        print(colored(" 3- ", 'cyan') + "Lorem ipsum dolor sit amet " + colored("(121)", 'yellow'))
        print(colored(" 4- ", 'cyan') + "Lorem ipsum dolor sit amet " + colored("(34)", 'blue'))
        print(colored(" 5- ", 'cyan') + "Lorem ipsum dolor sit amet " + colored("(321)", 'magenta'))
        print(feed)
        print(limit)
        return feed

    def find_subject(self,subject_name):
        print(subject_name)
        return subject_name
    
    def find_user(self,username):
        print(username)
        #return username

    


if __name__=="__main__":
    eksicli=Eksicli()
    eksicli.run()
