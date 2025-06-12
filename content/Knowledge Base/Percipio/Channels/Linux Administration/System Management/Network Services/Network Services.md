# Network Services

## 1. Dynamic Host Configuration Protocol (DHCP)

Dynamic Host Configuration Protocol (DHCP) simplifies IP address management by automating the configuration process for client devices on a network.

**DHCP Packet Flow:**

1. **Discovery:** A client device broadcasts a request on the local area network (LAN) to find available DHCP servers. Broadcasts do not cross routers; if no server exists on the LAN, the client cannot obtain an IP configuration.

2. **Offer:** The DHCP server responds with an IP configuration offer, selecting the appropriate address based on the client's request and its subnet.

3. **Acceptance:** The client accepts the offer, potentially with a lease expiration date. If the lease expires, the address may be returned to the server’s pool for reassignment.

4. **Acknowledgment:** The server acknowledges the acceptance, and the client can communicate on the network using the assigned IP address.

**Configuring DHCP on Ubuntu:**

To enable DHCP for IPv4 on Ubuntu:
- Access Network settings and select the Wired tab.
- Choose the IPv4 Method as "Automatic (DHCP)".

**Client-Side Configuration:**

For Debian-based distributions (like Ubuntu), set the `dhcp4` option to true in `/etc/netplan/<configuration_file>`. After editing, run `sudo netplan apply` to apply changes without rebooting.

**Setting Up a DHCP Server on Linux:**

1. Choose a DHCP server package (e.g., Kea).
2. Install with: `sudo apt install kea`.
3. Configure in `/etc/kea/kea-dhcp4.conf`, specifying the interfaces and subnet information for the IP pool.

Example configuration:
```json
{
  "interfaces": ["eth1"],
  "subnet": {
    "subnet": "192.168.4.0/24",
    "pool": [ ... ]
  }
}
```

Additional configurations may include lease duration, DNS server addresses, and default gateway settings.

**Security Considerations:**

- Evaluate the necessity of DHCP in secure environments. Using DHCP allows any device on the network to request an IP, which may pose a security risk.
- DHCP lacks authentication, meaning any device can connect and request an address.
- A compromised DHCP server could alter client configurations, leading to denial-of-service scenarios.

Balancing convenience and security is crucial when deciding to implement DHCP in a network.

## 2. Deploying a Linux DHCP Server

To install and configure a DHCP server on Ubuntu using the Kea DHCP server, follow these steps:

1. **Install Kea DHCP Server:**
   - Run the following command to install the Kea DHCP server:
     ```
     sudo apt install kea
     ```
   - Confirm the installation by typing `y` and pressing Enter.

2. **Navigate to Configuration Directory:**
   - Change to the Kea configuration directory:
     ```
     cd /etc/kea
     ```
   - List the contents to find `kea-dhcp4.conf`:
     ```
     ls
     ```

3. **Edit Configuration File:**
   - Open the DHCP configuration file:
     ```
     sudo nano kea-dhcp4.conf
     ```
   - Review the subnet and pool settings. Accept defaults or modify them as needed.

4. **Configure Option Data:**
   - Under the `option-data` section, specify the default gateway (router) IP address:
     ```json
     "data": "192.0.2.1"
     ```
   - To add DNS servers, append the following after the closing bracket of the router section:
     ```json
     {
       "name": "domain-name-servers",
       "data": ["IP_Address_1", "IP_Address_2"]
     }
     ```
   - Save changes with `Ctrl + S`, then confirm to write the file.

5. **Start the DHCP Server:**
   - Check the status of the DHCP server:
     ```
     sudo service kea-dhcp4-server status
     ```
   - If inactive, start the server:
     ```
     sudo service kea-dhcp4-server start
     ```
   - Confirm the server is active:
     ```
     sudo service kea-dhcp4-server status
     ```

6. **Log Management:**
   - To view logs related to the DHCP server, use:
     ```
     sudo journalctl -u kea-dhcp4-server
     ```
   - Alternatively, to search system logs:
     ```
     sudo cat /var/log/syslog | grep -i kea
     ```

At this point, you have a functional DHCP server configured to provide IP addresses to clients on your network.

## 3. Managing DHCP Client Settings in Linux

