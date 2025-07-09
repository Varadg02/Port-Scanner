import socket
import threading
from queue import Queue
import time

# Lock for thread-safe printing
print_lock = threading.Lock()

# Function to scan a single port
def scan_port(target, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Open port found: {port}")
        sock.close()
    except Exception as e:
        pass  # Silently ignore errors (host unreachable, etc.)

# Worker thread function
def threader():
    while True:
        port = q.get()
        scan_port(target, port)
        q.task_done()

# Input target and port range
target = input("Enter target (IP or domain): ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Invalid host. Please check the IP/domain.")
    exit()

port_range = input("Enter port range (e.g., 1-1000): ").strip()

try:
    start_port, end_port = map(int, port_range.split('-'))
except:
    print("[-] Invalid port range format. Use start-end (e.g., 20-80).")
    exit()

if start_port < 1 or end_port > 65535 or start_port > end_port:
    print("[-] Invalid port numbers. Ports must be between 1 and 65535.")
    exit()

print(f"\n[+] Scanning {target_ip} from port {start_port} to {end_port}...\n")
start_time = time.time()

# Queue for threads
q = Queue()

# Create thread pool
for _ in range(100):  # 100 threads for faster scanning
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

# Fill the queue with ports to scan
for port in range(start_port, end_port + 1):
    q.put(port)

q.join()  # Wait for all threads to finish

end_time = time.time()
print(f"\n[✔] Scan completed in {round(end_time - start_time, 2)} seconds.")
