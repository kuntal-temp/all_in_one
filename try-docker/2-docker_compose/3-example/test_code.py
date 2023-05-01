from flask import Flask
import call_my_redis
import call_my_db
from structlog import get_logger
log = get_logger()


app = Flask(__name__)


@app.route('/')
def hello():
    try:
        call_my_redis.simple_task()
        call_my_db.insert_data_into_table()
        log.info(f"all good")
    except Exception as e:
        log.debug(f"test call exception = {e}")
    return "Hello World Test"
  

if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True) 
