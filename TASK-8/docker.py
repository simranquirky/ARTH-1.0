
while 2:
	print("""
 Press  1 : To Start Docker(Docker must be installed)
 Press  2 : To see Docker Images
 Press  3 : To Run Docker
 Press  4 : To See All Running OS 
 Press  5 : To Pull an Image
 Press  6 : To Stop Container
 Press  7 : To Delete Container 
 Press  8 : To Stop Docker
 Press  9 : Exit
	""")

	print("Enter Your Choice : ",end="")

	ch=input()

	if int(ch) == 1:
		os.system("systemctl start docker")

	elif int(ch) == 2:
		os.system("docker images")

	elif int(ch) == 3:

	        image = input("\nGive The Image Name : ")
        	version = input("\nEnter Required Version : ")
        	os_name = input("\nEnter The Name You Want to Give: ")
        	os.system(" docker run -it --name {} {}:{}".format(image, version, os_name))

	elif int(ch) == 4:

	        os.system("docker ps -a")

	elif int(ch) == 5:

	        image = input("\nGive The Image Name : ")
        	version = input("\nEnter Version : ")

	        os.system("docker pull {}:{}".format(image,version))

	elif int(ch) == 6:

	        os_name = input("Enter The OS Name Which You Want to Stop: ")
        	os.system("docker stop {}".format(os_name))

	elif int(ch) == 7:
        	os_name = input("Enter The OS Name Which You Want to Delete: ")
        	os.system("docker rm {}".format(os_name))

	elif int(ch) == 8:

	        os.system("systemctl stop docker")
        	print("---------------Your Docker Service has Stopped --------------")

	elif int(ch) == 9:
        	exit()

	else:
        	print("You Entered Wrong Choice ...")
