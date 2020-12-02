"""
WSGI config for decoder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import socketio
import re

from django.core.wsgi import get_wsgi_application
from django.conf import settings

from qr_bar_decoder.views import sio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decoder.settings')

django_application = get_wsgi_application()  # This file must contain an "application" variable.

static_files = {  # Serving Static Files: https://python-socketio.readthedocs.io/en/latest/server.html#serving-static-files.
	# "/static": f"{settings.BASE_DIR}/static",
	# f"{settings.STATIC_URL}": settings.STATIC_ROOT,
	# "/static/": settings.STATIC_ROOT,
	f"{re.sub(r'/$', '', settings.STATIC_URL)}": settings.STATIC_ROOT,  # Do not need the Escaped Character "\".
}

def image_filter(name):
	return True if re.search(".svg$", name) else False

def configure_images_onto_static_files(url_pattern):
	images = filter(image_filter, os.listdir(f"{settings.STATIC_ROOT}{url_pattern}"))
	for i in images:
		static_files[f"{re.sub(r'/$', '', settings.STATIC_URL)}{url_pattern}{i}"] = {"filename": f"{settings.STATIC_ROOT}{url_pattern}{i}", "content_type": "image/svg+xml"}


configure_images_onto_static_files(settings.STATIC_IMAGES_URL_PATTERN)
configure_images_onto_static_files(settings.STATIC_GIS_IMAGES_URL_PATTERN)

application = socketio.WSGIApp(sio, django_application, static_files=static_files)
"""
[NOTES]: 
1. ".svg" content type: https://www.google.com/search?q=content_type+of+.svg&rlz=1C1CHBF_enVN892VN892&oq=content_type+of+.svg&aqs=chrome..69i57j0i22i30i457j0i22i30l6.12452j0j7&sourceid=chrome&ie=UTF-8.
"""
