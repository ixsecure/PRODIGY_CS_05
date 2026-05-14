# Network Packet Analyzer

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat&logo=python&logoColor=white)
![Library](https://img.shields.io/badge/Library-Scapy-00A3E0?style=flat)
![Type](https://img.shields.io/badge/Type-Network%20Analysis%20Tool-blue?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Internship](https://img.shields.io/badge/Internship-Prodigy%20InfoTech-blue?style=flat)

> Python tool that captures and analyzes network packets in real-time — protocol identification, header inspection, and payload analysis for educational purposes.

---

## About

This project was developed as part of the **Prodigy InfoTech** cybersecurity internship. It is a network packet analyzer built with Python and Scapy that sniffs live traffic from a specified network interface and extracts structured information from each packet — helping visualize how data actually travels across a network.

Understanding packet structure is a core skill in both **network security** and **penetration testing** — it is how tools like Wireshark, tcpdump, and Nmap work under the hood.

---

## Features

| Feature | Description |
|---|---|
| Live Packet Capture | Intercepts real-time traffic from a specified network interface |
| Protocol Identification | Detects and labels TCP, UDP, ICMP and other protocols |
| Header Inspection | Extracts source/destination IP addresses and port numbers |
| Payload Analysis | Displays raw or hex content contained within packets |
| Structured Output | Clean, readable display for each captured packet |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/ixsecure/PRODIGY_CS_05.git
cd PRODIGY_CS_05

# Install dependencies
pip install scapy

# Run with root privileges (required for packet capture)
sudo python packet_analyzer.py
```

> Note: Capturing network traffic requires root or administrator privileges on most systems.

---

## Usage

```bash
sudo python packet_analyzer.py
```

```
Network Packet Analyzer — @ixsecure
=====================================
Interface : eth0
Sniffing  : Started...

[Packet #1]
  Protocol  : TCP
  Source    : 192.168.1.10:52341
  Dest      : 142.250.74.46:443
  Payload   : b'\x16\x03\x01\x00\xee\x01\x00...'

[Packet #2]
  Protocol  : UDP
  Source    : 192.168.1.1:53
  Dest      : 192.168.1.10:49152
  Payload   : b'\x00\x01\x81\x80\x00\x01...'

[Packet #3]
  Protocol  : ICMP
  Source    : 192.168.1.10
  Dest      : 8.8.8.8
  Type      : Echo Request (ping)
```

---

## Code

```python
from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys

packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    print(f"\n[Packet #{packet_count}]")

    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto  = packet[IP].proto

        if TCP in packet:
            print(f"  Protocol  : TCP")
            print(f"  Source    : {src_ip}:{packet[TCP].sport}")
            print(f"  Dest      : {dst_ip}:{packet[TCP].dport}")
        elif UDP in packet:
            print(f"  Protocol  : UDP")
            print(f"  Source    : {src_ip}:{packet[UDP].sport}")
            print(f"  Dest      : {dst_ip}:{packet[UDP].dport}")
        elif ICMP in packet:
            print(f"  Protocol  : ICMP")
            print(f"  Source    : {src_ip}")
            print(f"  Dest      : {dst_ip}")
            print(f"  Type      : {packet[ICMP].type}")
        else:
            print(f"  Protocol  : Other ({proto})")
            print(f"  Source    : {src_ip}")
            print(f"  Dest      : {dst_ip}")

        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"  Payload   : {payload[:60]}")

    print("  " + "-" * 40)


def main():
    print("Network Packet Analyzer — @ixsecure")
    print("=====================================")
    interface = input("Interface (default: eth0): ").strip() or "eth0"
    count = input("Number of packets to capture (0 = unlimited): ").strip()
    count = int(count) if count.isdigit() else 0

    print(f"\nSniffing on {interface}... Press Ctrl+C to stop.\n")
    sniff(iface=interface, prn=analyze_packet, count=count, store=False)


if __name__ == "__main__":
    main()
```

---

## Protocols Explained

| Protocol | Layer | Common Use |
|---|---|---|
| TCP | Transport | HTTP, HTTPS, SSH, FTP — reliable, connection-based |
| UDP | Transport | DNS, DHCP, VoIP — fast, connectionless |
| ICMP | Network | Ping, traceroute — diagnostic and error reporting |

---

## Security Context

A packet analyzer is one of the most powerful tools in a security professional's arsenal. It is used for:

- **Network forensics** — investigating suspicious traffic after an incident
- **Intrusion detection** — spotting abnormal patterns in real-time
- **Protocol analysis** — understanding how applications communicate
- **Penetration testing** — identifying cleartext credentials or sensitive data in transit

Tools like **Wireshark** and **tcpdump** are built on the same principles as this project.

---

## What I learned

- Using **Scapy** for packet sniffing and dissection in Python
- Structure of IP, TCP, UDP, and ICMP packet headers
- How data is **encapsulated** across network layers (OSI model)
- Why **cleartext protocols** (HTTP, FTP, Telnet) are dangerous
- The difference between **passive sniffing** and **active interception**
- Importance of root privileges in low-level network operations

---

## Ethical Notice

> This tool is developed for **educational and authorized use only**.
> Capturing network traffic without explicit permission is illegal in most countries.
> Always use this tool on networks you own or have written authorization to test.

---

## Author

**Richmond Konan** — Junior Penetration Tester | Offensive Security | Cote d'Ivoire

- LinkedIn: https://linkedin.com/in/richmonddelmas
- GitHub: https://github.com/ixsecure
- Email: delmasrichmond@gmail.com

---

## Topics

`python` `scapy` `network-security` `packet-analyzer` `packet-sniffing` `cybersecurity` `tcp-ip` `network-forensics` `penetration-testing` `prodigy-infotech`
