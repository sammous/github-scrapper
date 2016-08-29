# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import MySQLdb
import hashlib
import pymongo

from scrapy.exceptions import DropItem
from scrapy.http import Request
from twisted.enterprise import adbapi

class GithubScrapperPipeline(object):
	def process_item(self, item, spider):
		return item

class SQLStore(object):
	def __init__(self, user, password, db, host):
		self.user = user
		self.password= password
		self.db = db
		self.host = host

	@classmethod
	def from_crawler(cls, crawler):
		return cls(
			user=crawler.settings.get('MYSQL_USER'),
			password=crawler.settings.get('MYSQL_PW'),
			db=crawler.settings.get('MYSQL_DB'),
			host=crawler.settings.get('MYSQL_HOST'),
		)

	def open_spider(self, spider):
		self.conn = MySQLdb.connect(user=self.user, passwd='root', db='github', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()
		print("\nCONNECTED TO DATABASE\n")

	def close_spider(self, spider):
		self.conn.close()

	def process_item(self, item, spider):
		try:
			var_lang = "users_" + item['language']
			query = """CREATE TABLE IF NOT EXISTS """ + var_lang + """(username VARCHAR(100), name VARCHAR(100), image VARCHAR(200), email VARCHAR(100), location VARCHAR(100), language VARCHAR(100), joined VARCHAR(100), PRIMARY KEY (username)) ENGINE = InnoDB, DEFAULT CHARSET=utf8"""
			self.cursor.execute(query)
			self.conn.commit()
			query_insert = "INSERT INTO " + var_lang + "(username, name, image, email, location, language, joined) VALUES (%s, %s, %s, %s, %s, %s, %s)"
			self.cursor.execute(query_insert,(item['username'].encode('utf-8'),item['name'].encode('utf-8'),item['image'].encode('utf-8'),item['email'].encode('utf-8'),item['location'].encode('utf-8'),item['language'],item['joined'].encode('utf-8')))
			self.conn.commit()
			print("\nROW INSERTED\n")

		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])

			return item

class MongoPipeline(object):

	collection_name = 'github_accounts'

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

	def close_spider(self, spider):
		self.client.close()

	def process_item(self, item, spider):
		self.db[self.collection_name].insert(dict(item))
		return item
