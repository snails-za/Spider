from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = r'https://www.baidu.com'

path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'
options = Options()

options.add_argument("--headless")
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(executable_path=path, options=options)
# browser = webdriver.Chrome(executable_path=path)

browser.get(url)
time.sleep(1)

# 截屏
browser.save_screenshot("img1.png")

# result = browser.page_source
#
# print(result)

my_input = browser.find_element_by_xpath(r'//*[@id="kw"]')
my_input.send_keys("父母")
time.sleep(1)
browser.save_screenshot("img2.png")


my_click = browser.find_element_by_id('su')
my_click.click()
time.sleep(1)
browser.save_screenshot("img3.png")

# 找到指定图片点击
# my_img = browser.find_elements_by_class_name('op-img-address-hoverview op-img-address-hover')[2]
my_img = browser.find_elements_by_xpath('//div[@class="op-img-address-divide-high"]//a')[0]

my_img.click()
time.sleep(2)
# print(list(my_img))
browser.save_screenshot("img4.png")
time.sleep(2)


browser.quit()






