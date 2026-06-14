import socket, time

S, P, T = "224.0.2.60", 4445, 2

servers = [
    {"motd": "MiniLanSpammer", "port": 25565},
]
N = 10

def announce(interval=1.5):
    msgs = [f"[MOTD]{s['motd']}[/MOTD][AD]{s['port']}[/AD]".encode() for s in servers]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, T)
    try:
        while True:
            [sock.sendto(m, (S, P)) for m in msgs]
            time.sleep(interval)
    finally:
        sock.close()

print(f"Анонсируем {N} сервер(а/ов)")
announce()
