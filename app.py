# -*- coding: utf-8 -*-
from flask import Flask, request
import logging, hashlib, MySQLdb
from logging.handlers import RotatingFileHandler


app = Flask(__name__)



@app.route('/liveStatus', methods=['POST'])
def index():
    app.logger.info(str(request.data))
    print request.data
    return 'JSON posted'

    # content = request.get_json()
    # token = "something"
    # timeToken = content['time'] + token
    # print timeToken
    #
    # print (content)
    # m = hashlib.md5(timeToken)
    # hashstr = m.hexdigest()
    # print hashstr
    # if hashstr == content['digest']:
	# print 'Writing to logs'
    # else:
    #     return 'forbidden'


def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "anuj!",
                           db = "liveFeed")
    c = conn.cursor()

    return c, conn

if __name__ == "__main__":
    # initialize the log handler
    logHandler = RotatingFileHandler('info.log', maxBytes=0, backupCount=0)

    # set the log handler level
    logHandler.setLevel(logging.INFO)

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)
    app.run(debug=True, host='0.0.0.0', port=8000)

