#!/usr/bin/python
# hello.py
#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type', 'text/html')])
#    return '<h1>Hello, web!</h1>'
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello2, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')




