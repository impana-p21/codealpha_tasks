import csv
from collections import defaultdict

INPUT_FILE = "sample_network_traffic.csv"

SUSPICIOUS_PORTS = {21, 23, 445, 3389}
FAILED_LOGIN_THRESHOLD = 3
PACKET_THRESHOLD = 1000

alerts = []
connection_count = defaultdict(int)
failed_logins = defaultdict(int)

with open(INPUT_FILE, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        source_ip = row["source_ip"]
        destination_ip = row["destination_ip"]
        protocol = row["protocol"]
        destination_port = int(row["destination_port"])
        packets = int(row["packets"])
        status = row["status"]

        connection_count[source_ip] += 1

        if destination_port in SUSPICIOUS_PORTS:
            alerts.append(
                f"[SUSPICIOUS PORT] {source_ip} connected to "
                f"{destination_ip}:{destination_port}"
            )

        if status == "FAILED":
            failed_logins[source_ip] += 1

        if packets > PACKET_THRESHOLD:
            alerts.append(
                f"[HIGH TRAFFIC] {source_ip} generated "
                f"{packets} packets to {destination_ip}"
            )

        if protocol == "ICMP" and packets > 500:
            alerts.append(
                f"[ICMP ANOMALY] High ICMP traffic from {source_ip}"
            )

for ip, count in failed_logins.items():
    if count >= FAILED_LOGIN_THRESHOLD:
        alerts.append(
            f"[BRUTE FORCE WARNING] {ip} generated "
            f"{count} failed login attempts"
        )

print("=" * 70)
print("          NETWORK INTRUSION DETECTION SYSTEM")
print("=" * 70)

print(f"\nTraffic records analyzed: {sum(connection_count.values())}")
print(f"Unique source IPs: {len(connection_count)}")
print(f"Security alerts detected: {len(alerts)}")

print("\nALERTS")
print("-" * 70)

if alerts:
    for number, alert in enumerate(alerts, 1):
        print(f"{number}. {alert}")
else:
    print("No suspicious activity detected.")

print("\nRECOMMENDED RESPONSE")
print("-" * 70)

if alerts:
    print("1. Investigate the source IP addresses.")
    print("2. Review related network and authentication logs.")
    print("3. Block or restrict malicious sources if confirmed.")
    print("4. Check affected systems for further compromise.")
    print("5. Continue monitoring network activity.")
else:
    print("Continue normal network monitoring.")

print("\n" + "=" * 70)
print("Detection analysis completed.")
print("=" * 70)
