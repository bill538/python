#!/usr/bin/env python

#
# William Hahn - 20200103
# Simple python flask web server for testing http calls
#

from flask import Flask, render_template, request, url_for, jsonify
app = Flask(__name__)

@app.route('/<path:path>', methods=['HEADER', 'GET', 'POST'])
def my_test_endpoint(path):
  print request.remote_addr, 'data from client:', path, request.form
  return jsonify({'ip': request.remote_addr}), 200

ip = "0.0.0.0"   # Bind to all ip interfaces
port_num = 8000      # Bind port number

if __name__ == '__main__':
    app.run(debug=True, host=ip, port=port_num)
