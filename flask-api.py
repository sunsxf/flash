#!/usr/bin/env python
# coding=utf-8

import redis
import json
import logging
from flask import Flask
from flask import request, jsonify, make_response

app = Flask(__name__)

log = logging.getLogger()
log.setLevel(logging.INFO)


@app.route('/')
def index():
    return "hello"


@app.route('/flash')
def check_flash():
    pkg = request.args.get('pkg')
    ver = request.args.get('ver')
    mk = request.args.get('mk')
    if 'etag' in request.headers:
        etag = request.headers['etag']
    else:
        etag = None
    if pkg is not None and ver is not None and mk is not None:
        _hs, _data = get_cache_data(pkg, ver, mk)

        if etag == _hs:
            resp = make_response('', 304)
            resp.headers['Content-Type'] = 'application/json'
            resp.headers['etag'] = _hs
            return resp
        else:
            if _data is not None:
                resp = make_response(_data, 200)
                resp.headers['Content-Type'] = 'application/json'
                resp.headers['etag'] = _hs
                return resp
            else:
                resp = make_response('', 200)
                resp.headers['Content-Type'] = 'application/json'
                resp.headers['etag'] = ''
                return resp

    return make_response('paras error', 404)


def get_cache_data(pkg, ver, mk):
    conn = redis.StrictRedis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )
    _key = "%s:%s:%s" % (pkg, ver, mk)
    _hs = conn.hget(_key, 'md5')
    _data = conn.hget(_key, 'json')
    return _hs, _data


if __name__ == '__main__':
    app.run(debug=False)
