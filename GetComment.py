import urllib.request
import urllib.parse
import json
import jsonpath
import re
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
import time

def handle_request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request

def get_response(request):
    response = urllib.request.urlopen(request)
    return response

def parse_json(json_text):
    obj = json.loads(json_text)
    ret = jsonpath.jsonpath(obj, '$.data.list.html')
    return ret[0]

def getComment(title,id,start,end):
    #herfs = []
    title = title.replace("/"," ")
    for i in range(start,end+1):
        comments = []
        time.sleep(2)

        url = "http://product.dangdang.com/index.php?r=comment%%2Flist&productId=%s&" \
              "categoryPath=01.41.05.03.00.00&mainProductId=%s&mediumId=0&pageIndex=%s&" \
              "sortType=2&filterType=1&isSystem=1&tagId=0&tagFilterCount=0&template=publish" % (id, id, i)

        json_text = get_response(handle_request(url=url)).read().decode('gbk')
        ret = parse_json(json_text)
        soup = BeautifulSoup(ret)
        print("正在爬取第%s页的评论" % i)
        itmes = soup.find_all(class_ = 'describe_detail')
        if(itmes is None):
            print("被挡了，正在尝试重新链接")
            time.sleep(30)
            i = i-1
            continue
        for item in itmes:
            print(item)
            #herfs.append(item.a.attrs['href'])
            if(item.a is not None):
                comments.append(item.a.string)
        print(comments)
        file_name = title + '.txt'
        with open(file_name, 'a') as f:
            for comment in comments:
                f.write(str(comment) + '\n')
    #print(herfs)
    #print(len(herfs))
    #print(len(comments))
    #


if __name__ == '__main__':
    getComment('人间失格（日本小说家太宰治的自传体小说，李现推荐）',23761145,1,10)