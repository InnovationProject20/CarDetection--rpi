FROM balenalib/raspberrypi3-debian:latest
RUN sudo apt update
RUN sudo apt upgrade
RUN sudo apt install python3-opencv
RUN sudo apt-get install python3-pip
RUN sudo pip3 install pillow
RUN sudo apt install redis-server
RUN sudo pip3 install redis
COPY ./ ./
RUN python3 -c "import cv2; print(cv2.__version__)"
RUN sudo service redis-server start 
CMD ["python3", "./carDetection.py"]
