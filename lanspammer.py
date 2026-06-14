import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

N = 10
servers = [{"motd": f"Сервер {i+1}", "port": 25565 + i} for i in range(N)]
msgs = [f"[MOTD]{sv['motd']}[/MOTD][AD]{sv['port']}[/AD]".encode() for sv in servers]

print("by slava240 or compotadmin")
print(f"spaming a {N} servers...")
while True:
    [s.sendto(m, ("255.255.255.255", 4445)) for m in msgs]
    time.sleep(1.5)
