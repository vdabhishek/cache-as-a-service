from flask import g
from Redis import redis
from flask import request, jsonify
from Redis.RedisHandler import Redis

@redis.before_request
def obj():
    g.handler = Redis()

@redis.route('/redis/createnamespace', methods=['POST'])
def create_redis_namespace():
    req_json = request.get_json()
    result = g.handler.create_redis_namespace(req_json)
    return jsonify({'status': result})

@redis.route('/redis/addkey', methods=['POST'])
def addkey():
    req_json = request.get_json()
    result = g.handler.addkey(req_json)
    return jsonify({'status': result})

@redis.route('/redis/deletekey', methods=['POST'])
def deletekey():
    req_json = request.get_json()
    result = g.handler.deletekey(req_json)
    return jsonify({'status': result})

@redis.route('/redis/updatekey', methods=['POST'])
def updatekey():
    req_json = request.get_json()
    result = g.handler.updatekey(req_json)
    return jsonify({'status': result})

@redis.route('/redis/getkey', methods=['GET'])
def getkey():
    req_json = request.get_json()
    result = g.handler.getkey(req_json)
    return jsonify({'status': result})
