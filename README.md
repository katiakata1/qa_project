# Your Drink Generator :clinking_glasses: 

If you were thinking about what drink to have next - I have a perfect solution for you. <br>
The application I created generates random a spirit type, its mixer and the size of the drink you should get.<br>
It also displays what drinks have you already had so you could have the count of them <br>
From Russia with love :bear:

## Project Brief 	:memo:

The application meets all the requirements specified by QA DevOps Bootcamp mentors and was completed in two week frame time.
Scope of the project includes:
- Project management tool to tract the progress
- An Application fully integrated using the Feature-Branch model into a Version Control System which will <br> subsequently be built through a CI server and deployed to a cloud-based virtual machine.
- If a change is made to a code base, then Webhooks should be used so that Jenkins recreates and redeploys the changed application
- The project must follow the service-oriented architecture described bellow 
- The project must be deployed using containerisation and an orchestration tool
- Create an Ansible Playbook that will provide the environment that the application needs to run
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

## Project Tracking and Reached Milestones :briefcase:

For the best project tracking, the Trello board was used. This step is necessary to manage the workflow and distribute the workload efficiently. The most challenging was to identify the possible path to follow in order to complete the project due to a wide range of methods available in order to achieve the same task. The Trello board is divided into initial tasks, tasks completed and tasks in progress. Also, issues
encountered along the development were noted as well (refer to a diagram bellow).

![trello board](https://user-images.githubusercontent.com/62849876/109438540-6eb89780-7a22-11eb-93eb-794ee1e4fe18.png)


## Project Structure 	:page_with_curl:

The application created satisfies the following:
- Service 1 posts request when activated and save responses on SQLAlchemy database. <br>
  Service 1 also displays the last five entries on a separate page using the Jinja2 template
- Service 2 and Service 3 receive a request from Service 1, generate random drink and amount of the drink
- Service 4 gets the outcome from Service 2 and send a particular mixer type configured by the "if" statement and sends it to Service 1 

This is also displayed in the diagram below: 
![flow_diagram](https://user-images.githubusercontent.com/62849876/109434134-a49e5180-7a0b-11eb-9369-7a8749c61b1d.png)

## Testing	:hammer_and_wrench:

Testing was the following task after front-end design and database structure configured and working without issues. The first step was to 
test the code on a local machine, and update a unittest package to unittest.mock for future testing purposes. This was done due to the fact 
that future services would be deployed in Docker containers making the unittest package ineffective under such conditions.

Following screenshots of passed tests and corresponding coverages represent four services described in the Project Structure section.

![service1_cov](https://user-images.githubusercontent.com/62849876/109439655-2c458980-7a27-11eb-89f0-7a329408f3b2.png)

![service2_cov](https://user-images.githubusercontent.com/62849876/109439661-3798b500-7a27-11eb-9dc5-562c7a4684a0.png)

![service3_cov](https://user-images.githubusercontent.com/62849876/109439664-39fb0f00-7a27-11eb-909d-1e5a57914195.png)

![service4_cov](https://user-images.githubusercontent.com/62849876/109439666-3c5d6900-7a27-11eb-9064-5300716e4ca7.png)

The only miss occurring and reduction in the coverage is due to the second line of the following command:
```
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
```
The test ignores the line due to certain file configuration in the repository. Meanwhile, all tests are passed resulting in a fully operating application. 

## Detailed process description and technologies involved	:world_map:

This project aimed to test our understanding the whole of the DevOps aspect of the application development and deployment. The most challenging part 
was to create links between different tools and to understand of the right order of their configuration. The diagram below represents the overall structure required from the app development, testing to deployment:

![process](https://user-images.githubusercontent.com/62849876/109441902-85fd8200-7a2e-11eb-95af-a73ba391d2bc.png)

The first step was to create an active connection between Visual Studio Code and Google Cloud Instance using external IP and ssh key. This simplified the code development 
due to VSC user-friendly interface compared to GCP vim. The only disadvantage was that every time the server is stopped, new external IP is generated. Therefore, it was necessary to reset the config file in VSC every time the instance was restarted. The second step was to initialise the git repo on the local machine resulting in active git control over the files created and stored at the remote repository. 
<br>
<br>
The project consisted of a minimum of four different services initially connected via http://localhost:port. Each service has a unique port so the traffic could access the port. 
After the application could perform basic functionality, it was deployed with docker and further with docker-compose. At this stage, the access links had to be changed by their file names rather than localhost name. It was also decided to create a database within the docker container, which had the same storage capacity as any other MySql instance. 
It was achieved by creating a Volume, which would store all entries even if all containers were being deleted. 
<br>
<br>
The following step included Ansible configuration. The project was initially developed on a single VM. Additional three VMs were created for the load distribution and possible risks reduction. Ansible's role was to install docker, docker swarm, allocate the swarm-manager and swarm-worker on available VMs. All VMs were created in the same region
(Oregon, us-west1-b) resulting in their free communication via internal IPs. Connection between all of them was achieved by generating an ssh key on the master VM (where
the code was developed) and saving the public key in all the rest VMs. Load Balancer (NGINX) was installed on a separate VM.
<br>
<br>
As mentioned before, after docker-compose.yml was running correctly, built containers were pushed to DockerHub. This step was required for future purposes when a 
swarm-master would pull custom images onto the new VM and deploy the application. All the services seemed to run correctly, however, when navigating to port 80, the SQLAlchemy
error would occur meaning that some connection is missing. This issue postponed Jenkins pipeline development greatly. The issue was resolved by crating an external MySql Instance was created and connected to the container via its external IP. 

## Risk Assessment :mag:

The following risk assessment describes possible risks associated with the project

![riskassessmnt](https://user-images.githubusercontent.com/62849876/109443623-e7bfeb00-7a32-11eb-9c5d-4e4a278be5bb.png)


## Future Improvements & Bugs

The UX/UI design should be developed for a user-friendly experience. Additionally, greater choice of spirits should be used.
<br> 


