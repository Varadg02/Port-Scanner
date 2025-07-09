# 🔍 Project 4: Port Scanner Using Python

## 📌 Problem Statement
Network ports act as gateways for communication. While essential for data exchange, **open or misconfigured ports** can pose security risks, often targeted in cyberattacks. Identifying these ports helps in basic vulnerability assessment.

## 🎯 Objective
Build a **Python-based port scanner** that can detect open ports on a specified IP address or domain. This tool helps in evaluating basic network security by revealing which ports are accessible.

## 🧰 Requirements
- Python 3.x
- Built-in libraries:
  - `socket`
  - `threading`
- Command-line terminal (Linux, macOS, Windows PowerShell)

## 🚀 Features
- Fast multi-threaded scanning
- CLI-based input for IP/website and port range
- Prints list of **open ports**
- Easy to use and extend

## 📂 Project Structure
port-scanner/
├── port_scanner.py
└── README.md

markdown
Copy
Edit

## 📜 Script Overview (`port_scanner.py`)
- Accepts target IP/hostname and port range
- Scans each port using `socket.connect_ex()`
- Uses `threading` to speed up scanning
- Displays list of open ports

## 💡 How It Works
1. User inputs target (e.g., `scanme.nmap.org`) and optional port range.
2. The script checks each port's status.
3. If the port is open (`connect_ex() == 0`), it is reported.
4. Threading is used to improve performance.

## 🖥️ How to Run

### 1. Clone or Download the Repository
```bash
git clone https://github.com/your-username/port-scanner.git
cd port-scanner
2. Run the Script
bash
Copy
Edit
python port_scanner.py
3. Input
Enter:

Target IP or domain (e.g., 127.0.0.1, scanme.nmap.org)

Port range (e.g., 1-1024)

✅ Example Output
pgsql
Copy
Edit
Enter target (IP or domain): scanme.nmap.org
Enter port range (e.g., 1-1000): 1-100

[+] Scanning scanme.nmap.org from port 1 to 100...

Open port found: 22
Open port found: 80

Scan completed in 3.47 seconds
