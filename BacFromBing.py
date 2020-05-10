import datetime
import os.path
import sys
import urllib.request

import requests
import win32api
import win32con

def save_img(img_url, dirname):
    try:
        if not os.path.exists(dirname):
            win32api.MessageBox(0, "文件夹 %s 不存在\nDirectory %s does not exist" % dirname % dirname, "失败 Error",
                                win32con.MB_ICONWARNING)
            #print('文件夹 Directory', dirname, '不存在，重新建立 does not exist')
            os.makedirs(dirname)
        basename = datetime.datetime.now().strftime('%Y-%m-%d') + ".jpg"
        filepath = os.path.join(dirname, basename)
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        win32api.MessageBox(0, "文件操作失败：%s\nFile operation failed: %s" % e % e, "失败 Error", win32con.MB_ICONWARNING)
    except Exception as e:
        win32api.MessageBox(0, "未知错误\nUnexpected error" % e % e, "失败 Error", win32con.MB_ICONWARNING)
    #print("保存至 Save to", filepath, "successfully!")
    return

def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)
    img_url = r.url
    img_url = img_url.replace('1920x1080', 'UHD')
    #print('图片地址 img_url:', img_url)
    return img_url

def main():
    Date = datetime.datetime.now().strftime('%Y-%m-%d')
    sign = False
    try:
        with open('Last_Date.txt', 'r+') as f:
            file_date = f.read()
            #print('上一次更新的时间 Last Updated:%s\n' % file_date)
            if file_date == Date:
                win32api.MessageBox(0, "已更新 Already Updated", "已更新 Already Updated", win32con.MB_OK)
                #print('已更新过，正在退出 Already Updated, exiting')
                sign = True
            else:
                f.seek(0)
                f.truncate()
                f.write(Date)
    except:
        with open('Last_Date.txt', 'w') as f:
            f.write(Date)
    if sign: sys.exit()
    #print('今日更新 Today\'s Update:%s\n' % Date)
    with open('SavePath.txt', 'r') as f:
        dirname = f.read()
    save_img(get_img_url(), dirname)

main()