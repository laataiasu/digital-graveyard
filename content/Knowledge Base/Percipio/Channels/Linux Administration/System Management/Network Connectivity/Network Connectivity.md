# Network Connectivity

## 1. IP Addressing

Managing network components in a Linux environment involves understanding IPv4 and IPv6 addressing.

**IPv4 Addressing**
- **Structure**: IPv4 uses 32-bit addresses, represented in dotted decimal notation as four octets (e.g., 192.126.128.190). Each octet is 8 bits, and the decimal value ranges from 0 to 255.
- **Special Addresses**: Certain ranges are reserved for internal use:
  - 10.0.0.0 to 10.255.255.255
  - 172.16.0.0 to 172.31.255.255
  - 192.168.0.0 to 192.168.255.255
- **Subnet Masks**: When configuring an IP address, a subnet mask defines the network and host portions of the address. 
  - Example: A subnet mask of 255.255.255.0 indicates the first three octets represent the network.
  - CIDR notation can also be used (e.g., /24 represents the same network mask).

**IPv6 Addressing**
- **Structure**: IPv6 addresses are 128 bits long, represented in hexadecimal format separated by colons (e.g., fe80::20c:29ff).
- **Hexadecimal Representation**: Uses base 16, where values range from 0-9 and A-F (e.g., A = 10, F = 15). 
- **Subnet Masks**: Similar to IPv4, represented in CIDR notation (e.g., /64).

Understanding both IPv4 and IPv6 is essential for a Linux technician today.

## 2. Common Linux Networking Commands

Common Linux networking commands are essential for configuring network settings and viewing statistics from the command line. Here’s an overview of key commands and concepts:

**Network Interfaces**
- Common interface names:
  - `lo`: Local loopback interface.
  - `eth0`, `eth1`: Ethernet interfaces.
  - `ens33`: Alternate naming convention for Ethernet.
  - `wlan0`, `wlan1`: Wireless interfaces.

**Network Configuration Commands**
1. **ifconfig** (older command):
   - `ifconfig -a`: List all active network configurations.
   - `ifconfig eth0`: View configuration for eth0.
   - `ifconfig eth0 up`: Bring the interface up.
   - `ifconfig eth0 down`: Bring the interface down.
   - Assign a static IP: `ifconfig eth0 <IP_ADDRESS> netmask <NETMASK>`.

2. **ip** (modern command):
   - `ip -4 a`: Show IPv4 addressing information.
   - `ip -6 a`: Show IPv6 addressing information.
   - `ip a`: Display all IP addressing (IPv4 and IPv6).
   - `ip a show eth0`: Show details for eth0.
   - Add an IP address: `ip a add <IP_ADDRESS>/<MASK> dev eth0`.

**Additional Commands**
- **hostname**: Displays the local machine name.
- **arp**: View/manage the ARP cache, which maps IP addresses to MAC addresses.
- **route**: View/manage the IP routing table.
- **traceroute**: Shows the route taken by packets to a target.
- **dig** and **nslookup**: Tools for DNS name resolution; `nslookup` has an interactive mode.
- **curl**: Transfer data over protocols like FTP and HTTP.
- **get**: Another command for transferring data.
- **netstat**: Monitor network connections and listening sockets.
- **nc** (netcat): Transfer data over TCP or UDP.
- **wget**: Download files from specified URLs.

Mastering these commands is crucial for effective Linux network management.

## 3. Managing Linux Network Interfaces and IP Addressing

In this demonstration, we will explore Linux commands for managing network interfaces and IP addressing.

**ifconfig Command**
- Use `ifconfig` to view network interfaces.
- If not installed, run `sudo apt install ifconfig`.
- Example output shows:
  - `ens33`: Local Ethernet interface.
  - `lo`: Local loopback interface with IP 127.0.0.1 (IPv6: ::1).
  - Link-local IPv6 addresses start with `fe80`.
  - MAC address and packet statistics are also displayed.
  
To bring an interface up or down:
- `sudo ifconfig ens33 up`
- `sudo ifconfig ens33 down` (be cautious when connected via SSH).

**ip Command**
- Use `ip a` to list all interfaces and their addresses.
- To add an IP address temporarily: `ip a add <IP_ADDRESS>/<CIDR> dev ens33` (e.g., `ip a add 200.1.1.1/24 dev ens33`).

**Persistent Network Configuration**
- Navigate to `/etc/netplan` and open the config file with `sudo nano <config_file>`.
- Example configuration:
  ```yaml
  network:
    ethernets:
      ens33:
        dhcp4: true  # Change to false for static IP
        addresses: [<STATIC_IP_ADDRESS>]
        gateway4: <DEFAULT_GATEWAY>
        nameservers:
          addresses: [<DNS_SERVER1>, <DNS_SERVER2>]
  ```
