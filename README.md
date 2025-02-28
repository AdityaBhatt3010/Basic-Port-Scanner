# Basic Port Scanner

## Description
The **Optimized Port Scanner** is a Python-based network scanning tool that efficiently checks for open ports on a given target IP address or multiple IPs. It allows users to specify a range of ports to scan, defaults to scanning ports 1-1000 if not specified, and provides a user-friendly output using colors.

## Features
- Supports scanning single or multiple IP addresses.
- Allows users to define a specific port range.
- Uses socket timeout to speed up the scanning process.
- Displays open ports in a structured and readable format.
- Outputs a message if no open ports are found.
- Colored output for better visibility.

## Requirements
Ensure you have Python installed along with the required dependency termcolor.

To install it run the command as follows:
```sh
pip install termcolor
```

Alternatively, simply run:
```sh
pip install -r requirements.txt
```

## Usage
1. Run the script:
   ```sh
   python PortScanner.py
   ```
2. Enter the target IP addresses (comma-separated for multiple targets):
   ```
   [*] Enter Targets To Scan (comma-separated): 192.168.1.1,192.168.1.2
   ```
3. Enter the port range to scan (or press enter for default 1-1000):
   ```
   [*] Enter Port Range to Scan (e.g., 1-1000 or just press enter for 1-1000): 1-500
   ```

## Example Output
```
[+] Starting Scan For 192.168.1.1
[+] Port 22 is Open
[+] Port 80 is Open
[+] Open Ports: 22, 80
```

If no open ports are found:
```
[-] No open ports found. All ports are closed.
```

## Screenshots
### Scan Result with Open Ports:
![Open Ports](https://github.com/user-attachments/assets/24d23272-e48d-44dc-af82-57db8536cede) <br/>

### Scan Result with All Ports Closed:
![Closed Ports](https://github.com/user-attachments/assets/860acf67-87ca-4069-910f-568eff37a583) <br/>

## Author
Developed by Aditya Bhatt.

