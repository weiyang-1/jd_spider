# -*- coding: utf-8 -*-

from pymongo import MongoClient
from configs.config import logger


class Mongo_db():

    def __init__(self):
        self.conn = MongoClient(host="127.0.0.1", port=27017)    #connect to mongodb
        self.db = self.conn.maimai  # 使用脉脉数据库
        self.collection = self.db.jobs

    def search(self, query=None, type=1, count=10):
        """查询的结果是dict生成器"""

        if type==1:
            # 只查找一个
            doc = self.collection.find_one()
            if not doc:
                return None
            logger.info(f"search success！")
            yield doc
        else:
            array = self.collection.find(query).limit(count)
            if not array:
                return None
            logger.info(f"search success！")
            for doc in array:
                yield doc


    def insert(self, text=dict):
        """插入数据"""
        try:
            self.collection.insert(text)
            logger.info(f"insert success！")
        except Exception as e:
            logger.error(e)
            logger.error("insert failed")

    def update(self, query=dict, new_text=dict, multi=False):
        """更新插入的数据以及选择更新的次数"""
        if not multi:
            try:
                self.collection.update(query,{"$set":new_text})
                logger.info(f"upload success！")
            except Exception as e:
                logger.error(e)
                logger.error("upload failed")
        else:
            try:
                self.collection.update(query, {"$set": new_text}, multi=True)
                logger.info(f"upload success！")
            except Exception as e:
                logger.error(e)
                logger.error("upload failed")


    def delete(self, query=dict, multi=False):
        """删除不需要的数据"""
        if multi:
            try:
                self.collection.remove(query)
                logger.info(f"delete succees！")
            except Exception as e:
                logger.error(e)
                logger.error("delete failed!")
        else:
            try:
                res = self.collection.find_one_and_delete(query)
                logger.info(f"delete succees！")
            except Exception as e:
                res = None
                logger.error(e)
                logger.error("delete failed!")
            if not res:
                logger.error("delete failed!")



if __name__ == '__main__':
    m = Mongo_db()
    for i in range(10):
        m.insert({"key":i})
    m.update({},{"count":1},multi=True)
    # m.delete({}, multi=True)
    res = m.search(type=2)
    for i in res:
        print(i)
