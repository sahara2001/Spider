# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from pymongo import IndexModel, ASCENDING
from items import PornnetItem

class PornnetMondoDBPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient("localhost", 27017)
        db = client["PornHub"] #table name?
        self.PhRes = db["PhRes"]
        idx = IndexModel([('link_url','ASCENDING')],unique=True) #set up table index (primary_key?)
        self.PhRes.create_indexes([idx])

        self.errors = 0

    def process_item(self, item, spider):
        print('MongoDBItem', item)
        
        #determine type and store into MongoDB

        if isinstance(item, PornnetItem):
            print('PornnetItem True')
            try:
                self.PhRes.update_one({'link_url': item['link_url']}, {'$set': dict(item)}, upsert=True)
            except Exception:
                self.errors += 1

                print('Error: %d-st error!' % self.errors)
            
        return item

            
