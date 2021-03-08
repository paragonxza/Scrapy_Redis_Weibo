# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    collection = 'users'
    #个人微博基本信息
    id = Field()
    name = Field()
    avatar = Field()
    cover = Field()
    gender = Field()
    description = Field()
    #粉丝数目
    fans_count = Field()
    #关注人数目
    follows_count = Field()
    #微博数目
    weibos_count = Field()
    #微博认证信息
    verified = Field()
    verified_reason = Field()
    verified_type = Field()
    #粉丝条目
    fans = Field()
    #爬取时间
    crawled_at = Field()


class UserRelationItem(Item):
    collection = 'users'
    id = Field()
    follows = Field()
    fans = Field()