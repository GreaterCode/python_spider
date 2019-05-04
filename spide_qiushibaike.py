import urllib.request
import urllib.response
from lxml import etree
import time
import json




def get_one_page(url):
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    try:
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        result = etree.HTML(content)
        return result
    except urllib.request.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)

def parse_one_page(html):
    # author age msg  好笑 comment 点赞 评论人：内容
    author = html.xpath('//div[@class="article block untagged mb15 typs_long"]/div/a/h2/text()')
    age = html.xpath('//div[@class="article block untagged mb15 typs_long"]/div/div/text()')
    msg = html.xpath('//div[@class="article block untagged mb15 typs_long"]/a/div/span[1]/text()')
    stats_vote = html.xpath(
        '//div[@class="article block untagged mb15 typs_long"]/div/span[@class="stats-vote"]/i/text()')
    stats_commit = html.xpath(
        '//div[@class="article block untagged mb15 typs_long"]/div/span[@class="stats-comments"]/a/i/text()')
    cmt_name = html.xpath('//div[@class="article block untagged mb15 typs_long"]/a/div/span[@class="cmt-name"]/text()')
    cmt_main_text = html.xpath('//div[@class="article block untagged mb15 typs_long"]/a/div/div[@class="main-text"]/text()')
    like_num = html.xpath('//div[@class="article block untagged mb15 typs_long"]/a/div/div/div[@class="likenum"]/text()')


    return (author, age, msg, stats_vote,stats_commit,cmt_name, cmt_main_text, like_num)

def write_to_file(content):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')

def main(page):
    url = 'http://www.qiushibaike.com/hot/page/' + str(page)
    html = get_one_page(url)
    content = parse_one_page(html)
    write_to_file(content)

    # for item in parse_one_page(html):
    #     print(item)

if __name__ == '__main__':
    for i in range(1, 10):
        print('-------------------------%s------------' % (i))
        main(i)
        time.sleep(1)
