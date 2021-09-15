# DEPLOYOING WORDPRESS SITE USING AWS EC2 AND RDS
➢ Create an AWS EC2 instance

➢ Configure the instance with Apache Webserver.

➢ Download php application name "WordPress".

➢ As wordpress stores data at the backend in MySQL
Database server. Therefore, you need to setup a
MySQL server using AWS RDS service using Free
Tier.

➢ Provide the endpoint/connection string to the
WordPress application to make it work.

# STEPS TO CREATE A RELATIONAL DATABASE SERVICE (RDS) FROM AWS
Login to your aws account.

Go to services and search for rds.You will be taken to a page as shown below:
![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBa1VUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--07ce96a1e98339c38422ab6c3530ba2a371ca30d/Screenshot%20(325).png "Logo Title Text 1")

You can start by clicking on the orange button "Create Database".

Now fill the page with the following options:

- Standard create

- Engine options as MYSQL

- version : mysql-5.7.31

- templates : free-tier(as per your choice you can change)

- Username and password of database can be auto-generated or typed manually.

- Keep record of master username and password for further login
into database.

- public access: NO

Other settings can be left as default 

Note: the Availability zone of your RDS and EC2 instance should be same

After this you can click on "create" button at the end of your page.

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBa2NUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--8fa2234c1847f8ff217178a5e1a8f45d96e93b68/Screenshot%20(329).png "Logo Title Text 2")

then wait for the rds to be available. The rds can take 5-10 minutes to be available, so wait patiently.

**Here RDS database setup is finally completed and endpoint or
database host has been provided by database instances.

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBazBUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--20688baa9128d35be76b616a2c43542f852fb56c/Screenshot%20(336).png "Logo Title Text 3")

**This endpoint URL will be used in configuring WordPress with
database from RDS. 

The security group of the rds should be as follows:
![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBa29UIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--491307dd98a06d78224cf4ff74b440bb7755228d/Screenshot%20(334).png "Logo Title Text 3")

# Steps To Launch An EC2 Instance
From services section search for ec2.

Click on Launch Instance.

--select the required image for your instance .

--and then you can keep rest of your settings as default and click on review and launch.

--now you need to create a key pair, if you have previously created key pair you can also use that.
Now click on launch and your ec2 instance is sucessfully created and running.

The security group of the ec2 instance should be as follows:

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBa3dUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--7519c37cd704f4e221e58f2e977ebaae06410dc4/Screenshot%20(335).png "Logo Title Text 4")

# Setting Up Your Ec2 Instance

Login to the ec2 instance terminal using putty.

We need to Install basic packages required for installing WordPress. (httpd, php, MySQL).

Run the following commands:

-- yum install httpd -y ( will install httpd package)

--yum install php-mysqlnd mysql -y (will install php and MYSQL)

--amazon-linux-extras install php7.3 (it will upgrade to php version 7.3)

 Now we will download WordPress version 5.1.1 which is supported with
this php version 7.3 .

So, to download and install WordPress version 5.1.1

--wget https://wordpress.org/wordpress-5.1.1.tar.gz

This version is supported with php version 7.1 to 7.3.

To unzip the WordPress file command is:

--tar -xzvf wordpress-5.1.1.tar.gz

Then , transfer files of wordpress directory into /var/www/html using command:

--cp -r wordpress/* /var/www/html

Now we need to start and enable httpd by running respective commands: 


--systemctl start httpd

 (to start httpd)

--systemctl enable httpd

(to enable httpd) 

To see wordpress api !! Type http://{instance_public_ip}/

Here it will ask for Database name , username , password , database host We already know username password and host .. So, First we need to create database.

# Create Database

Connect to your ec2 instance terminal in order to carry out the task.

So to create a database we need to login into mysql with our credentials, use the following command:

mysql -h <endpoint_url_of_rds> -u <username> -p

Then enter password which we have created using RDS. 

You will be taken to the mysql interpreter.

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBazhUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--b0a96a50755a609297880f2f0739e75c52cd14c3/Screenshot%20(338).png "Logo Title Text 5")

Now to create database ..command is

CREATE DATABASE ; (command to create database)

show databases; (command to see available databases)

Your database has been sucessfully created.

# Installing Wordpress
After this,  we need to give database connection details which will create wpconfig.php and will further connect to our database.

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbEFUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--3112d59eacfc73114fe95385d15fcd4242a972f7/Screenshot%20(339).png "Logo Title Text 6")

By default they might create wp-config.php file by their own , but it is also
obvious to face this issue saying.
!! Sorry , but I can’t create wp-config.php file …. !

So we have to manually create file wp-config.php inside /var/www/html
directory and copy paste the content they provide us in this error page.
And then click on Run the Installation.. !! This will load the admin page to
install wordpress.

Now enter the required credentials details and then finally click on install
wordpress.

This will open successfull login page of wordpress where we have to enter
our username and password . After login it will open wordpress dashboard…

![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbE1UIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--25e522a475bd98af5989ff383ae8a90ecde463b2/Screenshot%20(342).png "photo")

Finally we can create our blog using wordpress …and can see it by http://{public-ip-of-instance}/ 
  
![alt text](https://json.commudle.com/rails/active_storage/blobs/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBbFFUIiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--f74c5dafd57a022bdf39f5b2b7670c01bd39d811/Screenshot%20(343).png "photo1")

