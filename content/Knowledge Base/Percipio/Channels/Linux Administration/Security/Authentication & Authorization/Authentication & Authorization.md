# Authentication & Authorization

## 1. Authentication and Authorization

In this video, we discuss the roles of authentication and authorization in accessing resources in Linux.

**Authentication**
- Definition: Proof of identity.
- Methods:
  - Username and password (local or centralized, e.g., LDAP, cloud).
  - Single-factor authentication: One category of authentication (e.g., something you know).
  - Multi-factor authentication (MFA): Combines different factors:
    - Something you know (e.g., username, password).
    - Something you have (e.g., key fob, smart card).
    - Something you are (e.g., biometrics like fingerprints or facial recognition).
    - Gesture-based authentication: Movement or pattern recognition.

**Authorization**
- Grants specific access to resources (e.g., using `chmod` for file permissions).
- Can involve access to services such as confidential emails, VPNs, or web applications.

**Cloud Authentication**
- In environments like Microsoft Azure, centralized authentication can be managed using Azure Active Directory (AD).
- Allows for seamless user authentication across multiple Linux virtual machines without configuring each machine individually.
- Use of service principals and managed identities to authenticate software and manage permissions without hardcoding credentials.

**Multi-Factor Authentication (MFA) in Azure AD**
- User settings show MFA status as disabled, enabled, or enforced.
  - Enabled: MFA is turned on, but the user has not yet configured it.
  - Enforced: User has signed in, configured MFA, and is actively using it.
- MFA enhances security by making accounts harder to compromise compared to single-factor authentication.

**Linux Pluggable Authentication Modules (PAM)**
- Purpose: Separates authentication tasks from applications, allowing centralized management.
- PAM modules can be indirectly configured when setting up services like Secure Shell (SSH).
- Configuration files for various services are located in `/etc/pam.d`, allowing the integration of authentication without embedding it in applications directly.

## 2. Pluggable Authentication Modules (PAM)

Let’s explore Pluggable Authentication Modules (PAM) in Linux.

**PAM Overview**
- PAM is a built-in subsystem in all Linux distributions that separates authentication tasks from the main functions of applications (e.g., serving web pages or handling SSH connections).
- It acts as an intermediary between applications that require security services and the underlying security mechanisms.

**Key Functions of PAM**
- Manages account verification, user logins, password updates, and security audits.
- Typically, Linux technicians do not configure PAM directly, except in specific scenarios (e.g., when setting up LDAP for centralized authentication).

**PAM Library Files**
- PAM modules generally have a `.so` extension.
- Example modules include:
  - `pam_nologin.so`: Restricts logins for non-root users.
  - `pam_ftp.so`: Manages FTP access.

**PAM Configuration**
- Configuration files are located in `/etc/pam.d`.
- Common files include:
  - `common-account`: Modified for LDAP authentication.
  - Other files for services like `cron`, `login`, `passwd`, and `sudo`.

**PAM Configuration Syntax**
- Format: 
  ```
  module_type control_flag module_name [module_arguments]
  ```
  - **Module Type**: Specifies the task type (e.g., account).
  - **Control Flag**: Determines the outcome if authentication fails (e.g., `required` means all listed modules must succeed).
  - **Module Name**: The specific PAM module (e.g., `pam_nologin.so`).
  - **Module Arguments**: Additional parameters to control module behavior.

**Example: Denying SSH Access**
- To deny SSH access to specific users, add the following line to `/etc/pam.d/sshd`:
  ```
  auth required pam_listfile.so onerr=succeed item=user sense=deny file=/etc/ssh/deniedusers
  ```
  - This line checks against a specified file (`/etc/ssh/deniedusers`) and denies access if a listed username is found.

**Creating the Denied Users File**
- Create `/etc/ssh/deniedusers` and list usernames (one per line) that should be blocked from SSH access.

**Result of Denial**
- If a user listed in the `deniedusers` file attempts to log in via SSH, they will receive an "Access denied" message, even if the correct password is entered. 

This concise approach to PAM provides a framework for managing authentication processes effectively within Linux systems.

## 3. Managing Linux User Accounts and Password Settings

Here’s a streamlined overview of working with user accounts in Linux, focusing on both GUI and command-line methods.

