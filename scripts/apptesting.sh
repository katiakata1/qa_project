#!/bin/bash
#check the location
pwd

#install all dependencies
sudo update -y
sudo upgrade -y
sudo apt install -y python3-pip
sudo pip3 install --upgrade pip

#navigate to service1 folder, install dependencies and test it
cd service1
pip3 install -r requirements.txt
python3 -m pytest --cov 

#navigate to service2 folder
cd ../service2

python3 -m pytest --cov app

#navigate to service3
cd ../service3
python3 -m pytest --cov app

#navigate to service4
cd ../service4
python3 -m pytest --cov app

#return to the start point and deactivate the testing
cd ..