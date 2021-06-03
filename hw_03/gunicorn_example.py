import time
import json

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'application/json')])
    data = {
        'time': time.asctime(),
        'url': environ['HTTP_HOST'] + environ['PATH_INFO']
    }
    return [bytes(json.dumps(data), encoding='utf-8')]
