#!/bin/bash

#login to swarmmanager VM
ssh 10.138.0.15 << EOF

sudo rm -rf qa_project

git clone https://github.com/katiakata1/qa_project

cd qa_project

sudo docker login

sudo docker stack deploy --compose-file docker-compose.yml stack-project

EOF