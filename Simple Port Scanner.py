#Importing necessary libraries
import socket

#Common ports and services
common_ports = {
    20: "FTP (data transfer)",
    21: "FTP (control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    636: "LDAPS",
    989: "FTPS (data)",
    990: "FTPS (control)",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    8080: "HTTP-Proxy"
    }


#function definition
def scan_ports(host, start_port, end_port):
    print(f"scanning {host} from port {start_port} to {end_port}...\n")

#The for loop
    for port in range(start_port, end_port + 1): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) #half second timer
        result = sock.connect_ex((host, port)) #returns 0 if open
        if result == 0:
            service = common_ports.get(port, "Unknown service")
            print(f"Port {port}: OPEN ({service})")
        sock.close()
        #The else is implied, it just skips it, not outputting anything if the result is != 0

if __name__ == "__main__":
    target = input("Enter host to scan (e.g., '127.0.0.1' or 'scanme.nmpa.org'): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))


    scan_ports(target, start, end)
