from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    if IP in packet:
        source = packet[IP].src
        destination = packet[IP].dst

        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        print("\n" + "=" * 50)
        print(f"Source IP      : {source}")
        print(f"Destination IP : {destination}")
        print(f"Protocol       : {protocol}")

        if TCP in packet:
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        if Raw in packet:
            payload = bytes(packet[Raw].load)
            print(f"Payload        : {payload[:100]}")

print("Starting Network Sniffer...")
print("Capturing packets. Press Ctrl+C to stop.")

sniff(prn=packet_callback, store=False)
