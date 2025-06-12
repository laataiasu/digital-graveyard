# Software Management

## 1. Linux Software Management

**Package Repositories**  
A package repository is a centralized collection of software for installation on a Linux system. Repositories can be public (available over the internet) or private (hosted internally). Most modern Linux distributions automatically pull from public repositories during software installation. You can also compile software from source code using a compiler if you have the necessary dependencies.

**Security Considerations**  
Always consider the sources of your software. Use trusted package repositories where software is digitally signed and source code from reputable vendors or internal developers to comply with security policies.

**Repository Management**  
Linux systems can be configured to use multiple repositories, both public and private. When installing or upgrading software, the system checks these repositories.

**Command Line Tools for Package Management**  
1. **apt** (Debian-based systems, e.g., Ubuntu):  
   - `apt update`: Update the list of repositories and available software.  
   - `apt install <package>`: Install a software package.  
   - `apt upgrade`: Upgrade installed packages.  
   - `apt remove <package>`: Remove an installed package.  
   - `apt list`: List installed software packages.  

2. **yum** (Red Hat-based systems, e.g., Fedora):  
   - `yum install <package>`: Install software.  
   - `yum remove <package>`: Remove software.  
   - `yum update`: Update all packages.  
   - `yum list` or `yum info <package>`: Get information about installed packages.

3. **pacman** (Arch Linux):  
   - `pacman -S <package>`: Install a package.  
   - `pacman -Ss <package>`: Query available packages.  
   - `pacman -Qs <package>`: Query installed packages.  
   - `pacman -R <package>`: Remove a package.

**Example Commands**  
- Use `sudo apt update` to refresh the package listings, which informs you about upgradeable packages.
- To install a package like Docker, run `sudo apt install docker.io`, which checks dependencies and prompts for confirmation.

**Compiling from Source Code**  
When software is not available in repositories, you can compile from source. Steps include:  
1. Download the source file (e.g., using `wget`).
2. If compressed (e.g., tar.gz), decompress it with `tar -zxvf <file>`.
3. Change to the extraction directory.
4. Run `./configure` to generate a makefile.
5. Run `make` to compile the software.
6. Run `make install` to install the compiled software.

This outlines how to manage software and repositories in Linux, along with compiling software from source code.

## 2. Configuring the Linux Kernel

**Understanding the Linux Kernel**  
The Linux kernel manages resource access and hardware drivers, forming the core of the Linux operating system. Modifying the kernel is usually infrequent but important during troubleshooting or manual updates.

**Checking Kernel Information**  
- Use the command:  
  ```bash
  sudo uname -mrs
  ```  
  This displays the kernel version and architecture (e.g., `5.15.0-76-generic` on a 64-bit platform).

- For more details, check the kernel version signature with:  
  ```bash
  sudo cat /proc/version_signature
  ```

**Updating the Kernel**  
- Update the package repository list with:  
  ```bash
  sudo apt update
  ```  
- To install a specific kernel package, use:  
  ```bash
  sudo apt install <package-name>
  ```  
  **Note:** Always back up before changing the kernel to avoid boot issues.

**Managing Kernel Boot Options**  
- View the GRUB configuration file to see available kernel versions:  
  ```bash
  sudo cat /boot/grub/grub.cfg | more
  ```

**Loading and Removing Kernel Modules**  
- List currently loaded kernel modules:  
  ```bash
  lsmod
  ```  
- To filter for a specific module, use:  
  ```bash
  lsmod | grep <module-name>
  ```

- To remove a kernel module:  
  ```bash
  sudo modprobe -r <module-name>
  ```  
  After removal, you can verify it is no longer loaded using `lsmod`.

- To get details about a specific kernel module:  
  ```bash
  sudo modinfo <module-name>
  ```

- To load a kernel module:  
  ```bash
  sudo modprobe <module-name>
  ```  
  Verify it is loaded again using `lsmod`.

**Installing Custom Kernels**  
When updating to custom kernels, exercise caution as this may affect system stability. Often, this involves adding a repository and installing from it.

## 3. Managing Repositories

After watching the video, you will learn how to search for, install, update, and remove packages using yum on Red Hat-based systems.

**Using Yum for Package Management**  
Yum is a command-line utility for managing RPM (Red Hat Package Manager) packages. 

**Basic Commands**  
- **Get Help:**  
  ```bash
  yum --help
  ```

- **List Repositories:**  
  ```bash
  sudo yum repolist
  ```

- **List Installed Packages:**  
  ```bash
  sudo yum list installed | more
  ```

- **Filter Installed Packages:**  
  To find installed Python packages:  
  ```bash
  sudo yum list installed | grep python
  ```

- **Check for Updates:**  
  ```bash
  sudo yum check-update
  ```

- **Update Installed Packages:**  
  ```bash
  sudo yum update
  ```  
  Confirm the update by typing `y`.

**Installing New Packages**  
- **Search for a Package:**  
  To search for Docker:  
  ```bash
  sudo yum search docker
  ```

- **Get Package Information:**  
  To see details about Docker:  
  ```bash
  sudo yum info docker
  ```

- **Install a Package:**  
  To install Docker without confirmation:  
  ```bash
  sudo yum -y install docker
  ```

**Managing Services**  
- **Check Docker Status:**  
  ```bash
  sudo service docker status
  ```

- **Start Docker Service:**  
  ```bash
  sudo service docker start
  ```

- **Check Status Again:**  
  Verify that Docker is active:  
  ```bash
  sudo service docker status
  ```

