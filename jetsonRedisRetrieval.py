import redis
from io import StringIO
from flask import send_file
import cv2
import numpy as np
import subprocess
import shlex
from shlex import quote

r=redis.StrictRedis(host='192.168.1.110',password='nokia123')
imageCount = 0

while True:
	img_bytes = r.get('imagedata%d' %imageCount)
	if (img_bytes):
		decoded = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), 1)
		cv2.imwrite("retTest%d.jpg" %imageCount, decoded)

		fileName = ('retTest%d.jpg' %imageCount)
		command = './alpr.sh {}'.format(quote(fileName))
		print(command)
		subprocess.call(shlex.split(command))
		command = ""
		imageCount +=1
	#else:
		#print("no image\r\n")
