#!/usr/bin/env python
# coding: utf-8

import datetime
import pymongo

class Dbc(object):
    """docstring for ."""
    def __init__(self):
        self.dbName = 'wxBot'
    def start(self):
        print 'begin connect mongo db...'
        self.client = pymongo.MongoClient("localhost", 27017)
        self.db = self.client[self.dbName]
        return self.db

if __name__ == '__main__':
    rs = Dbc()
    db = rs.start()
    users = db.users
    groups = db.groups
    contacts = db.contacts
    users.insert({
        "name": "xutao",
        "age": 25
    })
    users.insert({
        "name": "duxx",
        "age": 23
    })
    groups.insert({
        "name": "前段组"
    })
    print 'insert a user'
