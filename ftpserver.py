# import socket
# import shutil
import os
# import sys

# ip = '192.168.0.108'
# port = 1234

# print('Tao socket moi')
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((ip, port))
#     print('May chu dang nghe...')
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         print(f'Ket noi tu {addr} duoc thanh lap!!')
#         sys.stdout.write("220 COMP 431 FTP server ready.\r\n")
#         conn.send(bytes("220 COMP 431 FTP server ready.\r\n", 'utf-8'))
    
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user('huong', '123', '.')
authorizer.add_anonymous(os.getcwd())

handler = FTPHandler
handler.authorizer = authorizer

handler.banner = "Ket noi may khach thanh cong."
server = FTPServer(("192.168.0.108", 7777), handler)

server.serve_forever()