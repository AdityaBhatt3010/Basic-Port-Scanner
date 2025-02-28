import socket
import termcolor

def scan(target, start_port, end_port):
    # Scans the given target for open ports within the specified range.
    print(termcolor.colored(f"\n[+] Starting Scan For {target}", 'cyan'))
    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            open_ports.append(port)

    if not open_ports:
        print(termcolor.colored("[-] No open ports found. All ports are closed.", 'red'))
    else:
        print(termcolor.colored(f"[+] Open Ports: {', '.join(map(str, open_ports))}", 'green'))


def scan_port(ip_address, port):
    # Attempts to connect to a port on the given IP address.
    # Returns True if the port is open, otherwise False.
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout to avoid long waiting
        sock.connect((ip_address, port))
        print(termcolor.colored(f"[+] Port {port} is Open", 'green'))
        sock.close()
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False


def main():
    # Main function to handle user input and initiate scanning.
    targets = input("[*] Enter Targets To Scan (comma-separated): ")
    port_range = input("[*] Enter Port Range to Scan (for example, 1-1000 or just press default first thousand ports): ")

    # Parse port range input
    if '-' in port_range:
        try:
            start_port, end_port = map(int, port_range.split('-'))
        except ValueError:
            print(termcolor.colored("[-] Invalid port range format. Using default (1-1000).", 'yellow'))
            start_port, end_port = 1, 1000
    else:
        try:
            end_port = int(port_range) if port_range else 1000
            start_port = 1  # Default start port
        except ValueError:
            print(termcolor.colored("[-] Invalid input. Using default (1-1000).", 'yellow'))
            start_port, end_port = 1, 1000

    # Scan each target
    if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", 'blue'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), start_port, end_port)
    else:
        scan(targets.strip(), start_port, end_port)


if __name__ == "__main__":
    main()
