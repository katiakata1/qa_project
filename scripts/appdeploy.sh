#!/bin/bash

#login to swarmmanager VM
ssh -i ~/.ssh/jenkins_agent_key swarm-manager << EOF

sudo rm -rf qa_project

git clone https://github.com/katiakata1/qa_project.git

cd qa_project

sudo docker stack rm stack-project

sudo docker login

sudo docker stack deploy --compose-file docker-compose.yaml stack-project

EOF