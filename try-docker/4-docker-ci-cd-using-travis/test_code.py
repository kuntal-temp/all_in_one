from flask import Flask
import call_my_redis
from structlog import get_logger
log = get_logger()


app = Flask(__name__)


@app.route('/')
def hello():
    call_my_redis.simple_task()
    log.info(f"all good")
    return "Hello Travis-ci"
  

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
