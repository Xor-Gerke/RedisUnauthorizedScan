# -*- coding: UTF-8 -*-
# !/usr/bin/python
import socket
import argparse

def redis(ip,port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            s.send(bytes("INFO\r\n", 'UTF-8'))
            result = s.recv(1024).decode()
            if 'redis_version' in result:
                print('[#]'+ip +":"+port +" 存在redis未授权")
            else:
                print('[-]'+ip +":"+port +" 不存在漏洞")
        except (socket.error, socket.timeout):
            print('[!]'+ip +":"+port +" 连接超时")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''redis检测工具 #author:gerke''')
    parser.add_argument('-t', dest='target',type=str, help='target/目标')
    parser.add_argument('-p',dest='port', type=str, help='port/请求端口')
    parser.add_argument('-f', dest='file',type=str, help='file/文件扫描{文件内容格式 target:port}')
    args = parser.parse_args()
    if args.target:
        if args.port:
            redis(args.target,args.port)
        else:
            port = 6379
            redis(args.target,port)
    elif args.file:
        with open(args.file,'r+') as f:
            lines = f.readlines()
            for line in lines:
                target = line.split(":", 1)[0]
                port = line.split(":", 1)[1]
                port = port.replace('\n','')
                redis(target,port)
            f.close()
    else:
        print("输入错误！请检测输入格式")
