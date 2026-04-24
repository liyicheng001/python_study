import requests
from bs4 import BeautifulSoup

# 你的章节链接
url = "https://read.zongheng.com/chapter/1520220/93787661.html?"

# 必须加UA，不然拦截
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
resp.encoding = "utf-8"
soup = BeautifulSoup(resp.text, "html.parser")

# 1. 获取章节标题
title = soup.find("title").get_text(strip=True)

# 2. 核心：抓取完整正文
content_box = soup.find("div", attrs={"class": "content"})
# 提取纯文字
content = content_box.get_text(strip=True)

# 打印
print(title)
print("="*30)
print(content)

# a_list = soup.find_all("a")
next_page = soup.find("a", string="下一章")
# print(next_page.get("href"))

# 拼接 下一章链接
next_url = "https://read.zongheng.com" + next_page.get("href")
print(next_url)

# print("\n页面所有链接：")
# for a in a_list:
#     link = a.get("href")
#     text = a.get_text(strip=True)
#     if link:
#         print(text, "→", link)