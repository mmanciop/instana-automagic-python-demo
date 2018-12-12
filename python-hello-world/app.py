#!/usr/bin/python

import os

PORT_NUMBER = int(os.environ.get('HTTP_PORT', '8080'))

print("Bootstrapping Python Hello World on port {PORT_NUMBER}")

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    return [b"Hello World"]