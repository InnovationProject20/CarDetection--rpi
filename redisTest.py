#to use this script type commands:
#	(1)python redisTest.py
#	(2)redis-cli -h (this ip address) -a (this password) redis-cli --raw get 'imagedata' >(desired filename)

from PIL import Image
import redis
import StringIO

def setPicture(picture,imageCount):
	output = StringIO.StringIO()
	#im = Image.open("/home/pi/carDetect/testMedia/testPictures/outTest1Fixed.jpg")
	im = Image.open(picture)
	im.save(output, format=im.format)

	r=redis.StrictRedis(host='localhost',password='nokia123')
	r.set('imagedata%d' %imageCount, output.getvalue())
	output.close()
