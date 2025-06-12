# Installation & File System Navigation

## 1. Overview of Linux

Linux is built on the foundation of older Unix operating systems, which means it shares many similarities. If you have experience with Unix, transitioning to Linux will be relatively straightforward. Developed by Linus Torvalds in the early 1990s, Linux comes in various distributions, often referred to as "distros." Most of these distros are free and open-source, though some may charge for downloads or support, primarily for security updates.

Distributions can be categorized into server versions, such as Ubuntu Server, and workstation versions, which typically include end-user productivity software and graphical desktop environments like Ubuntu Desktop. Additionally, specialized distributions are embedded in firmware for various devices, including IoT devices, elevators, and commercial security systems.

**Key Components of Linux**

1. **Linux Kernel**  
   The kernel is the core of the Linux operating system. When you apply updates, you may update either software packages or the kernel itself. It is essential to check which kernel version your documentation refers to, as configurations and troubleshooting methods can vary by version.

   - The kernel starts an initial process called `init`, located in the `/sbin` directory, which always has a process ID of 1. This is the first process launched by the kernel.

2. **Shared Libraries**  
   Linux relies on shared library files, typically found in the `/var/lib` directory. These binary files support various software packages and system components. Subdirectories often organize libraries for different software packages.

3. **Configuration Files**  
   Configuration files are usually located in the `/etc` directory. These can be individual files or grouped in subdirectories for specific software. Most configuration files are text files, allowing you to edit them using text editors like `vi`, `vim`, or `nano`. While not a strict rule, configuration files often have a `.conf` extension. 

   - Changes to configuration files usually require a restart of the associated daemon, although some daemons allow for a quicker reload of settings.

4. **Daemons**  
   Daemons are background processes that operate independently of user sessions. For instance, an Apache web server will run related daemons in the background. Similar to Windows services, daemons start automatically and may require specific user permissions.

   - To manage daemons, you can use commands like `service sshd status` to check the status of the SSH daemon. Other commands include `service sshd start` to start it and `service sshd stop` to terminate it.

5. **Command Line Tools**  
   Managing Linux can be done through command line tools. Different shell environments are specified in user account configuration files, allowing various command line shells (e.g., Bash, Korn shell, C shell) to load upon sign-in.

6. **Graphical User Interface (GUI)**  
   Some Linux distributions offer a GUI based on the X Window System, which can be started with the `startx` command. Remote X forwarding allows GUI applications on a Linux machine to be accessed from a Windows desktop through SSH. Popular desktop environments include GNOME and KDE.

**Conclusion**

This overview highlights the essential components of Linux and how they interact. From the kernel and shared libraries to configuration files, daemons, command line tools, and graphical user interfaces, understanding these elements is crucial for effectively managing and utilizing the Linux operating system.

## 2. Understanding Linux Distributions

Linux distributions (or "distros") are variations of the Linux operating system, often based on core distros like Debian, Red Hat, and SUSE. Over time, many specialized Linux distributions have emerged to cater to specific needs, such as industrial applications, music and video production, cybersecurity, and penetration testing.

The abundance of Linux distributions can be attributed to the open-source nature of the Linux kernel. This allows developers to build entire operating systems at little to no cost, mainly requiring time investment. Many new distributions are based on existing ones, enabling users to modify and improve them while sharing their changes with the open-source community.

While many distributions share similarities, they may differ in graphical user interfaces (GUIs), available software packages, and customization options. If you are familiar with one distribution, much of that knowledge will carry over to others.

**Common Linux Distributions and Their Use Cases**

1. **Debian**  
   A foundational Linux operating system, Debian serves as the base for many other distros, including Ubuntu.

2. **Ubuntu**  
   Based on Debian, Ubuntu is user-friendly and popular among newcomers. It offers both desktop and server versions.

3. **Fedora**  
   Known for incorporating the latest features and technologies, Fedora is often used by developers and tech enthusiasts.

