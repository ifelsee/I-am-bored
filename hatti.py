import os
import requests
from bs4 import BeautifulSoup
import time

link = 'https://webtoonhatti.com/webtoon/one-piece/bolum-0001-maceranin-baslangici/'


url = "https://webtoonhatti.com/webtoon/one-piece/bolum-0001-maceranin-baslangici/"



def dc(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    for i in soup.find_all("div",{"class":"reading-content"}):
        dir_title = [i.contents for i in soup.find_all("h1",{"id":"chapter-heading"})][0][0]
        dir_title = dir_title.replace("                    ","")
        try:
            os.mkdir(dir_title)
            os.chdir(dir_title)
            for j in i.find_all("img",{"class":"wp-manga-chapter-img"}):
                c = 0
                if j["src"][-3:] in ["jpg","png"]:
                    w = j["src"]
                    w = w.replace(w[0],"")[7:]
                    w = "https:{}".format(w)

                    os.system(f"wget -c --read-timeout=5 --tries=0 {w}")
                    time.sleep(0.5)
                    print(w)
            os.chdir("..")
        except:pass
def cu(url):
    genesis = input()
    try:
        os.mkdir(genesis)
    except:pass
    os.chdir(genesis)
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')

    print([j.find_all("a")[0].contets for j in [i.contents[3] for i in soup.find_all("ol",{"class":"breadcrumb"})]])
    for i in soup.find_all("select",{"class":"selectpicker single-chapter-select"}):
        for j in i.find_all("option",{"class":"short"}):

            dc(j["data-redirect"])



cu(url)
