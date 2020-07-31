from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time
from urllib.parse import quote
from GetComment import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

titles = []
urls = []

def get_titles_urls(page):

    browser.get('http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2019-0-1-%s' % page)
    html = browser.page_source
    soup = BeautifulSoup(html,'lxml')
    items = soup.find_all(class_ = 'name')

    for item in items:
        titles.append(item.a.attrs['title'])
        urls.append(item.a.attrs['href'])


def main():
    for i in range(1,11):
        print('正在爬取第%s页' % i)
        get_titles_urls(i)
        time.sleep(2)
    print(titles)
    print("题目爬取完成，正在写入文件")
    with open('titles.txt', 'w') as f:
        for title in titles:
            f.write(str(title) + '\n')
    #修改i的值可以控制从第几本书开始爬取。
    i = 132
    for k in range(i,len(urls)):
        print("正在爬取%s的评论，是第%s本书" % (titles[k],str(k+1)))
        getComment(titles[k],re.sub("\D","",urls[k]),1,10)
        #i = i+1
if __name__ == '__main__':
    #get_comment('http://product.dangdang.com/23761145.html')
    main()


