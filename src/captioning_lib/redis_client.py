import redis


class RedisClient:
    def __init__(self):
        self.client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

    def rpush(self, queue_name, data):
        return self.client.rpush(queue_name, data)

    def lpop(self, queue_name):
        return self.client.lpop(queue_name)