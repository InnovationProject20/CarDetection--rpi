from PIL import Image
import redis
import StringIO

output = StringIO.StringIO()
im = Image.open("/home/pi/carDetect/testMedia/testPictures/outTest9Fixed.jpg")
im.save(output, format=im.format)

r=redis.StrictRedis(host='localhost')
r.set('imagedata', output.getvalue())
output.close()
