#!/bin/bash

ssh -i ~/.ssh/jenkins_agent_key swarm-nginx << EOF

sudo rm -rf qa_project

git clone https://github.com/katiakata1/qa_project.git

cd qa_project/service6

sudo docker-compose up -d
EOF