**Managing User Accounts via GUI (Ubuntu Desktop)**
1. Open the application menu and search for "Users."
2. Click on "Users" to access the settings.
   - View current user account (e.g., Codey Blackwell).
   - Change password or view account activity.
3. To manage additional accounts, click "Unlock" and enter the account password.
4. After unlocking, you can add a new user:
   - Click "Add User."
   - Choose account type (Standard or Administrator).
   - Enter Full Name and Username (e.g., Lucas Brenner).
   - Set password options: either allow the user to set a password at next login or set it now.

**Managing User Accounts via Command Line**
1. Create a user with:
   ```bash
   sudo useradd -m jgold -g eastadmins
   ```
   - Use `-m` to create a home directory.
   - Specify the primary group with `-g`.
   - Note: If the group does not exist, create it first with:
   ```bash
   sudo groupadd eastadmins
   ```

2. Set a password for the new user:
   ```bash
   sudo passwd jgold
   ```

3. Verify user creation:
   - Check `/etc/passwd` for user details.
   - Check `/etc/shadow` for password hash.

4. Manage file ownership:
   - Change file owner:
   ```bash
   sudo chown jgold /scripts/script1.sh
   ```
   - Verify ownership with:
   ```bash
   ll /scripts
   ```

5. Add user to a group:
   - Create a group:
   ```bash
   sudo groupadd linuxadmins
   ```
   - Change the user's primary group:
   ```bash
   sudo usermod -g linuxadmins jgold
   ```

6. Switch user:
   - Use `su` to switch to another user:
   ```bash
   su - jgold
   ```
   - Verify current user with:
   ```bash
   id
   ```

7. Delete a user:
   ```bash
   sudo userdel jgold
   ```

**Conclusion**
This guide provides foundational commands and steps for managing user accounts in Linux, utilizing both graphical and command-line interfaces.

## 4. Creating and Managing Linux Groups

Here's a concise overview of managing Linux groups from the command line, highlighting key commands and concepts:

### Managing Linux Groups from the Command Line

1. **View Current Groups**:
   - To check existing groups, view the `/etc/group` file:
     ```bash
     sudo tail /etc/group
     ```

2. **Create a New Group**:
   - Use `groupadd` to create a new group (e.g., `linuxadmins`):
     ```bash
     sudo groupadd linuxadmins
     ```

3. **Create a New User and Assign to a Group**:
   - Create a new user (e.g., `jgold`) and assign them to `linuxadmins`:
     ```bash
     sudo useradd -m -g linuxadmins jgold
     ```

4. **Verify User Creation**:
   - Check the user details in `/etc/passwd`:
     ```bash
     sudo cat /etc/passwd | grep jgold
     ```

5. **Change User’s Primary Group**:
   - Create another group (e.g., `eastadmins`) and change `jgold`'s primary group:
     ```bash
     sudo groupadd eastadmins
     sudo usermod -g eastadmins jgold
     ```

6. **Add User to Additional Groups**:
   - To add `jgold` to multiple groups without changing the primary group:
     ```bash
     sudo usermod -aG linuxadmins,fulltimers jgold
     ```

7. **View Group Membership**:
   - Check group memberships:
     ```bash
     sudo cat /etc/group | grep jgold
     ```

8. **Rename a Group**:
   - Use `groupmod` to rename a group:
     ```bash
     sudo groupmod -n fulltimeemployees fulltimers
     ```

9. **Remove a User from a Group**:
   - Use `gpasswd` to remove a user from a specific group:
     ```bash
     sudo gpasswd -d jgold fulltimeemployees
     ```

10. **Delete a Group**:
    - To delete an entire group:
      ```bash
      sudo groupdel fulltimeemployees
      ```

### Summary
This guide provides essential commands for managing groups in Linux. From creating and modifying groups to managing user memberships, these commands facilitate effective group administration.

## 5. Viewing and Managing Linux User Configuration Files

Here’s a summarized overview of working with Linux user configuration files, highlighting key concepts and commands.

### Working with Linux User Configuration Files

1. **User Account Information**:
   - User accounts are stored in the `/etc/passwd` file:
     ```bash
     sudo tail /etc/passwd
     ```
   - Each entry contains the username, password placeholder, user ID (UID), primary group ID (GID), user information, home directory, and shell.

