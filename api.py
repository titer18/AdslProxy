# coding=utf-8
from adslproxy.api import server
from adslproxy.db import RedisClient
from adslproxy.config import *

if __name__ == '__main__':
    redis = RedisClient(host=REDIS_HOST, password=REDIS_PASSWORD)
    server(redis=redis)
