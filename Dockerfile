FROM resin/rpi-raspbian
RUN sudo apt update
RUN sudo apt install python-opencv
COPY ./ ./
CMD sh -c 'ln -s /dev/null /dev/raw1394'
RUN python -c "import cv2; print(cv2.__version__)"
RUN python carDetection.py
