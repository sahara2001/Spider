# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PornnetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cideo_title = scrapy.Field()
    image_url = scrapy.Field()
    video_duration = scrapy.Field()
    quality_480p = scrapy.Field()
    video_views = scrapy.Field()
    video_rating = scrapy.Field()
    link_url = scrapy.Field()
    
