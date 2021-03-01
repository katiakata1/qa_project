#!/bin/bash

#run Ansible
ansible-playbook -i inventory.yaml playbook.yaml

#return to the starting point
cd ..