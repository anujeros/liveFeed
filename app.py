# -*- coding: utf-8 -*-
from flask import Flask, request
import logging, hashlib, MySQLdb
from logging.handlers import RotatingFileHandler
from datetime import datetime


app = Flask(__name__)



@app.route('/liveStatus', methods=['POST'])
def index():
    app.logger.info(str(request.data))
#    #print request.data
    content = request.get_json()
    stream = content['stream']
    status = content['status']
    stream_time = content['time']
#    #stream_time = Convert.ToDateTime(stream_time)

    if str(stream_time)[-3:] == 'UTC':
        stream_time = stream_time[:-3]
    #print stream_time
    c, conn = connection()
    c.execute("insert into live_status (stream_name, status, time) values (%s,%s,%s)", (stream, status, stream_time))
    conn.commit()
    c.close()
    conn.close()
    return 'JSON posted'


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
                           passwd = "anuj",
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

