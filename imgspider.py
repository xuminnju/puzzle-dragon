#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import os
from multiprocessing import Pool

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
url = 'http://puzzledragonx.com/en/monsterbook.asp'
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')
numList = soup.select('td.index > div.indexframe > a')
for i,val in enumerate(numList):
    numList[i] = re.findall('monster.asp\?n=(.*)', val.get('href'))[0]


def get_img(num):
    try:
        path = r'D://img/%s.png' % num
        if os.path.exists(path):
            print('%s号宠物图片已经下载'%num)
            return
        url = 'http://puzzledragonx.com/en/img/monster/MONS_%s.jpg'%num
        imgbyte = requests.get(url, headers=headers).content
        with open(path,'wb') as fn:
            fn.write(imgbyte)
            print('%s号宠物图片已下载好'%num)
    except:
        print('下载失败')

if __name__ == '__main__':
    #print(numList)
    pool = Pool(processes=8)
    pool.map_async(get_img, (num for num in numList))
    pool.close()
    pool.join()
