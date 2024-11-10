
import socket

print("Welcome to DNS Lookup")
print("Enter your option: 1. URL to IP 2. IP to URL")

# Using input() instead of raw_input() for Python 3
op = input('Enter Option (1 or 2): ')
var = input('Enter URL/IP: ')

try:
    if op == '1':  # Compare with string '1'
        addr1 = socket.gethostbyname(var)
        print(f"IP Address: {addr1}")

    elif op == '2':  # Compare with string '2'
        addr6 = socket.gethostbyaddr(var)
        print(f"Hostname: {addr6[0]}, Aliases: {addr6[1]}, IP Addresses: {addr6[2]}")

    else:
        print("Invalid option. Please enter 1 or 2.")

except socket.gaierror:
    print("Error: Unable to resolve the given URL/IP.")
except Exception as e:
    print(f"An error occurred: {e}")