from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


url = r'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action='

options = Options()


path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(path)

browser.get(url)
time.sleep(3)
# browser.save_screenshot(r'douban1.png')
html = browser.page_source
with open("douban1.html", "w", encoding="utf8") as f:
    f.write(html)


"""让browser执行简单的js代码，下拉滚动条到底部"""
js = 'document.body.scrollTop=10000'
browser.execute_script(js)

time.sleep(3)
# browser.save_screenshot(r'douban2.png')
html = browser.page_source
with open("douban2.html", "w", encoding="utf8") as f:
    f.write(html)

browser.quit()


