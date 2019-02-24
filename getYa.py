#!/usr/bin/python
# -*- coding: utf-8 -*-
# import random
import random

import requests
import time
from bs4 import BeautifulSoup
import re

pattern = re.compile(u"(.*香港.*)|(.*澳门.*)|(.*台湾.*)|(.*韩国.*)|(.*泰国.*)|(.*越南.*)|(.*首尔.*)|(.*曼谷.*)|(.*胡志明.*)")

def getAll(starturl, pageCount):
    text_lst = []
    proxy = get_proxy().decode("utf-8")
    for x in range(1, pageCount):
        url = starturl+str(x)
        req = requests.get(url)
        if req.status_code != 200:
            return text_lst
        soup = BeautifulSoup(req.content, "html.parser")
        t1 = soup.find_all(class_="s xst")
        for tips in t1:
            url_2 = "http://bbs.ieltschn.com/" + tips["href"]
            #req2 = requests.get(url_2, proxies={"http": "http://{}".format(proxy)})
            req2 = requests.get(url_2)
            if req2.status_code != 200:
                return text_lst
            soup2 = BeautifulSoup(req2.content, "html.parser")
            contents = soup2.find_all(class_="t_fsz")
            for c in contents:
                dd = [cc for cc in c.text.split("\n") if len(cc) > 5] #
                for tt in dd:
                    if pattern.search(tt):
                        result = "http://bbs.ieltschn.com/" + tips["href"] + "," + tt.replace(",", "")+"\n"
                        text_lst.append(result)
            time.sleep(random.random()*10)
    return text_lst


def get_proxy():
    return requests.get("http://118.24.79.211:9184/get/").content

def delete_proxy(proxy):
    requests.get("http://118.24.79.211:9184/delete/?proxy={}".format(proxy))

if __name__ =="__main__":
    # dd = get_proxy().decode("utf-8")
    # lst1 = getAll(u"http://bbs.ieltschn.com/forum.php?mod=forumdisplay&fid=53&page=", 29)
    # print("lst1: has ", len(lst1))
    # print(lst1)
    '''
    lst2 = getAll(u"http://bbs.ieltschn.com/forum.php?mod=forumdisplay&fid=99&page=", 13)
    print("lst2: has ", len(lst2))
    print(lst2)
    lst3 = getAll(u"http://bbs.ieltschn.com/forum.php?mod=forumdisplay&fid=91&page=", 13)
    print("lst3: has ", len(lst3))
    print(lst3)
    lst4 = getAll(u"http://bbs.ieltschn.com/forum.php?mod=forumdisplay&fid=89&page=", 3)
    print("lst4: has ", len(lst4))
    print(lst4)
    '''
    lst5 = getAll(u"http://bbs.ieltschn.com/forum.php?mod=forumdisplay&fid=80&page=", 9)
    print("lst5: has ", len(lst5))
    print(lst5)

    # if None is not lst2:
    #     lst1.extend(lst2)
    # if None is not lst3:
    #     lst1.extend(lst3)
    # if None is not lst4:
    #     lst1.extend(lst4)
    # if None is not lst5:
    #     lst1.extend(lst5)

    with open("getYa.txt", "w") as w:
        w.writelines(lst2)


