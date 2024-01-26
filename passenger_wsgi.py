import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'herb8terapi'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'herb8terapi.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# def application(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     message = 'It works!\n'
#     version = 'Python %s\n' % sys.version.split()[0]
#     response = '\n'.join([message, version])
#     return [response.encode()]
