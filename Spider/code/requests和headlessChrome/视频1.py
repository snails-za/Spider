import requests
import urllib.request


def main():
    url = r'https://v7.pstatp.com/0198f9c1c9d7a882f2df39c638f90a15/5db3f92d/video/m/2206c32fbdb1ba044869fe98ac8f6616d761163576ed000048ceaabe1198/?a=1768&br=746&cr=0&cs=0&dr=0&ds=3&er=&l=20191026144315010014051093289B37CE&lr=&qs=0&rc=ajo8a247ZWU2bzMzOzczM0ApaDRoOTM2Z2Q7NzQ0PGRoZmdjZi9pM2piYWdfLS0uLS9zczZeMjE2NS8wMjAwNTA2Y2M6Yw%3D%3D'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
    r = requests.get(url=url, headers=headers)
    '''使用write保存文件需要获取链接的内容然后转换为二进制，但是urllib.request.urlretrieve只需要连接便可以保存'''
    with open("1.mp4", "wb") as fp:
        fp.write(r.content)
        print(r.content)
    # urllib.request.urlretrieve(url, "1.mp4")


if __name__ == '__main__':
    main()








