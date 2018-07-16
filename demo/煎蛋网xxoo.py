'''
name:weiheng
煎蛋网xxoo
'''
import os
import requests
from bs4 import BeautifulSoup


xxoo = requests.get(
    url="http://jandan.net/ooxx",
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
)

print(xxoo.text)

# bs = BeautifulSoup(xxoo.text,"html.parser")
# img_list = bs.find(name="ol",attrs={"class":"commentlist"})
# for tag in img_list.find_all(name = "li"):
#     a = tag.find("a")
#     print(a)
