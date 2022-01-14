

Configure Docker

👉Start and enable Docker services

👉 Pull the httpd server image from the Docker Hub

👉 Run the docker container and expose it to the public

👉 Copy the html code in /var/www/html directory
and start the web server

## Configure the Package for the Docker Installation
First of all we have to make a repository in order to install the docker software.
``` 
- name: "Creating  An yum repo for docker..... "
    yum_repository:
            name: "docker"
            description: "repo for DOcker"
            baseurl: "https://download.docker.com/linux/centos/7/x86_64/stable/"
            gpgcheck: no
```

## Installing the Docker Software
Now, we have two options for installing the docker software.


First option we can directly use the package module of ansible, but after this process an error will occur. This can’t help us to install a perfect docker software version. As we know installation of docker software can also be done by the help command module , But here in this case we can use the shell module instead of command module because in command modules we cannot use the keywords of the shell in shell module we can do so (for –nobest).
Second option is that we can install the docker software and look at the version of the installed docker version. Now we can copy this same version and we will run the package module with same version which will download the perfect docker software.
```
- name: "Installing Docker ....."
    package:
       name: "docker-ce-18.09.1-3.el7.x86_64"
       state: present
       
```
## Starting the Docker Service
Now let’s start the docker service by the help of ansible module. Now we are going to pull the image of httpd. So, we are going to use a module for pulling an image of docker by the help of docker image but we will face a problem as it will need a python module named “docker-py”. For installing this python module we need a pip module which is provided by ansible.
```
- name: "docker_image module need an python module i.e. docker-py ..."
    pip:
      name: docker-py
- name: "Pulling Image httpd ....."
    docker_image:
            name: httpd
            source: pull
```
## Now copy the (.html)code to the perfect place !!
We will create a .html page and transfer this file by the help of copy module. We have to make sure we have copied this file at a secured place.
``` 
- name: "Copying the html file (page) ...."
    copy:
        dest: "~/index.html"
        content: "Hii This page is Hosted From the HTTPD docker image !!"
```
## Launch the Docker Container and also expose it !!
Now we will start the docker container by the help of image HTTPD but when this image will start we will expose this image at a port and while starting we will attach a destination to this image where the .html file is located.
``` 
- name: "Lunching the docker image i.e. httpd ...."
    community.general.docker_container:
            name: webOS
            image: httpd
            ports:
                 - "888:80"
            state: started
```
## Allow the firewall for the port through which we have exposed that container
Now we have to allow the port through which the docker image is exposed.
``` 
- name: "lets allow firewall for the port which we have routed for to the docker webserver !!"
    firewalld:
            port: "888/tcp"
            state: enabled
            permanent: yes
            immediate: yes
 ```
