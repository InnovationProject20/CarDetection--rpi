# CarDetection---RPi
Car detection script on the raspberry pi, along with the xml document to help with car detection

## Prerequisite: 
1. Start the redis server on the host (jetson Nano)
2. Update the host address and password to the redis server

## Getting Started:
1. Clone the Repository to the local raspberry pi
2. Build the docker image with the command:  
>`$ sudo docker build <name of the container> .`
3. Run the container:  
>`$ sudo docker run <name of the container>:latest`

The Pi will then start reading the video data and send to the redis server for processing 

## Editing the container
1. To access the container and make adjustments yourself, use the command:  
>`$ sudo docker run --rm -it <name of the container> sh
2. Then, you can access the files (from this repository) via:  
>`# cd root`
