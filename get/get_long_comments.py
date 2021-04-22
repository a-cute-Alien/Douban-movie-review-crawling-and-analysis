import requests
from bs4 import BeautifulSoup
import json
import re

proxy = {
    'http': '113.121.79.133:9999',
}


def getLcomment(mvid, filename):
    start = 0
    while True:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36 ',
        }
        try:
            url = 'https://movie.douban.com/subject/' + str(mvid) + '/reviews?start=' + str(start)
            start += 20
            req = requests.get(url, headers=header, proxies=proxy)
            soup = BeautifulSoup(req.text, 'html.parser')
            node = soup.select('.short-content')
            for va in node:
                id = va.select('a')[0]['id'].replace('toggle-', '').replace('-copy', '')
                # print(id)
                ajaxUrl = 'https://movie.douban.com/j/review/' + str(id) + '/full'
                # print(ajaxUrl)
                response = requests.get(url=ajaxUrl, headers=header)
                data = json.loads(response.text)
                comment = re.sub('<.*?>', "", data['html'])
                with open(filename, "a", encoding='utf-8') as f:  # 打开文件
                    f.write(comment)
        except Exception as e:  # 有异常退出
            print(e)
            break


if __name__ == '__main__':
    mvid = input('电影的id为：')
    getLcomment(mvid)
