from celery import shared_task
from datetime import datetime
from structlog import get_logger
log = get_logger()


@shared_task
def sample_task():
    log.info(f"datetime now = {datetime.now()}")
    for i in range(0, 5):
        log.info(f"Task running step = {i}")
