from bs4 import BeautifulSoup


# 生成对象
soup = BeautifulSoup(open('../soup_text.html'), 'lxml')

# 根据标签进行查找
# print(soup)
# print(type(soup))
# print(soup.a)
# 获取属性
# print(soup.a['href'])
# print(soup.a["title"])
# print(soup.a['target'])
# print(soup.a.attrs)

# 获取内容
# print(soup.a.text)
# print(soup.a.string)
# print(soup.a.get_text())
# print(soup.div.text)
# print(soup.div.string)
# print(soup.div.get_text())

# find()
# print(soup.find("a", title='qin'))
# print(soup.find('a', alt='qi'))
# print(soup.find('a', class_='du'))
# print(soup.find('a', id='feng'))

# print(soup.find('a', class_='du'))

# find_all
# div = soup.find('div', class_='tang')
# print(div.find('a', class_='du'))
# print(soup.find_all('a'))
# print(len(soup.find_all('a')))

# div = soup.find("div", class_='tang')
# print(div.find_all('a'))
# print(div.find_all(['a', 'b']))
# print(div.find_all('a', limit=2))


# print(soup.select('.tang > ul > li > #feng'))
div = soup.find("div", class_='tang')
print(div.select('.du'))
