from pwn import *



money = 1
io = remote("chall.live.ctf.tsg.ne.jp", 61234)
res = io.recv(2048).decode()
for i in range(20000):
    print("-*-*-*-*-*-*-", i)
    data = str(money) + "\n"
    io.send(data.encode())
    res = io.recv(2048).decode()
    io.send(b"0\n")
    res = io.recv(2048).decode().split()
    if "flag" in res:
        print(res)
        break
    if res[4] == "0":
        money *= 36
        print("[*]", res[4])
        print(res)
        continue
    money = 1
    io.close()
    io = remote("chall.live.ctf.tsg.ne.jp", 61234)
    res = io.recv(2048).decode()