To work with the DHCP client side on Linux, specifically Ubuntu, follow these steps:

1. **Check Network Manager Status:**
   - Open a terminal and run:
     ```
     sudo service NetworkManager status
     ```
   - Ensure the service is active and running. Any error messages will help in troubleshooting.

2. **View System Logs:**
   - To check DHCP transactions, run:
     ```
     sudo cat /var/log/syslog | grep DHCP
     ```
   - Look for lease information and assigned IP addresses.

3. **Check Assigned IP Address:**
   - Use the command:
     ```
     ip a
     ```
   - Confirm that the IP address assigned matches the expected value.

4. **GUI Configuration:**
   - In the Ubuntu desktop environment, access network settings:
     - Search for "Network" and open "Network Connections."
   - Select your connection (e.g., "Wired connection 1") and check the IPv4 settings. Ensure it's set to "Automatic (DHCP)."
   - You can specify additional DNS servers if needed.

5. **View DNS Configuration:**
   - To see local DNS server settings, run:
     ```
     cat /etc/resolv.conf
     ```
   - To test DNS resolution, use:
     ```
     sudo nslookup www.skillsoft.com
     ```

6. **Ping and Troubleshooting:**
   - If DNS resolution works but pinging fails, it may indicate ICMP traffic is blocked:
     ```
     ping www.skillsoft.com
     ```
   - Stop the ping with `Ctrl + C`.

7. **Server Configuration:**
   - On an Ubuntu server, check for Network Manager:
     ```
     sudo service NetworkManager status
     ```
   - If not found, navigate to the Netplan configuration directory:
     ```
     cd /etc/netplan
     ls
     ```
   - Open the YAML configuration file to verify DHCP settings:
     ```
     cat 00-installer-config.yaml
     ```

8. **Verify DHCP Client Settings:**
   - Ensure `dhcp4` is set to `true` for the relevant interface.
   - Check the assigned IP address using:
     ```
     ip a
     ```

9. **Manually Trigger DHCP:**
   - To manually request a new IP configuration, use:
     ```
     sudo dhclient
     ```
   - To renew an existing lease:
     ```
     sudo dhclient -r ens33
     ```

By following these steps, you can effectively manage and troubleshoot DHCP client configurations on Ubuntu systems.

## 4. Domain Name System (DNS)

1. **DNS Basics**: DNS translates user-friendly domain names (like skillsoft.com) into IP addresses, which are necessary for routing internet traffic. It also allows for reverse lookups, where an IP address is mapped back to a domain name.

2. **DNS Zones vs. Domain Names**: A DNS domain name is simply the text label (e.g., skillsoft.com), while a zone refers to the configuration and records that support that name. Zone files contain various DNS records.

3. **Forward and Reverse Lookups**: Forward lookups resolve domain names to IP addresses using "A" records for IPv4 and "AAAA" records for IPv6. Reverse lookups use "PTR" records.

4. **DNS Record Types**:
   - **A Record**: Maps a domain name to an IPv4 address.
   - **AAAA Record**: Maps a domain name to an IPv6 address.
   - **MX Record**: Specifies mail servers for email delivery.
   - **CNAME Record**: Allows one domain to alias another.
   - **NS Record**: Indicates the authoritative DNS servers for a zone.
   - **SOA Record**: Contains metadata about the zone, like the primary name server and update information.
   - **TXT Record**: Can store arbitrary text, often used for verification purposes.

5. **DNS Configuration**: DNS settings can be configured in various operating systems. In Ubuntu, for instance, manual configurations can be done in the `/etc/netplan` directory.

6. **Security Considerations**: Hardening DNS servers is crucial to prevent attacks such as DNS spoofing or poisoning. Implementing DNSSEC can help ensure the integrity and authenticity of DNS responses.

7. **Monitoring and Anomalies**: Unusual DNS TXT queries can indicate security issues, and regular monitoring is essential to detect potential threats.

This overview captures the essential aspects of DNS and its critical role in network functionality and security. If you have any specific areas you’d like to delve deeper into or clarify further, just let me know!

## 5. Deploying a Linux DNS server 

1. **Update Package Repositories:**
   ```bash
   sudo apt update
   ```

