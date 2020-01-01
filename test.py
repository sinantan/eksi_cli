from bs4 import BeautifulSoup   
import requests


page_number = 1
all_entry = list()
info = list()
while True:
    try:
        url = 'https://eksisozluk.com/herkesle-iyi-gecinen-insan--4686926'+'?p=' + str(page_number)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
        response = requests.get(url,headers=headers)

        soup=BeautifulSoup(response.text,'html.parser')
        entry_div = soup.find("ul",{'id':'entry-item-list'})
        entry = entry_div.find_all("li")

        for i in entry:
            all_entry.append(i.find('div').text.strip())
            info.append(i.find('div',{'class':'info'}).text.strip())
        page_number=page_number+1

    except AttributeError:
        break

for x in range(len(all_entry)):
    print(all_entry[x],"\n")
    print(info[x],"\n")
    print(90*"-")


