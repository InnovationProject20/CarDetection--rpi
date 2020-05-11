#to use this script type commands:
#	(1)python redisTest.py
#	(2)put into command line: redis-cli -h (pi ip address of redis container) -a (redis-cli password) --raw get 'imagedata#' >(desired filename)
#		ex: redis-cli -h 192.168.1.110 -a nokia123 --raw get 'imagedata0' >test0.jpg
#		so this will get the variable set in the script--replace the zeros with higher numbers to check the other set variables
from PIL import Image
import redis
from io import BytesIO

def setPicture(picture,imageCount):
	#output = StringIO.StringIO(
	output = BytesIO()
	#im = Image.open("/home/pi/carDetect/testMedia/testPictures/outTest1Fixed.jpg")
	im = Image.open(picture)
	im.save(output, format=im.format)

	r=redis.StrictRedis(host='localhost',password='nokia123')
	r.set('imagedata%d' %imageCount, output.getvalue())
	output.close()
