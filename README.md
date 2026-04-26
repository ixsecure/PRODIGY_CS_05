# Network Packet Analyzer

A specialized Python tool designed to capture and analyze network packets in real-time. This project focuses on understanding network protocols, traffic flow, and data encapsulation for educational purposes.

## 📝 Overview
This analyzer sniffs network traffic and extracts critical information from each packet. It provides a structured view of network communication, helping users visualize how data travels across a network.

## 🚀 Key Features
- **Live Packet Capture:** Intercepts real-time traffic from specified network interfaces.
- **Protocol Identification:** Detailed analysis of protocols such as TCP, UDP, and ICMP.
- **Header Inspection:** Extracts and displays Source/Destination IP addresses and protocols.
- **Payload Analysis:** View the raw data or hex content contained within the packets.

## 🛠️ Installation
This tool requires the `Scapy` library. Note that capturing network traffic usually requires root or administrator privileges.

```bash
# Clone the repository
git clone [https://github.com/your-username/network-packet-analyzer.git](https://github.com/your-username/network-packet-analyzer.git)

# Install dependencies
pip install scapy