2. **Install BIND:**
   ```bash
   sudo apt install bind9 bind9utils bind9-doc
   ```

3. **Check BIND Status:**
   ```bash
   sudo service bind9 status
   ```

4. **Configure BIND:**
   - Edit `named.conf.options` to set options like recursion and forwarders.
   - Edit `named.conf.local` to define your zone.

5. **Create Zone File:**
   - Create a directory for zones:
     ```bash
     sudo mkdir /etc/bind/zones
     ```
   - Copy the template zone file and edit it to match your requirements.

6. **Check Configurations:**
   ```bash
   sudo named-checkconf
   sudo named-checkzone sales.quick24x7.com /etc/bind/zones/db.sales.quick24x7.com
   ```

7. **Restart BIND:**
   ```bash
   sudo service bind9 restart
   ```

8. **Adjust Firewall (if necessary):**
   ```bash
   sudo ufw allow Bind9
   ```

### Additional Tips:

- **Backup Configurations:** Always back up your configuration files before making changes.
  
- **Logs:** Check the log files in `/var/log/syslog` for any errors or messages from BIND.

- **Testing DNS Queries:** Use `dig` or `nslookup` to test your DNS setup:
   ```bash
   dig @localhost sales.quick24x7.com
   ```

- **Security Practices:** Consider implementing DNSSEC for added security and configure access control lists (ACLs) if necessary.

- **Client Configuration:** In your next demo, remember to point your Linux client to the new DNS server by modifying `/etc/resolv.conf` or through your network configuration settings.

## 6. Configuring DNS in Linux 

1. **Check the Current DNS Configuration:**
   - Check the symbolic link and its target:
     ```bash
     ls -l /etc/resolv.conf
     ```
   - View current DNS settings:
     ```bash
     cat /etc/resolv.conf
     ```

2. **Edit Netplan Configuration:**
   - Open your Netplan YAML file:
     ```bash
     sudo nano /etc/netplan/*.yaml
     ```
   - Ensure DHCP is set to `no`, configure static IP, and specify DNS servers:
     ```yaml
     network:
       ethernets:
         ens33:
           dhcp4: no
           addresses: [192.168.2.156/24]
           routes:
             - to: 0.0.0.0/0
               via: 192.168.2.1
           nameservers:
             addresses: [192.168.2.156, 8.8.8.8]
     ```

3. **Apply the Changes:**
   - Apply your Netplan configuration:
     ```bash
     sudo netplan apply
     ```

4. **Verify DNS Configuration:**
   - Check DNS servers in use:
     ```bash
     sudo resolvectl status
     ```

5. **Test DNS Resolution:**
   - Ping a known domain:
     ```bash
     ping www.google.com
     ```
   - Use `nslookup` or `dig` for further verification:
     ```bash
     nslookup www.skillsoft.com
     dig www.skillsoft.com
     ```

### Additional Tips:

- **Netplan Syntax:** Remember to use spaces instead of tabs for indentation in YAML files. Incorrect spacing can lead to configuration errors.

- **Fallback on GUI Tools:** If using Ubuntu Desktop, the GUI offers options for DNS configuration under the network settings. Just navigate to the IPv4 settings and add DNS servers there, similar to the CLI method.

- **Troubleshooting DNS:** If you encounter issues with name resolution:
  - Ensure your DNS server is running properly.
  - Check firewall settings to ensure traffic on UDP port 53 is allowed.

- **Testing with `dig`:** The `dig` command is very useful for detailed DNS queries and can be used for both A records and other types, such as MX (Mail Exchange) or TXT records.

- **Using `systemd-resolved`:** Remember that Ubuntu often uses `systemd-resolved` for name resolution. If you need to disable or modify its behavior, you might look into its settings.

## 7. Network Time Protocol (NTP)

**Network Time Protocol (NTP)**

NTP is essential for synchronizing time across devices over a network. It operates over UDP port 123 and enables time synchronization between servers and clients, regardless of device type. Different Linux distributions may use varying NTP software packages, affecting command syntax and configuration files, but the core concept remains consistent.

**Time Sources and Clients**  
NTP servers can provide time to various clients, including Linux, Windows, macOS, smartphones, and network appliances. NTP employs a hierarchy of time sources, with reliable servers providing time to others.

