# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import pymysql
from pymysql.err import OperationalError as OE
from zhihu_users.items import UserItem, FollowItem


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.db[UserItem.collection].create_index(
            [('url_token', pymongo.ASCENDING)])
        # self.db[FollowItem.collection].create_index(
        #     [('url_token', pymongo.ASCENDING)])

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, UserItem):
            self.db[item.collection].update(
                {'url_token': item.get('url_token')}, {'$set': item}, True)
        if isinstance(item, FollowItem):
            self.db[item.collection].update(
                {'url_token': item.get('url_token')},
                {
                    '$addToSet':
                    {
                        'relations': {"$each": item['relations']}
                    }
                }, True
            )
        return item


class MySQL_Pipeline(object):

    table_name = 'user_info'

    def __init__(self, sql_uri, user, pswd, sql_db):
        self.sql_uri = sql_uri
        self.user = user
        self.pswd = pswd
        self.sql_db = sql_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sql_uri=crawler.settings.get('SQL_URI'),
            user=crawler.settings.get('USER'),
            pswd=crawler.settings.get('PSWD'),
            sql_db=crawler.settings.get('SQL_DB')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(
            self.sql_uri, self.user, self.pswd, self.sql_db)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO user_info(name, answer_count, articles_count, follower_count) VALUES(%s, %s, %s, %s)"
        values = item.get('name'), int(item.get('answer_count')), int(item.get(
            'articles_count')), int(item.get('follower_count'))
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
        except OE:
            self.db.rollback()
        finally:
            return item
        # self.cursor.execute(sql, values)
        # self.db.commit()
        # return item
