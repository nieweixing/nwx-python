import socket, time
from threading import Lock

def scoket_port(ip, port):
  try:
    if port >= 65535:
      print('端口扫描结束')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((ip, port))
    if result == 0:
      lock = Lock()
      lock.acquire()
      print('端口被占用')
      lock.release()
  except Exception as e:
    print(str(e))

if __name__ == "__main__":
   scoket_port('192.168.30.31', 27018)       