- Apply changes with `sudo netplan apply`.

**Network Testing Commands**
1. **ping**: Test connectivity to an IP address.
   - Example: `ping 8.8.8.8` (stop with Ctrl+C).
  
2. **traceroute**: Trace the path to a target IP address.
   - Example: `traceroute 8.8.8.8`.

3. **netstat**: View current socket connections.
   - Use `netstat` alone for all connections.
   - Filter for specific services: `netstat | grep ssh`.

These commands are essential for effective network management in a Linux environment.

## 4. Network Routing

Network routing ensures that traffic destined for a specific host travels through the most efficient path, often across multiple routers. Here are the key concepts:

- **Routers**: Devices that connect different networks, typically with at least two network interfaces. They can be dedicated hardware or computers with multiple network interface cards (NICs) and IP routing enabled.

- **Routing Tables**: Each device on the network, including clients, has a routing table that helps determine the next hop for traffic. For IPv4, a default route is represented as `0.0.0.0`, pointing to the default gateway (e.g., `192.168.2.1`).

- **Traffic Flow**: When a client sends traffic to a destination, it first checks its routing table. If no specific route is found, it uses the default route to reach the local router. The local router then checks its routing table to determine how to forward the traffic, possibly sending it to another router.

- **TTL (Time to Live)**: An IP packet includes a TTL field that decrements with each router it passes through, limiting the number of routers the packet can traverse.

**Routing Types**:
- **Static Routing**: Manually entered routes in the routing table, manageable only for small networks.
- **Dynamic Routing**: Protocols like RIP, OSPF, and EIGRP allow routers to share routing information automatically, updating routing tables across networks.

**Linux Routing Commands**:
- **View Routing Table**: Use `route` or `ip route show` to display the current routing table.
- **Add Default Gateway**: Use `route add default gw <IP_ADDRESS>` or `ip route add default via <IP_ADDRESS>`.
- **Add Host Route**: Use `route add -host <IP_ADDRESS>` or `ip route add <NETWORK_ADDRESS>/<MASK> dev <INTERFACE>`.

**Traceroute Command**: Use `traceroute <IP_ADDRESS>` to see the path your traffic takes through the network.

**Making Routes Persistent**:
- For Ubuntu, modify `/etc/netplan/<config_file>` to add persistent routes:
  ```yaml
  routes:
    - to: <TARGET_NETWORK>
      via: <GATEWAY_IP>
      metric: <VALUE>
  ```

Understanding these concepts and commands is essential for Linux technicians to configure and troubleshoot network traffic effectively.

## 5. Configuring Linux Routing in the Linux OS

Here's a concise guide on configuring Linux routing using the `route` command and managing routing tables with Netplan.

### Configuring Linux Routing

1. **View Current Routing Table**:
   You can display the routing table using either of these commands:
   ```bash
   route
   ip route show
   ```

2. **Adding a Route**:
   To direct traffic to a specific network through a designated gateway, use the following command:
   ```bash
   sudo ip route add 200.1.1.0/24 via 192.168.2.90 dev ens33
   ```
   - This command routes traffic destined for `200.1.1.0/24` through the gateway `192.168.2.90` using the interface `ens33`.

3. **Verify the Route Addition**:
   After adding a route, confirm it by running:
   ```bash
   ip route show
   ```
   You should see the new route listed.

4. **Deleting a Route**:
   To remove a route, use:
   ```bash
   sudo ip route delete 200.1.1.0/24
   ```
   - Run `ip route show` again to verify that the route has been removed.

5. **Making Routes Persistent**:
   To ensure routes persist after a reboot, you'll need to modify a configuration file.

   - Navigate to the Netplan directory:
     ```bash
     cd /etc/netplan
     ```

   - Open the configuration file (e.g., `00-installer-config.yaml`):
     ```bash
     sudo nano 00-installer-config.yaml
     ```

   - Add a routes section, ensuring proper indentation with spaces (not tabs):
     ```yaml
     routes:
       - to: 200.1.1.0/24
         via: 192.168.2.90
     ```

   - Save the file and apply the changes:
     ```bash
     sudo netplan apply
     ```

6. **Check Routes Again**:
   After applying the Netplan configuration, confirm that your routes are correctly set:
   ```bash
   ip route show
   ```

### Important Notes
- **Syntax Sensitivity**: Be cautious with YAML indentation; use spaces and ensure proper alignment.
- **Routing Tables**: Understanding how to manipulate routing tables is crucial for network configuration and troubleshooting.

This guide should help you effectively manage Linux routing configurations using the `route` command and Netplan!