2. **Group Information**:
   - Group details can be found in the `/etc/group` file:
     ```bash
     sudo tail /etc/group
     ```
   - This file shows group names, GIDs, and members.

3. **Switching Users**:
   - Use `su - <username>` to switch to another user with a full login:
     ```bash
     su - jgold
     ```

4. **File Creation and Permissions**:
   - When a user creates a file, the user is the owner, and the primary group becomes the group owner:
     ```bash
     touch file1.txt
     ls -l
     ```

5. **Changing Default Shell**:
   - To change a user’s shell from `/bin/sh` to `/bin/bash`, edit `/etc/passwd`:
     ```bash
     sudo nano /etc/passwd
     ```
   - Modify the user’s entry accordingly.

6. **Shadow Password File**:
   - The `/etc/shadow` file stores hashed passwords:
     ```bash
     sudo tail /etc/shadow
     ```
   - To lock or unlock a user account:
     ```bash
     sudo passwd -l jgold   # Lock
     sudo passwd -u jgold   # Unlock
     ```

7. **Skeleton Directory**:
   - The `/etc/skel` directory contains files that will be copied to new user home directories:
     ```bash
     ls /etc/skel
     ```
   - To create a new user and populate their home directory with files from `/etc/skel`:
     ```bash
     sudo useradd -m cjackson
     ```

### Summary
Understanding these configuration files and their interactions is crucial for effective user and group management in a Linux environment. From user account creation to customizing home directories, this knowledge allows for smoother administration and user experience.

## 6. Using sudo to Gain Elevated Privileges

Here's a concise summary of configuring and using `sudo` in Linux, based on your demo.

### Configuring `sudo` in Linux

1. **Purpose of `sudo`**:
   - `sudo` (short for "superuser do") allows regular users to execute commands with elevated privileges without logging in as the root user. This enhances security and accountability.

2. **Basic Usage**:
   - To check user permissions, run:
     ```bash
     id
     ```
   - Running a command that requires elevated privileges, such as:
     ```bash
     fdisk -l
     ```
   - Without `sudo`, you might see "Permission denied." Using `sudo`:
     ```bash
     sudo fdisk -l
     ```

3. **Configuration Files**:
   - **Main configuration**: `/etc/sudoers`
     - View with:
       ```bash
       sudo cat /etc/sudoers
       ```
   - **Syntax breakdown**:
     ```
     user host=(target_user:target_group) command
     ```
     - `user`: User or group (prefix with `%` for groups).
     - `host`: From which host the command can be run (ALL means any).
     - `(target_user:target_group)`: Specify the user or group to run as.
     - `command`: Which commands the user can run.

4. **Editing the Sudoers File**:
   - Always use `visudo` to edit the sudoers file:
     ```bash
     sudo visudo
     ```
   - This prevents syntax errors that could lock you out of sudo access.

5. **Adding User Permissions**:
   - To allow user `jgold` to run `fdisk`, add the following line under the user privilege specification:
     ```
     jgold ALL=(ALL) /usr/sbin/fdisk
     ```
   - Save and exit `visudo`.

6. **Testing Permissions**:
   - Switch to `jgold`:
     ```bash
     su - jgold
     ```
   - Try running:
     ```bash
     fdisk -l
     ```
     - Expect "Permission denied."
   - Now, run:
     ```bash
     sudo fdisk -l
     ```
     - Enter `jgold`'s password to execute the command.

7. **Finding Binaries**:
   - To locate where a command is stored, use:
     ```bash
     whereis fdisk
     ```

### Summary
Using `sudo` allows for secure management of user privileges, letting administrators grant specific command access to regular users. Always edit the sudoers file with `visudo` to prevent configuration errors. This approach promotes accountability and minimizes risks associated with using the root account directly.

## 7. Linux Remote Management

Here's a summary of key points regarding remote management of Linux hosts, focusing on command line and GUI tools, as well as secure practices:

### Remote Management of Linux Hosts

1. **Overview**:
   - Remote management is crucial for Linux technicians to administer servers effectively, whether they are on-premises or cloud-based.

