from flask import Flask
from flask import render_template
from flask import jsonify

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import picamera

app = Flask(__name__)
camera = picamera.PiCamera()

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/captureImage', methods=['GET'])
def captureImage():
    camera.capture('./static/test.jpg')
    return 'DONE'

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(80)  # serving on port 5000
IOLoop.instance().start()
