The task that we are going to perform in this blog are:

🎇Configure Namenode (Master).

🎇Format the Namenode.

🎇Configure the Datanode (Slave).

🎇Check the connection between Datanode and Namenode.

Here I am going to launch 3 instances on AWS cloud. First will act as Controller Node, Second for Namenode and the last one is Datanode. Here Namenode and Datanode are acting as Managed Nodes.

![image](https://user-images.githubusercontent.com/60690997/149521128-49c0302d-7c6e-49c8-9fab-46b1a870e0b6.png)

Firstly, In the controller node, We need to install Ansible. Before this Install Python using the yum install python3 Command.

![image](https://user-images.githubusercontent.com/60690997/149521248-8f8bb0cd-59e2-40b8-a8a7-dcd751f434c6.png)

Now We will setup the configuration file of Ansible by making a directory using mkdir /etc/ansible/ command. We need to write some code inside the configuration file of ansible.

![image](https://user-images.githubusercontent.com/60690997/149521269-bf333301-fb16-46eb-a2fb-1b3253fa8a37.png)

To avoid some warnings given by the command we have to disable it, using command_warnings=false

The remote user is that we are going to log in, here we have launched the ec2 instances hence the remote username is ec2-user

Also, we need to disable the ssh key, as when we do ssh it asks you for yes or no. We have to write host_key_checking=false to disable it.

Ansible uses existing privilege escalation systems to execute tasks with root privileges or with another user’s permissions. Because this feature allows you to ‘become’ another user, different from the user that logged into the machine (remote user), we call it to become. The become keyword leverages existing privilege escalation tools like sudo, su, pfexec, doas, pbrun, dzdo, ksu, runas, machinectl, and others.

To login in to that newly launched OS, we need to provide its respective key. Here .pem format will work. We need to give permission to that key in the read mode. Command for that:-

chmod 400 keyname.pem

After setting up the configuration file, the next step is to create inventory. To create an Inventory create a text file and inside the text file provide managed node IP address, username, password, and connection type as shown.

![image](https://user-images.githubusercontent.com/60690997/149521297-bc8ffb28-7928-4662-8b72-5de94db8e494.png)

Note: In this Inventory, we have given the .pem file for password as we are doing this practical/task on AWS cloud. If we want we can do it in Local VM(s). The changes we need to do are simple and as follows:

![image](https://user-images.githubusercontent.com/60690997/149521327-84af7b79-f355-420f-ace0-eb603b5accee.png)


Now, check the connectivity with Managed Node using the command ansible all -m ping.

![image](https://user-images.githubusercontent.com/60690997/149521346-2253881b-1ef8-4a95-b7cd-69bcb51dd529.png)

Now Start writing the playbook for configuring the Namenode. Also, It is good that we know how to setup a cluster manually as it provides the steps, and hence writing the playbook will be very much easy.

![image](https://user-images.githubusercontent.com/60690997/149521356-a6538523-182d-4089-a2d9-30b2abb45216.png)

Now just the playbook using the command ansible-playbook namenode.yml If no error comes then you will see that Namenode is configured and the service is running perfectly.

Here We can see all the tasks are performing great. Also, I have shown the content I wrote in the hdfs-site.xml and core-site.xml file as they are very much important.

Atlast by running the “ jps ” command manually we can also check the service is running or not.

Now let us write the playbook for Datanode. Again to the steps to configure it manually would be helpful. By chance I have attached the images which show how it executes afterward. Don’t worry about the code, I will provide my GitHub repo link at the end where you will find the entire code.

![image](https://user-images.githubusercontent.com/60690997/149521400-3e960237-2eb8-4a42-bcac-b40b6a141acd.png)

![image](https://user-images.githubusercontent.com/60690997/149521415-46915ee5-f8f1-4695-9c7d-ca9b8b3498d6.png)

Hence, here the execution of the datanode1.yml completes and the final result can be seen in the below-attached image.

![image](https://user-images.githubusercontent.com/60690997/149521432-db0b81f7-aafc-419e-aceb-92a931cfbf70.png)

Finally, we have configured Namenode and Datanode using Ansible.

Let’s Check the report of the cluster we configured.
Here we can see that here Number of Datanodes is 1 and it is contributing its storage to the cluster.

We can Verify it from Hadoop WebUI.

![image](https://user-images.githubusercontent.com/60690997/149521460-8a9ff473-03a5-42af-8b02-7521b41c94cc.png)

So that’s how we can set up the Hadoop cluster using Ansible.

