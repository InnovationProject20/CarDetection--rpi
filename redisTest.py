#to use this script type commands:
#       (1-from source(pi))python redisTest.py
#       (2-from destination(jetson))redis-cli -h (source ip address) -a (source password) redis-cli --raw get 'imagedata' >(desired filename).(same file type as source)

from PIL import Image
import redis
import StringIO

output = StringIO.StringIO()
im = Image.open("/home/pi/carDetect/testMedia/testPictures/outTest1Fixed.jpg")
im.save(output, format=im.format)

r=redis.StrictRedis(host='localhost',password='nokia123')
r.set('imagedata', output.getvalue())
output.close()
