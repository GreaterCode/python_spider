# coding=utf8
import requests
import json
import time

def douban_movie(page):
    tv_list = []
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=100&page_start=' + str(page)
    r = requests.get(url, verify=False)
    content = r.content
    result = json.loads(content)
    print(result)

    tvs = result['subjects']

    for i in range(0, len(tvs)):
        tv = {}
        tv['rate'] = tvs[i]['rate']
        tv['cover'] = tvs[i]['cover']
        tv['url'] = tvs[i]['url']
        tv['title'] = tvs[i]['title']
        tv_list.append(tv)
    return tv_list


if __name__ == "__main__":
    for i in range(20):
        result = douban_movie(i)
        time.sleep(1)
        for j in result:
            print(j)

