from flask import Blueprint

memcached = Blueprint('memcached', __name__)

import Memcached.MemcachedRoutes
