from flask import Blueprint

redis = Blueprint('redis', __name__)

import Redis.RedisRoutes
