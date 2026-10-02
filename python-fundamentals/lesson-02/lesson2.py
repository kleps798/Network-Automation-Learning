# Python Fundamentals - Lesson 2
# Lists and Indexing
# Network Automation Journey

devices = ["router1", "router2", "switch1", "firewall1"]
print(devices)
print(devices[2])
print(devices[3])
print(len(devices))
devices.append("router3")
print(devices)
print(len(devices))

for device in devices:
    print(device)

# Using f string

hostname = "router1"
ip_address = "10.10.10.2"
vendor = "cisco"


print(f"{hostname} | {ip_address} | {vendor}")   

for device in devices:
    print(f"Device: {device}")