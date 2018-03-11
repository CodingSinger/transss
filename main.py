import getopt
import hashlib
import random
import time

import pygame as pygame
import requests
import sys

s = requests.Session()
m = hashlib.md5()
appId = "4d38fd17135b64d0"
secret = "CjeJMW4p2wPlqmuXMm19snjvPy9vd2XG"
rs ={"mode":"1","level":"3"}



class Dict:
    def __init__(self):
        self.url = "http://openapi.youdao.com/api"

    def translate(self, text, fl="EN", to="zh-CHS"):
        salt = str(int(time.time() * 1000) + random.randint(0, 9))

        sign = appId + text + salt + secret
        m.update(sign.encode("utf8"))
        sign = m.hexdigest()

        data = {
            "q": text,
            "from": fl,
            "to": to,
            "appKey": appId,
            "salt": salt,
            "sign": sign
        }
        resp = s.get(self.url, params=data)
        return resp.json()


if __name__ == '__main__':

    def parseArgs(args):

        if len(sys.argv) < 2:
            print("usage: ttt <word> -m <mode> -l <levelNum>")
            sys.exit()
        rs["word"] = sys.argv[1]

        try:
            opts, args = getopt.getopt(args[2:], "hm:l::", ["mode=", "level="])
        except getopt.GetoptError:
            print("ttt -m <mode> -l <levelNum>")
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print("ttt <word> -m <mode> -l <levelNum>")
                sys.exit()
            elif opt in ("-m", "--mode"):
                rs["mode"] = arg
            elif opt in ("-l", "--level"):
                rs["level"] = arg



    parseArgs(sys.argv)
    dic = Dict()

    if rs["mode"] != "1":

        resp = dic.translate(rs["word"], fl="zh-CHS", to="EN")
    else:
        resp = dic.translate(rs["word"])

    if resp["errorCode"] != "0":
        print("出错,错误码" + resp['errorCode'])
    else:

        s = print("翻译结果==========\n")

        print(resp["translation"][0]+"\n")
        for i in resp["basic"]["explains"]:
            print(i)


        # 使用get方法获得url的内容
        # response = requests.get(resp["tSpeakUrl"])
        # # 由于response的格式为requests.models.Response无法直接print，用text转成str格式
        # # 若用于下载图片、视频、音频等多媒体格式,应用response.content转成二进制的bytes格式
        # html = response.content
        # # 打印网页
        # print(html)
        #
        # import urllib.request
        #
        # res = urllib.request.urlopen(resp["speakUrl"])
        #
        # data = res.read()
        # with open("1.mp3", "wb") as file:
        #     file.write(data)
        #
        # # f = open("/Users/zhengzechao/Downloads/1.wav", "rb")
        # # data = f.read()
        # # html = response.read()
        # # import pygame
        # #
        # pygame.init()
        # pygame.mixer.init()
        # #
        # track = pygame.mixer.music.load("1.mp3")  # 载入音乐文件
        # pygame.mixer.music.play(loops=5)  # 开始播放
        #
        # time.sleep(3)