**Importance of NTP**  
Accurate time synchronization is critical for:

- **Enterprise Operations**: Ensures correct timestamps for log files, audit files, and user log-ins, especially in systems like Microsoft Active Directory.
- **Network Services**: Services like DHCP depend on accurate time to manage IP address lease expirations.
- **Cybersecurity**: Accurate timestamps are vital for threat hunting and correlating events across platforms.
- **User Productivity**: Ensures that documents, invoices, and other files have correct timestamps.

**Linux Commands**  
Use the `timedatectl` command to set the local system date, time, and time zone. Running `timedatectl` without parameters returns the local time, time zone, synchronization status, and whether NTP is active.

**Configuring NTP on Ubuntu**  
Specify NTP sources in `/etc/system/timesyncd.conf`. You can also set the polling interval for checking synchronization.

To check the status of the NTP daemon, use:
```
systemctl status systemd-timesyncd
```
This will show whether it is active and the time server it is synchronizing with.

**Installing and Configuring NTP**  
While many NTP packages automatically point to public time sources, you can configure them for internal servers, especially in secure environments. 

For setting up an NTP server with Chrony, use:
```
sudo apt install chrony
sudo nano /etc/chrony/chrony.conf
sudo systemctl restart chrony.service
```

Additional NTP options include installing the NTP daemon or OpenNTP. 

Further demonstrations will cover the NTP server setup process.

## 8. How NTP works in Linux.

Start by issuing the `date` command to display the current date, time, and timezone information. It's crucial that all devices on the network agree on the time for accurate timestamps in log files and user documents.

Next, use the `timedatectl` command to check local date and time, universal time, and timezone information. This command will also indicate whether the system clock is synchronized and if NTP is active.

To check the status of the NTP service, run:
```
sudo service systemd-timesyncd status
```
This will show that NTP is active and that the daemon is running. Linux typically comes configured as an NTP client by default, synchronizing time with an internet time server.

To see available time zones, run:
```
sudo timedatectl list-timezones
```
You can filter the output by piping it to `grep`. For example, to find Canadian time zones, use:
```
sudo timedatectl list-timezones | grep -i Canada
```
To set the timezone, run:
```
sudo timedatectl set-timezone Canada/Atlantic
```
Setting the correct timezone is essential for accurate date and time stamps.

You can also install and configure an NTP server if needed. This is useful in an enterprise environment where you want to control time or in isolated networks that cannot connect to the internet. For instance, you can install Chrony:
```
sudo apt install chrony
```
After installation, check the daemon status:
```
sudo service chronyd status
```
This confirms that Chrony is running and actively communicating with a time source.

To configure Chrony, edit the configuration file:
```
sudo nano /etc/chrony/chrony.conf
```
This file references publicly available NTP time sources. You can specify your own sources if necessary.

To check the status of time sources, use:
```
chronyc activity
```
This command returns information about available time sources, such as:
```
200 OK 8 sources online
```

You can also check for client devices using:
```
chronyc clients
```
To see where your server is obtaining time, use:
```
chronyc sources
```
This will display a list of public NTP servers you are connected to for time synchronization. 

## 9. Configuring Secure Shell (SSH) in Linux

In this demonstration, I will configure SSH for secure command line access from one Linux host to a remote Linux server using public key authentication.

**Generating SSH Key Pair**  
1. **Open Terminal** on the client machine.
2. Check your current directory:
   ```bash
   pwd
   ```
   You should see your home directory (e.g., `/home/cblackwell`).

3. List all items, including hidden files:
   ```bash
   ls -a
   ```
   Verify the presence of the hidden `.ssh` directory.

4. Navigate to the `.ssh` directory:
   ```bash
   cd .ssh
   ```

5. Generate the SSH key pair:
   ```bash
   ssh-keygen
   ```
   - Accept the default path for the private key (`/home/cblackwell/.ssh/id_rsa`).
   - Set a passphrase to protect the private key.

6. Verify the generated keys:
   ```bash
   ls
   ```
   You should see `id_rsa` (private key) and `id_rsa.pub` (public key).

