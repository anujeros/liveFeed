# -*- coding: utf-8 -*-
from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)



@app.route('/', methods=['POST'])
def index():


    print (request.is_json)

    content = request.get_json()
    print content['status']
    print (content)
    if content:
        app.logger.info('testing logs ' + str(request.data))
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

