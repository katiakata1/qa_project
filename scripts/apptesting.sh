#!/bin/bash
#check the location
pwd

#install all dependencies
pip3 install -r requirements.txt

#navigate to service1 folder
cd service1

#comlete the testing for service1
python3 -m pytest --cov 

#navigate to service2 folder
cd ../service-2

python3 -m pytest --cov 

#navigate to service3
cd ../service-3
python3 -m pytest --cov

#navigate to service4
cd ../service-4
python3 -m pytest --cov

#return to the start point and deactivate the testing
cd ..
deactivate