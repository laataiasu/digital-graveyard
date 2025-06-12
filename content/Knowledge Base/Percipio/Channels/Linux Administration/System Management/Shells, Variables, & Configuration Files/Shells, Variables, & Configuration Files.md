# Shells, Variables, & Configuration Files

## 1. Linux Configuration Files

Linux services and software packages are typically configured using text files, usually with a .conf extension. Most configuration files are located in the /etc/ directory or its subdirectories. Some software may create their own subdirectories within /etc/ for multiple configuration files. 

For example, run-level directories like rc3.d contain start and kill scripts for daemons associated with specific run levels. Common configurations include a global file like logrotate.conf, which may include additional settings from subdirectories.

To view or edit configuration files, you can use commands like:

- **cat /etc/apache2/apache2.conf**: View the entire file.
- **cat /etc/apache2/apache2.conf | more**: View file output one screen at a time.
- **grep "log" /etc/apache2/apache2.conf**: Search for specific text within the file.
- **head /etc/apache2/apache2.conf**: View the first 10 lines.
- **tail /etc/apache2/apache2.conf**: View the last 10 lines.

For editing, you can use text editors like:

- **vi or vim**: Older but powerful editors; commands include `:w` (write) and `:q` (quit).
- **nano**: More user-friendly; use Ctrl+X to exit and confirm to save changes.

These tools help manage configuration effectively, enabling customization and optimization of Linux services.

## 2. Managing Linux Configuration Files

In this demonstration, we’ll manage Linux configuration files. The number of configuration files depends on the installed software on your Linux host, but default configuration files are present in any Linux distribution under the /etc/ directory.

To explore:

1. Change to the /etc/ directory:
   - `cd /etc`
   - `ls` to list the contents.

Configuration files typically have extensions like .conf or .cfg, but this isn’t mandatory. Some software creates its own subdirectories, such as for the Uncomplicated Firewall (UFW). 

2. Navigate to UFW:
   - `cd ufw`
   - `ls` to see specific config files.

Next, change to the SSH directory:

3. Navigate to SSH:
   - `cd ssh`
   - `ls` to list files such as ssh_config and sshd_config. The latter is for the SSH server daemon, while the former is for the SSH client.

4. View configuration files:
   - `cat ssh_config` (for client settings).
   - `cat sshd_config` (for server settings).

The sshd_config file may include references to additional configuration files in /etc/ssh/sshd_config.d. You can modify settings such as the listening port, which defaults to 22. Uncomment this line to change it, then restart the service.

5. Change to the configuration directory:
   - `cd sshd_config.d`
   - `ls` to view files like 50-cloud-init.conf.
   - `sudo cat 50-cloud-init.conf` shows that password authentication is enabled.

Next, install the Apache web server:

6. Install Apache:
   - `sudo apt install apache2`
   - Confirm with 'Y'.

After installation, navigate to Apache's configuration directory:

7. Change to Apache configuration:
   - `cd /etc/apache2`
   - `ls` to see files including apache2.conf.

8. View the configuration file:
   - `cat apache2.conf`

This file typically includes other configuration files, like ports.conf:

9. View ports.conf:
   - `cat ports.conf`

You can edit the listening port (default is 80) with:
   - `sudo nano ports.conf`

10. Test connectivity:
    - First, check the server's IP: `ip a` (address is 10.0.0.4).
    - Test with: `sudo wget http://10.0.0.4`.

11. Change the listening port in ports.conf to 82, save, and restart Apache:
    - `sudo service apache2 restart`

12. Test again with the new port:
    - `sudo wget http://10.0.0.4:82`

If the default port (80) was used without specifying the new port, you’d receive a connection error. 

Remember, configuration files generally reside in /etc/ and are text files. You need appropriate permissions to edit them, and always restart the relevant service to apply changes.

## 3. Linux Shells

Sure! Managing Linux shells is a crucial skill for interacting with and automating tasks on a Linux system. Here’s a concise overview of the key points you covered:

### What is a Shell?
- A **Linux shell** is an interface that allows users to interact with the operating system by typing commands.
- Shells can be used interactively or invoked through scripts.

### Common Shells
- **Bash (Bourne Again Shell)**: The default shell for many Linux distributions.
- **Dash**: A lightweight shell often used for scripting; `/bin/sh` may point to this on Ubuntu.
- **Korn Shell (ksh)**: Known for its speed and programming features.
- **C Shell (csh)**: Offers a different syntax and command structure.

### Viewing and Changing User Shells
- User shells are defined in `/etc/passwd`, with the last field indicating the shell to be used at login.
- Use `cat /etc/passwd | grep username` to find a specific user's shell.

### Installing Shells
- If a shell isn’t installed, you can add it using a package manager. For example, `sudo apt install mksh` for the Korn Shell.

### The Shebang Line
- The first line in a script specifies which shell to use. It starts with `#!` followed by the path to the shell (e.g., `#!/bin/bash`).
- This line is essential for the script to run correctly under the intended shell.

### Shell Behavior Differences
- Different shells handle features like variable scope, command syntax, and completion differently.
- For example, tab completion works in Bash but not in C Shell.

