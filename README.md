# Project--Built an ETL pipeline in a  Docker Container that extract data from a local input folder  using a  python script  and then transform the data by combining all data files in a remote Virutal Machine (VM) server and then loading the data into a local ouput folder

## Author: 👤 **Joshua Omolewa**

## 1. Business Scenario
Data engineer is required to build a docker container that contains a python script that  joins two or more csv files into a single file  and ensures the output file is still available even if the container is shutdown.

## 2. Business Requirements
Download input csv files, combine csv files using a containerized python script and upload the dockerfile and final csv file to Github repository.


## 3. Specification Detail
There are 2 folders (input and output). There are 2 csv files (t1 and t2) in the input folder.
Step required:
- Use the python script to read the data from input folder.
- Write the result data into output folder.
- The python script is in the container.The input and output folder is in the host. 
- Ensure container is running  first, and then run python script (This means when you use docker run to start up the container, the python script will not run. The python script only runs when you give container an order with command docker exec)


## 4. Project Architecture
<img src="https://github.com/Joshua-omolewa/Containerized_python_docker_project/blob/main/img/project_architecture.jpg"  width="70%" height="70%">

## 5. Project Workflow
The project diagram is as below

<img src="https://github.com/Joshua-omolewa/wecloud_data_project2/blob/main/img/Docker_lab_Process.jpg"  width="70%" height="50%">


## STEPS USED TO COMPLETE THIS PROJECT
* Created a python python script called `py_script.py` in Virtual Machine
* Created a docker file name "joshua_docker_file" (make sure docker file is the same directory so other commands can execute) that copy the python script into the docker image when created 
* Created a docker image by runing this command `docker build -f joshua_docker_file . -t python_app:6.0`  using -t to create repository name and tag as 6.0
* Created an instance of the docker image (Docker container) by  runing this command `docker run -v /home/dataengr/weclouddata_project2/wecloud_data_project2/input:/app/input -v /home/dataengr/weclouddata_project2/wecloud_data_project2/output:/app/output  python_app:6.0` -v is to mount my local drive to container in order to access my local input data folder and output folder.This enables my python script to access the input data csv files.
* Verify container is runing  by excecuting command `docker ps -a`.
* Execute the python script in the container using `docker exec -it jolly_hopper python3 py_script.py` jolly_hoper is the container name ( or container id can be used)
* Push project files  to git repo using `git push`

## PROJECT FILES

* [DOCKER FILE](https://github.com/Joshua-omolewa/wecloud_data_project2/blob/main/joshua_docker_file)

* [PYTHON SCRIPT](https://github.com/Joshua-omolewa/wecloud_data_project2/blob/main/py_script.py)

* [INPUT DATA FOLDER](https://github.com/Joshua-omolewa/wecloud_data_project2/tree/main/input)

* [OUPTUT DATA FOLDER](https://github.com/Joshua-omolewa/wecloud_data_project2/tree/main/output)

## PROJECT COMMANDS BEING EXECUTED ON TERMINAL

![FINAL DOCKER IMAGE](https://github.com/Joshua-omolewa/wecloud_data_project2/blob/main/img/FINAL%20DOCKER%20IMAGE.jpg)

# Follow Me On
  
* LinkedIn: [@omolewajoshua](https://www.linkedin.com/in/joshuaomolewa/)  
* Github: [@joshua-omolewa](https://github.com/Joshua-omolewa)


## Show your support

Give a ⭐️ if this project helped you!
