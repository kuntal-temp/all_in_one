import redis
import os
from structlog import get_logger
log = get_logger()


# Pickup Host and Port from Docker environment
REDIS_HOST = os.getenv('REDIS_HOST', None)
REDIS_PORT = os.getenv('REDIS_PORT', None)


def simple_task():
    try:
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
        r.set('key', 'value')
        log.info(f"print from redis {r.get('key')}")
    except Exception as e:
        log.debug(f"Unable to connect Redis Exception : {e}")
