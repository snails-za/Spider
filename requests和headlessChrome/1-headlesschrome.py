from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disale-gpu")

path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(executable_path=path, options=chrome_options)

# 上网
url = "http://www.baidu.com"
browser.get(url)

time.sleep(3)

browser.save_screenshot('baidu.png')


browser.quit()
