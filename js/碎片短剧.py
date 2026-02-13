# coding=utf-8
# !/usr/bin/python

"""
"""

from Crypto.Util.Padding import unpad
from Crypto.Util.Padding import pad
from urllib.parse import unquote
from Crypto.Cipher import ARC4
from urllib.parse import quote
from base.spider import Spider
from Crypto.Cipher import AES
from datetime import datetime
from bs4 import BeautifulSoup
from base64 import b64decode
import urllib.request
import urllib.parse
import datetime
import binascii
import requests
import base64
import json
import time
import sys
import re
import os

sys.path.append('..')

xurl = "https://free-api.bighotwind.cc"

xurl1 = "https://speed.howdbm.com"

headerx = {
    "Authorization": "86d3796d-03b3-4ba1-98f4-d98c55cf298b",
    "User-Agent": "Mozilla/5.0 (Linux; Android 12; 22041211A Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Safari/537.36",
    "UUID": "707c81939662391f",
    "Host": "free-api.bighotwind.cc",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip, deflate"
          }

headers = {
    'User-Agent': 'com.android.chrome/131.0.6778.200 (Linux;Android 9) AndroidXMedia3/1.8.0'
          }

class Spider(Spider):

    def getName(self):
        return "首页"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):
        result = {"class": []}

        url = f'{xurl}/papaya/papaya-api/theater/tags'
        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        data = detail.json()

        for vod in data['data']:

            name = vod['text_val']

            id = vod['id']

            result["class"].append({"type_id": id, "type_name": "" + name})

        return result

    def homeVideoContent(self):
        pass

    def categoryContent(self, cid, pg, filter, ext):
        result = {}
        videos = []

        if pg:
            page = int(pg)
        else:
            page = 1

        url = f'{xurl}/papaya/papaya-api/videos/page?type=1&tagId={cid}&pageNum={str(page)}&pageSize=12'
        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        data = detail.json()

        for vod in data['list']:

            name = vod['title']

            itemId = vod['itemId']

            videoCode = vod['videoCode']

            content = vod.get('content')
            if not content:
                content = '未知'

            id = str(itemId) + "@" + str(videoCode) + "@" + content

            imageKey = vod['imageKey']

            imageName = vod['imageName']

            pic = f"{xurl1}/papaya/papaya-file/files/download/{imageKey}/{imageName}"

            remark = vod['tags']

            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": '' + remark
                   }
            videos.append(video)

        result = {'list': videos}
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def detailContent(self, ids):
        did = ids[0]
        result = {}
        videos = []
        xianlu = ''
        bofang = ''

        fenge = did.split("@")

        url = f'{xurl}/papaya/papaya-api/videos/info?videoCode={fenge[1]}&itemId={fenge[0]}'
        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        data = detail.json()

        content = '' + fenge[2]

        data = data['data']['episodesList']

        for vod in data:

            fileKey = vod['resolutionList'][0]['fileKey']

            fileName = vod['resolutionList'][0]['fileName']

            id = f'{xurl1}/papaya/papaya-file/files/download/{fileKey}/{fileName}'

            name = vod['episodes']

            bofang = bofang + str(name) + '$' + str(id) + '#'

        bofang = bofang[:-1]

        xianlu = '碎片专线'

        videos.append({
            "vod_id": did,
            "vod_content": content,
            "vod_play_from": xianlu,
            "vod_play_url": bofang
                     })

        result['list'] = videos
        return result

    def playerContent(self, flag, id, vipFlags):

        result = {}
        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = id
        result["header"] = headers
        return result

    def searchContentPage(self, key, quick, pg):
        result = {}
        videos = []

        if pg:
            page = int(pg)
        else:
            page = 1

        url = f'{xurl}/papaya/papaya-api/videos/page?type=5&search={key}&pageNum={str(page)}&pageSize=12'
        detail = requests.get(url=url, headers=headerx)
        detail.encoding = "utf-8"
        data = detail.json()

        for vod in data['list']:

            name = vod['title']

            itemId = vod['itemId']

            videoCode = vod['videoCode']

            content = vod.get('content')
            if not content:
                content = '未知'

            id = str(itemId) + "@" + str(videoCode) + "@" + content

            imageKey = vod['imageKey']

            imageName = vod['imageName']

            pic = f"{xurl1}/papaya/papaya-file/files/download/{imageKey}/{imageName}"

            remark = vod['tags']

            video = {
                "vod_id": id,
                "vod_name": name,
                "vod_pic": pic,
                "vod_remarks": '' + remark
                    }
            videos.append(video)

        result['list'] = videos
        result['page'] = pg
        result['pagecount'] = 9999
        result['limit'] = 90
        result['total'] = 999999
        return result

    def searchContent(self, key, quick, pg="1"):
        return self.searchContentPage(key, quick, '1')

    def localProxy(self, params):
        if params['type'] == "m3u8":
            return self.proxyM3u8(params)
        elif params['type'] == "media":
            return self.proxyMedia(params)
        elif params['type'] == "ts":
            return self.proxyTs(params)
        return None