4. **Arch Linux**  
   A minimalist distribution that allows for deep customization and is ideal for experienced users.

5. **SUSE Linux**  
   This distribution is often used in enterprise environments, known for its stability and support.

6. **Kali Linux**  
   Previously known as "Linux Auditor," Kali is a specialized distribution focused on cybersecurity and penetration testing, packed with various tools for security professionals.

7. **64 Studio**  
   Designed for media production, 64 Studio includes specialized kernel modules for audio recording and high-quality video editing.

8. **AsteroidOS**  
   Aimed at smartwatches, AsteroidOS provides features for tracking fitness metrics and other health data.

9. **Audio File Distributions**  
   These distros are optimized for high-fidelity sound and are perfect for audiophiles who require superior audio quality.

10. **Apertis**  
   Used in modern vehicles for infotainment systems, Apertis integrates features like GPS, environmental controls, and media options.

11. **Raspbian**  
   Tailored for Raspberry Pi devices, Raspbian supports various applications such as gaming, robotics, and video surveillance.

**Using Linux Distributions**

You don't need to be a software developer to benefit from Linux distributions. Most are available as prepackaged, open-source solutions that you can download and use freely. While some software may require payment, the core components of many distributions are available at no cost. This accessibility makes Linux a versatile choice for both personal and business environments.

## 3. BIOS, UEFI, and the Linux Startup Process

The Linux startup process begins with the BIOS or UEFI, which are essential firmware interfaces. The BIOS, located on the motherboard or peripheral cards, initializes hardware and prepares the system for booting. It manages tasks such as retaining system time and memory configuration.

UEFI, the successor to BIOS, offers enhanced features like Secure Boot, which ensures that only trusted operating system files can boot. It supports a graphical user interface for configuration and can handle larger disks compared to BIOS.

**Linux Runlevels**

Runlevels define the operational state of a Linux system. Key runlevels include:

- **0**: Shutdown
- **1**: Single-user mode (rescue mode)
- **3**: Multi-user mode without GUI
- **5**: Multi-user mode with GUI
- **6**: Reboot

The current runlevel can be checked using the `runlevel` command. You can change runlevels using commands like `sudo init 0` (shutdown) or `sudo init 6` (reboot).

**The Linux Startup Process**

1. **Initialization**: The system begins with BIOS or UEFI, which loads the Master Boot Record (MBR) into memory. The MBR contains the boot code for the operating system.

2. **GRUB Bootloader**: The MBR loads the GRUB (Grand Unified Bootloader), which reads its configuration file (`/boot/grub/grub.cfg`). GRUB can present a boot menu for multi-boot systems or emergency options.

3. **Kernel Loading**: After selecting an OS from the GRUB menu, the compressed Linux kernel (named `vmlinuz`) is loaded. The `mkinitrd` command is used to create the initial RAM disk (initrd), which is necessary for mounting the root filesystem.

4. **Starting the Init Process**: The `init` process, with a process ID of 1, is launched. It establishes a temporary RAM disk until the kernel is fully operational. The kernel then determines the default startup runlevel and launches the appropriate scripts.

5. **Runlevel Configuration**: As the system enters a specific runlevel, the startup scripts located in directories like `/etc/rc3.d` are executed. Scripts starting with "S" initiate services, while those with "K" stop services.

**Using Commands for Configuration**

- **`dracut`**: This utility is used for creating and managing the initramfs, which helps with the startup process.
- **`mkinitrd`**: Creates the initial RAM disk to mount the root filesystem.
- **`vmlinuz`**: Refers to the compressed Linux kernel.
- **GRUB Bootloader**: Manages the booting of the operating system and offers options for startup configuration.

**Secure Boot and TPM**

UEFI Secure Boot ensures that only digitally signed operating system files are loaded. It works with the Trusted Platform Module (TPM), which stores cryptographic keys used for disk encryption. If the OS disk is encrypted, a user may need to enter a PIN during boot for decryption.

