'''
name:weiheng
获取新闻之家新闻资讯
'''
import  os
import requests
from bs4 import BeautifulSoup


#1.模拟浏览器发送请求
res = requests.get(
    url="https://www.autohome.com.cn/news/"
)
#指定响应体编码格式
res.encoding = "gbk"
#res.text获取响应体
# print(res.text)
#获取res的bytes类型数据   res.content

# 2. 获取响应结果之后，对结果进行解析,首先获取一个bs对象
bs = BeautifulSoup(res.text,"html.parser")

# 3. 找标签
container = bs.find(name="div",attrs={"id":"auto-channel-lazyload-article"})
data_list = container.find_all("li")
for tag in data_list:
    # 4. 获取标签中的文本数据
    title = tag.find("h3")
    if not title:
        continue

    summary = tag.find("p")

    # 5. 获取文章的详细内容  --->  获取标签中的属性
    a = tag.find("a")
    href = a.attrs.get("href")
    href = "https:" + href

    # 6. 下载文章图片
    img = tag.find("img")
    img_url = img.get("src") # img.get("src") == img.attrs.get("src")
    img_url = "https:" + img_url

    #获取图片名:知识点使用str.rsplit
    img_name = img_url.rsplit("/",maxsplit=1)[1]

    img_path = os.path.join("imgs",img_name)
    img_res = requests.get(
        url = img_url
    )
    with open(img_path,'wb') as f:
        f.write(img_res.content)

    print(title.text)
    print(summary.text)
    print(href)
    print(img_url)

