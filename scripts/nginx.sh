#!/bin/bash

ssh 10.138.0.18 << EOF

sudo rm -rf qa_project

git clone https://github.com/katiakata1/qa_project

cd qa_project

cd service6

sudo docker-compose down --rmi local

sudo docker-compose up -d

EOF