## 6. Configuring Linux Routing in the Cloud

Here’s a concise guide on configuring routing for Linux virtual machines in Microsoft Azure, highlighting the key steps involved in setting up a route table and associating it with a subnet.

### Configuring Linux Routing in Microsoft Azure

1. **Access the Azure Portal**:
   - Sign in to the Azure portal and navigate to the **Virtual Machines** section.

2. **Select Your Virtual Machine**:
   - Click on the virtual machine (e.g., **Ubuntu1**) to view its settings.
   - Go to the **Networking** section to check its network configuration.

3. **Inspect the Virtual Network and Subnet**:
   - Identify the virtual network (e.g., **Ubuntu1-vnet**) and subnet (e.g., **default**) the VM is connected to.
   - Click on the subnet link to view its properties and IPv4 address range.

4. **Create a Route Table**:
   - From the Azure home page, click on **Create a resource** and search for **Route Table**.
   - Click on **Route Table**, then **Create**.
   - Fill in the details: select a resource group (e.g., **HQ**), specify a name (e.g., **eastroutetable1**), and choose a region (e.g., **East US**). 
   - Click **Review + create** and then **Create**.

5. **Add Routes to the Route Table**:
   - After creation, navigate to the route table properties and click on **Routes**.
   - Click **Add** to create a new route. For example:
     - **Route name**: SendOutboundTrafficToFW
     - **Destination type**: IP Addresses
     - **Destination IP address**: `0.0.0.0/0` (captures all traffic)
     - **Next hop type**: Virtual appliance
     - **Next hop address**: (e.g., the internal IP of a firewall, e.g., `10.0.0.100`).
   - Click **Add** to save the route.

6. **Associate the Route Table with a Subnet**:
   - In the route table settings, click on **Subnets** and then **Associate**.
   - Choose the virtual network (e.g., **Ubuntu1-vnet**) and the subnet (e.g., **default**) to associate the route table.
   - Click **OK** to complete the association.

7. **Verify Association**:
   - Return to the subnet properties to confirm that the route table (e.g., **eastroutetable1**) is now associated with the subnet.

### Summary
By following these steps, you configure routing for Linux virtual machines in Azure, ensuring that all VMs in the subnet route traffic through a specified firewall or virtual appliance. This setup enhances traffic control and security for your cloud environment.

## 7. Capturing and Analyzing Network Traffic Using tcpdump

Here's a streamlined guide to using `tcpdump` in Linux for capturing and analyzing network traffic:

### Using `tcpdump` for Network Traffic Analysis

#### 1. **Check Network Interfaces**
Before using `tcpdump`, identify the active network interfaces:
```bash
ip a
```
Note the interface you want to monitor (e.g., `ens33`).

#### 2. **Capture Traffic**
To capture network traffic on a specific interface:
```bash
sudo tcpdump -i ens33 -v
```
- `-i ens33`: specifies the interface.
- `-v`: provides verbose output.

Press `Ctrl+C` to stop the capture.

#### 3. **Write to a File**
To save captured packets to a file:
```bash
sudo tcpdump -i ens33 -v -w packetcapture1.pcap
```
This will create a file named `packetcapture1.pcap` in the current directory.

#### 4. **Read from a Capture File**
To read and analyze the saved capture:
```bash
sudo tcpdump -r packetcapture1.pcap
```

#### 5. **Filter Captured Traffic**
You can filter captured traffic to focus on specific hosts, ports, or protocols.

- **Capture traffic from a specific host:**
```bash
sudo tcpdump -i ens33 host 192.168.2.11 -v
```

- **Capture traffic destined for a specific host:**
```bash
sudo tcpdump -i ens33 dst 192.168.2.11 -v -w hostfilter.pcap
```

- **Filter by protocol (e.g., ICMP):**
```bash
sudo tcpdump -i ens33 -v -n icmp
```

- **Capture traffic on a specific port (e.g., port 22 for SSH):**
```bash
sudo tcpdump -i ens33 -v port 22
```

#### 6. **Using `grep` for Further Filtering**
You can pipe the output of a read command through `grep` to search for specific terms:
```bash
sudo tcpdump -r hostfilter.pcap | grep netbios
```

#### 7. **Explore More Options**
For comprehensive options and filters available with `tcpdump`, refer to the manual:
```bash
man tcpdump
```

### Summary
`tcpdump` is a powerful tool for network analysis in Linux. By capturing, filtering, and reviewing traffic, you can troubleshoot network issues effectively.

## 8. Capturing and Analyzing Network Traffic Using Wireshark

Here's a concise guide on how to analyze network traffic using Wireshark, based on your description:

### Capturing and Analyzing Network Traffic with Wireshark

