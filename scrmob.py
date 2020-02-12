user 

agent = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}

==========================================================

now we can add this dictionary while requesting to change the user agent


request = requests.get("http://127.0.0.1:1000",headers=agent) #see the additional argument named headers
===================================================================================



import requests
from bs4 import BeautifulSoup


if __name__=="__main__":
    req = requests.get("https://www.yellowpages.com.au/search/listings?clue=Restaurants&locationClue=&lat=&lon=&selectedViewMode=list")
    #req.content = html page source and we are using the html parser
    soup = BeautifulSoup(req.content,"html.parser")
    print(soup)
    =======================================================
    
parser

import requests
from bs4 import BeautifulSoup


if __name__=="__main__":
    agent = {'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Mobile/7B405'}
    req = requests.get("https://www.yellowpages.com.au/search/listings?clue=Restaurants&locationClue=&lat=&lon=&selectedViewMode=list",headers=agent)
  
    soup = BeautifulSoup(req.content,"html.parser")
    for i in soup.find_all("a",class_="listing-name"):
        print(i.text)
