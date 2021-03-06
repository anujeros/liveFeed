# -*- coding: utf-8 -*-
from flask import Flask, request
import logging, hashlib
from logging.handlers import RotatingFileHandler


app = Flask(__name__)



@app.route('/liveStatus', methods=['POST'])
def index():

    content = request.get_json()
    token = "something"
    timeToken = content['time'] + token
    print timeToken

    print (content)
    m = hashlib.md5(timeToken)
    hashstr = m.hexdigest()
    print hashstr
    if hashstr == content['digest']:
	print 'Writing to logs'
        app.logger.info(str(request.data))
        return 'JSON posted'
    else:
        return 'forbidden'

# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == "__main__":
    # initialize the log handler
    logHandler = RotatingFileHandler('info.log', maxBytes=1000, backupCount=1)

    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)
    app.run(debug=True)

