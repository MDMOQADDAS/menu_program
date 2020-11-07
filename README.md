# menu_program

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
		while i!=1:#=======Main Menu Started=====================
			print("""
			press 1 : To General Command
			press 2 : To LVM
			press 3 : To Big data (Hadoop)
			press 4 : To AWS CLI
			press 5 : To Docker
			press 6 : To Web Server
			press 7 : To exit""")
			#===========Main Menu closed======================
			mch = int(input("Enter your choice : "))
			#================Taking action after choice-===OPTION-1=============
			if mch==1:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press  1 : To check date
					press  2 : To check calender
					press  3 : To Check Ip Address
					press  4 : To create partition
					press  5 : To create directory
					press  6 : To delete directory
					press  7 : To check files in current folder
					press  8 : To make users
					press  9 : To open firefox
					press 10 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system("date")
					elif ch==2: os.system("cal")
					elif ch==3: os.system("ifconfig enp0s3")
					elif ch==4:
						fpath  = input("Enter the file path as (/dev/sda ): ")		
						os.system(("fdisk {}").format(fpath))
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
						ffox = input("Enter which you want to search or url : " )
						os.system(("firefox {}").format(ffox))
					

			
					#=======Bottom-of-this-blocke================================
					elif ch==10: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================

			elif mch==2:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To convert drive into physical volume
					press 2 : To create Volume Group
					press 3 : To display physical volume
					press 4 : To display volume group
					press 5 : To create partition
					preSS 6 : To Format
					press 7 : To Mount
					press 8 : To increase static partition
					press 9 : To decrease startic partition
					press 10 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: 
						mname = input("\t\t\tEnter the drive name :	")
						os.system(("pvcreate {} ").format(mname))
					elif ch==2:
						vg = input("\t\t\tEnter the vgname :	")
						mname1 = input("\t\t\tEnter the drive name : ")
						mname2 = input("\t\t\tEnter the drive name : ")
						os.system(("vgcreate {}  {} {} ").format(vg,mname1,mname2))
					elif ch==3: os.system("pvdisplay")
					elif ch==4: os.system("vgdisplay")
					elif ch==5:
						size = input("\t\t\tEnter the size :	")
						name = input("\t\t\tEnter the lvname :	")
						vgname =input("\t\t\tEnter the vgname:  ")
						os.system(("lvcreate --size {}G  --name {} {}").format(size,name,vgname))
					elif ch==6:
						vgname =input("\t\t\tEnter the vgname:  ")
						lvname = input("\t\t\tEnter the lvname :	")
						os.system(("mkfs.ext4 /dev/{}/{}").format(ip,vgname,lvname))
						
					elif ch==7:
						vgname =input("\t\t\tEnter the vgname:  ")
						lvname = input("\t\t\tEnter the lvname :	")
						dire = input("\t\t\tEnter the directory:	")
						os.system(("mount /dev/{}/{}  /{}").format(ip,vgname,lvname,dire))
						

					elif ch==8:
						vg = input("\t\t\tEnter the vgname name :	")
						size = input("\t\t\tEnter the size to extend: ")
						lvname = input("\t\t\tEnter the lv name : ")
						os.system(("lvextend --size  +{}G  /dev/{}/{} ").format(size,vg,lvname))
						os.system(("resize2fs /dev/{}/{} ").format(vg,lvname))

					elif ch==9:
						vg = input("\t\t\tEnter the vgname name :	")
						lvname = input("\t\t\tEnter the lv name : ")
						size = input("\t\t\tEnter the size to decrease: ")
						dire = input("\t\t\tEnter the directory which mounted:	")
						os.system(("umount /{}").format(dire))
						os.system(("e2fsck -f /dev/{}/{} ").format(vg,lvname))
						os.system(("resize2fs /dev/{}/{} ").format(vg,lvname))
						os.system(("lvreduce -L  -{}G  /dev/{}/{} ").format(ip,size,vg,lvname))
						os.system(("mkfs.ext4 /dev/{}/{} ").format(vg,lvname))
						os.system(("mount /dev/{}/{}  /{} ").format(vg,lvname,dire))
			
					#=======Bottom-of-this-blocke================================
					elif ch==10:	m=1
					else:	print("Wrong Input.......")					 
					input("Press Enter to continue....")					
					os.system("clear")					
					os.system("tput setaf 7")
					#=============================================================


			
			elif mch==3:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To configure hadoop clusture
					press 2 : To start hadoop clusture
					press 3 : To check hadoop clusture start or not
					press 4 : To check the reports of clusture
					press 5 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1:
						print("Now hdfs files opening..")
						input("Press Enter to continue")
						os.system("vim /etc/hadoop/hdfs-site.xml")
						print("Now core file opening..")
						input("Press Enter to continue")
						os.system("vim /etc/hadoop/core-site.xml")
					elif ch==2:
						node = input("Enter which node you want to start (namenode/datanode) : ")
						if node=='namenode': os.system("hadoop-daemon.sh start namenode")
						elif node=='datanode':  os.system("hadoop-daemon.sh start datanode")
					elif ch==3: os.system("jps")
					elif ch==4: os.system("hadoop dfsadmin -report")
					

			
					#=======Bottom-of-this-blocke================================
					elif ch==5: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================

			elif mch==4:

				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1  : To configure aws cli
					press 2  : To describe instances
					press 3  : To describe keypair
					press 4  : To describe volumes
					press 5  : To describe volume status
					press 6  : To describe security group
					press 7  : To create key-pair
					press 8  : To create security group
					press 9  : To Start instance
					press 10 : To stop instance
					press 11 : To Lauch an instance
					press 12 : To Create volume
					press 13 : To attach volume
					press 14 : To deattach volume
					press 15 : To delete key-pair
					press 16 : To delete security group
					press 17 : To delete volume
					press 18 : To terminate instances
					press 19 : To create s3 bucket
					press 20 : To check list of s3 bucket
					press 21 : To delete the s3 bucket
					press 22 : To put object in s3 bucket
					press 23 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system("aws configure")
					elif ch==2: os.system("aws ec2 describe-instances")
					elif ch==3: os.system("aws ec2 describe-key-pairs")			
					elif ch==4: os.system("aws ec2 describe-volumes")
					elif ch==5: os.system("aws ec2 describe-volume-status")
					elif ch==6: os.system("aws ec2 describe-security-groups")
					elif ch==7: 
						kname = input("Enter the key-pair name : ")
						os.system(("aws ec2 create-key-pair  --key-name {}").format(kname))
					elif ch==8:
						gname = input("Enter security group name : ")
						os.system(("aws ec2 create-security-group  --description check --group-name  {}  --vpc-id  vpc-a107eaca").format(gname))

					elif ch==9: 
						iid = input("Enter the instance id : ")
						os.system(("aws ec2 start-instances  --instance-ids {} ").format(iid))
					elif ch==10: 
						iid = input("Enter the instance id : ")
						os.system(("aws ec2 stop-instances  --instance-ids {} ").format(iid))
					elif ch==11:
						iid = input("Enter the image-id : ")
						it = input("Enter the instance-type : ")
						kname = input("Enter the key-name : ")
						sgid = input("Enter the security-group-id : ")
						os.system(("aws ec2 run-instances  --image-id {} --instance-type {} --key-name {}  --security-group-ids {}").format(iid,it,kname,sgid))

					elif ch==12:
						az = input("Enter Availability zone : ")
						size = int(input("Enter the size : "))
						vt = input("Enter Volume type : ")
						io = input("Enter inuput output speed(iops) : ")
						os.system(("aws ec2 create-volume  --availability-zone {} --size {} --volume-type {} --iops {} ").format(az,size,vt,io))


					elif ch==13:
						iid = input("Enter the instance id : ")
						vid = input("Enter the volume id : ")
						device = input("Enter the drive name : ")
						os.system(("aws ec2 attach-volume --instance-id {} --volume-id {} --device {}").format(iid,vid,device))


					elif ch==14:
						iid = input("Enter the instance id : ")
						vid = input("Enter the volume id : ")
						device = input("Enter the drive name : ")
						os.system(("aws ec2 detach-volume --instance-id {} --volume-id {} --device {}").format(iid,vid,device))

					elif ch==15:
						kname = input("Enter the key-name : ")
						os.system(("aws ec2 delete-key-pair --key-name {}").format(kname))
					elif ch==16:
						sid = input("Enter the security group id : ")
						os.system(("aws ec2 delete-security-group --group-id {}").format(sid))
					elif ch==17:
						vid = input("Enter the volume id : ")
						os.system(("aws ec2 delete-volume --volume-id {}").format(vid))
					elif ch==18:
						iid = input("Enter the instance id: ")
						os.system(("aws ec2 terminate-instances --instance-ids {}").format(iid))

					elif ch==19:
						bname = input("Enter the bucket name : ")
						region = input("Enter the region : ")
						os.system(("aws s3api create-bucket --acl public-read --bucket {}  --region {} --create-bucket-configuration LocationConstraint=ap-south-1").format(bname,region))

					elif ch==20: os.system("aws s3api list-buckets")
					elif ch==21:
						bname = input("Enter the bucket name : ")
						os.system(("aws s3api delete-bucket  --bucket {}").format(bname))


					elif ch==22:
						bname = input("Enter the bucket name : ")
						path = input("Enter the path where file located : ")
						fname = input("Enter the file name : ")
						os.system(("aws s3api put-object  --bucket {}  --body {}  --key {}").format(bname,path,fname))
				

					

			
					#=======Bottom-of-this-blocke================================
					elif ch==23: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================

			elif mch==5:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1  : To install docker
					press 2  : To check the version of docker
					press 3  : To check the running container
					press 4  : To check all the stop container
					press 5  : To check status of docker
					press 6  : To check the docker image
					press 7  : To download the docker image
					press 8  : To Launch the docker container
					press 9  : To check the logs of particular os
					press 10 : To Start the docker service
					press 11 : To start stop docker container
					press 12 : To delete docker image
					press 13 : To delete docker container
					press 14 : To delete all docker contaier
					press 15 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system("yum install docker-ce --nobest")
					elif ch==2: os.system("docker --version")
					elif ch==3: os.system("docker ps ")
					elif ch==4: os.system("docker ps -a")
					elif ch==5: os.system("systemctl status docker")
					elif ch==6: os.system("docker images")			
					elif ch==7:
						dimage = input("Enter the image name : ")				
						os.system(("docker pull {}").format(dimage))
					elif ch==8:
						osname = input("Enter the docker os name for good ex : ")
						dimage = input("Enter the image name : ")
						os.system(("docker run -it --name {} {}").format(osname,dimage))
					
					elif ch==9:
						osname = input("Enter the os name : ")
						os.system(("docker logs {}").format(osname))
					elif ch==10:
						os.system("systemctl start docker")
					elif ch==11:
						osname = input("Enter the os name : ")
						os.system(("docker start {}").format(osname))
						os.system(("docker attach {}").format(osname))
					elif ch==12:
						osname = input("Enter the os name : ")
						os.system(("docker rmi {}").format(osname))
					elif ch==13:
						osname = input("Enter the os name : ")
						os.system(("docker rm {}").format(osname))
					elif ch==14: os.system("docker rm `docker ps -a -q`")
					#=======Bottom-of-this-blocke================================
					elif ch==15: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================

			elif mch==6:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To install web server service
					press 2 : To start web server service
					press 3 : To write html code
					press 4 : To stop web service
					press 5 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: print("hi")
					

			
					#=======Bottom-of-this-blocke================================
					elif ch==5: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================



			#=================Bottom==================
			elif mch==7:	i=1
			else:	print("Wrong Input.......")
			os.system("clear")
			os.system("tput setaf 7")
			#=========================================
	#===================================LOCAL-EXECUTION-BLOCK END HERE===========================

		
	#===================================REMOTE-EXECUTION-STARTED FROM HERE=======================
	elif r=='remote':
		ip  = input("Enter IP : ")
		i=0
		while i!=1:#=======Main Menu Started=====================
			print("""
			press 1 : To General Command
			press 2 : To LVM
			press 3 : To Big data (Hadoop)
			press 4 : To AWS CLI
			press 5 : To Docker
			press 6 : To Web Server
			press 7 : To exit
			""")
			#===========Main Menu closed======================
			mch = int(input("Enter your choice : "))
			#================Taking action after choice-==OPTION-1=============
			if mch==1:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
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
					press 10 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system(("ssh root@{} date").format(ip))
					elif ch==2: os.system(("ssh root@{} cal").format(ip))
					elif ch==3: os.system(("ssh root@{} ifconfig enp0s3").format(ip))
					elif ch==4:
						fpath  = input("Enter the file path as (/etc/root/ : ")		
						os.system(("ssh root@{} cd {}").format(ip,fpath))
						input()
					elif ch==5:
						di = input("Enter the directory name : ")			
						os.system(("ssh root@{} mkdir /{}").format(ip,di))
					elif ch==6:
						di = input("Enter the directory name : ")
						os.system(("ssh root@{} rm -rf /{}").format(ip,di))
					elif ch==7: os.system("ls")
					elif ch==8:
						user = input("Enter the user name : ")
						os.system(("ssh root@{} useradd {}").format(ip,user))
					elif ch==9:
						ffox = input("Enter which you want to search or url " )
						os.system(("ssh root@{} firefox {}").format(ip,ffox))
					

			
					#=======Bottom-of-this-blocke================================
					elif ch==10: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================


			elif mch==2:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To convert drive into physical volume
					press 2 : To create Volume Group
					press 3 : To display physical volume
					press 4 : To display volume group
					press 5 : To create partition
					preSS 6 : To Format
					press 7 : To Mount
					press 8 : To increase static partition
					press 9 : To decrease startic partition
					press 10 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1:
						mname = input("\t\t\tEnter the drive name :	")
						os.system(("ssh root@{} pvcreate {} ").format(ip,mname))
					elif ch==2:
						vg = input("\t\t\tEnter the vgname :	")
						mname1 = input("\t\t\tEnter the drive name : ")
						mname2 = input("\t\t\tEnter the drive name : ")
						os.system(("ssh root@{} vgcreate {}  {} {} ").format(ip,vg,mname1,mname2))

					elif ch==3: os.system(("ssh root@{} pvdisplay").format(ip))
					elif ch==4: os.system(("ssh root@{} vgdisplay").format(ip))
					elif ch==5:
						size = input("\t\t\tEnter the size :	")
						name = input("\t\t\tEnter the lvname :	")
						vgname =input("\t\t\tEnter the vgname:  ")
						os.system(("ssh root@{} lvcreate --size {}G  --name {}  {}").format(ip,size,name,vgname))		
					elif ch==6:
						vgname =input("\t\t\tEnter the vgname:  ")
						lvname = input("\t\t\tEnter the lvname :	")
						os.system(("ssh root@{} mkfs.ext4 /dev/{}/{}").format(ip,vgname,lvname))	
					elif ch==7:
						vgname =input("\t\t\tEnter the vgname:  ")
						lvname = input("\t\t\tEnter the lvname :	")
						dire = input("\t\t\tEnter the directory:	")
						os.system(("ssh root@{} mount /dev/{}/{}  /{}").format(ip,vgname,lvname,dire))
		
					elif ch==8:
						vg = input("\t\t\tEnter the vgname name :	")
						size = input("\t\t\tEnter the size to extend: ")
						lvname = input("\t\t\tEnter the lv name : ")
						os.system(("ssh root@{} lvextend --size  +{}G  /dev/{}/{} ").format(ip,size,vg,lvname))
						os.system(("ssh root@{} resize2fs /dev/{}/{} ").format(ip,vg,lvname))
					elif ch==9:
						vg = input("\t\t\tEnter the vgname name :	")
						lvname = input("\t\t\tEnter the lv name : ")
						size = input("\t\t\tEnter the size to decrease: ")
						dire = input("\t\t\tEnter the directory which mounted:	")
						os.system(("ssh root@{} umount /{}").format(ip,dire))
						os.system(("ssh root@{} e2fsck -f /dev/{}/{} ").format(ip,vg,lvname))
						os.system(("ssh root@{} resize2fs /dev/{}/{} ").format(ip,vg,lvname))
						os.system(("ssh root@{} lvreduce -L  -{}G  /dev/{}/{} ").format(ip,size,vg,lvname))
						os.system(("ssh root@{} mkfs.ext4 /dev/{}/{} ").format(ip,vg,lvname))
						os.system(("ssh root@{} mount /dev/{}/{}  /{} ").format(ip,vg,lvname,dire))
			
					#=======Bottom-of-this-blocke================================
					elif ch==10: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================


			elif mch==3:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To configure hadoop clusture
					press 2 : To start hadoop clusture
					press 3 : To check hadoop clusture start or not
					press 4 : To check the reports of clusture
					press 5 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============

					if ch==1:
						print("Now hdfs files opening..")
						input("Press Enter to continue")
						os.system(("ssh root@{} vim /etc/hadoop/hdfs-site.xml").format(ip))
						print("Now core file opening..")
						input("Press Enter to continue")
						os.system(("ssh root@{} vim /etc/hadoop/core-site.xml").format(ip))

					elif ch==2:
						node = input("Enter which node you want to start (namenode/datanode) : ")
						if node=='namenode': os.system(("ssh root@{} hadoop-daemon.sh start namenode").format(ip))
						elif node=='datanode':  os.system(("ssh root@{} hadoop-daemon.sh start datanode").format(ip))
					elif ch==3: os.system(("ssh root@{} jps").format(ip))
					elif ch==4: os.system(("ssh root@{} hadoop dfsadmin -report").format(ip))

					#=======Bottom-of-this-blocke================================
					elif ch==5: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================

			elif mch==4:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1  : To configure aws cli
					press 2  : To describe instances
					press 3  : To describe keypair
					press 4  : To describe volumes
					press 5  : To describe volume status
					press 6  : To describe security group
					press 7  : To create key-pair
					press 8  : To create security group
					press 9  : To Start instance
					press 10 : To stop instance
					press 11 : To Lauch an instance
					press 12 : To Create volume
					press 13 : To attach volume
					press 14 : To deattach volume
					press 15 : To delete key-pair
					press 16 : To delete security group
					press 17 : To delete volume
					press 18 : To terminate instances
					press 19 : To create s3 bucket
					press 20 : To check list of s3 bucket
					press 21 : To delete the s3 bucket
					press 22 : To put object in s3 bucket
					press 23 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system(("ssh root@{} aws configure").format(ip))
					elif ch==2: os.system(("ssh root@{} aws ec2 describe-instances").format(ip))
					elif ch==3: os.system(("ssh root@{} aws ec2 describe-key-pairs").format(ip))			
					elif ch==4: os.system(("ssh root@{} aws ec2 describe-volumes").format(ip))
					elif ch==5: os.system(("ssh root@{} aws ec2 describe-volume-status").format(ip))
					elif ch==6: os.system(("ssh root@{} aws ec2 describe-security-groups").format(ip))
					elif ch==7: 
						kname = input("Enter the key-pair name : ")
						os.system(("ssh root@{} aws ec2 create-key-pair  --key-name {}").format(ip,kname))
					elif ch==8:
						gname = input("Enter security group name : ")
						os.system(("ssh root@{} aws ec2 create-security-group  --description check --group-name  {}  --vpc-id  vpc-a107eaca").format(ip,gname))

					elif ch==9: 
						iid = input("Enter the instance id : ")
						os.system(("ssh root@{} aws ec2 start-instances  --instance-ids {} ").format(ip,iid))
					elif ch==10: 
						iid = input("Enter the instance id : ")
						os.system(("ssh root@{} aws ec2 stop-instances  --instance-ids {} ").format(ip,iid))
					elif ch==11:
						iid = input("Enter the image-id : ")
						it = input("Enter the instance-type : ")
						kname = input("Enter the key-name : ")
						sgid = input("Enter the security-group-id : ")
						os.system(("ssh root@{} aws ec2 run-instances  --image-id {} --instance-type {} --key-name {}  --security-group-ids {}").format(ip,iid,it,kname,sgid))

					elif ch==12:
						az = input("Enter Availability zone : ")
						size = int(input("Enter the size : "))
						vt = input("Enter Volume type : ")
						io = input("Enter inuput output speed(iops) : ")
						os.system(("ssh root@{} aws ec2 create-volume  --availability-zone {} --size {} --volume-type {} --iops {} ").format(ip,az,size,vt,io))


					elif ch==13:
						iid = input("Enter the instance id : ")
						vid = input("Enter the volume id : ")
						device = input("Enter the drive name : ")
						os.system(("ssh root@{} aws ec2 attach-volume --instance-id {} --volume-id {} --device {}").format(ip,iid,vid,device))


					elif ch==14:
						iid = input("Enter the instance id : ")
						vid = input("Enter the volume id : ")
						device = input("Enter the drive name : ")
						os.system(("ssh root@{} aws ec2 detach-volume --instance-id {} --volume-id {} --device {}").format(ip,iid,vid,device))

					elif ch==15:
						kname = input("Enter the key-name : ")
						os.system(("ssh root@{} aws ec2 delete-key-pair --key-name {}").format(ip,kname))
					elif ch==16:
						sid = input("Enter the security group id : ")
						os.system(("ssh root@{} aws ec2 delete-security-group --group-id {}").format(ip,sid))
					elif ch==17:
						vid = input("Enter the volume id : ")
						os.system(("ssh root@{} aws ec2 delete-volume --volume-id {}").format(ip,vid))
					elif ch==18:
						iid = input("Enter the instance id: ")
						os.system(("ssh root@{} aws ec2 terminate-instances --instance-ids {}").format(ip,iid))


					elif ch==19:
						bname = input("Enter the bucket name : ")
						region = input("Enter the region : ")
						os.system(("ssh root@{} aws s3api create-bucket --acl public-read --bucket {}  --region {} --create-bucket-configuration LocationConstraint=ap-south-1").format(ip,bname,region))

					elif ch==20: os.system("aws s3api list-buckets")
					elif ch==21:
						bname = input("Enter the bucket name : ")
						os.system(("ssh root@{} aws s3api delete-bucket  --bucket {}").format(ip,bname))


					elif ch==22:
						bname = input("Enter the bucket name : ")
						path = input("Enter the path where file located : ")
						fname = input("Enter the file name : ")
						os.system(("ssh root@{} aws s3api put-object  --bucket {}  --body {}  --key {}").format(ip,bname,path,fname))



			
					#=======Bottom-of-this-blocke================================
					elif ch==23: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================


			elif mch==5:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1  : To install docker
					press 2  : To check the version of docker
					press 3  : To check the running container
					press 4  : To check all the stop container
					press 5  : To check status of docker
					press 6  : To check the docker image
					press 7  : To download the docker image
					press 8  : To Launch the docker container
					press 9  : To check the logs of particular os
					press 10 : To Start the docker service
					press 11 : To start stop docker container
					press 12 : To delete docker image
					press 13 : To delete docker container
					press 14 : To delete all docker contaier
					press 15 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==1: os.system(("ssh root@{} yum install docker-ce --nobest").format(ip))
					elif ch==2: os.system(("ssh root@{} docker --version").format(ip))
					elif ch==3: os.system(("ssh root@{} docker ps ").format(ip))
					elif ch==4: os.system(("ssh root@{} docker ps -a").format(ip))
					elif ch==5: os.system(("ssh root@{} systemctl status docker").format(ip))
					elif ch==6: os.system(("ssh root@{} docker images").format(ip))			
					elif ch==7:
						dimage = input("Enter the image name ")				
						os.system(("ssh root@{} docker pull {}").format(ip,dimage))
					elif ch==8:
						osname = input("Enter the docker os name for good ex : ")
						dimage = input("Enter the image name : ")
						os.system(("ssh root@{} docker run -it --name {} {}").format(ip,osname,dimage))
					
					elif ch==9:
						osname = input("Enter the os name : ")
						os.system(("ssh root@{} docker logs {}").format(ip,osname))
					elif ch==10:
						os.system(("ssh root@{} systemctl start docker").format(ip))

					elif ch==11:
						osname = input("Enter the os name : ")
						os.system(("docker start {}").format(osname))
						os.system(("docker attach {}").format(osname))
					elif ch==12:
						osname = input("Enter the os name : ")
						os.system(("docker rmi {}").format(osname))
					elif ch==13:
						osname = input("Enter the os name : ")
						os.system(("docker rm {}").format(osname))
					elif ch==14: os.system("docker rm `docker ps -a -q`")

							

			
					#=======Bottom-of-this-blocke================================
					elif ch==15: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================


			elif mch==6:
				m=0
				while m!=1:#====Sum-Menu Started=====================
					os.system("tput setaf 3")
					print("""
					press 1 : To install web server service
					press 2 : To start web server service
					press 3 : To write html code
					press 4 : To stop web service
					press 5 : To Exit
					""")
					#========Sub-Menu Closed=======================
					ch = int(input("Enter your choice : "))
					os.system("tput setaf 6")
					#==============Taking Action after choice=============
					if ch==50: os.system(("ssh root@{} yum install httpd").format(ip))
					elif ch==51: os.system(("ssh root@{} systemctl start httpd").format(ip))
					elif ch==52: os.system(("ssh root@{} vim /etc/var/www/new.html").format(ip))

					#=======Bottom-of-this-blocke================================
					elif ch==5: m=1
					else:	print("Wrong Input.......")
					input("Press Enter to continue....")
					os.system("clear")
					os.system("tput setaf 7")
					#=============================================================





			#=================Bottom==================
			elif mch==7:	i=1
			else:	print("Wrong Input.......")
			os.system("clear")
			os.system("tput setaf 7")
			#=========================================



	#==============================REMOTE-EXECUTION-BLOCK-END-HERE===============================






	elif r=='exit': j=1
	else: print("Wrong Input...")
	os.system("tput setaf 7")				
