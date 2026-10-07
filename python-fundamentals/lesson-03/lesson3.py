# Python Fundamentals - Lesson 3
# Dictionaries
# Network Automation Learning Journey

device = {
    "hostname": "CORE-RTR-01",
    "ip_address": "10.10.10.1",
    "vendor": "cisco",
    "device_type": "router",
    "ios_version": "17.9.4",
    "status": "UP"

}

device2 ={
    "hostname": "CORE-SW-01",
    "ip_address": "10.10.10.10",
    "vendor": "cisco",
    "device_type": "switch",
    "ios_version": "17.12.4",
    "status": "DOWN"
    }

devices =[device, device2]

for device in devices:
    if device["status"] == "UP":
        print(f"{device['hostname']} | {device['ip_address']} | {device['vendor']} | {device['status']}") 
    else:
        print(f"{device['hostname']} | {device['ip_address']} | {device['vendor']} | DOWN - CHECK DEVICE ")