#### 1. **Introduction to Wireshark**
- **Wireshark** is a free, open-source packet capturing and network analysis tool available on multiple platforms (Windows, Linux, macOS).
- It helps troubleshoot network issues and audit traffic.

#### 2. **Starting Wireshark**
- Launch Wireshark. The interface includes a menu bar with options like **File, Edit, View, Capture**, and more.
- Identify the network interface you want to capture traffic from (e.g., Wi-Fi, Ethernet).

#### 3. **Capturing Traffic**
- Double-click the network interface to start capturing packets.
- Wireshark will display captured packets in a list with columns for **No., Time, Source, Destination, Protocol, Length, and Info**.

#### 4. **Stopping the Capture**
- Click the **Stop** button to halt the capturing process.

#### 5. **Examining Packet Details**
- Select a packet to view its details in the packet headers.
  - **Ethernet II Header**: Contains MAC addresses (Layer 2).
  - **IP Header**: Contains source/destination IP addresses (Layer 3).
  - **TCP Header**: Shows source/destination port numbers (e.g., port 443 for HTTPS).

#### 6. **Applying Display Filters**
- Use the display filter bar to refine the displayed packets.
  - Example: To filter for HTTPS traffic, type `tcp.port == 443` and press Enter.
- You can also filter by protocol (e.g., `ftp`).

#### 7. **Saving Captured Data**
- Save your packet capture for later analysis via the **File** menu.

#### 8. **Analyzing Credentials and Sensitive Data**
- Be cautious: protocols like **FTP** and **Telnet** transmit credentials in clear text.
- For instance, you might see usernames and passwords during analysis, highlighting the need for secure protocols (like SSH) instead.

#### 9. **Using Follow TCP Stream**
- To simplify analysis, select a packet and navigate to **Analyze > Follow > TCP Stream**.
- This shows the entire conversation in a single view, making it easier to understand the interaction.

#### 10. **Using tcpdump with Wireshark**
- You can capture packets using `tcpdump` in Linux and save them to a `.pcap` file.
- Open this file in Wireshark for analysis.

### Conclusion
Wireshark is a powerful tool for analyzing network traffic. By capturing packets, applying filters, and examining detailed headers, you can troubleshoot network issues effectively and identify potential security vulnerabilities. Always prefer secure protocols to protect sensitive data.

## 9. Sychronizing Files Between Hosts Using rsync

Here's a concise summary of how to use `rsync` for file synchronization between Linux hosts, based on your description:

### Synchronizing Files Between Linux Hosts with `rsync`

#### 1. **Introduction to `rsync`**
- `rsync` is a powerful tool for copying and synchronizing files and directories between local and remote systems over SSH.

#### 2. **Checking Current Files**
- Start by checking the current directory and its contents on the source machine:
  ```bash
  pwd        # Show current directory
  ls        # List files and directories
  ```

#### 3. **Reviewing `rsync` Options**
- Use the `man rsync` command to explore various options:
  - `-a`: Archive mode (preserves permissions, timestamps, etc.)
  - `-r`: Recursively copy directories.
  - `-v`: Verbose output.
  - Additional options include `-H`, `-p`, `-A`, `-o`, and `-g` for preserving hard links, permissions, ACLs, and ownership.

#### 4. **Verifying Network and SSH Connection**
- Check the server's IP address:
  ```bash
  ip a
  ```
- Ensure the SSH daemon is running:
  ```bash
  sudo service sshd status
  ```
- Test connectivity by pinging the server from the client:
  ```bash
  ping 192.168.2.42
  ```

#### 5. **Using `rsync` to Sync Files**
- On the client machine, use the `rsync` command to pull files from the server:
  ```bash
  rsync -arv cblackwell@192.168.2.42:/home/cblackwell/ ubuntu_server_files/
  ```
- This command synchronizes the home directory of `cblackwell` from the server to a directory named `ubuntu_server_files` on the client.

#### 6. **Checking the Results**
- After running `rsync`, navigate to the `ubuntu_server_files` directory and check the contents:
  ```bash
  cd ubuntu_server_files
  ls -a       # Show all files, including hidden ones
  ```

#### 7. **Incremental Updates**
- If you run the `rsync` command again without changes on the server, it will show "receiving incremental file list" but won’t copy anything.
- Modify a file on the server (e.g., add a line in `Project_A.txt`), then run `rsync` again to see it only sync changed files.

#### 8. **Scheduling with Cron Jobs**
- Consider setting up a cron job to automate periodic synchronization with `rsync`.

### Conclusion
Using `rsync` allows efficient file synchronization between Linux hosts, minimizing data transfer by only updating changed files. This makes it an ideal choice for backups and file mirroring.

