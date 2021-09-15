
## What is Docker and why is it used?
Docker is a software that works on container technology. It is used for deploying OS (also known as containers). It is an open platform for developing, shipping and running applications. The infrastructure is easy to manage, same as you manage other applications.
## How to install docker on your linux OS
(in my case Redhat Linux)
#### Step 1: cd /etc/yum.repos.d (change the directory to /etc/yum.repos.d)

#### Step 2: Create a file named docker.repo in this diectory. Within the file write the following lines of code:

[docker]

baseurl=https://download.docker.com/linux/centos/7/x86_64/stable

gpgcheck=0

docker.repo file
#### Step 3: yum install docker-ce --nobest

In order to confirm successful installation in your base system , run :

docker --version

Now, you need to start docker services, use command ‘systemctl start docker‘.

Check the status of your docker using command ‘ systemctl status docker‘, active status is a green signal to continue working on it.

 status
## Launch container on top of Docker
#### Step 1: docker images

Shows the list of docker images, if you have none in the list, you need to pull the image of required OS.

#### Step 2: docker pull centos:7

In order to pull centos:7 image.

docker image launch
#### Step 3: docker run -it centos:7

The above command launches the image on top of docker, now you are inside your container.

## Configuring Apache server on top of Container
#### Step 1: Run command yum install httpd , for installing httpd server.

install httpd server on docker os
#### Step 2: Now you need to start httpd services.

In normal linux OS , systemctl start httpd works for it, but in container OS this command is not supported as you can see in the image below. Rather, you need to use, /usr/sbin/httpd.

start httpd services 
You can make html pages in directory /var/www/html. In my case, I made a file task7-2.html with a few lines of code.

After saving the html pages, you need to restart httpd services, using command:

/usr/sbin/httpd -k restart

You can check the successful start of your services, but using the command given below in your base OS.

curl 172.17.0.2/<file_name>

check your site
## Setting up Python Interpreter on top of Container
#### Step 1: yum install python3

installing python interpreter on Docker
- Confirm your installation , using command python3.

- check python interpreter
You can run Python codes and the interpreter successfully displays the output.

runnimg python commands on top of docker
Thanks for reading!
