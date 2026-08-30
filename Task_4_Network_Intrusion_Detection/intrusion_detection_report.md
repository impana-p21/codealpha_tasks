# Network Intrusion Detection System

## 1. Introduction

A Network Intrusion Detection System (NIDS) monitors network traffic and identifies suspicious or potentially malicious activity.

This project demonstrates a basic intrusion detection system using Python. It analyzes sample network traffic records and generates security alerts based on predefined detection rules.

## 2. Objectives

The objectives of this project are:

- Analyze network traffic.
- Detect suspicious network activity.
- Identify connections to commonly abused ports.
- Detect repeated failed login attempts.
- Identify unusually high network traffic.
- Detect unusual ICMP traffic.
- Generate security alerts.
- Recommend appropriate response actions.

## 3. Technologies Used

- Python
- CSV
- File handling
- Collections module

## 4. Detection Rules

### Suspicious Ports

The system monitors commonly abused or insecure services:

- Port 21 - FTP
- Port 23 - Telnet
- Port 445 - SMB
- Port 3389 - Remote Desktop Protocol

Connections to these ports generate alerts for further investigation.

### Failed Login Detection

The system counts failed login attempts from each source IP.

If an IP generates three or more failed login attempts, a brute-force warning is generated.

### High Traffic Detection

If a traffic record contains more than 1000 packets, the system generates a high-traffic alert.

### ICMP Anomaly Detection

Large volumes of ICMP traffic can indicate unusual network behavior. The system generates an alert when ICMP traffic exceeds the defined threshold.

## 5. System Workflow

1. Read network traffic from the CSV file.
2. Process each traffic record.
3. Extract source IP, destination IP, protocol, port, packet count and status.
4. Compare traffic against detection rules.
5. Generate alerts for suspicious activity.
6. Count failed login attempts.
7. Display security alerts.
8. Provide recommended response actions.

## 6. Sample Detection Results

The sample traffic contains several suspicious activities.

### Suspicious Ports

Connections to ports such as 23, 445 and 3389 are flagged for investigation.

### Brute Force Activity

The IP address `10.0.0.50` generates multiple failed login attempts and triggers a brute-force warning.

### High Traffic

The system identifies a traffic record containing more than 1000 packets.

### ICMP Anomaly

The system detects unusually high ICMP traffic from a source IP.

## 7. Response Mechanisms

When suspicious activity is detected, recommended actions include:

1. Investigating the source IP.
2. Reviewing network and authentication logs.
3. Blocking or restricting malicious sources after confirmation.
4. Checking affected systems for compromise.
5. Continuing network monitoring.

## 8. Limitations

This project is an educational prototype and does not replace a production IDS such as Snort or Suricata.

It analyzes predefined sample traffic rather than monitoring a live network interface.

A production intrusion detection system would require:

- Real-time packet capture
- More advanced signatures
- Threat intelligence
- Log correlation
- Automated response
- Centralized monitoring
- Dashboard visualization

## 9. Future Enhancements

Possible improvements include:

- Real-time packet capture using Scapy.
- Integration with Snort or Suricata.
- Real-time alert notifications.
- Database storage for detected events.
- Web-based monitoring dashboard.
- Machine learning based anomaly detection.
- Automated IP blocking after verification.

## 10. Conclusion

The project demonstrates the basic working principles of a Network Intrusion Detection System.

By analyzing network traffic and applying predefined security rules, the system can identify suspicious ports, repeated failed login attempts, high traffic volumes and unusual ICMP activity.

This project provided practical understanding of network monitoring, intrusion detection and security alert generation.
