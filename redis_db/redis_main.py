from redis import Redis
import redis


def main():
    conn_pool = redis.ConnectionPool(host='localhost', port=6379, db=2)
    redis_cli = redis.Redis(connection_pool=conn_pool)

