### BASIC IDEA ABOUT AWS
AWS stands in short for Amazon web services. AWS is a secure cloud platform. Under this platform one can use Software as a Service, Infrastructure as a Service and much more. In addition to these the services are much scalable on the go. It works on Pay as you go model which means you have to pay only for the services you use and for the time you use those services. AWS CLI makes use of such services easier.

AWS CLI
Amazon web services do provide us with a graphical interface to manage our tasks. But in the technological world the tech guys, prefer to use the command line interface.

To start with you will have to download the AWS CLI software available.

Since most users work on Windows environment in general so we are sharing the links for the msi installer for Windows

- CLICK HERE TO DOWNLOAD AWS CLI MSI INSTALLER FOR WINDOWS( 64 bits)
https://s3.amazonaws.com/aws-cli/AWSCLI64.msi

- CLICK HERE TO DOWNLOAD AWS CLI MSI INSTALLER FOR WINDOWS( 32 bits)
https://s3.amazonaws.com/aws-cli/AWSCLI32.msi

If you are using environment other than windows, you can head over to the aws site to find one. Sorry for the inconvenience!

Coming to the setup , just go with the next option and in the end finish.

## AWS CLI setup

### Creating an IAM user in AWS
Now after setting up the aws cli on your system , you need to go to your aws console to create an IAM user, in simple term this user will get credentials like ID and Security key to allow you to authenticate to your aws account from the CLI. So let’s start!

#### STEP 1:

Login to your AWS console >> Click on Services >> Search in the bar for ‘access management’ >> Click on IAM option

AWS console services page
#### STEP 2:

You are now on the IAM ( Identity and Access Management ) page. Click on Add User

ADD user in AWS
#### STEP 3:

Fill in the required details, go with access type as programmatic access >> next.

add new user in IAM of AWS
#### STEP 4:

Select the ‘power user access‘ option and continue clicking next in case you do not want the task to be cumbersome.

AWS console image
AWS console
#### STEP 5:

Lastly click on ‘ create user‘ and done!

add tags in AWS
create user in AWS
You are ready with your auto-generated credentials for authentication.

Using the CLI
Head to the command prompt of your windows.

#### STEP 1 : Type in the command prompt ‘aws configure‘

#### STEP 2: Fill in the Access key ID and Secret access key and then your region(in my case us-east-2c) and you are ready to go

Using the AWS CLI
### What is a Key Pair in AWS?
Key pair are basically security credentials that proves your identity when you connect to any instance( OS) . They are called pair because they consist of two keys, a public key and a private key.

### How to create a Key Pair in AWS CLI?
Command :` aws ec2 create-key-pair --key-name <name_of _the_key>`

How to create a Key Pair
You can check in your console in the Key pairs section that you have successfully created a new key pair.

create a Key Pair in AWS CLI
### What are Security Groups in AWS?
Security groups are like firewall rules set for your instance to control the traffics both incoming and outgoing.

### How to create Security Group in AWS CLI?
Command : `aws ec2 create-security-group --group-name <security group name> --description <description>`

How to create Security Group 

Check in your console to confirm you have successfully created a security group.

create Security Group in AWS CLI


### How to launch instance in AWS CLI using above security group and key pair
Command:`aws ec2 --image-id <iamge ID> --count <number of instances> --instance-type <type> --key-name <key name> --security-group-ids <ID of the previously created security group>`

How to launch instance  
Check in the console to confirm the successful launch of your instance with the key pair and security group created by you.

launch instance in AWS CLI 
### What is EBS in AWS?
Amazon EBS allows you to create storage volumes and attach them to your instance. They are somewhat like physical disk drives , once attached to an instance you can create file systems on top of these volumes.

### How to create an EBS volume of definite size in AWS CLI?
Here, we are creating a volume of size 1 GB.

Command: `aws ec2 create-volume --size 1 --availability-zone <the zone>`

How to create an EBS volume of definite size
Confirm the successful creation of your EBS volume by checking the console.

 create an EBS volume of definite size in AWS CLI
Your EBS volume will be of no use until and unless you attach it to some instance. you can work on your volume only after attaching it to some instance.

### How to attach an EBS volume to an instance using AWS CLI?
Command : `aws ec2 attach-volume --volume-id <Volume ID> --instance-id <ID of the instance where you want to attach it> --device <path>`

How to attach an EBS volume to an instance 
The ‘In-use’ tag in the console window confirms the successful attachment of the EBS.

attach an EBS volume to an instance 
I hope you find this article useful. Keep Reading!
