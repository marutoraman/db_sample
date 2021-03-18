# -*- coding: utf-8 -*-
from datetime import datetime as dt
from pytz import timezone
import socket
import ssl
import urllib.error
import urllib.request
import os
import datetime

def now_timestamp():
    return dt.now().strftime("%Y-%m-%d %H:%M:%S")

def list_to_bool(l:list):
    bool_list=[]
    for item in l:
        bool_list.append(False if item == "0" or item == 0 else True)
    
    return bool_list

def create_proxy_dict(id,password,host,port,proxy_flg=True):
    if proxy_flg:
        proxy_url=f"http://{id}:{password}@{host}:{port}"
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        return {}

def get_global_ip():
    return socket.gethostbyname(socket.gethostname())

def down_load_img(url, path):
    ''' URLを指定し、画像を指定のフォルダに配置する '''
    # ファイル名の作成
    values = url.split('/')
    filename = values[-1]
    filename = filename.split('.')[0]
    # ファイルパスの指定
    if os.name == 'posix':
        path = '{}/{}.jpg'.format(path, filename)
    elif os.name == 'nt':
        path = '{}\\{}.jpg'.format(path, filename)

    # 画像URLからダウンロード
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def get_date_delta(delta):
    now = datetime.datetime.now()
    return now+datetime.timedelta(days=int(delta))
