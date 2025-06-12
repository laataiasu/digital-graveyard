# Shell Scripting with Bash

## 1. Linux Shell Scripts

**Linux Shell Scripts**

- **Definition**: A Linux shell script is a text file containing commands that can be executed to automate tasks. Scripts can be run by calling their name and scheduled with cron.

- **Shebang Line**: The first line in a script specifies which shell to use. It starts with `#!` followed by the path to the shell, e.g., `#!/bin/bash` for Bash or `#!/bin/csh` for C shell. This ensures compatibility with the syntax and variable handling of the specified shell.

- **Script Content**: You can include any valid Linux commands, define functions, and reference other scripts. 

- **Permissions**: For a script to run, it must have execute (`x`) and read (`r`) permissions set using `chmod +rx script.sh`.

- **Functions**: Functions allow you to group commands. To define a function:
  ```bash
  function show_ipinfo() {
      # commands go here
  }
  ```
  You can call the function simply by using its name.

- **Using grep**: The `grep` command filters text:
  - `grep -i "^toronto" /budgets/*.xls`: Finds lines starting with "toronto" (case insensitive) in `.xls` files.
  - `grep "costcenter.*344"`: Matches lines containing "costcenter" followed by "344".
  - `egrep "^Y{2,}" airports.txt`: Matches lines starting with at least two "Y"s.
  - `egrep "Y{1,2}" airports.txt`: Matches lines containing either one or two "Y"s.

- **Difference between grep and egrep**: `egrep` allows more flexible regular expressions without needing to escape special characters.

- **Tee Command**: The `tee` command outputs to both the screen and a file:
  ```bash
  lsblk --scsi | tee output.txt
  ```
  
- **Find Command**: Used for searching files:
  ```bash
  find / -name "*.xls" -user cblackwell > cblackwell_files.txt 2>/dev/null
  ```
  This searches for `.xls` files owned by `cblackwell`, discarding any error messages.

- **sed Command**: Performs substitutions in text files:
  ```bash
  sed -e 's/toronto/vancouver/' filename.txt
  ```

- **awk Command**: Processes text files with structured data:
  - To skip the first line: 
    ```bash
    awk 'NR > 1' locations.txt
    ```
  - To extract specific columns:
    ```bash
    awk -F, '{print $1, $3}' customers.txt
    ```

- **Basic Bash Script Example**:
  ```bash
  #!/bin/bash
  clear
  echo "Enter your first name:"
  read firstname
  echo "Hello, $firstname"
  echo "Today's date is: $(date)"
  ```