### Changing User Shells
- You can change a user's default shell by editing the `/etc/passwd` file.
- Use `sudo nano /etc/passwd` to modify the shell for a specific user.

### Example Workflow
1. **View User Shell**: `cat /etc/passwd | grep mbishop`
2. **Install a Shell**: `sudo apt install csh`
3. **Change User Shell**: Edit `/etc/passwd` to set `/usr/bin/csh` as the default for `mbishop`.
4. **Switch User**: `su - mbishop`, confirming the change with a percent sign prompt.

### Conclusion
Managing shells effectively allows for flexibility in executing commands and scripts, tailoring environments to suit different tasks. Familiarity with various shells and their specific features enhances productivity in a Linux environment. If you have specific questions or topics you'd like to dive deeper into, feel free to ask!

## 4. Manipulating Linux Environment Variables

**Working with Environment Variables in Linux**

Environment variables are storage locations in memory that hold values, such as names, IDs, or addresses. In Linux, using Bash, you can view all environment variables in your session by typing:

```bash
env
```

This command lists all environment variables and their values. For example, the `SSH_CONNECTION` variable can be viewed in uppercase, as variable names are case-sensitive in Linux.

To find specific variables, you can use:

```bash
env | grep -i PATH
```

The `PATH` variable is crucial for locating binaries. You can display its value with:

```bash
echo $PATH
```

You can create your own variables. For example, to create a variable called `CostCenter` with the value "Toronto":

```bash
CostCenter="Toronto"
```

To retrieve the value, use:

```bash
echo $CostCenter
```

Case sensitivity matters; using lowercase will return nothing:

```bash
echo $costcenter
```

To store the result of a command in a variable, use backticks. For example, to store IP address information:

```bash
IP=`ip a | grep inet | grep brd`
```

To display the stored value:

```bash
echo $IP
```

However, user-defined variables won't show up with the `env` command, as it only lists environment variables. Use `set` to see all variables, including user-defined ones:

```bash
set | grep IP
set | grep CostCenter
```

**Variable Scope in Scripts**

When you run a script, it spawns a new shell. If you define a variable like `CostCenter` and try to access it within a script, it won’t be available unless you export it. Here’s how to create a script:

1. Create the script file:

```bash
sudo nano newscript.sh
```

2. Add the shebang line and echo the variable:

```bash
#!/bin/bash
clear
echo $CostCenter
```

3. Save and exit, then make the script executable:

```bash
sudo chmod +x newscript.sh
```

4. Running the script:

```bash
./newscript.sh
```

This may return nothing if `CostCenter` isn’t exported. To make it available in the script, export it:

```bash
export CostCenter
```

After exporting, if you run the script again, it will now return the value of `CostCenter`:

```bash
echo $CostCenter
./newscript.sh
```

Exporting makes the variable accessible to child shells and scripts.

## 5. Using Ansible to Manage Linux Configurations

**Installing and Configuring Ansible**

Ansible is a centralized configuration management tool used to manage multiple Linux hosts efficiently, avoiding the need for manual configuration on each machine.

**Installation Steps:**

1. **Add Ansible PPA:**
   ```bash
   sudo apt-add-repository ppa:ansible/ansible
   ```

2. **Install Ansible:**
   ```bash
   sudo apt install ansible
   ```

3. **Navigate to Ansible Directory:**
   ```bash
   cd /etc/ansible
   ```

4. **Edit the Hosts File:**
   ```bash
   sudo nano hosts
   ```
   Add entries like:
   ```
   [your_group]
   10.0.0.7 ansible_user=cblackwell ansible_ssh_pass=Pa$$w0rdABC123
   ansible_python_interpreter=/usr/bin/python3
   ```

**Security Note:** Storing passwords in plain text poses security risks. Consider using SSH key authentication for better security.

5. **Install `sshpass`:**
   ```bash
   sudo apt install sshpass
   ```

**Testing Connectivity:**

1. **Ping All Hosts:**
   ```bash
   sudo ansible all -m ping
   ```
   Look for output indicating success.

2. **Run a Command Across All Hosts:**
   ```bash
   sudo ansible all -a "ls /"
   ```

**Output Redirection:**
To save command output to a file:
```bash
sudo ansible all -a "ls /" > /home/cblackwell/rootlisting_ansiblenodes.txt
```

3. **View the Output File:**
   ```bash
   cd
   cat rootlisting_ansiblenodes.txt
   ```

**Creating an Ansible Playbook:**

1. **Create a Playbook File:**
   ```bash
   sudo nano ansible_aptupdate.yaml
   ```

2. **Structure the Playbook:**
   Example content:
   ```yaml
   - hosts: all
     become: yes
     tasks:
       - name: Update APT package cache
         apt:
           update_cache: yes
           cache_valid_time: 3600
   ```

3. **Run the Playbook:**
   ```bash
   sudo ansible-playbook ansible_aptupdate.yaml
   ```

**Conclusion:**

Ansible is a powerful tool for managing configurations across multiple servers. While it’s effective for small to medium-sized deployments, larger environments might benefit from alternatives like Puppet or Terraform, which serve similar purposes.