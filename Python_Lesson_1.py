
# Python Fundamental - Lesson 1
# Variables, Data Types, f-string and if/else
#Network Automation Learning Journey

hostname = "Steve-Router-1"
ip_address = "10.1.1.1"
vendor = "Cisco"
number_of_interfaces = 24
cpu_usage = 37.5
device_status = True

print(hostname)
print(ip_address)
print(vendor)
print(number_of_interfaces)
print(cpu_usage)
print(device_status)
print(type(hostname))
print(type(ip_address))
print(type(vendor))
print(type(number_of_interfaces))
print(type(cpu_usage))
print(type(device_status))
print(f"{hostname} | IP: {ip_address} | Interfaces {number_of_interfaces} | CPU: {cpu_usage}% | Status: {device_status}")

if device_status:
    print("Device Status: UP")

else:
    print("Device Status: DOWN")  

if cpu_usage < 70:
    print("CPU Status: NORMAL")

else
    print("CPU Status: HIGH")  
