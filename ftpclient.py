from ftplib import FTP
import os
from getpass import getpass

host = '192.168.15.1'
user = 'huong'
password = '123456789'

# host = input("Host: ")
# user = input("Username: ")
# password = getpass()

# def filterf(filter_text,file):
#     filtered = open(f"{filter_text}.txt","a")
#     for text in file:
#         if filter_text in text:
#             print(" "+text)
#             filtered.writelines(text)

with FTP(host) as ftp:
    try:
        ftp.login(user=user, passwd=password)
        ftp.encoding = "utf-8"
    except:
        print("Ket noi khong thanh cong")
        exit()
    print("Ket noi thanh cong!")

    while True:
        answer = input("$ ")
        ftp.voidcmd('TYPE i')

        if answer == 'ex':
            break

        elif answer == "help":
            print("cd:\t\t  Chuyen doi thu muc")
            print("ls:\t\t  In cac thu muc con trong thu muc hien hanh")
            print("download:\t  Tai thu muc tu server")
            print("upload:\t\t  Tai thu muc len server")
            print("exit:\t\t  Thoat chuong trinh")

        elif answer == "ls":
            for file in ftp.nlst(): #ftp.retrlines('LIST')
                print(file)
        
        elif answer == "clear":
            os.system('cls')
        
        else:
            answer = answer.split(' ', 2)
            if answer[0] == "cd":
                try:
                    ftp.cwd(answer[1])
                except:
                    print("Thu muc khong ton tai")
            
            elif answer[0] == "dl":
                with open(answer[1], 'wb') as f:
                    try:
                        ftp.retrbinary('RETR '+ answer[1], f.write, 1024)
                        print(f'Tai file {answer[1]} thanh cong')
                    except:
                        print(f'Khong the tai {answer[1]} ve may')

            elif answer[0] == "filter":
                filter_file = open(answer[1], "r")
                filter_text = input("Du lieu can filter: ")
                filter = open(f"{filter_text}.txt", "a+")
                for texts in filter_file:
                    if filter_text in texts:
                        filter.writelines(texts)
                        break

            elif answer[0] == "ul":
                with open(answer[1], 'rb') as f:
                    try:
                        ftp.storbinary(f'STOR {answer[1]}', f)
                        print(f'Tai file {answer[1]} thanh cong')
                    except:
                        print(f'Khong the tai {answer[1]} len server')

    print("Dang xuat thanh cong")
