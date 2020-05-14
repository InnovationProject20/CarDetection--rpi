#!/bin/bash
nohup redis-server &
cd /root
# if you remove the last line, then remove the '&' in next line
python3 /root/carDetection.py &
/bin/bash
