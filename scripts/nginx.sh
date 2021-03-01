#!/bin/bash

ssh 35.233.228.219 << EOF

sudo rm -rf qa_project

git clone https://github.com/katiakata1/qa_project

cd qa_project

cd service6

sudo docker-compose down --rmi local

sudo docker-compose up -d

EOF
