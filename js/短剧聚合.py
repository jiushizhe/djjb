from base.spider import Spider
import requests
import re
import sys

sys.path.append('..')

xurl = "https://api.xingzhige.com"
headerx = {
    'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.0.0; zh-cn; Mi Note 2 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/10.1.1'
}


class Spider(Spider):
    def getName(self):
        return "短剧"

    def init(self, extend):
        pass

    def isVideoFormat(self, url):
        pass

    def manualVideoCheck(self):
        pass

    def homeContent(self, filter):  
        result = {}
        result = {"class": [
            {"type_id": "推荐榜", "type_name": "推荐榜"},
            {"type_id": "新剧", "type_name": "新剧"},
            {"type_id": "逆袭", "type_name": "逆袭"},
            {"type_id": "霸总", "type_name": "霸总"},
            {"type_id": "现代言情", "type_name": "现代言情"},
            {"type_id": "打脸虐渣", "type_name": "打脸虐渣"},
            {"type_id": "豪门恩怨", "type_name": "豪门恩怨"},
            {"type_id": "神豪", "type_name": "神豪"},
            {"type_id": "马甲", "type_name": "马甲"},
            {"type_id": "都市日常", "type_name": "都市日常"},
            {"type_id": "战神归来", "type_name": "战神归来"},
            {"type_id": "小人物", "type_name": "小人物"},
            {"type_id": "女性成长", "type_name": "女性成长"},
            {"type_id": "大女主", "type_name": "大女主"},
            {"type_id": "穿越", "type_name": "穿越"},
            {"type_id": "都市修仙", "type_name": "都市修仙"},
            {"type_id": "强者回归", "type_name": "强者回归"},
            {"type_id": "亲情", "type_name": "亲情"},
            {"type_id": "古装", "type_name": "古装"},
            {"type_id": "重生", "type_name": "重生"},
            {"type_id": "闪婚", "type_name": "闪婚"},
            {"type_id": "赘婿逆袭", "type_name": "赘婿逆袭"},
            {"type_id": "虐恋", "type_name": "虐恋"},
            {"type_id": "追妻", "type_name": "追妻"},
            {"type_id": "天下无敌", "type_name": "天下无敌"},
            {"type_id": "家庭伦理", "type_name": "家庭伦理"},
            {"type_id": "萌宝", "type_name": "萌宝"},
            {"type_id": "古风权谋", "type_name": "古风权谋"},
            {"type_id": "职场", "type_name": "职场"},
            {"type_id": "奇幻脑洞", "type_name": "奇幻脑洞"},
            {"type_id": "异能", "type_name": "异能"},
            {"type_id": "无敌神医", "type_name": "无敌神医"},
            {"type_id": "古风言情", "type_name": "古风言情"},
            {"type_id": "传承觉醒", "type_name": "传承觉醒"},
            {"type_id": "现言甜宠", "type_name": "现言甜宠"},
            {"type_id": "奇幻爱情", "type_name": "奇幻爱情"},
            {"type_id": "乡村", "type_name": "乡村"},
            {"type_id": "历史古代", "type_name": "历史古代"},
            {"type_id": "王妃", "type_name": "王妃"},
            {"type_id": "高手下山", "type_name": "高手下山"},
            {"type_id": "娱乐圈", "type_name": "娱乐圈"},
            {"type_id": "强强联合", "type_name": "强强联合"},
            {"type_id": "破镜重圆", "type_name": "破镜重圆"},
            {"type_id": "暗恋成真", "type_name": "暗恋成真"},
            {"type_id": "民国", "type_name": "民国"},
            {"type_id": "欢喜冤家", "type_name": "欢喜冤家"},
            {"type_id": "系统", "type_name": "系统"},
            {"type_id": "真假千金", "type_name": "真假千金"},
            {"type_id": "龙王", "type_name": "龙王"},
            {"type_id": "校园", "type_name": "校园"},
            {"type_id": "穿书", "type_name": "穿书"},
            {"type_id": "女帝", "type_name": "女帝"},
            {"type_id": "团宠", "type_name": "团宠"},
            {"type_id": "年代爱情", "type_name": "年代爱情"},
            {"type_id": "玄幻仙侠", "type_name": "玄幻仙侠"},
            {"type_id": "青梅竹马", "type_name": "青梅竹马"},
            {"type_id": "悬疑推理", "type_name": "悬疑推理"},
            {"type_id": "皇后", "type_name": "皇后"},
            {"type_id": "替身", "type_name": "替身"},
            {"type_id": "大叔", "type_name": "大叔"},
            {"type_id": "喜剧", "type_name": "喜剧"},
            {"type_id": "剧情", "type_name": "剧情"}],
            }

        return result

    def categoryContent(self, cid, pg, filter, ext):
        videos = []
        page = int(pg) if pg else 1
        url = f"{xurl}/API/playlet/?keyword={cid}&page={str(page)}"
        detail = requests.get(url=url, headers=headerx)
        if detail.status_code != 200:
            return {'list': []}

        detail.encoding = "utf-8"
        data = detail.json()

        for vod in data['data']:
            videos.append({
                "vod_id": f"{vod['author']}@{vod['type']}@{vod['desc']}@{vod['book_id']}",
                "vod_name": vod['title'],
                "vod_pic": vod['cover'],
                "vod_remarks": '' +  vod['type']
            })

        return {
            'list': videos,
            'page': pg,
            'pagecount': 9999,
            'limit': 90,
            'total': 999999
        }

    def detailContent(self, ids):
        did = ids[0]
        fenge = did.split("@")
        book_id = fenge[3]

        url = f"{xurl}/API/playlet/?book_id={book_id}"
        detail = requests.get(url=url, headers=headerx)
        if detail.status_code != 200:
            return {'list': []}

        data = detail.json()

        if data.get('code') != 0:
            return {'list': []}

        detail_info = data['data']['detail']
        video_list = data['data']['video_list']

        bofang_list = []
        for video in video_list:
            bofang_list.append(f"{video['title']}${video['video_id']}")
        bofang = '#'.join(bofang_list)

        vod_info = {
            "vod_id": did,
            "vod_pic": detail_info['cover'],
            "vod_actor": fenge[0],
            "vod_remarks": f"{detail_info['duration']}{detail_info.get('record_number', '')}",
            "vod_content": f'' +  detail_info['desc'],
            "vod_play_from": "短剧专线",
            "vod_play_url": bofang,
            "type_name": fenge[1]
        }

        return {'list': [vod_info]}

    def playerContent(self, flag, id, vipFlags):
        url = f"{xurl}/API/playlet/?video_id={id}&quality=1080p"
        detail = requests.get(url=url, headers=headerx)
        if detail.status_code != 200:
            return {}

        data = detail.json()
        if data.get('code') != 0:
            return {}

        play_url = data['data']['video']['url']
        return {
            "parse": 0,
            "playUrl": '',
            "url": play_url,
            "header": headerx
        }

    def searchContentPage(self, key, quick, pg):
        videos = []
        page = int(pg) if pg else 1
        url = f"{xurl}/API/playlet/?keyword={key}&page={str(page)}"
        detail = requests.get(url=url, headers=headerx)
        if detail.status_code != 200:
            return {'list': []}

        data = detail.json()
        for vod in data['data']:
            videos.append({
                "vod_id": f"{vod['author']}@{vod['type']}@{vod['desc']}@{vod['book_id']}",
                "vod_name": vod['title'],
                "vod_pic": vod['cover'],
                "vod_remarks":  '' + vod['type']
            })

        return {
            'list': videos,
            'page': pg,
            'pagecount': 9999,
            'limit': 90,
            'total': 999999
        }

    def searchContent(self, key, quick, pg="1"):
        return self.searchContentPage(key, quick, pg)












