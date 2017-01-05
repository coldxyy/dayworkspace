# -*- coding: utf-8 -*-
import urllib
import json

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

if __name__ == '__main__':

    key = '638533d6f5803fa7d49e8a391961cbbc'
    api = 'http://www.tuling123.com/openapi/api?key=' + key + '&info='
    while True:
        info = raw_input('我: ')
        request = api + info

        response = getHtml(request)
        dic_json = json.loads(response)
        print '机器人: '.decode('utf-8') + dic_json['text']
        page = urllib.urlopen("http://api.map.baidu.com/location/ip?ak=KrmZxHHwvLnl4Xfyt0FMMVzgGLaaxU2j&ip="+"211.69.16.1"+"&coor=bd09ll")
        html = page.read()
        abc=json.loads(html)
        print abc["address"]
        print abc["content"]["address"]
        print abc["content"]["address_detail"]["city"]
        print abc["content"]["address_detail"]["city_code"]
        print abc["content"]["address_detail"]["district"]
        print abc["content"]["address_detail"]["province"]
        print abc["content"]["point"]["x"]
        print abc["content"]["point"]["y"]
