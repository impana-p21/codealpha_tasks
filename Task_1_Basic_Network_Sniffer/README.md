
Basic Network Sniffer

Project Overview

This project is a basic network packet sniffer developed using Python and the Scapy library.

The program captures network packets and displays useful information such as source IP address, destination IP address, network protocol, port numbers, and available packet payload data.

Objectives

* Understand how network packets are transmitted.
* Learn the basic structure of network traffic.
* Identify common network protocols.
* Capture and analyze packets using Python.
* Understand source and destination IP addresses.
* Gain practical knowledge of network security.

Technologies Used

* Python
* Scapy
* TCP/IP Networking

Features

* Captures network packets in real time.
* Displays source IP address.
* Displays destination IP address.
* Identifies TCP, UDP, and ICMP protocols.
* Displays source and destination ports.
* Displays limited payload information when available.

Installation

Install Python on your system.

Install Scapy using:

pip install scapy

Or install the dependency using:

pip install -r requirements.txt

How to Run

Run the program using:

python network_sniffer.py

On some operating systems, administrator or root privileges may be required for packet capture.

The program will start capturing network packets and display their details in the terminal.

Press:

Ctrl + C

to stop the program.

Sample Output

Starting Network Sniffer...
Capturing packets. Press Ctrl+C to stop.
==================================================
Source IP      : 192.168.1.10
Destination IP : 142.250.183.14
Protocol       : TCP
Source Port    : 52341
Destination Port: 443
==================================================
Source IP      : 192.168.1.10
Destination IP : 8.8.8.8
Protocol       : UDP
Source Port    : 54321
Destination Port: 53

The actual IP addresses, ports, protocols, and payload information depend on the network traffic captured while the program is running.

Ethical and Security Considerations

This project is intended for educational and authorized cybersecurity purposes.

Network traffic should only be captured on devices and networks for which the user has permission.

The program should not be used to intercept private communications or monitor networks without authorization.

Learning Outcomes

Through this project, I learned about:

* Network packet structure.
* TCP and UDP protocols.
* ICMP protocol.
* IP addressing.
* Source and destination ports.
* Packet capture using Scapy.
* Basic network traffic analysis.
* Ethical considerations in network monitoring.

Conclusion

The Basic Network Sniffer demonstrates how Python and Scapy can be used to capture and analyze network packets.

The project provides practical exposure to networking concepts and introduces fundamental techniques used in network security and traffic analysis.
