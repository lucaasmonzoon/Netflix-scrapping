from os import times
from bs4 import BeautifulSoup
import requests
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
r=requests.get("https://www.netflix.com/ar-en/title/70143836")
soup=BeautifulSoup(r.text,features="html.parser")

name=soup.find("h1",{"class":"title-title"}).text
Year=soup.find("span",{"class":"title-info-metadata-item item-year"}).text
MaturityNumber=soup.find("span",{"class":"maturity-number"}).text
synopsis=soup.find("div",{"class":"title-info-synopsis"}).text
awards=soup.find("div",{"class":"hook-text"}).text
print(name)
print(synopsis)
print(Year)
print(MaturityNumber)
print(awards)
temporadas=soup.find("select",{"id":"undefined-select"})
año_estrenos=soup.find_all("div",{"class":"season-release-year"})
synopsis_temp=soup.find_all("p",{"class":"season-synopsis"})
episodios=soup.find_all("div",{"class":"season"})


for temporada in temporadas:
    s=0
    i=temporadas.index(temporada)
    eps=episodios[i].find_all("h3",{"class":"episode-title"})
    synopsis_ep=episodios[i].find_all("p",{"class":"epsiode-synopsis"})
    duraciones=episodios[i].find_all("span",{"class":"episode-runtime"})
    print(temporada.text)
    print(año_estrenos[i].text)
    print(synopsis_temp[i].text)
    
    
    for ep in eps:

        print(ep.text)
        print(duraciones[s].text)
        print(synopsis_ep[s].text)
        s=s+1
    
    


