# -*- coding:utf-8 -*-
from lxml import etree
import requests


class TiebaSpider(object):

    def __init__(self, tieba_name, begin_page, end_page):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.base_url = "https://tieba.baidu.com"
        self.tieba_name = tieba_name
        self.begin_page = int(begin_page)
        self.end_page = int(end_page)

    def send_request(self, url, params={}):
        try:
            html = requests.get(url, params=params, headers=self.headers).content
            return html
        except Exception as e:
            print(e)

    def load_page(self, html):
        html_obj = etree.HTML(html)
        link_list = html_obj.xpath("//div[@class='t_con cleafix']/div/div/div/a/@href")

        for link in link_list:
            html = self.send_request(self.base_url + link)
            self.load_image(html)

    def load_image(self, html):
        html_obj = etree.HTML(html)
        link_list = html_obj.xpath("//img[@class='BDE_Image']/@src")

        for link in link_list:
            data = self.send_request(link)
            self.write_image(data, link[-11:])

    def write_image(self, data, filename):
        print
        "[INFO]: 正在下载%s..." % filename
        with open(u"E:\tmp" + filename, "wb") as f:
            f.write(data)

    def start_work(self):
        for page in range(self.begin_page, self.end_page + 1):
            pn = (page - 1) * 50
            keyword = {"kw": self.tieba_name, "pn": pn}
            html = self.send_request(self.base_url + "/f?", keyword)
            self.load_page(html)


if __name__ == "__main__":
    tieba_name = input("请输入需要爬取的贴吧名:")
    begin_page = input("请输入爬取的起始页:")
    end_page = input("请输入爬取的结束页:")

    Tieba = TiebaSpider(tieba_name, begin_page, end_page)
    Tieba.start_work()
