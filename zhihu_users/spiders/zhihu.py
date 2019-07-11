# -*- coding: utf-8 -*-
import json
import time
import re

import requests
import scrapy
from scrapy import Request
from zhihu_users.items import UserItem, FollowItem

pattern = "(.*?)members/(.*?)/follow(.*?)"


class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'zhou-bo-lei'

    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    fans_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    fans_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    # url = "https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=0&limit=20"

    def start_requests(self):

        yield Request(self.user_url.format(user=self.start_user, include=self.user_query), callback=self.parse_user)

        yield Request(self.follows_url.format(user=self.start_user, include=self.follows_query, offset=0, limit=20), callback=self.parse_follows, dont_filter=True)

        yield Request(self.follows_url.format(user=self.start_user, include=self.fans_query, offset=0, limit=20), callback=self.parse_fans, dont_filter=True)

    def parse_user(self, response):
        # print(response.text)
        result = json.loads(response.text)
        item = UserItem()

        # user_url = result.get('url')
        # followers_url = user_url + '/followers'
        # following_url = user_url + '/following'

        for field in item.fields:
            if field in result.keys():
                item[field] = result.get(field)
        yield item

        yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, offset=0, limit=20), callback=self.parse_follows)
        yield Request(self.fans_url.format(user=result.get('url_token'), include=self.fans_query, offset=0, limit=20), callback=self.parse_fans)
        # yield Request(self.follows_url.format(user=result.get('url_token'), include=self.follows_query, offset=0, limit=20), callback=self.parse_relation_list)
        # yield Request(self.fans_url.format(user=result.get('url_token'), include=self.follows_query, offset=0, limit=20), callback=self.parse_relation_list)

    def parse_follows(self, response):
        # print(response.text)
        results = json.loads(response.text)
        item = FollowItem()

        if 'data' in results.keys():
            data = results.get('data')

            item['url_token'] = re.search(pattern, results.get(
                'paging').get('previous'), re.S).group(2)
            item['relations'] = [data[i].get('name')
                                 for i in range(min(20, len(data)))]
            yield item

            for result in results.get('data'):
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_follows)

    def parse_fans(self, response):
        results = json.loads(response.text)
        item = FollowItem()

        if 'data' in results.keys():
            data = results.get('data')

            item['url_token'] = re.search(pattern, results.get(
                'paging').get('previous'), re.S).group(2)
            item['relations'] = [data[i].get('name')
                                 for i in range(min(20, len(data)))]
            yield item

            for result in data:
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query), callback=self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page, callback=self.parse_fans)

    # def crackImageCode(self):
    #     browser = Chrome()
    #     unhuman_url = "https://www.zhihu.com/account/unhuman?type=unhuman&message=%E7%B3%BB%E7%BB%9F%E6%A3%80%E6%B5%8B%E5%88%B0%E6%82%A8%E7%9A%84%E5%B8%90%E5%8F%B7%E6%88%96IP%E5%AD%98%E5%9C%A8%E5%BC%82%E5%B8%B8%E6%B5%81%E9%87%8F%EF%BC%8C%E8%AF%B7%E8%BF%9B%E8%A1%8C%E9%AA%8C%E8%AF%81%E7%94%A8%E4%BA%8E%E7%A1%AE%E8%AE%A4%E8%BF%99%E4%BA%9B%E8%AF%B7%E6%B1%82%E4%B8%8D%E6%98%AF%E8%87%AA%E5%8A%A8%E7%A8%8B%E5%BA%8F%E5%8F%91%E5%87%BA%E7%9A%84&need_login=true"
    #     browser.get(unhuman_url)

    # def parse_relation_list(self, response):
    #     results = json.loads(response.text)
    #     item = FollowItem()

    #     if 'data' in results.keys():
    #         data = results.get('data')
    #         for i in range(20):
    #             info = data.get(str(i))
    #             item['url_token'] = info.get('url_token')

    #     yield item
