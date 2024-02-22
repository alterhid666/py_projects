import json
import requests
from lxml import etree


class MySpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        self.sum_dict = {
            'list': []
        }

    def urequest(self):
        response = requests.get(url=self.url, headers=self.headers)
        return response

    def getMainHTml(self):
        for i in range(0, 51):
            self.url = f'https://gz.ziroom.com/z/z0-p{i}/'
            response = self.urequest().content.decode()
            tree = etree.HTML(response)
            div_list = tree.xpath('//div[@class="Z_list-box"]/div')
            new_div_list = div_list[:4] + div_list[5:]
            for div in new_div_list:
                title = div.xpath('.//h5/a/text()')[0]
                average = div.xpath('.//div[@class="desc"]/div[1]/text()')[0]
                info = div.xpath('.//div[@class="desc"]/div[2]/text()')[0].strip()
                dic = {
                    '房屋名称': title,
                    '房屋面积-层高': average,
                    '房屋信息': info
                }
                self.sum_dict['list'].append(dic)

    def SaveJson(self):
        with open('自如def.json', 'w', encoding='utf-8') as f:
            json.dump(self.sum_dict, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    m = MySpider()
    m.getMainHTml()
    m.SaveJson()
