import datetime
import os.path
import urllib.request

import requests


def save_img(img_url, dirname):
    try:
        if not os.path.exists(dirname):
            print('文件夹 Directory', dirname, '不存在，重新建立 does not exist')
            os.makedirs(dirname)
        basename = datetime.datetime.now().strftime('%Y-%m-%d') + ".jpg"
        filepath = os.path.join(dirname, basename)
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败 Failed：', e)
    except Exception as e:
        print('错误 Error：', e)
    print("保存 Save", filepath, "successfully!")
    return

def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url
    img_url = img_url.replace('1920x1080', 'UHD')
    print('img_url:', img_url)
    return img_url

def main():
    with open('SavePath.txt', 'r') as f:
        dirname = f.read()
    save_img(get_img_url(), dirname)
main()
