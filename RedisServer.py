#!/usr/bin/env python
# coding: utf-8
import redis

class RedisServer(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 6379
        self.db = 0
        self.client = redis.StrictRedis(host = self.host, port = self.port, db = self.db)
    def start(self):
        print '[*] RedisServer...启动'
        return self.client
if __name__ == '__main__':
    rs = RedisServer()
    r = rs.start()
    r.set('test22','value22')