**Updating and Removing Packages**  
- **Update a Specific Package:**  
  ```bash
  sudo yum update docker
  ```

- **Remove a Package:**  
  To remove Docker without confirmation:  
  ```bash
  sudo yum -y remove docker
  ```

- **Check Available Packages:**  
  Verify Docker is removed:  
  ```bash
  sudo yum list docker
  ```

**Using RPM**  
You can also use RPM commands directly:
- **Install a Package:**  
  ```bash
  rpm -i <package-name>
  ```

- **Remove a Package:**  
  ```bash
  rpm -e <package-name>
  ```

For more options, refer to the RPM manual:  
```bash
man rpm
```

## 4. Using pacman to Manage Linux Repositories and Updates

Upon completing this video, you will learn how to use pacman to locate, install, update, and remove packages on Arch Linux.

**Using Pacman for Package Management**

**Viewing Configuration and Repositories**
- **Check Pacman Configuration:**
  ```bash
  sudo cat /etc/pacman.conf
  ```
- **View Repository List:**
  ```bash
  sudo cat /etc/pacman.d/mirrorlist
  ```

**Updating Packages**
- **Update Package Database and Upgrade Installed Packages:**
  ```bash
  sudo pacman -Syu
  ```
  Confirm with `Y` when prompted.

**Searching for Packages**
- **Search for Available Packages:**
  To check if Docker is available:
  ```bash
  sudo pacman -Ss docker
  ```

- **Check Installed Packages:**
  To see if Docker is installed:
  ```bash
  sudo pacman -Q docker
  ```

**Installing Packages**
- **Install a Package:**
  To install Docker:
  ```bash
  sudo pacman -S docker
  ```
  Confirm installation with `Y`.

**Managing Services**
- **Check Status of Docker:**
  ```bash
  sudo systemctl status docker
  ```

- **Start Docker Service:**
  ```bash
  sudo systemctl start docker
  ```

- **Verify Docker is Running:**
  ```bash
  sudo systemctl status docker
  ```

- **Access Docker Command-Line Interface:**
  Just type:
  ```bash
  docker
  ```
  This will show help for Docker commands.

**Removing Packages**
- **Remove an Installed Package:**
  To remove Docker:
  ```bash
  sudo pacman -R docker
  ```
  Confirm removal with `Y`.

## 5. Utilizing apt to Manage Linux Repositories and Updates

In this video, you will learn how to utilize `apt` to manage packages on Debian-based Linux distributions, specifically Ubuntu.

### Utilizing `apt` for Package Management

**Examining Repositories**
- **View Current Repositories:**
  ```bash
  sudo cat /etc/apt/sources.list
  ```

**Updating Package Information**
- **Update Repository Information:**
  This command fetches the latest package lists from the configured repositories.
  ```bash
  sudo apt update
  ```

**Upgrading Installed Packages**
- **Upgrade All Installed Packages:**
  After updating the package lists, upgrade the packages.
  ```bash
  sudo apt upgrade
  ```
  Confirm the action by typing `Y` when prompted.

**Listing Installed Packages**
- **View Installed Packages:**
  You can list all installed packages along with their versions.
  ```bash
  sudo apt list --installed
  ```

**Installing Packages**
- **Install a Specific Package:**
  For example, to install Docker:
  ```bash
  sudo apt install docker.io
  ```
  Confirm the installation by typing `Y`.

**Verifying Installation**
- **Check the Status of the Docker Service:**
  After installation, verify if the Docker daemon is running.
  ```bash
  sudo service docker status
  ```

**Removing Packages**
- **Remove an Installed Package:**
  To uninstall Docker:
  ```bash
  sudo apt remove docker.io
  ```
  Confirm by typing `Y`.

**Adding Additional Repositories**
- **Add a New Repository:**
  Use the following command to add a new APT repository:
  ```bash
  sudo add-apt-repository <repository-url>
  ```
  Follow the prompts to complete the addition.

**Importing Public Keys**
- **Add a Public Key for a Repository:**
  If a repository requires a public key for verification, use:
  ```bash
  sudo apt-key add <key-file>
  ```

## 6. Building Linux Software from Source

In this video, you will learn how to compile and install Linux software from source using the `./configure`, `make`, and `make install` commands.

### Building Linux Software from Source

1. **Create a Downloads Directory:**
   - Start by creating a directory for your source files.
   ```bash
   mkdir downloads
   cd downloads/
   ```

2. **Download Source Code:**
   - Use `curl` to download the source code of the software (e.g., Git).
   ```bash
   curl --output git.tar.gz https://<source-url>
   ```

3. **Extract the Archive:**
   - Extract the downloaded compressed archive.
   ```bash
   tar -zxf git.tar.gz
   cd git-<version>/
   ```

4. **Check for Configuration File:**
   - Look for the `configure` script, which checks system dependencies.
   ```bash
   ls config*
   ```

5. **Run the Configuration Script:**
   - Execute the `./configure` command to check for necessary compilers and dependencies.
   ```bash
   ./configure
   ```
   - If you see an error about a missing compiler, install it (e.g., GCC).
   ```bash
   sudo apt install gcc
   ```

6. **Re-run the Configuration:**
   - After installing the compiler, run the `./configure` command again.
   ```bash
   ./configure
   ```

7. **Compile the Software:**
   - Use `make` to compile the source code into binary files.
   ```bash
   sudo make
   ```

8. **Install the Compiled Software:**
   - After compilation, install the software with:
   ```bash
   sudo make install
   ```

9. **Verify Installation:**
   - Check if the installation was successful by checking the version.
   ```bash
   git --version
   ```