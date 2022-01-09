from bs4 import BeautifulSoup
import lxml
import requests

# ------------------------------- part 1：课程讲解 -------------------------------
# with open("website.html") as file:
#     contents = file.read()

# parser 解析 html 文件
# 方法1：直接使用 html.parser 解析，但是有可能在某些网站不能使用
# soup = BeautifulSoup(contents, "html.parser")
# 方法2：使用 lxml 库来解析
# soup = BeautifulSoup(contents, "lxml")

# 解析后就可以单独使用 html 标签里的内容了
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)  # 返回第一个 a 标签

# 获取 html 中所有的 a 标签，返回一个数组
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())  # 获取 a 标签的内容
#     print(tag.get("href"))  # 获取 a 标签的链接值

# 获取 html 中 id=name 的 h1 标签
# heading = soup.find(name="h1", id="name")
# print(heading)

# 获取 html 中 class=heading 的 h3 标签
# 注意：因为 class 是 python 中的保留关键字，所以这里使用的是 class_
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.name)

# 复杂的 selector，用法和 css 的 selector 类似
# company_url = soup.select_one(selector="p a")  # 获取包裹在 p 标签中的 a 标签
# print(company_url)
# name = soup.select_one(selector="#name")  # 获取 id=name 的标签
# print(name)
# headings = soup.select(".heading")  # 获取所有 class=heading 的标签
# print(headings)

# ------------------------------- part 2：爬一个真实的网页 -------------------------------
# 目的：获取下面这个新闻网页中，得票数最多的 新闻名 和 链接
# 网址为：https://news.ycombinator.com/

response = requests.get(url="https://news.ycombinator.com/")  # 获取页面的 html
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")  # 获取所有标题
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_num = max(article_upvotes)
largest_index = article_upvotes.index(largest_num)

print(article_texts[largest_index])
print(article_links[largest_index])
print(article_upvotes[largest_index])
