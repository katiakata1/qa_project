# Your Drink Generator :clinking_glasses: 

If you were thinking about what drink to have next - I have a perfect solution for you. <br>
The application I created generates random a spirit type, its mixer and the size of the drink you should get.<br>
It also displays what drinks have you already had so you could have the count of them <br>
From Russian with love :bear:

## Project Brief

The application meets all the requirements specified by QA DevOps Bootcamp mentors and was completed in two week frame time.
Scope of the project includes:
- Project management tool to tract the progress
- An Application fully integrated using the Feature-Branch model into a Version Control System which will <br> subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the service-oriented architecture described bellow 
- The project must be deployed using containerisation and an orchestration tool
- Create an Ansible Playbook that will provision the environment that the application needs to run
- The project must make use of a reverse proxy to make your application accessible to the user

**Tools used to achieve the scope requirements**

- Kanban Board: Trello Board
- Version Control: Git
- CI Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX

## Project Deliverables

The application created satisfies the following:
- Service 1 posts requests when activated and save responces on SQLAlchemy database. <br>
  Service 1 also displays five last entries on separate page.
- Service 2 and Service 3 receive a request from Service 1, generate random drink and amount of the drink
- Service 4 gets the outcome from Service 2 and send a particular mixer type configured by "if" statement <br>
  and sends it to the Service 1 

This is also dispalyed in the diagram below: 
![flow_diagram](https://user-images.githubusercontent.com/62849876/109434134-a49e5180-7a0b-11eb-9369-7a8749c61b1d.png)

## Project Tracking
  