For older Linux distributions that may not support Secure Boot, you might need to disable this feature for compatibility.

Understanding the interaction between Linux, BIOS, and UEFI, as well as mastering related commands, will enhance your ability to configure and troubleshoot Linux systems effectively.

## 4. Linux Installation Sources

1. **ISO Images**: 
   - Downloadable from the internet, ISO images can be burned to DVD or used to create bootable USB drives. They are commonly used for installing Linux on physical or virtual machines.

2. **USB Drives**: 
   - A popular method for installation, USB drives can be formatted and made bootable with a Linux distribution's ISO image, allowing easy installation on various machines.

3. **Hard Disk Drives**: 
   - If you have pre-existing installation files on a hard disk or a separate partition, you can boot from there to install Linux.

4. **PXE Boot**: 
   - PXE allows computers to boot from a network interface instead of local storage. This is particularly useful for deploying installations across multiple machines in a network environment, pulling installation files from a PXE server.

5. **Virtual Machines**: 
   - You can install Linux on virtual machines using pre-installed images, making setup quick and straightforward.

6. **Scripted Installations**: 
   - These involve running pre-configured scripts during installation to automate the setup process. Different distributions have their own methods, such as Ubuntu’s autoinstall and Red Hat's Kickstart.

7. **Cloud Templates**: 
   - In cloud environments like AWS or Azure, infrastructure as code allows you to use templates to automate the deployment of Linux servers.

**Manual vs. Automated Installation**

- **Manual Installation**: Involves a hands-on approach, where the user specifies installation options such as language, keyboard layout, and network settings during the setup process.

- **Automated Installation**: Utilizes pre-defined scripts or network boot methods to streamline the installation process, making it faster and reducing manual input.

**Summary of Key Boot Sources**

- **ISO Images**: Download and use for physical or virtual installations.
- **USB Drives**: Convenient for quick installations.
- **Hard Disk Drives**: Can be used if files are stored locally.
- **PXE Boot**: Enables network-based installations, ideal for larger deployments.
- **Virtual Machines**: Simplifies testing and deployment.
- **Cloud Templates**: Automate deployment in cloud environments.

By understanding these various boot sources and installation methods, you’ll be better equipped to install and configure Linux systems in a variety of environments.

## 5. Installing a Linux Server

### Step 1: Download the ISO Image
1. **Choose Your Distribution**: Visit the official website of the Linux distribution you want to install (e.g., Ubuntu, Red Hat, SUSE).
2. **Download the ISO**: Navigate to the downloads section and click the button to download the server ISO image. Save it to your local downloads folder.

### Step 2: Set Up a Virtual Machine (If Installing Virtually)
1. **Open Virtualization Software**: Launch your virtualization tool (e.g., VMware Workstation, VirtualBox).
2. **Create a New Virtual Machine**:
   - Select **Typical** setup.
   - Choose **Install from ISO** and browse to select the downloaded ISO file.
3. **Configure VM Settings**:
   - Name your VM and select a storage location.
   - Specify the amount of RAM, virtual CPUs, and disk space (e.g., 80 GB).
   - Customize the network settings (e.g., bridge to your network).

### Step 3: Boot from the ISO
1. **Power On the VM**: Start the virtual machine, which should boot from the ISO automatically.
2. **Select Installation Option**: Choose "Try or Install" from the boot menu.

### Step 4: Installation Process
1. **Language Selection**: Choose your preferred language for the installation.
2. **Keyboard Layout**: Select the keyboard layout you want to use.
3. **Installation Type**: Choose "Install Ubuntu Server" (or equivalent for other distributions).
4. **Network Configuration**: Accept the default DHCP settings to automatically obtain an IP address.
5. **Mirror Selection**: Use the default package mirror for downloading installation packages.

### Step 5: Disk Setup
1. **Storage Layout**: Choose to use the entire disk (default option) for installation.
2. **File System Configuration**: Accept the default Logical Volume Management (LVM) setup for disk partitioning.
3. **Confirm Disk Changes**: Review the storage summary and confirm to proceed with installation.