**Copying the Public Key to the Server**  
7. Use the `ssh-copy-id` command to transfer the public key:
   ```bash
   ssh-copy-id cblackwell@<remote_host>
   ```
   - Replace `<remote_host>` with the server’s name or IP address.
   - Confirm the authenticity of the server when prompted, and enter the password for the `cblackwell` account.

**Server-Side Verification**  
8. On the remote server, navigate to the `.ssh` directory:
   ```bash
   cd ~/.ssh
   ```

9. Check the `authorized_keys` file:
   ```bash
   cat authorized_keys
   ```
   The public key from your client machine should be listed here.

**Connecting to the Remote Server**  
10. To connect to the remote server in the future, use:
    ```bash
    ssh cblackwell@<remote_host>
    ```
    - Enter the passphrase for the private key when prompted.

11. Once logged in, verify the connection:
    ```bash
    ip a
    ```
    You should see the server's IP address (e.g., `192.168.2.156`).

12. To exit the SSH session, type:
    ```bash
    exit
    ```

You are now back on your local machine. This setup ensures secure, password-less SSH access as long as you have your private key and its passphrase.

## 10. Transferring Files Using SCP and SFTP

Great, let’s go over how to transfer files using SCP (Secure Copy Protocol) and SFTP (Secure File Transfer Protocol), as well as how to install and configure an Apache web server.

### Transferring Files with SCP

**1. Using SCP to Copy Files from Server to Client:**

- Start on your Ubuntu Linux server. Check your current directory:
  ```bash
  pwd
  ```
- List the files in the `projects` directory:
  ```bash
  ls projects
  ```

- Switch to your client machine (where you are logged in as `cblackwell`). Check your working directory:
  ```bash
  pwd
  ```

- Use the `scp` command to copy a file from the server to your client:
  ```bash
  scp cblackwell@<server_ip>:/home/cblackwell/projects/Project_A.txt .
  ```

- After the transfer, confirm the file is there:
  ```bash
  ls
  ```

- For the second file, `Project_B.txt`, run:
  ```bash
  scp cblackwell@<server_ip>:/home/cblackwell/projects/Project_B.txt .
  ```
  You’ll be prompted for the passphrase to unlock your private key.

- To copy an entire directory recursively, use:
  ```bash
  scp -r cblackwell@<server_ip>:/home/cblackwell/projects ./projects
  ```
  Verify the files in your local `projects` directory:
  ```bash
  ls projects
  ```

### Transferring Files with SFTP

**2. Using SFTP for Interactive File Transfers:**

- Start an SFTP session:
  ```bash
  sftp cblackwell@<server_ip>
  ```

- Within the SFTP prompt, check your remote working directory:
  ```bash
  pwd
  ```

- List files on the remote server:
  ```bash
  ls
  ```

- To check your local working directory:
  ```bash
  lpwd
  ```

- To upload a local file:
  ```bash
  put sample_local_file.txt
  ```

- Confirm the upload:
  ```bash
  ls
  ```

- To download a file from the server:
  ```bash
  get filelist.txt
  ```

- Exit the SFTP session:
  ```bash
  exit
  ```

### Installing and Configuring an Apache Web Server

**3. Setting Up Apache:**

- Update the package list:
  ```bash
  sudo apt update
  ```

- Install the Apache2 web server:
  ```bash
  sudo apt install apache2
  ```

- Check the status of Apache:
  ```bash
  sudo service apache2 status
  ```

- Start the Apache service:
  ```bash
  sudo service apache2 start
  ```

- Allow HTTP traffic through the firewall:
  ```bash
  sudo ufw allow 80/tcp
  ```

- Check the Apache configuration file:
  ```bash
  sudo nano /etc/apache2/apache2.conf
  ```
  Note that Apache references other configuration files, such as `ports.conf`.

- Verify the default listening port:
  ```bash
  cat /etc/apache2/ports.conf
  ```

- Check the web root directory:
  ```bash
  ls /var/www/html
  ```

- Find your server's IP address:
  ```bash
  ip a
  ```

- Test the Apache server from a web browser by entering the server's IP address. You should see the Apache2 default page.

### Conclusion

You now have a solid understanding of how to transfer files securely between Linux hosts using SCP and SFTP, as well as how to install and configure an Apache web server. This setup enables secure file transfer and web hosting capabilities on your Linux servers.