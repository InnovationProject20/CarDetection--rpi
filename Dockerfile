FROM balenalib/raspberrypi3-debian:latest
#FROM debian
RUN apt-get clean -y && apt-get -y update && apt-get upgrade -y && apt-get install -y \
wget less nano python3-opencv python3-pip redis-server redis-tools

RUN pip3 install pillow 
RUN pip3 install redis

COPY ./ /root/.

#RUN python3 -c "import cv2; print(cv2.__version__)"

ADD ./start.sh /root/
ADD ./carDetection.py /root/ 

EXPOSE 6379

RUN chmod +x /root/start.sh

CMD ["/root/start.sh"]