### Step 6: Personalization
1. **User Setup**: Enter your name, server name, username, and password.
2. **SSH Server Installation**: Opt to install OpenSSH Server for remote access.
3. **Additional Packages**: Choose any additional software packages you want to install.

### Step 7: Complete Installation
1. **Finish Installation**: Wait for the installation process to complete.
2. **Reboot**: Select "Reboot Now" to restart the server.

### Step 8: Initial Configuration
1. **Login**: Once the server reboots, log in with the credentials you set during installation.
2. **Check Network Configuration**: Run `ip a` to verify the server's IP address.
3. **Remote Access**: Use an SSH client (e.g., PuTTY) to connect to the server remotely, entering the server's IP address.

By following these steps, you'll successfully install a Linux server OS from an ISO image, whether on physical hardware or in a virtual environment.

## 6. Installing a Linux Desktop

To install a Linux desktop OS from an ISO image, follow these steps:

### Step 1: Download the ISO Image
1. **Select Your Distribution**: Go to the official website of the Linux distribution you want (e.g., Ubuntu).
2. **Download the ISO**: Navigate to the download section, and click the button to download the desktop ISO image. Save it to your local machine.

### Step 2: Set Up a Virtual Machine (If Using Virtualization)
1. **Open Virtualization Software**: Launch your virtualization tool (e.g., VMware Workstation, VirtualBox).
2. **Create a New Virtual Machine**:
   - Choose **Typical** setup.
   - Select **Installer disk image file (iso)** and browse for the downloaded ISO.
3. **Name and Location**: Name your virtual machine (e.g., "Ubuntu Desktop") and specify the storage location.
4. **Disk Size**: Allocate a suitable disk size (e.g., 80 GB).
5. **Network Settings**: Customize the network adapter to use a bridged connection if needed.

### Step 3: Boot from the ISO
1. **Power On the VM**: Start the virtual machine. It should automatically boot from the ISO image.
2. **Keyboard Layout**: Choose your keyboard layout when prompted.

### Step 4: Installation Process
1. **Installation Type**: Select "Normal installation" to include all applications, including a web browser and office software. Opt to download updates during installation.
2. **Disk Setup**: Confirm the default option to erase the detected disk and install the OS.
3. **Confirm Changes**: Review the partitioning changes and click **Continue**.

### Step 5: Personalization
1. **Set Up User Details**: Enter your name, computer name, username, and password. Decide whether to enable automatic login.
2. **Installation Progress**: Wait as the installer copies files to the new file system.

### Step 6: Complete Installation
1. **Reboot**: After installation completes, click "Restart Now" to reboot the virtual machine.

### Step 7: Initial Configuration
1. **Login**: Sign in with your username and password.
2. **Online Accounts**: You may be prompted to connect online accounts—choose to skip if desired.
3. **Update Software**: Check for any available updates and install them.

### Step 8: Verify Connectivity
1. **Test Internet Access**: Open a web browser (e.g., Firefox) to ensure you have internet connectivity.
2. **Explore Applications**: Access various installed applications like LibreOffice or the terminal.

### Step 9: System Commands
- To check your IP address, open a terminal and run:
  ```bash
  ip a
  ```
- To view the hostname, type:
  ```bash
  hostname
  ```

By following these steps, you'll have successfully installed a Linux desktop OS from an ISO image, ready for use!

## 7. Deploying a Cloud-based Linux Server

To install a Linux cloud-based virtual machine using Microsoft Azure, follow these steps:

### Step 1: Access the Azure Portal
1. **Go to Azure Portal**: Open a web browser and navigate to [portal.azure.com](https://portal.azure.com).
2. **Sign In**: Log in with your Azure account credentials.

### Step 2: Create a New Virtual Machine
1. **Create a Resource**: Click on **Create a resource** in the upper left corner.
2. **Select Virtual Machine**: Choose **Virtual machine** from the list of options.

### Step 3: Choose a Linux Distribution
1. **Marketplace Search**: In the Marketplace, you can see common virtual machine types. For more options, click on **See more in Marketplace** and filter by "Linux."
2. **Select Distribution**: Find and select your desired Linux distribution (e.g., Ubuntu 23.04).
3. **Review Details**: Check the details and pricing, then click **Create**.

### Step 4: Configure the Virtual Machine
1. **Resource Group**: Choose an existing resource group or create a new one to organize your resources.
2. **VM Name and Region**: Name your VM (e.g., "Ubuntu1") and select a region (e.g., East US).
3. **Image**: Ensure the selected image is the correct version of Linux (e.g., Ubuntu 23.04).
4. **Size**: Choose the VM size based on the resources needed (e.g., 4 virtual CPUs, 16 GB RAM).
5. **Authentication**: Select authentication method:
   - **SSH Public Key** or **Username and Password**. Fill in the necessary details (username and password).
6. **Inbound Ports**: Ensure SSH (port 22) is allowed for remote access.

### Step 5: Configure Disks and Networking
1. **Disks**: Review and confirm the disk settings (you can typically use the default settings).
2. **Networking**: Accept the default settings for creating a new virtual network and subnet.

### Step 6: Review and Create
1. **Review Settings**: Click on **Review + create** and verify all settings.
2. **Create VM**: Click the **Create** button to start the deployment. Azure will set up your VM along with necessary resources.

### Step 7: Access Your Virtual Machine
1. **Find Public IP**: Once deployment is complete, go to **All resources** or filter by **Virtual machines** to find your VM. Note the public IP address.
2. **Using PuTTY**:
   - Open PuTTY and enter the public IP address in the Host Name field and ensure the port is set to 22.
   - Save the session as "Azure-Ubuntu" for future use.
3. **Connect**: Click **Open** to connect. Accept the server fingerprint when prompted.

### Step 8: Log In
1. **Enter Credentials**: Log in using the username and password you set during VM creation.
2. **Check Network**: Once logged in, you can run commands like:
   - `ip a` to display network interfaces.
   - Note that the public IP won’t appear inside the VM, as it's an Azure resource.

### Summary
You have successfully deployed a Linux cloud-based virtual machine in Microsoft Azure! You can now configure and use your VM as needed.

## 8. Managing Linux Hardware

### 1. Understanding the /dev Directory
- **Location**: The `/dev` directory contains device files representing hardware devices.
- **Command**: Use `ls /dev` to list devices. For mass storage devices, run:
  ```bash
  ls /dev/sd?
  ```
  This shows recognized storage devices like `sda`, `sdb`, etc.

### 2. Installing Drivers
- To install drivers (e.g., Nvidia), use:
  ```bash
  sudo apt install <driver-package-name>
  ```
  Confirm installation when prompted.

### 3. Exploring /proc Directory
- **Dynamic Information**: The `/proc` directory contains runtime information about the system.
- **Command**: Check CPU details with:
  ```bash
  cat /proc/cpuinfo
  ```

### 4. Listing PCI Devices
- Use `lspci` to list all PCI devices. For detailed output, run:
  ```bash
  lspci -v | more
  ```
  This shows information about various hardware connected via the PCI bus.

### 5. Listing USB Devices
- To see connected USB devices, use:
  ```bash
  lsusb -v
  ```

### 6. Retrieving BIOS/UEFI Information
- Use `dmidecode` to gather information about the BIOS/UEFI:
  ```bash
  sudo dmidecode | more
  ```
  This provides details like BIOS version and release date.

### Summary
These commands help you understand and manage your Linux system's hardware, making it easier to troubleshoot and maintain your setup.

## 9. Using Linux File System Navigation Commands

### 1. Checking Your Location
- **Command**: `pwd`
  - **Purpose**: Prints the current working directory.

### 2. Changing Directories
- **Command**: `cd <directory>`
  - **Purpose**: Changes the current directory.
  - **Shortcut**: `cd` alone returns you to your home directory.

### 3. Listing Files and Directories
- **Command**: `ls`
  - **Purpose**: Lists files in the current directory.
  - **Options**:
    - `ls -l`: Long format, shows details including permissions.
    - `ls -a`: Lists all files, including hidden ones (those starting with a dot).
    - `ll`: A shortcut for `ls -l`.

### 4. Creating Directories
- **Command**: `mkdir <directory>`
  - **Purpose**: Creates a new directory.
  - **Option**: `mkdir -p <path>` creates parent directories as needed.

### 5. Copying Files
- **Command**: `cp <source> <destination>`
  - **Purpose**: Copies files from the source to the destination.

### 6. Moving Files
- **Command**: `mv <source> <destination>`
  - **Purpose**: Moves (or renames) files.

### 7. Creating Empty Files
- **Command**: `touch <filename>`
  - **Purpose**: Creates an empty file or updates the timestamp of an existing file.

### 8. Removing Directories and Files
- **Command**: `rmdir <directory>`
  - **Purpose**: Removes an empty directory.
  - **Command**: `rm <file>`
  - **Purpose**: Removes files; add `-r` to remove non-empty directories (e.g., `rm -r <directory>`).

### 9. Accessing Manual Pages
- **Command**: `man <command>`
  - **Purpose**: Displays the manual for a command, providing usage details and options.

### Summary
These commands will help you navigate and manage files within the Linux file system effectively. Understanding when and how to use them is crucial for system management.

## 10. Navigating the Linux File System

### 1. Check Current Directory
- **Command**: `pwd`
  - **Purpose**: Prints the working directory.

### 2. Change Directory
- **Command**: `cd <directory>`
  - **Purpose**: Changes the current directory. Use `cd` alone to return to the home directory.

### 3. List Files and Directories
- **Command**: `ls`
  - **Purpose**: Lists files in the current directory.
  - **Options**:
    - `ls -l`: Long format listing with details (permissions, owner, etc.).
    - `ls -d <pattern>`: Lists only the directory entries matching the pattern without diving into subdirectories.
    - Use wildcards (`*`) and character classes (`[Bb]*`) for flexible matching.

### 4. Create Directories
- **Command**: `mkdir <directory>`
  - **Purpose**: Creates a new directory.

### 5. List Block Devices
- **Command**: `lsblk`
  - **Purpose**: Lists block devices and their details.
  - **Option**: `lsblk --scsi` for SCSI devices.

### 6. Disk Partitioning
- **Command**: `fdisk /dev/sda -l`
  - **Purpose**: Lists partitions on a disk.
  - **Note**: Use `sudo` for elevated permissions.

### 7. Mount File Systems
- **Command**: `mount`
  - **Purpose**: Displays currently mounted file systems and their mount points.

### 8. Disk Usage
- **Command**: `df`
  - **Purpose**: Shows disk space usage for mounted file systems.
  - **Option**: `df -h` for human-readable output.

### 9. Disk Usage by Directory
- **Command**: `du`
  - **Purpose**: Displays disk usage for files and directories.
  - **Options**:
    - `du -h`: Human-readable format.
    - `du -sh *`: Summarizes disk usage of all items in the current directory.
    - Combine with `sort` to order by size: `du -sh * | sort -hr`.

### Example Commands in Context
- To create a directory:
  ```bash
  mkdir Budgets
  ```
  
- To list files starting with a specific letter but not in subdirectories:
  ```bash
  ls -d b*
  ```

- To view detailed disk partition info:
  ```bash
  sudo fdisk -l /dev/sda
  ```

- To check disk usage in a human-readable format:
  ```bash
  du -h
  ```

### Summary
These commands are essential for navigating and managing files within the Linux file system. Familiarity with them will enhance your efficiency in using Linux systems.

## 11. Search for files in the Linux

### 1. The `find` Command
The `find` command searches for files in a directory hierarchy based on various criteria.

#### Basic Syntax:
```bash
find [path] [options] [expression]
```

#### Common Options:
- **`-name`**: Search for files by name.
- **`-user`**: Filter files by owner.
- **`-type`**: Specify the type of file (e.g., `d` for directories, `f` for files).
- **`-perm`**: Search based on permissions.

#### Examples:
- **Search for files named with variations of "budget":**
  ```bash
  sudo find / -name "[Bb]udget*"
  ```
- **Search for files owned by a specific user:**
  ```bash
  sudo find / -name "[Bb]udget*" -user lbrenner
  ```
- **Search for directories named "apache2":**
  ```bash
  sudo find / -type d -name "apache2"
  ```
- **Search for files with specific permissions:**
  ```bash
  sudo find / -type f -perm 0740
  ```

### 2. Redirecting Output
You can redirect output to a file and run processes in the background:
```bash
sudo find / -name "[Bb]udget*" -user lbrenner > lbrenner_owner_results.txt 2>/dev/null &
```

### 3. The `locate` Command
The `locate` command searches for files using a pre-built database, making it faster than `find`.

#### Setup:
- If `locate` isn't installed, use:
  ```bash
  sudo apt install plocate
  ```
- Update the database with:
  ```bash
  sudo updatedb
  ```

#### Examples:
- **Search for entries related to "mysql":**
  ```bash
  locate mysql
  ```
- **Search for files ignoring case:**
  ```bash
  locate -i budget*
  ```
- **Count occurrences of search results:**
  ```bash
  locate -c budget*
  ```

### Summary
Both `find` and `locate` are powerful tools for searching the Linux file system. Use `find` for more granular searches based on file attributes, and `locate` for quick searches using a database. Remember to keep the database updated for accurate results with `locate`.

## 12. Filtering Data with Linux Commands

### 1. `grep`
The `grep` command is used for searching text using patterns.

#### Basic Syntax:
```bash
grep [options] pattern [file]
```

#### Key Options:
- **`-i`**: Ignore case during the search.
- **`-r`**: Recursively search through directories.
- **`-v`**: Invert the match (show lines that do NOT match).

#### Examples:
- **Search for "london" in `cities.txt` (case-insensitive):**
  ```bash
  cat cities.txt | grep -i london
  ```
- **Search all files in the current directory for "london":**
  ```bash
  grep -i london *
  ```

### 2. `sed`
`sed` is a stream editor for filtering and transforming text.

#### Basic Syntax:
```bash
sed [options] 'command' [file]
```

#### Common Commands:
- **`s/pattern/replacement/`**: Substitute a pattern with a replacement.

#### Examples:
- **Replace "London" with "Liverpool" in `customers.txt` (output only):**
  ```bash
  sed 's/London/Liverpool/' customers.txt
  ```
- **Redirect the output to a new file:**
  ```bash
  sed 's/London/Liverpool/' customers.txt > new_customers.txt
  ```

### 3. `awk`
`awk` is a powerful programming language designed for pattern scanning and processing.

#### Basic Syntax:
```bash
awk [options] 'pattern {action}' [file]
```

#### Common Usage:
- **Print specific columns from a file.**
- **Use `$1`, `$2`, etc., to reference fields in a record.**

#### Examples:
- **Print the second and third columns (last name, first name) from `customers.txt`:**
  ```bash
  awk '{print $2, $3}' customers.txt
  ```
- **Add line numbers to output:**
  ```bash
  awk '{print NR, $0}' customers.txt
  ```
- **Using a colon as a delimiter to extract the first column from `/etc/passwd`:**
  ```bash
  awk -F: '{print $1}' /etc/passwd
  ```

### Summary
These commands allow you to search, filter, and manipulate text data in various ways. They can be combined with other commands and used in scripts for more complex processing. Exploring their extensive options and features can help you become proficient in data manipulation in Linux.