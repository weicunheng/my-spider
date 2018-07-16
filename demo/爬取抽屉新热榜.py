'''
name:weiheng
爬取抽屉新热榜
爬资讯
自动登陆并点赞
'''
import os
import requests
from bs4 import BeautifulSoup


chouti = requests.get(
    url="https://dig.chouti.com/",
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
)

bs = BeautifulSoup(chouti.text,"html.parser")

item_list = bs.find_all(name="div",attrs={"class":"item"})

for tag in item_list:
    part1 = tag.find(name="div",attrs={"class":"part1"})
    part1_a = part1.find("a")
    summary = tag.find(name="div",attrs={"class":"area-summary"})

    new_pic = tag.find(name="div",attrs={"class":"news-pic"})
    img = new_pic.find("img")
    img_url = img.attrs.get("original")
    img_url = img_url.rsplit("?",maxsplit=1)[0]
    img_url = "https:" + img_url


    # img_data = requests.get(
    #     url=img_url
    # )
    # filename = img_url.rsplit("/",maxsplit=1)[1]
    #
    # path = os.path.join("chouti",filename)
    # with open (path,"wb") as f:
    #     f.write(img_data.content)
    img_name = img_url.rsplit("/", maxsplit=1)[1]

    img_path = os.path.join("chouti", img_name)
    img_res = requests.get(
        url=img_url
    )
    with open(img_path, 'wb') as f:
        f.write(img_res.content)


    print(part1_a.text.strip())
    if not summary:
        continue
    print(summary.text)
    print("-------------------\n\n")