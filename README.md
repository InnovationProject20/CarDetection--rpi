# CarDetection---RPi
This is an innovation project of Students from Metropolia University of Applied Sciences, working in collaboration with NOKIA.
The goal of this project is to create a modular systems of IoT devices for license plate recognition. Each module consists of a Raspberry Pi 3B+, equipped with a Pi Noir camera module to record live video feed and detect vehicles. Once having identify vehicles and finished pre-processing, the frames are sent the the master module consisting of a single Jetson Nano via Redis, for lincense plate recognition. The final data is then cross-checked with an online database for further applications

This repository contains all the materials needed for the Raspberry Pi, which includes:
1. The files needed for video capturing, image preprocessing and sending data to the server (to be uploaded to dockerhub)
2. The docker image to build containers for each new Pi module

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
