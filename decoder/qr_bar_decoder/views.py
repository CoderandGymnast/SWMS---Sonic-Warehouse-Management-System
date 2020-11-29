import numpy as np
import cv2
import imutils
import datetime
import base64
import re
import time
import socketio
import eventlet

from pyzbar import pyzbar

from django.shortcuts import render
from django.conf import settings

# from engineio.payload import Payload

# Payload.max_decode_packets = 500

# from django.shortcuts import render

# [LIVE STREAMING]: Async mode & thread.

# Set async_mode to 'threading', 'eventlet', 'gevent' or 'gevent_uwsgi' to
# force a mode else, the best mode is selected automatically from what's
# installed - Reference: https://github.com/miguelgrinberg/python-socketio/blob/master/examples/server/wsgi/django_example/socketio_app/views.py.
async_mode = None  # Asynchronous mode.

sio = socketio.Server(async_mode=async_mode)
thread = None

def index(request):
	return render(
		request,
		"qr_bar_decoder/index.html",
	)


@sio.event
def connect(sid, environment):  # "Infinite loops prevents the client connections.
	print(f"connect {sid}")

# counter = 0
@sio.on("Live Streaming Package")
def process_live_streaming_package(sid, data):

	# sio.emit("barcode", {"data": "Sonic coder"}, room=sid)  # Socket.IO room: https://python-socketio.readthedocs.io/en/latest/server.html#rooms.

	with open("capture.webp", "wb") as f:
		f.write((base64.b64decode(re.sub("^data:image/webp;base64,", "", data))))

	img = base64.b64decode(re.sub("^data:image/webp;base64,", "", data))
	npimg = np.fromstring(img, dtype=np.uint8)
	image = imutils.resize(cv2.imdecode(npimg, 1), width=settings.FRAME_MAX_WIDTH)
	# image = cv2.imdecode(npimg, 1)
	# image = cv2.imread("capture.png") # Deprecated method.
	barcodes = pyzbar.decode(image)
	print(barcodes)

	# return 0

	# global counter
	# counter += 1
	# print(counter)

	csv = open("./barcodes.csv", "w")
	found = set()
	for barcode in barcodes:

		(x, y, w, h) = barcode.rect
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

		barcode_data = barcode.data.decode("utf-8")
		sio.emit("Barcodes", {"data": barcode_data}, room=sid)  # Socket.IO room: https://python-socketio.readthedocs.io/en/latest/server.html#rooms.
		barcode_type = barcode.type

		text = "{} ({})".format(barcode_data, barcode_type)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data))
		if barcode_data not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(), barcode_data))
			csv.flush()
			found.add(barcode_data)

def profile(request):
	return render(
		request,
		"registration/profile.html"
	)
