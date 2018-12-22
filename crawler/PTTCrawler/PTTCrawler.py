import requests
import time
import json
import os
from bs4 import BeautifulSoup



class PTTCrawler:

    ## TODO (1) : start_crawl_a2b

    PTT_URL = 'https://www.ptt.cc'

    def __init__(self,board_name):
        self.articles = []
        self.today = time.strftime("%Y/%m/%d")
        self.all = False;
        self.board_name = board_name

    # def get_article_date(self,url):
    #     res = requests.get(url=url,cookies={'over18': '1'})
    #     if res.status_code != 200:
    #         print('Invalid url:', res.url)
    #         return None
    #     else:
    #         soup = BeautifulSoup(res.text, 'html5lib')
    #         article_datetime = soup.find('div',id="main-content").find_all('div',"article-metaline")[-1].text
    #         struct_time = time.strptime(article_datetime[2:],"%a %b %d %H:%M:%S %Y")
    #         return time.strftime("%Y/%m/%d", struct_time)

    def get_web_page(self,url):
        res = requests.get(url=url,cookies={'over18': '1'})
        if res.status_code != 200:
            print('Invalid Board Name:', res.url)
            return None
        else:
            return res.text

    def get_articles(self, content):
        soup = BeautifulSoup(content, 'html5lib')
        ptt_today_date = self.today[5:].lstrip("0")   # 2018/01/01 -> 1/01

        # All articles
        divs = soup.find_all('div', 'r-ent')
        count = len(self.articles)
        
        for div in divs:
            if div.find('div', 'date').text.strip() == ptt_today_date or self.all == True :  # check same date or crawl all
                if div.find('a'):  # Link indicates that it has not been deleted
                    push = div.find('div', 'nrec').text
                    href = PTTCrawler.PTT_URL+div.find('a')['href']
                    title = div.find('a').text
                    author = div.find('div', 'author').text
                    date = div.find('div', 'date').text
                    self.articles.append({
                        'title': title,
                        'date': date,
                        'push': push,
                        'href': href,
                        'author': author
                    })

        print("以爬",len(self.articles),"篇文章")
        # Previous page link
        prev_btn = soup.find('div', 'btn-group btn-group-paging').find_all('a')[1]
        if (prev_btn.has_attr('href')):
            prev_url = PTTCrawler.PTT_URL+prev_btn['href']
        else:
            return

        # The number of articles has increased, so keep crawling.
        if count != len(self.articles):
            time.sleep(1) # Let it climb slowly
            self.get_articles(self.get_web_page(prev_url))


    def start_crawl_today(self):
        first_page = self.get_web_page(PTTCrawler.PTT_URL + '/bbs/'+self.board_name+'/index.html')
        if first_page:
            self.get_articles(first_page)
            print("今天有",len(self.articles),"篇文章")

    def start_crawl_all(self):
        first_page = self.get_web_page(PTTCrawler.PTT_URL + '/bbs/'+self.board_name+'/index.html')
        if first_page:
            self.all = True
            self.get_articles(first_page)
            print("總共有",len(self.articles),"篇文章")
            self.all = False

    def start_crawl_a2b(self,page_a,page_b):
        pass
        

    def get_the_point(self,threshold):

        for article in self.articles:
            if article['push'].isnumeric():
                if int(article['push']) > threshold:
                    print(article)
            elif article['push'] == "爆":
                    print(article)

    def dump_ptt(self):
        with open(self.board_name+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.articles, f, indent=4, ensure_ascii=False)

    def empty_articles(self):
        self.articles = []

if __name__ == '__main__':
    board_name = input("Please input board name : ")
    ptt = PTTCrawler(board_name)
    ptt.start_crawl_today()
    # ptt.start_crawl_all()
    ptt.get_the_point(99)
    ptt.dump_ptt()
    