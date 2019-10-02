from urllib import request
import re

def main():
    url = r"https://www.i4.cn/wper_4_19_1_1.html"
    html = r'<img class="pngFix" src="(.*?png)" alt=""'
    
    r = request.urlopen(url)
    htmls = str(r.read(), encoding="utf-8")
    
    get_htmls = re.findall(html, htmls)
    
    for html in get_htmls:
        with open("1.png", "w") as f:
            f.write(html)
if __name__ == "__main__":
    main()
