## THE ARCHITECTURE INCLUDES:
- Web server configured on EC2 instance.
- Document Root(var/www/html) made persistent by mounting on EBS Block Device.
- Static Objects used in code such as pictures stored in S3
- Setting up content delivery network using Cloudfront and using the domain as S3 bucket.
- Finally place the Cloudfront URL on the webapp code for security and low latency.
### 1. LAUNCH AN EC2 INSTANCE
We have discussed the way to launch an instance using aws cli, in our previous Article . Click here to read it.

Use putty to login to your launced instance or simply press on the connect button (in case of amazon’s private linux image). By doing this you will get the terminal window of the launched instance , so that you can proceed forward.

### 2. INSTALL APACHE SERVER ON THE INSTANCE
In the terminal type in the commands below

Command line 1: sudo su root

Command line 2: yum install httpd

The above command installs the httpd server in your EC2 instance.

WEb server installation through cli
Now you need to start the httpd services using the command :

`systemctl start httpd`

You can confirm that your services has started successfully by running the command:

`systemctl status httpd`

amazon cli
### 3.CREATE A VOLUME AND ATTACH IT TO THE INSTANCE LAUNCHED
We have discussed the way to create an ebs volume of definite size and to attach it to a particular instance using aws cli in our previous Article . Click here to read it.

### 4. CREATE PARTITION, FORMAT IT AND THEN MOUNT IT TO MAKE IT PERSISTENT
#### Create a partition:

`fdisk /dev/xvdf`

partition creation through AWS
#### Format the partition:

`mkfs.ext4 /dev/xvdf`

cli of amazon
#### Mount the partition:

`mount /dev/xvdf /var/www/html`

You can confirm the successful mounting of the partition using the command:

`df -h`

aws cli
### 5. CREATE A S3 BUCKET AND UPLOAD AN IMAGE AND MAKE IT PUBLIC
In order to create an S3 bucket run:

`aws s3api create-bucket --acl public-read-write --bucket <bucket_name> --region <region> --create-bucket-configuration LocationConstraint=<region>`

creating bucket thrugh aws
For uploading the image to the bucket use:

`aws s3 cp <local_address_of_file> s3://<bucket_name>`

command line of amazon
The main step includes to make the object public which can be done using:

`aws s3api put_object_acl --bucket <bucket_name> --key <file_name> --acl public-read`

aws commnad line
### 6 . CREATE A CLOUDFRONT DISTRIBUTION
Use command given below to create cloudfront distribution:

`aws cloudfront create-distribution --origin-domain-name <bucket_name>.s3.amazonaws.com`

creating cloudfront through AWS
cloudfront
### 7. CREATE HTML FILE AS PER YOUR WISH AND ADD OBJECT FILE TO IT
Create html file according to your own desire.

`cd /var/www/html`

`vi <html_file _name>`

Use your knowledge of html ,css etc, to creatively decorate the page.

Add object to the file using the domain name you recieved while creatig the cloudfront distribution

Url: `http://<domain_name_ending_with_cloudfront.net>/<file_name>`

html file configuration
### 8. VISIT YOUR WEBPAGE
The webpage url: http:/<public_ip>/<html_file_name>
