from flask import g
from Memcached import memcached
from flask import request, jsonify
from Memcached.MemcachedHandler import Memcached

@memcached.before_request
def obj():
    g.handler = Memcached()

@memcached.route('/memcached/createamespace', methods=['POST'])
def create_memcached_namespace():
    req_json = request.get_json()
    result = g.handler.create_memcached_namespace(req_json)
    return jsonify({'status': result})

@memcached.route('/memcached/addkey', methods=['POST'])
def addkey():
    req_json = request.get_json()
    result = g.handler.addkey(req_json)
    return jsonify({'status': result})

@memcached.route('/memcached/deletekey', methods=['POST'])
def deletekey():
    req_json = request.get_json()
    result = g.handler.deletekey(req_json)
    return jsonify({'status': result})

@memcached.route('/memcached/updatekey', methods=['POST'])
def updatekey():
    req_json = request.get_json()
    result = g.handler.updatekey(req_json)
    return jsonify({'status': result})

@memcached.route('/memcached/getkey', methods=['POST'])
def getkey():
    req_json = request.get_json()
    result = g.handler.getkey(req_json)
    return jsonify({'status': result})
