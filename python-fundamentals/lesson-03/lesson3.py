# Python Fundamentals - Lesson 3
# Dictionaries
# Network Automation Learning Journey

device = {
    "hostname": "CORE-RTR-01",
    "ip_address": "10.10.10.1",
    "vendor": "cisco",
    "device_type": "router"

}

print(device["hostname"])
print(device["vendor"])
print(device["device_type"])
print(f"The {device['hostname']} has an IP Address of {device['ip_address']} and the vendor is {device['vendor']} with device type {device['device_type']} ")

