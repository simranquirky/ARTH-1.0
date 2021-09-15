import subprocess as sp
import xml.etree.ElementTree as ET
import os
print("\t\t\tWelcome to the TUI to make Life Easier")

print("\t\t\t--------------------------------------")

print("\t\t\t\t\tMenu")
print("\t\t\t\t\t----")
print("""
 Press  1 : To check hadoop is installed
 Press  2 : To install hadoop
 Press  3 : To make directory
 Press  4 : To configure hdfs-site.xml file
 Press  5 : To configure core-site.xml
 Press  6 : To format name node
 Press  7 : To start hadoop services
 Press  8 : To configure client
 Press  9 : To upload files on datanode
 Press 10 : To remove file
 Press 11 : To check the report of hadoop cluster
 Press 12 : To stop hadoop services
 Press 13 : To read files from data node
 Press 14 : To check the files in hadoop cluster
 Press 15 : Exit
""")

print("Enter Your Choice : ",end="")

ch=input()

if int(ch) == 1:
	check_hadoop = sp.getstatusoutput("rpm -q hadoop")
	check_jdk = sp.getstatusoutput("rpm -q jdk")
	if check_hadoop[0] != 0:
		os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm  --force")
		print("Hadoop is installed now!!")
		os.system("rpm -i jdk-8u171-linux-x64.rpm")
	else:
		print("Hadoop is already installed!!")

elif int(ch) == 2:
	os.system("rpm -i hadoop-1.2.1-1.x86_64.rpm  --force")
	print("Hadoop is now installed")
	os.system("rpm -i jdk-8u171-linux-x64.rpm")
	os.system("hadoop version")

elif int(ch) ==3:
	make_dir = input("Enter folder/directory name: ")
	os.system("mkdir {}".format(make_dir))
	print("Directory {} is created".format(make_dir))

elif int(ch) == 4:
	node = input("Which node you want to configure (name node/data node)?  " )
	make_dir = input("Enter folder/directory name: ")
	if "name" in node  or  "name node" in node:
		os.chdir(r"/etc/hadoop")
		cwd = os.getcwd()
		print("You are in directory {}".format(cwd))
		os.system('echo \<configuration\> >> hdfs-site.xml')
		os.system('echo \<property\> >> hdfs-site.xml')
		os.system('echo \<name\>dfs.name.dir\</\name\>  >> hdfs-site.xml')
		os.system('echo \<value\>{}\</\value\>  >> hdfs-site.xml'.format(make_dir)
		os.system('echo \</property\> >> hdfs-site.xml')
		os.system('echo \</\configuration\> >> hdfs-site.xml')
	elif "data" in node or "data node" in node:
		make_dir = input("Enter folder/directory name: ")
		os.chdir("/etc/hadoop")
		cwd = os.getcwd()
		print("you are in directory {}".format(cwd))
		os.system('echo \<configuration\> >> hdfs-site.xml')
		os.system('echo \<property\> >> hdfs-site.xml')
		os.system('echo \<name\>dfs.data.dir\</\name\>  >> hdfs-site.xml')
		os.system('echo \<value\>{}\</\value\>  >> hdfs-site.xml'.format(make_dir)
		os.system('echo \</property\> >> hdfs-site.xml')
		os.system('echo \</\configuration\> >> hdfs-site.xml')
	else:
		print("Sorry I don't understand!! Please select name node or data node")

elif int(ch) == 5:
	config = input('Which node you want to configure (name node/datanode)? ')
	if "name" in config or "name node"  in config:
		name_ip = input("Enter name node IP address: ")
		name_port = input("Enter port number: ")
		os.chdir(r"/etc/hadoop")
		os.system('echo \<configuration\> >> core-site.xml')
		os.system('echo \<property\> >> core-site.xml')
		os.system('echo \<name\>fs.default.name\</\name\>  >> core-site.xml')
		os.system('echo \<value\>hdfs://{}:{}\</\value\>  >> core-site.xml'.format(name_ip,name_port)
		os.system('echo \</property\> >> core-site.xml')
		os.system('echo \</\configuration\> >> core-site.xml')	
	elif "data" in config or "data node" in config:
		data_ip = input("Enter namenode IP adress: ")
		name_port = input("Enter port number: ")
		os.chdir(r"/etc/hadoop")
		os.system('echo \<configuration\> >> core-site.xml')
		os.system('echo \<property\> >> core-site.xml')
		os.system('echo \<name\>fs.default.name\</\name\>  >> core-site.xml')
		os.system('echo \<value\>hdfs://{}:{}\</\value\>  >> core-site.xml'.format(name_ip,name_port)
		os.system('echo \</property\> >> core-site.xml')
		os.system('echo \</\configuration\> >> core-site.xml')

	else:
		print("Sorry I don't understand!! Please select name node or data node")

elif int(ch) == 6:
	os.system("hadoop format -namenode")
	print("Name node is formatting please start services")

elif int(ch) == 7:
	confirm  = input("Which node you want to start (name node/data node) ")
	if "name" in confirm or "name node"  in confirm:
		os.system("hadoop-daemon.sh start namenode")
	elif "data" in confirm or "data node" in confirm:
		os.system("hadoop-daemon.sh start datanode")
	else:
		print("Sorry I don't understand!! Please select namenode or data node")


elif int(ch) == 8:
	client = intput("Enter name node IP address: ")
	name_port = input("Enter port number: ")
	os.chdir(r"/etc/hadoop")
	os.system('echo \<configuration\> >> core-site.xml')
	os.system('echo \<property\> >> core-site.xml')
	os.system('echo \<name\>fs.default.name\</\name\>  >> core-site.xml')
	os.system('echo \<value\>hdfs://{}:{}\</\value\>  >> core-site.xml'.format(name_ip,name_port)
	os.system('echo \</property\> >> core-site.xml')
	os.system('echo \</\configuration\> >> core-site.xml')

elif int(ch) == 9:
	file1 = input("Enter file name: ")
	os.system("hadoop fs -put {} /".format(file1))

elif int(ch) == 10:
	rm_file = input("Enter file name which you want to remove: ")
	os.system("hadoop fs -rm {} ".format(rm_file))

elif int(ch) == 11:
	os.system("hadoop dfsadmin -report")

elif  int(ch) == 12:
	service = input("Do you want to stop services of (name node/data node)? ")
	if "name" in service or "name node" in service:
		os.system("hadoop-daemon.sh stop namenode")
	elif "data" in service or "data node" in service:
		os.system("hadoop-daemon.sh stop datanode")
	else:
		print("Sorry I don't understand!! Please select data node")

elif int(ch) == 13:
	read_file = input("Enter file name which you want to read: ")
	os.system("hadoop fs -cat /{}".format(read_file))

elif int(ch) ==14:
	os.system("hadoop fs -ls")

elif int(ch) == 15:
	exit()

else:
	print("Please select options from above menu")
