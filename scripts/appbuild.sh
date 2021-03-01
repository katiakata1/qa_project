#!/bin/bash

#change permission settings
sudo chmod 666 /var/run/docker.sock

#remove all containers
docker-compose down --rmi all

#build the containers again
docker-compose build

#login to DockerHub
sudo docker login

#push newly made images to the DockerHub
sudo docker-compose push