2. **Network Exposure**:
   - Avoid exposing Linux virtual machines (VMs) directly to the Internet.
   - Use a **jump box** (a server with both public and private interfaces) to access internal hosts without public IP exposure.
   - Consider whether root should have SSH access, typically restricting it for security reasons.

3. **Connection Considerations**:
   - Use a **VPN** for secure access to internal networks.
   - Decide on connection methods based on the environment (cloud vs. on-premises).

4. **Common Remote Management Tools**:
   - **SSH (Secure Shell)**: The standard for secure command-line access, enabling secure file transfers and X forwarding for GUI applications.
   - **VNC**: A GUI-based tool for managing Linux hosts with a graphical interface.
   - **SCP (Secure Copy)** and **SFTP**: Secure methods for transferring files between hosts.
   - **Deprecated Tools**: Avoid using older, insecure tools like telnet and rlogin, which transmit data in plain text.

5. **SSH Public Key Authentication**:
   - Preferred over password-based authentication for security.
   - Each user generates a public/private key pair:
     - The **private key** (stored securely on the technician's workstation) must be protected and never shared.
     - The **public key** (can be shared) must be placed in the `~/.ssh/authorized_keys` file on the remote server.
   - Key generation example:
     ```bash
     ssh-keygen -t rsa
     ```

6. **Connecting via SSH**:
   - When a connection is made, the user may be prompted for a passphrase protecting the private key, not the user account password on the server.

7. **Cloud-based Linux VM Management**:
   - Platforms like Microsoft Azure offer options to reset passwords and SSH keys for Linux VMs.
   - Admins can reset the SSH public key through the cloud interface if access is lost.

### Summary
Efficiently managing Linux hosts remotely requires a strong understanding of secure practices, effective tools, and network architecture. Utilizing SSH with public key authentication is crucial for security, while understanding the implications of network exposure and using appropriate tools enhances management capabilities.

## 8. Secure Shell (SSH) Port Forwarding and Tunneling

Here's a concise overview of SSH tunneling and its variations, focusing on local and remote port forwarding, as well as dynamic port forwarding:

### SSH Tunneling Overview

1. **Definition**:
   - SSH tunneling creates a secure, encrypted connection over which traffic can be sent, similar to a VPN but specifically for SSH.

2. **Local Port Forwarding**:
   - **Purpose**: Forwards traffic from a local port to a specified port on a remote server.
   - **Use Case**: Useful for accessing services behind firewalls that allow SSH but block other ports.
   - **Example Command**:
     ```bash
     ssh -L local_port:remote_host:remote_port user@sshserver
     ```
   - **Diagram Explanation**:
     - The SSH client listens on a local port (e.g., port 80) and forwards incoming traffic to the SSH server where a service (like Apache) is running on the specified port (e.g., port 80).

3. **Remote (Reverse) Port Forwarding**:
   - **Purpose**: Forwards traffic from a port on the remote SSH server back to a specified port on the local SSH client.
   - **Use Case**: Useful for making a service running on a local client machine accessible to users on the internet via the SSH server.
   - **Example Command**:
     ```bash
     ssh -R remote_port:localhost:local_port user@sshserver
     ```
   - **Diagram Explanation**:
     - Internet users connect to the SSH server on a remote port (e.g., port 80), which then forwards the traffic back through the SSH tunnel to the local machine's specified port (e.g., port 2000).

4. **Dynamic Port Forwarding**:
   - **Purpose**: Similar to local port forwarding but designed for applications that require a SOCKS proxy.
   - **Use Case**: Allows multiple types of traffic through a single connection, useful for applications that need to connect through a proxy.
   - **Example Command**:
     ```bash
     ssh -D local_port user@sshserver
     ```

5. **Configuration Considerations**:
   - To enable remote port forwarding on the SSH server, the `GatewayPorts` option must be configured in the SSH server's configuration file (typically `/etc/ssh/sshd_config`).

### Summary
SSH tunneling provides flexible options for securely managing connections and services. Local port forwarding allows access to remote services, remote port forwarding enables external access to local services, and dynamic port forwarding serves as a proxy. Proper configuration and understanding of these methods are essential for effective remote management of Linux hosts.

## 9. Configuring SSH Remote Management

Here's a streamlined overview of configuring SSH remote management using public key authentication, as demonstrated in your scenario:

### Configuring SSH Remote Management with Public Key Authentication

1. **Overview**:
   - SSH (Secure Shell) is used for securely managing Linux hosts over a network, replacing less secure protocols like Telnet and rlogin.

2. **Setting Up on the Client**:
   - Begin on the client machine (e.g., Ubuntu2) where the technician will initiate the SSH connection.
   - Switch to the user account intended for SSH access (e.g., `jgold`):
     ```bash
     su - jgold
     ```
   - Confirm you're in the correct home directory:
     ```bash
     pwd  # Should display /home/jgold
     ```

3. **Generating SSH Key Pair**:
   - Use the `ssh-keygen` command to create a public/private RSA key pair:
     ```bash
     ssh-keygen -t rsa
     ```
   - Accept the default location (`~/.ssh/id_rsa`) for the private key and set a passphrase for added security.
   - Verify the key files:
     ```bash
     ls -a ~/.ssh
     ```
   - You should see `id_rsa` (private key) and `id_rsa.pub` (public key).

4. **Copying the Public Key to the Server**:
   - Use the `ssh-copy-id` command to transfer the public key to the target server (e.g., Ubuntu1 with IP `10.0.0.4`):
     ```bash
     ssh-copy-id jgold@10.0.0.4
     ```
   - When prompted, confirm the server's fingerprint and enter the password for `jgold` on the target server.

5. **Verifying Key Installation**:
   - On the target server (Ubuntu1), check the `authorized_keys` file in the `.ssh` directory:
     ```bash
     ls -a /home/jgold/.ssh
     cat /home/jgold/.ssh/authorized_keys
     ```
   - Ensure your public key is listed in this file.

6. **Connecting to the Server**:
   - Now, initiate the SSH connection:
     ```bash
     ssh jgold@10.0.0.4
     ```
   - Enter the passphrase for your private key when prompted (not the password for `jgold` on the server).
   - You should now be logged into the remote server, indicated by a change in the command prompt.

7. **Conclusion**:
   - You've successfully set up SSH remote management using public key authentication, enhancing security by requiring possession of the private key along with the username.

This process establishes a secure, encrypted connection for remote management and can greatly reduce the risk of unauthorized access compared to traditional password-based methods.

## 10. Installing and Configuring an LDAP Server

Here’s a structured overview of your LDAP server installation and configuration demonstration:

### Installing and Configuring an LDAP Server

**Overview of LDAP**:
- **LDAP** (Lightweight Directory Access Protocol) is a protocol used to access and manage directory information over a network, typically through TCP port **389** (unencrypted) or **636** (encrypted).

#### Step 1: Prepare the Server

1. **Set Hostname**:
   ```bash
   sudo hostnamectl set-hostname ubuntu1
   ```

2. **Update `/etc/hosts`**:
   - Open the hosts file:
   ```bash
   sudo nano /etc/hosts
   ```
   - Add the following line (or update existing):
   ```
   10.0.0.4 ubuntu1
   ```

#### Step 2: Install LDAP Components

3. **Install LDAP Packages**:
   ```bash
   sudo apt install slapd ldap-utils
   ```
   - Confirm installation by typing **Y**.

4. **Set Administrator Password**:
   - During installation, enter a password for the LDAP admin account and confirm it.

#### Step 3: Verify Installation

5. **Check LDAP Configuration**:
   ```bash
   sudo slapcat
   ```
   - This should show basic LDAP information, including the distinguished name (DN).

6. **Check Service Status**:
   ```bash
   sudo service slapd status
   ```
   - Ensure the service is active and running.

#### Step 4: Configure LDAP

7. **Reconfigure LDAP**:
   ```bash
   sudo dpkg-reconfigure slapd
   ```
   - Follow prompts:
     - Omit OpenLDAP server configuration? **No**
     - DNS domain name: **quick24x7.local**
     - Organization name: **quick24x7**
     - Set admin password.
     - Confirm the database removal option as **No**.
     - Move old database? **Yes**

8. **Verify the New Configuration**:
   ```bash
   sudo slapcat
   ```
   - Check for the new DN: `dc=quick24x7,dc=local`.

#### Step 5: Update LDAP Configuration File

9. **Edit LDAP Configuration**:
   ```bash
   sudo nano /etc/ldap/ldap.conf
   ```
   - Update settings:
     - Uncomment the `BASE` line and set to:
       ```
       BASE dc=quick24x7,dc=local
       ```
     - Uncomment and set the `URI` line to:
       ```
       URI ldap://ubuntu1:389
       ```

10. **Test LDAP Search**:
    ```bash
    sudo ldapsearch -x
    ```
    - Ensure the server responds correctly.

#### Step 6: Add Organizational Unit (OU)

11. **Create LDIF File**:
    ```bash
    sudo nano ou.ldif
    ```
    - Add the following content to define a new OU:
    ```
    dn: ou=hq,dc=quick24x7,dc=local
    objectClass: top
    objectClass: organizationalUnit
    ou: hq
    ```

12. **Add the OU to LDAP Directory**:
    ```bash
    sudo ldapadd -x -D "cn=admin,dc=quick24x7,dc=local" -W -f ou.ldif
    ```
    - Enter the LDAP admin password when prompted.

#### Step 7: Verify the New OU

13. **Check Entries with slapcat**:
    ```bash
    sudo slapcat
    ```
    - Look for the new OU entry in the output.

14. **Verify with ldapsearch**:
    ```bash
    sudo ldapsearch -x
    ```
    - Confirm that the `hq` OU is listed in the results.

### Conclusion
You have successfully installed and configured an LDAP server, created an organizational unit, and verified your setup. In future demonstrations, you can explore setting up LDAP clients to utilize this centralized directory for user authentication.

## 11. Configuring LDAP Client Authentication

Here’s a structured overview of your LDAP client installation and configuration demonstration:

### Installing and Configuring an LDAP Client

**Overview of LDAP Client**:
- An LDAP client allows devices to authenticate users against a centralized LDAP server instead of relying on local accounts. This streamlines user management across multiple systems.

#### Step 1: Prepare the Environment

1. **Ping the LDAP Server**:
   ```bash
   ping ubuntu1
   ```
   - Ensure the LDAP server responds. If not, check for firewall issues.

2. **Check LDAP Server Status**:
   ```bash
   sudo service slapd status
   ```
   - Verify that the OpenLDAP Server Daemon is active.

3. **View LDAP Directory**:
   ```bash
   sudo slapcat
   ```
   - Confirm existing objects in the directory, including user accounts and organizational units (OUs).

#### Step 2: Install Required Packages

4. **Install LDAP Client Packages**:
   ```bash
   sudo apt install libnss-ldapd libpam-ldapd ldap-utils -y
   ```
   - This installs necessary libraries and utilities for LDAP client functionality.

#### Step 3: Configure LDAP Client

5. **Configure LDAP Settings**:
   - During the installation, provide the following:
     - **LDAP server URI**: `ldap://ubuntu1`
     - **Search base**: `dc=quick24x7,dc=local`

6. **Specify LDAP Services**:
   - Ensure to configure the `passwd`, `group`, and `shadow` services to use LDAP.

7. **Update PAM Configuration**:
   - Edit `/etc/pam.d/common-session`:
   ```bash
   sudo nano /etc/pam.d/common-session
   ```
   - Add the following line to enable home directory creation:
   ```
   session optional pam_mkhomedir.so skel=/etc/skel umask=077
   ```

8. **Restart Client Daemons**:
   - Restart the necessary services:
   ```bash
   sudo systemctl restart nscd nslcd
   ```

#### Step 4: Test LDAP User Authentication

9. **Verify User Creation**:
   - Check for local user accounts:
   ```bash
   sudo cat /etc/passwd | grep ldapuser1
   ```
   - You should not see a local entry for `ldapuser1`.

10. **Switch to LDAP User**:
    - Attempt to switch to the LDAP user account:
    ```bash
    su - ldapuser1
    ```
    - Enter the password for `ldapuser1` when prompted.

11. **Verify Home Directory**:
    - Upon successful login, check that a home directory for `ldapuser1` has been created under `/home`.

### Conclusion
You have successfully installed and configured an LDAP client on your Linux host, allowing it to authenticate users against the centralized LDAP server. This setup simplifies user management across multiple machines by relying on a single user account for each user.