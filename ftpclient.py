# import socket
# import sys
# import os
# import shutil

# SERVER_IP = '192.168.0.108'
# SERVER_PORT = 1234

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((SERVER_IP, SERVER_PORT))
#     data = s.recv(1024)
#     print(data)

# from ftplib import FTP


# ftp = FTP('')
# # connect server
# ftp.connect('192.168.0.108',1026)
# # try to login
# ftp.login()
# # setting the path
# ftp.cwd('directory_name') 
# ftp.retrlines('LIST')

# # prepare for upload file
# def uploadFile():
#     # set file name   
#     filename = 'testfile.txt' 
#     # file store 
#     ftp.storbinary('STOR '+filename, open(filename, 'rb'))
#     ftp.quit()

# # prepare for download file
# def downloadFile():
#     filename = 'testfile.txt' #replace with your file in the directory ('directory_name')
#     localfile = open(filename, 'wb')
#     ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
#     ftp.quit()
#     localfile.close()

# uploadFile()

from ftplib import FTP 
from getpass import getpass
import os

ftp = FTP('')
try:
	ftp.connect('192.168.0.108', 7777)
except:
	print("Loi khong ket noi duoc voi server")
	exit()

username = input("Username: ")
password = getpass()

try:
	ftp.login(username, password)
	ftp.encoding = 'utf-8'
except:
	print("Username hoac password bi sai")
	exit()

print("Ket noi thanh cong!")

print("commands: help, cd, ls, download, upload, exit")
while True:
	answer = input("$ ")
	ftp.voidcmd('TYPE i')
	print(end='')

	if answer == "exit":
		break

	elif answer == "help":
		print("cd:\t\t  Chuyen doi thu muc")
		print("ls:\t\t  In cac thu muc con trong thu muc hien hanh")
		print("download:\t  Tai thu muc tu server")
		print("upload:\t\t  Tai thu muc len server")
		print("exit:\t\t  Thoat chuong trinh")

	elif answer == "ls":
		print(f"Current path: {ftp.pwd()}")#thu muc hien tai
		for file in ftp.nlst():
			print(file)
	
	elif answer == "clear":
		os.system('cls')

	else:
		answer = answer.split(' ', 1)
		if answer[0] == "cd":
			try:
				ftp.cwd(answer[1])
			except:
				print("Thu muc khong ton tai")
	
		elif answer[0] == "download":
			with open(answer[1], 'wb') as file:
				try:
					print(f"Doi tai {answer[1]}")
					ftp.retrbinary('RETR '+ answer[1], file.write, 1024)
					print(f"Tai thanh cong {answer[1]}")
				except:
					print(f"Khong the tai file {answer[1]}")

		
		elif answer[0] == "upload":
			ftp.cwd('/')
			with open(answer[1], "rb") as file:
				try:
					print("Dang tai file len server")
					ftp.storbinary(f'STOR {answer[1]}', file, 1024)
					print(f"Tai len thanh cong")
				except:
					print("Khong the tai file len server")
			
print("Logging you out")