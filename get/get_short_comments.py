import requests
from bs4 import BeautifulSoup


def getScomment(mvid, filename):
    start = 0
    while True:
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }

        try:
            url = 'https://movie.douban.com/subject/' + str(mvid) + '/comments?start=' + str(
                start) + '&limit=20&sort=new_score&status=P&comments_only=1'
            start += 20
            req = requests.get(url, headers=header)
            res = req.json()
            res = res['html']
            soup = BeautifulSoup(res, 'html.parser')
            node = soup.select('.comment-item')
            for va in node:
                comment = va.select_one('.short').text
                with open(filename, 'a', encoding='utf-8') as f:
                    f.write(comment + '\n')
                print(comment)
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    mvid = input('电影的id为：')
    getScomment(mvid)
