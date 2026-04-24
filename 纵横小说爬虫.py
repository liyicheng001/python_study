# 引入所需的库
import requests
from bs4 import BeautifulSoup

# 全局变量：初始章节 + 下一章链接
start_url = input("请输入小说第一章的链接：")
next_url = start_url

if not start_url:
    print("❌ 请输入有效的链接！")
    exit()

# 保存的txt文件名
save_file = "all.txt"

# 爬取小说
def fetch_novel(url):
    global next_url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, "html.parser")

    # 标题
    title = soup.find("div", attrs={'class': 'title_txtbox'}).get_text()
    print("\n" + "="*50)
    print(title)
    print("="*50)

    # 正文 不strip，保留换行排版
    content_box = soup.find("div", attrs={"class": "content"})
    content = content_box.get_text(separator="\n")
    print(content)

    # ========== 自动保存到本地TXT ==========
    with open(save_file, "a", encoding="utf-8") as f:
        f.write("="*30 + "\n")
        f.write(title + "\n\n")
        f.write(content + "\n\n")
    print(f"\n💾 本章已自动保存到：{save_file}")

    # 获取下一章链接
    next_tag = soup.find("a", string=lambda t: t and "下一章" in t)
    if next_tag:
        next_url = "https://read.zongheng.com" + next_tag.get("href")
        print("✅ 下一章已就绪")
    else:
        next_url = None
        print("\n❌ 已经是最后一章了")

# 命令控制
def zhiling():
    global next_url
    case = input("\n请输入命令（开始看小说 / 下一章 / exit）：")
    
    if case.lower() == 'exit':
        print("退出程序。")
        return False
    
    elif case == '开始看小说':
        fetch_novel(start_url)
    
    elif case == '下一章':
        if next_url:
            fetch_novel(next_url)
        else:
            print("❌ 没有下一章了！")
    
    return True



# 主循环
print("📖 小说阅读器已启动！")
while True:
    if not zhiling():
        break