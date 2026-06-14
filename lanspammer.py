import socket, time

S, P, T = "224.0.2.60", 4445, 2

def announce(servers, interval=1.5):
    msgs = [f"[MOTD]{s['motd']}[/MOTD][AD]{s['port']}[/AD]".encode() for s in servers]
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, T)
    try:
        while True:
            [sock.sendto(m, (S, P)) for m in msgs]
            time.sleep(interval)
    finally:
        sock.close()

announce([
    {"motd": "Выживание", "port": 25565},
    {"motd": "Творческий", "port": 25566},
    {"motd": "Мини-игры", "port": 25567},
])
