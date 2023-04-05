import socket
import pyperclip

domain = input("Enter a domain name: ")
try:
    ip = socket.gethostbyname(domain)
    pyperclip.copy(ip)
    print(f"The IP address of {domain} is {ip}, and it has been copied to the clipboard.")
except socket.gaierror:
    print("Error: could not resolve domain name.")
