## Joshua Omolewa

# Wecloud project 
Mini Project--Docker Container

Data Engineering Diploma


## 1. Business Scenario
To create a docker container that contains a python script that  joins two csv files into a single file  and ensures the output file is still available even if the container is shutdown.

## 2. Business Requirements
Download input csv files, combine csv files using a containerized python script and upload your dockerfile and final csv file to the repository you created on Github.


## 3. Specification Detail
There are 2 folders (input and output) and 1 python script. There are 2 csv files (t1 and t2) in the input folder.
Step required:
Use the python script to read the data from input folder.
Write the result data into output folder.
The python script is in the container.
The input and output folder is in the host
Try to make container running first, and then run python script (This means when you use docker run to start up the container, the python script will not run. The python script only runs when you give container an order with command docker exec)


## 4. Diagram
The project diagram is as below

![Docker_lab_Process](https://github.com/Joshua-omolewa/wecloud_data_project2/blob/main/img/Docker_lab_Process.jpg)

## STEPS USED TO COMPLETE THIS PROJECT
* Create a python python script called py_script.py
* Create a docker file name joshua_docker_file (make sure docker file is the same directory so other commands can execute)
* Create docker image by runing this command `docker build -f joshua_docker_file . -t python_app:6.0`  using -t to create repository name and tag as 6.0
* Create an instance of the docker image (Docker container) by  runing this command `docker run -v /home/dataengr/weclouddata_project2/wecloud_data_project2/input:/app/input -v /home/dataengr/weclouddata_project2/wecloud_data_project2/output:/app/output  python_app:6.0` -v is to mount my local drive to container in order to access my local input data.This enables my python script to acces the input data csv files.
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
