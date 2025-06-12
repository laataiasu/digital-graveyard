# File Systems & Permissions Management

## 1. Video: IP Addressing (it_oslsys_04_enus_02)

### IPv4 Addressing
- **Definition**: IPv4 uses 32-bit IP addresses, represented in dotted decimal notation (e.g., 192.126.128.190).
- **Structure**: Four octets (8 bits each) separated by dots; each octet ranges from 0 to 255.
- **OSI Model**: Maps to Layer 3 (Network Layer) of the OSI model, involved in IP routing and addressing.
- **Reserved Ranges**: 
  - 10.0.0.0 to 10.255.255.255
  - 172.16.0.0 to 172.31.255.255
  - 192.168.0.0 to 192.168.255.255
- **Subnet Masks**: Defines network vs. host portions of an IP address.
  - Example: 255.255.255.0 indicates the first three octets are the network portion.
  - CIDR notation: /24 (indicates 24 bits are used for the network).

### IPv6 Addressing
- **Definition**: IPv6 addresses are 128 bits long, represented in hexadecimal format.
- **Structure**: Separated by colons (e.g., fe80::20c:29ff).
- **Hexadecimal**: Uses base 16 (0-9, A-F) for representation.
- **Subnet Mask**: Represented in CIDR notation (e.g., /64).

---

## 2. Video: Common Linux Networking Commands (it_oslsys_04_enus_03)

### Overview of Commands
- Mastery of network configurations and statistics from the command line is essential for Linux technicians.

### Common Commands
- **ifconfig**: Older command for configuring network interfaces.
  - `ifconfig -a`: Lists all active network configurations.
  - `ifconfig eth0 up`: Brings the eth0 interface up.
- **ip**: Modern command for managing network interfaces.
  - `ip -4 a`: Displays IPv4 addresses.
  - `ip a`: Shows all IP addresses (IPv4 and IPv6).
  - `ip a add <IP_address>/<mask> dev <interface>`: Assigns an IP address temporarily.

### Additional Commands
- **hostname**: Displays the local machine name.
- **arp**: Manages ARP cache, showing IP-MAC address mappings.
- **route**: Views and manages the IP routing table.
- **traceroute**: Shows the path traffic takes to a specified target.
- **dig & nslookup**: DNS resolution tools; nslookup has an interactive mode.
- **curl**: Transfers data over protocols like FTP and HTTP.
- **wget**: Downloads files from the web.
- **netstat**: Monitors network connections and listening sockets.
- **nc (netcat)**: Transfers data over network connections (TCP/UDP).

### Command Usage Examples
- `hostname`: Returns the hostname.
- `ip -6 a`: Returns IPv6 information.
- `netstat | grep ssh`: Checks if the SSH service is listening on a port.
- `wget <URL>`: Downloads a file from the specified URL.


## 1. Managing Linux Network Interfaces and IP Addressing

### ifconfig Command
- Use `ifconfig` to manage network interfaces.
- If not installed, run: 
  ```
  sudo apt install ifconfig
  ```

### Interface Information
- Displays interfaces, e.g., `ens33` (Ethernet) and `lo` (Loopback).
- Loopback address: 
  - IPv4: `127.0.0.1`
  - IPv6: `::1`
- Ethernet interface example:
  - IPv4 address: `<address>`
  - Subnet mask: `255.255.255.0`
  - IPv6 link-local address: starts with `fe80`
  - Prefix length: `/64`

### Managing Interfaces
- To bring an interface up or down:
  ```
  sudo ifconfig ens33 up
  sudo ifconfig ens33 down
  ```

### IP Address Command
- Use `ip a` for a listing of interfaces and IP information.
- To add an IP address:
  ```
  ip a add 200.1.1.1/24 dev ens33
  ```
- Note: Changes are not persistent after reboot.

### Configuring Persistent Settings
- For Ubuntu, edit `/etc/netplan/<config_file>` using:
  ```
  sudo nano /etc/netplan/<config_file>
  ```
- Example config directives:
  ```
  network:
    ethernets:
      ens33:
        dhcp4: true
  ```
- For static IP, set `dhcp4` to `false` and specify `addresses`, `gateway`, and `nameservers`.
- Apply changes:
  ```
  sudo netplan apply
  ```

### Testing Connectivity
- Use `ping` to check connectivity:
  ```
  ping 8.8.8.8
  ```
- Stop pinging with `Ctrl+C`.

### Tracing Route
- Use `traceroute` to see the path to a destination:
  ```
  traceroute 8.8.8.8
  ```

### Viewing Network Statistics
- Use `netstat` to see active connections:
  ```
  netstat
  netstat | grep ssh
  ```

---

## 2. Network Routing

### Importance of Network Routing
- Routing directs traffic efficiently across routers to reach specific hosts.
- Involves devices with multiple interfaces, including routers and computers.

### Routing Basics
- Routers consult their routing tables to direct traffic.
- Default route in IPv4: `0.0.0.0`, typically pointing to the local gateway (e.g., `192.168.2.1`).

### Packet Flow Example
- Traffic sent from client to router, which consults its routing table.
- The path may involve multiple routers and interfaces.
- IP packets have a Time to Live (TTL) that decrements with each hop.

### Linux Routing Commands
- View routing table:
  ```
  route
  ip route show
  ```
- Add a default gateway:
  ```
  route add default gw <gateway_ip>
  ```
- Add a specific host route:
  ```
  route add -host <host_ip> reject
  ```

### Making Routes Persistent
- Edit `/etc/netplan/<config_file>` for persistent routes:
  ```
  routes:
    - to: <target_network>
      via: <gateway_ip>
      metric: <value>
  ```
- Ensure correct metric values for routing efficiency.

### Conclusion
- Understanding routing is essential for managing Linux hosts and troubleshooting network issues.