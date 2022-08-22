import json
import subprocess
import sys

from flask import Flask, jsonify
from Redis import redis
from Memcached import memcached

app = Flask(__name__)
app.register_blueprint(redis) 
app.register_blueprint(memcached)
