import urllib.request
import os.path
import time
from datetime import datetime
import cv2
import glob
import os
import shutil
import base64
import requests
import json

#if not os.path.exists(date):
    #os.mkdir(date)   # 画像保存用のフォルダ作製

## BASIC認証関係
def setup_basic_auth(base_uri, user, password):
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(
            realm=None,
            uri=base_uri,
            user=user,
            passwd=password)
    auth_handler = urllib.request.HTTPDigestAuthHandler(password_mgr)
    opener = urllib.request.build_opener(auth_handler)
    urllib.request.install_opener(opener)

## ファイルに保存
def download_file(url):
    filename = date+os.path.basename(url)
    print('Downloading ... {0} as {1}'.format(url, filename))
    #urllib.request.urlretrieve(url, filename)
    img = urllib.request.urlopen(url)
    print(img.info()['Content-Type'])
    #print(img.read())
    with open('a.jpg','wb') as f:
        f.write(img.read())
    time.sleep(capture_interval)

## 取得した画像を鯖に投げる
def pic_post(fromPath, toPath, capture_interval):
    img = urllib.request.urlopen(fromPath)
    print(img.info()['Content-Type'])
    base64_img = base64.b64encode(img.read())
    base64_img = base64_img.decode()
    data = {'img':base64_img}
    r = requests.post(toPath,headers = {'Content-Type':'application/json',},data =json.dumps(data))
    print(r.text)
    time.sleep(capture_interval)


if __name__ == '__main__':
    ## 送信先Addr
    toPath = 'http://127.0.0.1:8000/photo/in/'

    ## 取得するAddr, 認証ID
    #fromPath = 'https://www.ne.senshu-u.ac.jp/~proj2021-19/img/logo.png'
    fromPath = 'http://192.168.0.70:13626/snapshot.jpg'
    username = 'admin'
    pw = 'ne191114'

    ## 画像取得間隔（秒）,  繰り返し回数
    capture_interval, count = 5, 3
    ## 画像取得
    for b in range(count):
        date = datetime.now().strftime("%Y%m%d_%H%M%S")
        setup_basic_auth(fromPath, username, pw)
        pic_post(fromPath,toPath, capture_interval)
