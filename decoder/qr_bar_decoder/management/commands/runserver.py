import sys

from django.core.management.commands.runserver import Command as RunCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from qr_bar_decoder.views import sio

def create_accountant_role():
	group, created = Group.objects.get_or_create(name="Accountant")
	permissions = ["add_list", "view_list", "change_list", "delete_list", "add_product", "view_product", "change_product", "delete_product"]
	for codename in permissions:
		permission = Permission.objects.get(codename=codename)
		group.permissions.add(permission)

def create_warehouse_manager_role():
	group, created = Group.objects.get_or_create(name="Warehouse Manager")
	permissions = ["add_section", "view_section", "change_section", "delete_section"]
	for codename in permissions:
		permission = Permission.objects.get(codename=codename)
		group.permissions.add(permission)

def create_roles():
	create_accountant_role()
	create_warehouse_manager_role()

class Command(RunCommand):
	help = 'Run the Socket.IO server'

	def handle(self, *args, **options):

		create_roles()

		try:
			print(f"Asynchronous mode '{sio.async_mode}' selected.")
			if sio.async_mode == 'threading':
				super(Command, self).handle(*args, **options)
			elif sio.async_mode == 'eventlet':
				import eventlet
				import eventlet.wsgi
				from decoder.wsgi import application
				eventlet.wsgi.server(eventlet.listen(('', 8000)), application, debug=False)
			elif sio.async_mode == 'gevent':
				from gevent import pywsgi
				from decoder.wsgi import application
				try:
					from geventwebsocket.handler import WebSocketHandler
					websocket = True
				except ImportError:
					websocket = False
				# from gevent import monkey
				# monkey.patch_all()
				if websocket:
					pywsgi.WSGIServer(
						('', 8000), application,
						handler_class=WebSocketHandler).serve_forever()
				else:
					pywsgi.WSGIServer(('', 8000), application).serve_forever()
			elif sio.async_mode == 'gevent_uwsgi':
				print('Start the application through the uwsgi server. Example:')
				print('uwsgi --http :5000 --gevent 1000 --http-websockets '
					  '--master --wsgi-file decoder/wsgi.py --callable '
					  'application')
			else:
				print('Unknown async_mode: ' + sio.async_mode)
		except KeyboardInterrupt:
			print("...")
			sys.exit(0)


"""
[NOTES]:
* Run server script: https://github.com/django/django/blob/master/django/core/management/commands/runserver.py.
*  Run server script with a specific asynchronous mode: https://github.com/miguelgrinberg/python-socketio/blob/master/examples/server/wsgi/django_example/socketio_app/management/commands/runserver.py.
* Django + Socket.IO + Eventlet = Too freaking slow.
"""

"""
[WHY MUST OVERRIDE THE DEFAULT RUNSERVER SCRIPT]:
This custom script avoids:
1. "RuntimeError: You need to use the eventlet server. See the Deployment secti
on of the documentation for more information.".
2. "greenlet.error: cannot switch to a different thread python socketio"
3. The server could not trigger an event multiple times.
"""
