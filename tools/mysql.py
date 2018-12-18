# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect("localhost","test","123456","maimai")
cur = db.cursor()


def search():

    cur.execute("select * from use_info;")
    return cur


def upload():

    cur.execute("select * from use_info;")
    return cur




