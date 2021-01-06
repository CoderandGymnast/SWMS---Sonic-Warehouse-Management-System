import numpy as np
import cv2
import imutils
import datetime
import base64
import re
import time
import socketio
import eventlet
import os

from pyzbar import pyzbar

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from webptools import dwebp
from django.conf import settings
from .models import Video, Section

from django.utils import timezone

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

	if request.user.is_authenticated:
		return render(
			request,
			"qr_bar_decoder/index.html",
		)
	else:
		return HttpResponseRedirect(f"{reverse('login')}?next={reverse('qr_bar_decoder:index')}")


@sio.event
def connect(sid, environment):  # "Infinite loops prevents the client connections.
	print(f"connect {sid}")


frames = []

"""
[NOTES]: I don't know why this woker does not miss any frame.
"""

out = None

"""
[NOTES]: Must follow all steps to record videos.
"""
@sio.on("START SECTION")
def process_start_section(sid, data):
	section_id = data
	global out

	print("Before exception")
	try:
		os.mkdir(f"{settings.MEDIA_ROOT}/{section_id}")
	except FileExistsError:  # Built-in exception.
		print("FileExistsError: [WinError 183] Cannot create a file when that file already exists")

	print("After exception...")
	out = cv2.VideoWriter(f"{settings.MEDIA_ROOT}/{section_id}/capture.mp4", 0x00000021, 24, (settings.VIDEO_WIDTH, settings.VIDEO_HEIGHT))  # https://stackoverflow.com/questions/49530857/python-opencv-video-format-play-in-browser
	s = Section.objects.get(pk=section_id)
	capture = Video(name=timezone.now(), url=f"{settings.DOMAIN_NAME}{settings.MEDIA_URL}{section_id}/capture.mp4", section=s)
	capture.save()



@sio.on("STOP SECTION")
def process_stop_section(sid, data):
	global frames
	for frame in frames:
		out.write(frame)
	frames = []
	out.release()


# counter = 0
@sio.on("Live Streaming Package")
def process_live_streaming_package(sid, data):
	# global counter
	# print(counter)
	# if counter == 50:
	# 	return
	# else:
	# 	counter += 1
	# sio.emit("barcode", {"data": "Sonic coder"}, room=sid)  # Socket.IO room: https://python-socketio.readthedocs.io/en/latest/server.html#rooms.

	# with open("capture.webp", "wb") as f:
	# 	f.write((base64.b64decode(re.sub("^data:image/webp;base64,", "", data))))

	img = base64.b64decode(re.sub("^data:image/webp;base64,", "", data))
	# dwebp("capture.webp", "frame.png", "-o")
	# frame = cv2.imread("frame.png")
	# out.write(frame)

	npimg = np.fromstring(img, dtype=np.uint8)

	image = imutils.resize(cv2.imdecode(npimg, 1), width=settings.VIDEO_WIDTH)
	frames.append(image)

	# image = cv2.imdecode(npimg, 1)
	# image = cv2.imread("capture.png") # Deprecated method.
	barcodes = pyzbar.decode(image, symbols=[pyzbar.ZBarSymbol.CODE128])
	print(barcodes)

	csv = open("./barcodes.csv", "w")
	found = set()
	for barcode in barcodes:

		(x, y, w, h) = barcode.rect
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

		barcode_data = barcode.data.decode("utf-8")
		# sio.emit("Barcodes", {"data": barcode_data}, room=sid)  # Socket.IO room: https://python-socketio.readthedocs.io/en/latest/server.html#rooms.
		sio.emit("Barcodes", {"data": barcode_data})

		barcode_type = barcode.type

		text = "{} ({})".format(barcode_data, barcode_type)
		cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		print("[INFO] Found {} barcode: {}".format(barcode_type, barcode_data))
		if barcode_data not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(), barcode_data))
			csv.flush()
			found.add(barcode_data)