This script clears the screen, prompts for user input, and displays a greeting along with the current date. Use backticks \(`\) to capture command output for variables.

## 2. Shell Script Comparison, Piping, and Redirection Operators

**Shell Script Commands**

- **Comparison Operators**: The `if` statement is fundamental for testing conditions.
  - Example:
    ```bash
    if test $USER = "root"; then
        echo "Welcome root!"
    else
        echo "Welcome $USER"
    fi
    ```
    - `$USER` is an environment variable for the logged-in username.
  
- **Case Construct**: Use when testing multiple values.
  - Example:
    ```bash
    echo "MENU SYSTEM"
    echo "1. Quit"
    echo "2. Show IP Address"
    echo "Enter Selection:"
    read choice

    case $choice in
        1) exit ;;
        2) ip a ;;
        *) echo "I don't know" ;;
    esac
    ```

- **Piping**: Connect the output of one command to another.
  - Example:
    ```bash
    DGW_VAR=$(ip route show | grep default | tr -s ' ' ':' | cut -d':' -f3)
    echo $DGW_VAR
    ```
    - This command finds the default gateway and formats it.

- **Redirection**: Direct input/output of commands.
  - `<` reads from a file, `>` writes output to a file, `>>` appends to a file, and `2>/dev/null` discards error messages.
  - Example of appending:
    ```bash
    function backup {
        tar -cvf /backup-$(date +%Y%m%d).tar /data >> /var/log/backup_log-$(date +%Y%m%d).log
    }
    ```

**Looping Constructs**

- **For Loop**: Executes a block for each item in a list.
  - Example:
    ```bash
    #!/bin/bash
    clear
    totalsize=0
    for i in /webfiles/*.htm; do
        currentsize=$(ls -l $i | tr -s ' ' | cut -d' ' -f5)
        totalsize=$((totalsize + currentsize))
    done
    echo "Total size: $totalsize" | tee results.txt
    ```

- **While Loop**: Continues until a condition is false.
  - Example:
    ```bash
    while true; do
        clear
        echo "UTILITY MENU"
        echo "1. Option 1"
        echo "2. Option 2"
        read selection

        case $selection in
            1) show_ipinfo ;;
            2) exit ;;
        esac
        read junk  # Pause until a key is pressed
    done
    ```

- **Until Loop**: Runs until a condition becomes true.
  - Example:
    ```bash
    until [ condition ]; do
        # commands
    done
    ```

- **Breaking and Continuing**: 
  - Use `break` to exit a loop entirely.
  - Use `continue` to skip the current iteration and move to the next.
  - Example:
    ```bash
    while true; do
        if [ condition ]; then
            break
        fi
        # other commands
    done
    ```

- **Select Loop**: Creates a simple menu system.
  - Example:
    ```bash
    select option in "Option 1" "Option 2"; do
        case $option in
            "Option 1") echo "You chose option 1" ;;
            "Option 2") echo "You chose option 2" ;;
            *) echo "Invalid option" ;;
        esac
    done
    ```

These constructs help manage flow control and execution within shell scripts effectively.

## 3. Managing Linux Environment and Shell Script Variables

### Linux Environment and Shell Script Variables

1. **Displaying Environment Variables**
   - Use `env` to list all environment variables and their values.
   - Example: The `USER` variable shows the current username (e.g., `cblackwell`).
   - The `PATH` variable contains paths separated by colons (`:`).

2. **Referencing Variables**
   - Use `echo` to display variable values with a `$` sign.
   - Variable names are case-sensitive. Use `$USER` for the uppercase version.

3. **Creating Variables**
   - Define a variable at the command line: `city="Zurich"`.
   - It exists only in the current shell session. Use `echo $city` to see the value.

4. **Storing Command Output in Variables**
   - To store command output, enclose the command in backticks (`` ` ``).
   - Example: `currentdate=\`date\`` stores the current date and time.
   - Use `echo $currentdate` to see the stored value.

5. **Listing Variables**
   - Use `set | more` to display all defined variables, including user-defined ones.

6. **Exporting Variables**
   - Variables are scoped to their declaring context. Use `export variable_name` to make it available in child processes.
   - Example: After `export scriptvar`, it can be accessed in scripts.

7. **Exit Codes**
   - Use `$?` to check the exit status of the last executed command.
   - `0` indicates success; non-zero indicates an error. Example: a nonexistent command returns `127`.

## 4. Writing and Running a Simple Shell Script

1. **Purpose of Shell Scripts**
   - Shell scripts automate tasks by executing a series of commands.

2. **Creating a Shell Script**
   - Use a text editor (e.g., `nano`) to create the script file (e.g., `script1.sh`).
   - Start with a shebang line: `#!/bin/bash`.

3. **Script Structure**
   - Separate commands by new lines or use semicolons (`;`).
   - Example:
     ```
     clear; 
     let totalsize=0; 
     let currentsize=0
     ```

4. **Using Loops in Scripts**
   - Use a `for` loop to iterate over files:
     ```
     for i in webfiles/*.htm; do
       currentsize=\`ls -l $i | tr -s " " | cut -f5 -d " "\`;
       totalsize=$((totalsize + currentsize))
     done
     ```

5. **Output Results**
   - Use `echo` to display results and redirect to a file:
     ```
     echo "The total space used is $totalsize bytes" | tee html_file_results.txt
     ```

6. **Setting Permissions**
   - Use `chmod` to set the executable permission for the script:
     ```
     chmod +rx script1.sh
     ```

7. **Executing the Script**
   - Run the script with `./script1.sh`. The output shows the total size of specified files.

This structured approach provides clarity on working with shell script variables and creating basic scripts in a Linux environment.

## 5. Deploying a Shell Script to AWS Virtual Machines

### Deploying a Script on an AWS Linux Virtual Machine

1. **AWS Management Console**
   - Log in to the AWS Management Console.
   - Search for "EC2" to access virtual machine instances.

2. **Launching an Instance**
   - Select the desired region (e.g., US East).
   - Click "Launch instance" to start the deployment process.
   - Name the instance (e.g., `Ubuntu3`).

3. **Choosing an OS Image**
   - Select the operating system, such as Ubuntu Server 22.04, from the Quick Start tab.

4. **Selecting Instance Type**
   - Choose the instance type based on workload requirements, considering CPU and memory needs.

5. **Key Pair Selection**
   - Select a key pair (e.g., `KeyPair1`) for secure access to the instance. The private key is stored locally, while the public key is on the VM.

6. **Network Settings**
   - Configure security groups to control traffic. Default settings allow SSH access from anywhere, but you can restrict it to your IP.

7. **User Data for Initialization**
   - Scroll to "Advanced details" and locate the User data field.
   - Enter initialization commands to execute on startup. Example:
     ```bash
     #!/bin/bash
     sudo apt update
     sudo apt install -y apache2 docker.io
     logger "Test msg from AWS..."
     ```

8. **Launching the Instance**
   - Click "Launch instance" to start the virtual machine.

9. **Accessing the Instance**
   - Copy the Public IPv4 address from the instance properties.
   - Use an SSH client (e.g., PuTTY) to connect:
     - Paste the IP address in PuTTY.
     - Configure the private key for authentication under Connection > SSH > Auth.
     - Open the connection.

10. **Verifying Installation**
    - Once logged in, check service statuses:
      - Run `sudo service apache2 status` to confirm Apache is running.
      - Use `sudo cat /var/log/syslog | grep AWS` to verify the logger message was recorded.

11. **Editing User Data**
    - In the AWS Management Console, select the instance and go to Actions > Instance Settings > Edit User Data to view the initialization script. Note that it can only be edited when the instance is stopped.

This process demonstrates how to efficiently deploy an AWS virtual machine with automated setup tasks using a script.

## 6. Parameterizing Shell Scripts

### Parameterizing a Shell Script

Parameterizing a shell script allows you to pass command-line arguments, enabling your script to behave dynamically based on those inputs. Here’s a breakdown of how to achieve this with examples.

#### Basic Parameterization Example

1. **Creating a Simple Script**
   - Open a terminal and use `nano` to create a script named `script2.sh`:

     ```bash
     nano script2.sh
     ```

   - Add the following content:

     ```bash
     #!/bin/bash
     clear
     echo "This script is called: $0"
     echo "The value of parameter 1 is: $1"
     echo "The value of parameter 2 is: $2"
     ```

   - Save and exit (Ctrl + X, then Y, then Enter).

2. **Making the Script Executable**
   - Change the permissions to make the script executable:

     ```bash
     chmod +rx script2.sh
     ```

3. **Running the Script**
   - Run the script without parameters:

     ```bash
     ./script2.sh
     ```

   - You’ll see that `$1` and `$2` are empty.

   - Now run it with parameters:

     ```bash
     ./script2.sh John Doe
     ```

   - The output will show the script name and the parameters you passed.

#### Advanced Parameterization with `getopts`

For more complex scenarios, you can use `getopts` to handle options and their arguments.

1. **Creating a Script with `getopts`**
   - Create another script named `script3.sh`:

     ```bash
     nano script3.sh
     ```

   - Add the following content:

     ```bash
     #!/bin/bash
     while getopts ":h:o:" option; do
         case $option in
             h) echo "Supplied host name is: $OPTARG";;
             o) echo "Supplied operation is: $OPTARG";;
             *) echo "You must supply values for specified parameters";;
         esac
     done
     ```

   - Save and exit.

2. **Making the Script Executable**
   - Again, change the permissions:

     ```bash
     chmod +rx script3.sh
     ```

3. **Running the Script with Options**
   - Run the script without parameters:

     ```bash
     ./script3.sh
     ```

   - The output will indicate that values must be supplied.

   - Test with an unknown option:

     ```bash
     ./script3.sh -x
     ```

   - The catch-all response will indicate a parameter requirement.

   - Now run with valid options:

     ```bash
     ./script3.sh -h host1 -o ping
     ```

   - The output should confirm both the host and operation:

     ```
     Supplied host name is: host1
     Supplied operation is: ping
     ```

### Summary

By parameterizing your shell scripts, you gain flexibility and control over their behavior. You can easily capture command-line arguments using positional parameters (`$1`, `$2`, etc.) for basic scripts or utilize `getopts` for more complex options. This allows for enhanced user interaction and functionality in your scripts, paving the way for more robust automation.

## 7. Array Variables in Bash

In this demonstration, we'll explore how to use array variables in a Bash shell script, allowing you to store and manipulate collections of related items efficiently.

#### Creating and Populating an Array

1. **Creating an Array from the Command Line**
   - Start by opening your terminal.
   - Create an array called `colors` to store color names:

     ```bash
     colors[0]="red"
     colors[1]="blue"
     ```

2. **Displaying Array Elements**
   - To display individual elements, use the syntax `${array_name[index]}`:

     ```bash
     echo ${colors[0]}  # Outputs: red
     echo ${colors[1]}  # Outputs: blue
     ```

3. **Displaying All Elements**
   - To display all elements in the array, use the `@` symbol:

     ```bash
     echo ${colors[@]}  # Outputs: red blue
     ```

4. **Counting Elements in the Array**
   - To count how many elements are in the array, use:

     ```bash
     echo ${#colors[@]}  # Outputs: 2
     ```

5. **Counting Characters in a Specific Element**
   - To count the number of characters in a specific element:

     ```bash
     echo ${#colors[1]}  # Outputs: 4 (for "blue")
     ```

#### Modifying Array Elements

1. **Replacing Array Values**
   - You can replace a specific element by directly assigning a new value:

     ```bash
     colors[1]="green"  # Changes blue to green
     echo ${colors[@]}  # Outputs: red green
     ```

2. **Echoing Changes**
   - To echo and see the output, remember it will show the updated values, but the original values remain unchanged in the array unless explicitly modified.

#### Populating an Array from a File

1. **Reading from a File**
   - Suppose you have a file named `stockvalues.txt` with numeric values. To load these into an array, use:

     ```bash
     stockvaluesvar=($(cat stockvalues.txt))
     ```

2. **Displaying File Contents in the Array**
   - To display the contents of the `stockvaluesvar` array:

     ```bash
     echo ${stockvaluesvar[@]}
     ```

#### Looping Through Array Elements

1. **Using a Loop to Process Each Element**
   - You can loop through each element in the array using a `for` loop:

     ```bash
     for individualstockvalue in "${stockvaluesvar[@]}"; do
         echo $individualstockvalue
     done
     ```

   - This will print each item in the `stockvaluesvar` array on a new line.

### Summary

Using array variables in Bash allows for efficient storage and manipulation of related data. With the ability to create, modify, and loop through arrays, you can handle collections of items seamlessly. This capability is especially useful for tasks such as processing lists of values from files or executing batch operations on groups of related data. 

Understanding these concepts will enhance your scripting skills and enable you to create more dynamic and powerful scripts in your Linux environment.

## 8. Creating a Shell Script Function

### Creating Shell Script Functions in Bash

In this demo, we'll learn how to create and use functions in Bash scripts. Functions allow you to group commands together so they can be reused easily within your scripts.

#### Defining a Function

1. **Basic Function Syntax**
   - To define a function, use the following syntax:

     ```bash
     function_name() {
         # commands
     }
     ```

   - For example, let's create a simple function called `general_details`:

     ```bash
     general_details() {
         clear
         hostname
         id
     }
     ```

   - You can call this function simply by typing its name:

     ```bash
     general_details
     ```

2. **Calling the Function**
   - When you call the function, it will execute the commands defined within it. In this case, it will clear the screen, display the hostname, and show user ID information.

#### Writing a Function in a Script

1. **Creating a Script with Functions**
   - Open a text editor (e.g., `nano`) to create a new script, for example, `functiontest.sh`:

     ```bash
     nano functiontest.sh
     ```

   - Start with the shebang line:

     ```bash
     #!/bin/bash
     ```

   - Define the function within the script:

     ```bash
     show_ipinfo() {
         IP_VAR=$(ifconfig | grep "inet" | tr -s " " ":" | cut -f3 -d ":")
         DGW_VAR=$(ip route show | grep "default" | tr -s " " ":" | cut -f3 -d ":")
         echo "IP ADDRESSES: $IP_VAR"
         echo "DEFAULT GATEWAY: $DGW_VAR"
         echo "DNS Servers:"
         cat /etc/resolv.conf | grep "nameserver" | grep -v "#"
     }
     ```

   - Call the function at the end of your script:

     ```bash
     show_ipinfo
     ```

2. **Running the Script**
   - Save and exit the editor.
   - Make the script executable:

     ```bash
     chmod +x functiontest.sh
     ```

   - Run the script:

     ```bash
     ./functiontest.sh
     ```

   - You should see output displaying your IP addresses, default gateway, and DNS servers.

#### Exporting Functions

1. **Making Functions Available in Other Scripts**
   - If you want a function defined in one script to be available in another, you can export it:

     ```bash
     export -f general_details
     ```

   - Create another script, e.g., `exportedfunction.sh`, that simply calls the exported function:

     ```bash
     #!/bin/bash
     general_details
     ```

   - Make this script executable:

     ```bash
     chmod +x exportedfunction.sh
     ```

   - Run the script:

     ```bash
     ./exportedfunction.sh
     ```

   - It will execute the `general_details` function defined earlier.

### Summary

Functions in Bash scripts provide a way to encapsulate code, making scripts more organized and easier to maintain. By defining functions, you can avoid code duplication and increase readability. Additionally, exporting functions allows them to be reused across multiple scripts, enhancing modularity in your scripting tasks. 

Understanding how to create and manage functions is crucial for effective shell scripting in a Linux environment.

## 9. Writing and Running a Backup Shell Script

### Automating Backups with Shell Scripts and Cron

In this guide, we'll explore how to create a backup shell script in Linux and automate its execution using Cron. This process allows technicians to back up important files seamlessly.

#### Creating a Backup Script

1. **Open a Text Editor**
   - Start by creating or opening a backup script file. We'll use `nano` for this example:
     ```bash
     nano backup.sh
     ```

2. **Setting Script Permissions**
   - Before writing the script, ensure that the file has the correct permissions. If you want the script to run with root privileges, use the following command:
     ```bash
     chmod 4755 backup.sh
     ```
   - The `4755` sets the user ID bit and grants read and execute permissions.

3. **Writing the Backup Script**
   - Start with the shebang line to specify the interpreter:
     ```bash
     #!/bin/bash
     ```
   - Define variables for the backup filename based on the current date:
     ```bash
     day=$(date +%d)
     month=$(date +%m)
     year=$(date +%Y)
     ```
   - Create a function to handle the backup:
     ```bash
     full_backup() {
         tar -czvf full_backup-$year-$month-$day.tar.gz /home > full_backup_log.log 2>/dev/null
     }
     ```
   - Call the function directly:
     ```bash
     full_backup
     ```

4. **Testing the Script**
   - Save your script and exit the editor.
   - Make sure the script runs correctly by executing:
     ```bash
     ./backup.sh
     ```
   - Verify that the backup file and log were created:
     ```bash
     ls
     ```

#### Scheduling the Backup Script with Cron

1. **Open the Crontab**
   - Use the following command to edit the crontab for your user:
     ```bash
     crontab -e
     ```

2. **Define the Cron Job**
   - To schedule the backup script to run at midnight every Saturday, add the following line:
     ```bash
     0 0 * * 6 /home/cblackwell/backup.sh
     ```
   - This line specifies:
     - `0` minutes
     - `0` hours (midnight)
     - `*` every day of the month
     - `*` every month
     - `6` for Saturday

3. **Save and Exit**
   - After adding the cron job, save the changes and exit the editor.

4. **Confirm the Cron Job**
   - You can list your current cron jobs to verify:
     ```bash
     crontab -l
     ```

#### Additional Considerations

- **Permissions**: Make sure that the backup script has the necessary permissions to access the files being backed up.
- **Testing**: Always test your backup script manually before scheduling it with Cron to ensure it works as expected.
- **Cron Syntax**: If you need to modify the timing or frequency of the backup, consult the `man` page for crontab:
  ```bash
  man 5 crontab
  ```

### Conclusion

Creating a backup script and scheduling it with Cron is an effective way to automate the backup process in Linux. By following these steps, you can ensure your important files are regularly backed up without manual intervention, improving data security and reliability.

## 10. Writing and Running a "For" Looping Shell Script

It looks like you're diving into shell scripting with for and while loops! Here's a concise breakdown of what you've covered:

### For Loop Variations

1. **Basic For Loop**:
   - Syntax: `for ((i=1; i<5; i++))`
   - Example:
     ```bash
     for ((i=1; i<5; i++)); do
       echo $i
     done
     ```
   - Output: 1, 2, 3, 4

2. **For Loop with Range**:
   - Syntax: `for i in {5..10}`
   - Example:
     ```bash
     for i in {5..10}; do
       echo $i
     done
     ```
   - Output: 5, 6, 7, 8, 9, 10

3. **For Loop with Custom Increment**:
   - Syntax: `for i in {5..10..2}`
   - Example:
     ```bash
     for i in {5..10..2}; do
       echo $i
     done
     ```
   - Output: 5, 7, 9

4. **Using If to Control Flow**:
   - Example with break:
     ```bash
     for i in {5..10..2}; do
       if [ $i -eq 9 ]; then
         break
       fi
       echo $i
     done
     ```
   - Output: 5, 7

5. **Processing Array Elements**:
   - Example:
     ```bash
     IPs=("192.168.1.1" "192.168.1.2")
     for host_ip in "${IPs[@]}"; do
       ping -c 2 $host_ip
     done
     ```

### While Loop Basics

1. **Basic While Loop**:
   - Syntax: `while [ $i -le 6 ]`
   - Example:
     ```bash
     i=1
     while [ $i -le 6 ]; do
       echo $i
       i=$((i + 1))
     done
     ```
   - Output: 1, 2, 3, 4, 5, 6

2. **Endless While Loop**:
   - Example of menu script:
     ```bash
     while true; do
       clear
       echo "1: Show IP Info"
       echo "2: List Logged On Users"
       echo "3: Exit"
       read selection
       case $selection in
         1) show_ipinfo ;;
         2) who ;;
         3) break ;;
       esac
       read -p "Press enter to continue..."
     done
     ```

3. **User Input Loop**:
   - Example:
     ```bash
     while true; do
       read -p "Enter hours worked and hourly wage or -1 to quit: " hours wage
       if [ $hours -eq -1 ]; then
         break
       fi
       pay=$((hours * wage))
       echo "Pay: $pay"
     done
     ```

### Key Points

- **Loop Structure**: Both loops require a condition and a block of code to execute.
- **Control Flow**: Use `break` to exit loops when certain conditions are met.
- **Read User Input**: Use the `read` command to interact with users within loops.

## 11. Troubleshooting Shell Scripts

When writing shell scripts, attention to detail is crucial due to the strict syntax rules across different shells (C shell, Korn shell, Bash shell).

**Running Scripts**
- To run a script, you must be in the correct directory. For example, to execute `menu.sh` from a subdirectory, type `./menu.sh`.

**File Permissions**
- Check permissions with `ls -l`. For instance, user `cblackwell` owns `menu.sh`, giving it read, write, and execute permissions (`rwx`).
- Change ownership: `sudo chown root menu.sh`.
- Check permissions again; root will now have `rwx`. Remove group and other permissions:
  - `sudo chmod g-rwx menu.sh`
  - `sudo chmod o-rx menu.sh`
- Now, `cblackwell` cannot execute the script due to lack of permissions. 

**Setting the Special User ID Bit**
- Use `sudo chmod 750 menu.sh` to grant read and execute permissions to the group.
- If `cblackwell` is part of this group, the script will run successfully.
- To remove execute permission for the group: `sudo chmod g-x menu.sh`.
- Restoring execute permission: `sudo chmod g+x menu.sh`.

**Special User ID Bit Explained**
- To set the special user ID bit: `sudo chmod 4750 menu.sh`. The leading `4` sets this bit.
- Confirm the change with `ls -l`; a lowercase `s` indicates the special user ID is set.
- The script can now run with the permissions of the root user, even if invoked by `cblackwell`.

**Functions in Shell Scripts**
- When declaring a function, ensure it's called in the script. Functions don't require parentheses when called.
- Always include a correct shebang line (e.g., `#!/bin/bash`) at the start of scripts to avoid unexpected behavior.

**Variable Scope**
- Variables are local to the shell they are defined in. For example, if a script echoes a variable that hasn’t been defined in the current shell, it will return nothing.
- Define a variable: `scriptvar="Testing 1 2 3"`.
- To access it outside its defining shell, export it: `export scriptvar`.
- After exporting, the variable will be accessible in other scripts or shells.

**Syntax and Best Practices**
- Always use `$` before variable names when referencing them.
- Use backticks (`` ` ``) around commands when storing their output in a variable.

By following these guidelines, you can effectively write and troubleshoot shell scripts, ensuring they function as intended.
