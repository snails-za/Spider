from selenium import webdriver
import time

while True:
    url = r'https://www.baidu.com'

    path = r'C:\Users\wangju\Desktop\Spider\chromedriver_win32\chromedriver.exe'

    browser = webdriver.Chrome(executable_path=path)

    browser.get(url)
    time.sleep(3)

    # 截屏
    # browser.save_screenshot("img1.png")

    # result = browser.page_source
    #
    # print(result)

    my_input = browser.find_element_by_xpath(r'//*[@id="kw"]')
    my_input.send_keys("你好")
    browser.save_screenshot("img2.jpg")


    my_click = browser.find_element_by_id('su')
    my_click.click()
    time.sleep(3)
    browser.save_screenshot("img3.png")

    browser.quit()







