import redis
from io import StringIO
from flask import send_file
import cv2
import numpy as np

r=redis.StrictRedis(host='192.168.1.110',password='nokia123')

img_bytes = r.get('imagedata0')
decoded = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), 1)
cv2.imwrite("retTest0.jpg",decoded)
