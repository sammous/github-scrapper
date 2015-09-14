# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib

from scrapy.exceptions import DropItem
from scrapy.http import Request
from twisted.enterprise import adbapi

class GithubScrapperPipeline(object):
    def process_item(self, item, spider):
        return item

class SQLStore(object):
	def __init__(self):
	    self.conn = MySQLdb.connect(user='root', passwd='root', db='github', host='localhost', charset="utf8", use_unicode=True)
	    self.cursor = self.conn.cursor()
	    #log data to json file
	    print("\nCONNECTED TO DATABASE\n")


	def process_item(self, item, spider): 

	    try:
	    	#var_lang = "users_" + item['language']
	    	self.cursor.execute("""CREATE TABLE IF NOT EXISTS emails_table(username VARCHAR(100), name VARCHAR(100), image VARCHAR(200), email VARCHAR(100), location VARCHAR(100), language VARCHAR(100), joined VARCHAR(100), PRIMARY KEY (username)) ENGINE = InnoDB, DEFAULT CHARSET=utf8""")
	    	self.conn.commit()
	    	query_insert = "INSERT INTO emails_table(username, name, image, email, location, language, joined) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
	        self.cursor.execute(query_insert,(item['username'].encode('utf-8'),item['name'].encode('utf-8'),item['image'].encode('utf-8'),item['email'].encode('utf-8'),item['location'].encode('utf-8'),item['language'],item['joined'].encode('utf-8')))
	        self.conn.commit()
	        print("\nROW INSERTED\n")

	    except MySQLdb.Error, e:
	        print "Error %d: %s" % (e.args[0], e.args[1])

	        return item