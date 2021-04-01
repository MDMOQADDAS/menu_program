import os

os.system("tput setaf 3")
print("\t\t\tWelcome in Menu Program!!")
os.system("tput setaf 7")
print("\t\t\t--------------------------")
j=0
while j!=1:

	os.system("tput setaf 2")
	#==================================Asking where run these command=============================
	r= input("\t\tHow you want to run these command ? (local/remote/exit):	")
	os.system("tput setaf 1")

	#========================Local execution block starting from here===================================
	if r=='local':
		i=0
		while i!=1:
			print("""
			press  1 : To check date
			press  2 : To check calender
			press  3 : To Check Ip Address
			press  4 : To go in any folder
			press  5 : To create directory
			press  6 : To delete directory
			press  7 : To check files in current folder
			press  8 : To make users
			press  9 : To open firefox

			press 10 : To configure hadoop clusture
			press 11 : To start hadoop clusture
			press 12 : To check hadoop clusture start or not
			press 13 : To check the reports of clusture

			press 14 : To configure aws cli
			press 15 : To describe instances
			press 16 : To describe keypair
			press 17 : To describe volumes
			press 18 : To describe volume status
			press 19 : To describe security group
			press 20 : To create key-pair
			press 21 : To create security group
			press 22 : To Start instance
			press 23 : To stop instance
			press 24 : To Lauch an instance
			press 25 : To Create volume
			press 26 : To attach volume
			press 27 : To deattach volume
			press 28 : To delete key-pair
			press 29 : To delete security group
			press 30 : To delete volume
			press 31 : To terminate instances
			press 32 : To create s3 bucket
			press 33 : To check list of s3 bucket
			press 34 : To delete the s3 bucket
			press 35 : To put object in s3 bucket

			press 36 : To install docker
			press 37 : To check the version of docker
			press 38 : To check the running container
			press 39 : To check all the stop container
			press 40 : To check status of docker
			press 41 : To check the docker image
			press 42 : To download the docker image
			press 43 : To Launch the docker container
			press 44 : To check the logs of particular os
			press 45 : To Start the docker service
			press 46 : To start stop docker container
			press 47 : To delete docker image
			press 48 : To delete docker container
			press 49 : To delete all docker contaier

			press 50 : To install web server service
			press 51 : To start web server service
			press 52 : To write html code
			press 53 : To stop webserver service							
			press 60 : To Exit
			
			""")
			#===========================asking choice============================================
			os.system("tput setaf 6")
			ch = int(input("\t\t\tEnter ur Choice :	"))
			os.system("tput setaf 1")
			#=========================Taking action on the response===============================
			
			if ch==1:	os.system("date")
			elif ch==2: os.system("cal")
			elif ch==3: os.system("ifconfig enp0s3")
			elif ch==4:
				fpath  = input("Enter the file path as (/etc/root/..) : ")			
				os.system(("cd {}").format(fpath))
				input()
			elif ch==5:
				di = input("Enter the directory name : ")			
				os.system(("mkdir /{}").format(di))
			elif ch==6:
				di = input("Enter the directory name : ")
				os.system(("rm -rf /{}").format(di))
			elif ch==7: os.system("ls")
			elif ch==8:
				user = input("Enter the user name : ")
				os.system(("useradd {}").format(user))
			elif ch==9:
				ffox = input("Enter which you want to search or url " )
				os.system(("firefox {}").format(ffox))
			elif ch==10:
				print("Now hdfs files opening..")
				input("Press Enter to continue")
				os.system("vim /etc/hadoop/hdfs-site.xml")
				print("Now core file opening..")
				input("Press Enter to continue")
				os.system("vim /etc/hadoop/core-site.xml")

			elif ch==11:
				node = input("Enter which node you want to start (namenode/datanode) : ")
				if node=='namenode': os.system("hadoop-daemon.sh start namenode")
				elif node=='datanode':  os.system("hadoop-daemon.sh start datanode")
			elif ch==12: os.system("jps")
			elif ch==13: os.system("hadoop dfsadmin -report")
			elif ch==14: os.system("aws configure")
			elif ch==15: os.system("aws ec2 describe-instances")
			elif ch==16: os.system("aws ec2 describe-key-pairs")			
			elif ch==17: os.system("aws ec2 describe-volumes")
			elif ch==18: os.system("aws ec2 describe-volume-status")
			elif ch==19: os.system("aws ec2 describe-security-groups")
			elif ch==20: 
				kname = input("Enter the key-pair name : ")
				os.system(("aws ec2 create-key-pair  --key-name {}").format(kname))
			elif ch==21:
				gname = input("Enter security group name : ")
				os.system(("aws ec2 create-security-group  --description check --group-name  {}  --vpc-id  vpc-a107eaca").format(gname))

			elif ch==22: 
				iid = input("Enter the instance id : ")
				os.system(("aws ec2 start-instances  --instance-ids {} ").format(iid))
			elif ch==23: 
				iid = input("Enter the instance id : ")
				os.system(("aws ec2 stop-instances  --instance-ids {} ").format(iid))
			elif ch==24:
				iid = input("Enter the image-id : ")
				it = input("Enter the instance-type : ")
				kname = input("Enter the key-name : ")
				sgid = input("Enter the security-group-id : ")
				os.system(("aws ec2 run-instances  --image-id {} --instance-type {} --key-name {}  --security-group-ids {}").format(iid,it,kname,sgid))

			elif ch==25:
				az = input("Enter Availability zone : ")
				size = int(input("Enter the size : "))
				vt = input("Enter Volume type : ")
				io = input("Enter inuput output speed(iops) : ")
				os.system(("aws ec2 create-volume  --availability-zone {} --size {} --volume-type {} --iops {} ").format(az,size,vt,io))


			elif ch==26:
				iid = input("Enter the instance id : ")
				vid = input("Enter the volume id : ")
				device = input("Enter the drive name : ")
				os.system(("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}").format(iid,vid,device))


			elif ch==27:
				iid = input("Enter the instance id : ")
				vid = input("Enter the volume id : ")
				device = input("Enter the drive name : ")
				os.system(("aws ec2 detach-volume --instance-id {} --volume-id {} --device {}").format(iid,vid,device))

			elif ch==28:
				kname = input("Enter the key-name : ")
				os.system(("aws ec2 delete-key-pair --key-name {}").format(kname))
			elif ch==29:
				sid = input("Enter the security group id : ")
				os.system(("aws ec2 delete-security-group --group-id {}").format(sid))
			elif ch==30:
				vid = input("Enter the volume id : ")
				os.system(("aws ec2 delete-volume --volume-id {}").format(vid))
			elif ch==31:
				iid = input("Enter the instance id: ")
				os.system(("aws ec2 terminate-instances --instance-ids {}").format(iid))

			elif ch==32:
				bname = input("Enter the bucket name : ")
				region = input("Enter the region : ")
				os.system(("aws s3api create-bucket --acl public-read --bucket {}  --region {} --create-bucket-configuration LocationConstraint=ap-south-1").format(bname,region))

			elif ch==33: os.system("aws s3api list-buckets")
			elif ch==34:
				bname = input("Enter the bucket name : ")
				os.system(("aws s3api delete-bucket  --bucket {}").format(bname))


			elif ch==35:
				bname = input("Enter the bucket name : ")
				path = input("Enter the path where file located : ")
				fname = input("Enter the file name : ")
				os.system(("aws s3api put-object  --bucket {}  --body {}  --key {}").format(bname,path,fname))


			elif ch==36: os.system("yum install docker-ce --nobest")
			elif ch==37: os.system("docker --version")
			elif ch==38: os.system("docker ps ")
			elif ch==39: os.system("docker ps -a")
			elif ch==40: os.system("systemctl status docker")
			elif ch==41: os.system("docker images")			
			elif ch==42:
				dimage = input("Enter the image name : ")				
				os.system(("docker pull {}").format(dimage))
			elif ch==43:
				osname = input("Enter the docker os name for good ex : ")
				dimage = input("Enter the image name : ")
				os.system(("docker run -it --name {} {}").format(osname,dimage))
			
			elif ch==44:
				osname = input("Enter the os name : ")
				os.system(("docker logs {}").format(osname))
			elif ch==45:
				os.system("systemctl start docker")
			elif ch==46:
				osname = input("Enter the os name : ")
				os.system(("docker start {}").format(osname))
				os.system(("docker attach {}").format(osname))
			elif ch==47:
				osname = input("Enter the os name : ")
				os.system(("docker rmi {}").format(osname))
			elif ch==48:
				osname = input("Enter the os name : ")
				os.system(("docker rm {}").format(osname))
			elif ch==49: os.system("docker rm `docker ps -a -q`")


			elif ch==50: os.system("yum install httpd")
			elif ch==51: os.system("systemctl start httpd")
			elif ch==52: 
				file = input("e
				os.system("vim /etc/var/www/new.html")


			#=================Bottom==================
			elif ch==60:	i=1
			else:	print("Wrong Input.......")
		

			os.system("tput setaf 1")
			input("Are you sure to exit..")
			os.system("clear")
			os.system("tput setaf 7")
	#===================================================Local execution block end here ================
		

	#====================================Remote execution block starting from here=============


	elif r=='remote':
		os.system("tput setaf 3")
		ip = input("\t\t\tEnter IP of os : ")
		os.system("tput setaf 1")
		i=0
		while i!=1:
			print("""
			press  1 : To check date
			press  2 : To check calender
			press  3 : To Check Ip Address
			press  4 : To go in any folder
			press  5 : To create directory
			press  6 : To delete directory
			press  7 : To check files in current folder
			press  8 : To make users
			press  9 : To open firefox
			
			press 10 : To configure hadoop clusture
			press 11 : To start hadoop clusture
			press 12 : To check hadoop clusture start or not
			press 13 : To check the reports of clusture	


			press 14 : To configure aws cli
			press 15 : To describe instances
			press 16 : To describe keypair
			press 17 : To describe volumes
			press 18 : To describe volume status
			press 19 : To describe security group
			press 20 : To create key-pair
			press 21 : To create security group
			press 22 : To Start instance
			press 23 : To stop instance
			press 24 : To Lauch an instance
			press 25 : To Create volume
			press 26 : To attach volume
			press 27 : To deattach volume
			press 28 : To delete key-pair
			press 29 : To delete security group
			press 30 : To delete volume
			press 31 : To terminate instances
			press 32 : To create s3 bucket
			press 33 : To check list of s3 bucket
			press 34 : To delete the s3 bucket
			press 35 : To put object in s3 bucket

			press 36 : To install docker
			press 37 : To check the version of docker
			press 38 : To check the running container
			press 39 : To check all the stop container
			press 40 : To check status of docker
			press 41 : To check the docker image
			press 42 : To download the docker image
			press 43 : To Launch the docker container
			press 44 : To check the logs of particular os
			press 45 : To Start the docker service
			press 46 : To start stop docker container
			press 47 : To delete docker image
			press 48 : To delete docker container
			press 49 : To delete all docker contaier

			press 50 : To install web server service
			press 51 : To start web server service
			press 52 : To write html code
			press 53 : To stop webserver service
			press 54 : To
			press 51 : To
			press 52 : To				
			press 60 : To Exit
			
			""")
			
			

			#===========================asking choice============================================
			os.system("tput setaf 6")
			ch = int(input("\t\t\tEnter ur Choice :	"))
			#=========================Taking action on the response===============================
		

			
			
			
			if ch==1:	os.system(("ssh root@{} date").format(ip))
			elif ch==10:
				print("Now hdfs files opening..")
				input("Press Enter to continue")
				os.system(("ssh root@{} vim /etc/hadoop/hdfs-site.xml").format(ip))
				print("Now core file opening..")
				input("Press Enter to continue")
				os.system(("ssh root@{} vim /etc/hadoop/core-site.xml").format(ip))

			elif ch==11:
				node = input("Enter which node you want to start (namenode/datanode) : ")
				if node=='namenode': os.system(("ssh root@{} hadoop-daemon.sh start namenode").format(ip))
				elif node=='datanode':  os.system(("ssh root@{} hadoop-daemon.sh start datanode").format(ip))
			elif ch==12: os.system(("ssh root@{} jps").format(ip))
			elif ch==13: os.system(("ssh root@{} hadoop dfsadmin -report").format(ip))
			elif ch==14: os.system(("ssh root@{} aws configure").format(ip))
			elif ch==15: os.system(("ssh root@{} aws ec2 describe-instances").format(ip))
			elif ch==16: os.system(("ssh root@{} aws ec2 describe-key-pairs").format(ip))			
			elif ch==17: os.system(("ssh root@{} aws ec2 describe-volumes").format(ip))
			elif ch==18: os.system(("ssh root@{} aws ec2 describe-volume-status").format(ip))
			elif ch==19: os.system(("ssh root@{} aws ec2 describe-security-groups").format(ip))
			elif ch==20: 
				kname = input("Enter the key-pair name : ")
				os.system(("ssh root@{} aws ec2 create-key-pair  --key-name {}").format(ip,kname))
			elif ch==21:
				gname = input("Enter security group name : ")
				os.system(("ssh root@{} aws ec2 create-security-group  --description check --group-name  {}  --vpc-id  vpc-a107eaca").format(ip,gname))

			elif ch==22: 
				iid = input("Enter the instance id : ")
				os.system(("ssh root@{} aws ec2 start-instances  --instance-ids {} ").format(ip,iid))
			elif ch==23: 
				iid = input("Enter the instance id : ")
				os.system(("ssh root@{} aws ec2 stop-instances  --instance-ids {} ").format(ip,iid))
			elif ch==24:
				iid = input("Enter the image-id : ")
				it = input("Enter the instance-type : ")
				kname = input("Enter the key-name : ")
				sgid = input("Enter the security-group-id : ")
				os.system(("ssh root@{} aws ec2 run-instances  --image-id {} --instance-type {} --key-name {}  --security-group-ids {}").format(ip,iid,it,kname,sgid))

			elif ch==25:
				az = input("Enter Availability zone : ")
				size = int(input("Enter the size : "))
				vt = input("Enter Volume type : ")
				io = input("Enter inuput output speed(iops) : ")
				os.system(("ssh root@{} aws ec2 create-volume  --availability-zone {} --size {} --volume-type {} --iops {} ").format(ip,az,size,vt,io))


			elif ch==26:
				iid = input("Enter the instance id : ")
				vid = input("Enter the volume id : ")
				device = input("Enter the drive name : ")
				os.system(("ssh root@{} aws ec2 attach-volume --instance-id {} --volume-id {} --device {}").format(ip,iid,vid,device))


			elif ch==27:
				iid = input("Enter the instance id : ")
				vid = input("Enter the volume id : ")
				device = input("Enter the drive name : ")
				os.system(("ssh root@{} aws ec2 detach-volume --instance-id {} --volume-id {} --device {}").format(ip,iid,vid,device))

			elif ch==28:
				kname = input("Enter the key-name : ")
				os.system(("ssh root@{} aws ec2 delete-key-pair --key-name {}").format(ip,kname))
			elif ch==29:
				sid = input("Enter the security group id : ")
				os.system(("ssh root@{} aws ec2 delete-security-group --group-id {}").format(ip,sid))
			elif ch==30:
				vid = input("Enter the volume id : ")
				os.system(("ssh root@{} aws ec2 delete-volume --volume-id {}").format(ip,vid))
			elif ch==31:
				iid = input("Enter the instance id: ")
				os.system(("ssh root@{} aws ec2 terminate-instances --instance-ids {}").format(ip,iid))


			elif ch==32:
				bname = input("Enter the bucket name : ")
				region = input("Enter the region : ")
				os.system(("ssh root@{} aws s3api create-bucket --acl public-read --bucket {}  --region {} --create-bucket-configuration LocationConstraint=ap-south-1").format(ip,bname,region))

			elif ch==33: os.system("aws s3api list-buckets")
			elif ch==34:
				bname = input("Enter the bucket name : ")
				os.system(("ssh root@{} aws s3api delete-bucket  --bucket {}").format(ip,bname))


			elif ch==35:
				bname = input("Enter the bucket name : ")
				path = input("Enter the path where file located : ")
				fname = input("Enter the file name : ")
				os.system(("ssh root@{} aws s3api put-object  --bucket {}  --body {}  --key {}").format(ip,bname,path,fname))


			elif ch==36: os.system(("ssh root@{} yum install docker-ce --nobest").format(ip))
			elif ch==37: os.system(("ssh root@{} docker --version").format(ip))
			elif ch==38: os.system(("ssh root@{} docker ps ").format(ip))
			elif ch==39: os.system(("ssh root@{} docker ps -a").format(ip))
			elif ch==40: os.system(("ssh root@{} systemctl status docker").format(ip))
			elif ch==41: os.system(("ssh root@{} docker images").format(ip))			
			elif ch==42:
				dimage = input("Enter the image name : ")				
				os.system(("ssh root@{} docker pull {}").format(ip,dimage))
			elif ch==43:
				osname = input("Enter the docker os name for good ex : ")
				dimage = input("Enter the image name : ")
				os.system(("ssh root@{} docker run -it --name {} {}").format(ip,osname,dimage))
			
			elif ch==44:
				osname = input("Enter the os name : ")
				os.system(("ssh root@{} docker logs {}").format(ip,osname))
			elif ch==45:
				os.system(("ssh root@{} systemctl start docker").format(ip))

			elif ch==46:
				osname = input("Enter the os name : ")
				os.system(("docker start {}").format(osname))
				os.system(("docker attach {}").format(osname))
			elif ch==47:
				osname = input("Enter the os name : ")
				os.system(("docker rmi {}").format(osname))
			elif ch==48:
				osname = input("Enter the os name : ")
				os.system(("docker rm {}").format(osname))
			elif ch==49: os.system("docker rm `docker ps -a -q`")



			elif ch==50: os.system(("ssh root@{} yum install httpd").format(ip))
			elif ch==51: os.system(("ssh root@{} systemctl start httpd").format(ip))
			elif ch==52: os.system(("ssh root@{} vim /etc/var/www/new.html").format(ip))










			#==========================Bottom Thing===============
			elif ch==60:	
				i=1
			else:	
				print("Wrong Input...........")



		
			os.system("tput setaf 1")
			input("Are you sure to exit")
			os.system("clear")
			os.system("tput setaf 7")

	#==========================Remote execution block end here=============================


	elif r=='exit':	j=1
	else:print("Wrong Input..........")
	os.system("tput setaf 7")






#==============================================================Program Ends============================
