import requests
import urllib
import re
import os

'''def main():
    img_url='https://pay.xidian.edu.cn/'

    headers={
        'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
        'Accept-Encoding' :'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'Connection': 'Keep-Alive',
        'Host': 'pay.xidian.edu.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'
    }

    for i in range(10):
        print('正在下载第', i+1, '张图片')
    '''

def getHtml(url):
    page=urllib.request.urlopen(url)
    html=page.read()
    html=html.decode('utf-8')
    return html

def getImg(html):   # 爬不同网页要修改这里的str
    str = '<img id="loginform-verifycode-image" src="(.*)" alt'
    imgre=re.compile(str)
    imglist=imgre.findall(html)
    return imglist

def make_dir(folder):
    path=os.getcwd()+'\\'+folder
    if not os.path.isdir(path):
        os.makedirs(path)
    return path

def save_img(url,path,imglist,filename):
    img_url=url+imglist[0]
    # filename=path+'\\'+'test.jpg'
    img=urllib.request.urlretrieve(img_url,filename)


if __name__=='__main__':
    path=make_dir('CaptchaImg')
    url='https://pay.xidian.edu.cn/'
    for i in range(100):
        html=getHtml(url)
        imglist=getImg(html)
        filename=path+'\\'+str(i+1)+'.jpg'
        save_img(url,path,imglist,filename)

