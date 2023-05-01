import redis
from structlog import get_logger
log = get_logger()


host = 'my-redis-cache'


def simple_task():
    try:
        r = redis.Redis(host=host, port=6379)
        r.set('key', 'value')
        log.info(f"print from redis {r.get('key')}")
    except Exception as e:
        log.debug(f"Unable to connect Redis Exception : {e}")
