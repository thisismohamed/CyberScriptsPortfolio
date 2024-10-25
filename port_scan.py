import socket
import logging

logging.basicConfig(level=logging.DEBUG)

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        if sock.connect_ex((host,port)) == 0:
            logging.info(f"[INFO] Port {port} is open")
        else:
            print(f"[WARNING] Port {port} is close", end="\r")
        sock.close()
    except socket.error as error:
        logging.error(f"[ERROR] Error has an occurred: {str(error)}")

def main():
    host = input("Enter the ethical target to scan for open ports: ")
    for port in range(1, 65535):
        scan_port(host, port)

if __name__ == "__main__":
    main()
