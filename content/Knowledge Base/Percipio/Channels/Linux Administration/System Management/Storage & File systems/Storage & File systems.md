# Storage & File systems

## 1. Linux Storage
As a Linux technician, a solid understanding of Linux storage is essential.

### Mass Storage Devices in Linux
- Mass storage devices are referenced as files located under `/dev`, which stands for Device.
- Examples include:
  - `/dev/sda` (first mass storage device)
  - `/dev/sdb` (second mass storage device)

### Partitioning in Linux
- Storage media can be partitioned into multiple sections.
- Partition numbering in Linux starts at one, not zero:
  - First partition of `/dev/sda` is `/dev/sda1`
  - Second partition is `/dev/sda2`
  - For a second mass storage device, the first partition would be `/dev/sdb1`.

### Partition Types: MBR vs. GPT
- **Master Boot Record (MBR)**:
  - Maximum individual partition size: 2 terabytes.
  - Maximum of four partitions.

- **GUID Partition Table (GPT)**:
  - No practical disk size limit.
  - More than 128 partitions possible in some implementations.

### Setting Partition Types for RAID
- To use disks in a RAID array (e.g., software RAID), use the `fdisk` command.
- To set the partition type to Linux RAID autodetect:
  - Press `T` in `fdisk` and enter `FD`.

### File System Types
To use partitions, they must be formatted with file systems, including:
- **ext2, ext3, ext4**: Extended file systems commonly used in Linux.
- **XFS**: High-performance file system for UNIX and Linux.
- **Reiser4FS**: Supports journaling to record disk transactions.

### Managing Linux File Systems and Storage Devices
- Several built-in commands are essential for managing storage:
  - **`lsblk`**: Lists block devices.
  - **`fdisk`**: Partitions disks and views existing partitions.
  - **`mkfs`**: Formats disk partitions (similar to Windows).
    - For specific file systems, use `mkfs.<filesystem>` (e.g., `mkfs.reiser4`).

### Mounting File Systems
After creating a file system, make it accessible by:
1. Creating an empty subdirectory (mount point).
2. Mounting the partition (e.g., `/dev/sda1`) into that directory.

### Example Commands
- **List SCSI Devices**:  
  ```bash
  lsblk --scsi
  ```
- **List Partitions on `/dev/sda`**:  
  ```bash
  sudo fdisk -l /dev/sda
  ```
- **Interactively Manage Partitions**:  
  Use `fdisk` without `-l` to create or remove partitions.

### Conclusion
Understanding how Linux handles mass storage, partitioning, and file systems is fundamental for effective system management.

## 2. File System Hierarchy Standard (FHS)
The File System Hierarchy Standard (FHS) provides a standardized directory structure for UNIX and Linux systems. This standard helps maintain familiarity across different distributions, although some may have slight variations.

### Key Directories in the Linux File System

- **/** (Root Directory)
  - The root file system, where all files and directories reside. All storage devices and network resources are mounted under this directory.

- **/bin**
  - Contains essential binary command line tools. Common commands like `passwd`, `cat`, and `grep` are found here.

- **/boot**
  - Stores boot loader files, such as those for GRUB (GRand Unified Bootloader). Typically, this directory is on a separate small partition.

- **/dev**
  - Represents hardware devices as files. This includes mass storage devices, optical drives, and special files like `/dev/null` for output suppression.

- **/etc**
  - Houses configuration files for the operating system and installed applications. Often contains subdirectories for specific services with configuration files typically having extensions like `.conf` or `.cfg`.

- **/home**
  - Contains user home directories, including for the root user.

- **/lib**
  - Contains library files that support the binaries found in `/bin` and other directories.

- **/media**
  - Used for mounting removable storage media, such as USB drives. These typically auto-mount under `/media`.

- **/mnt**
  - A temporary mount point for file systems that are mounted manually.

- **/var**
  - Stands for variable data, including log files for the system and services. May have subdirectories for different services.

- **/opt**
  - Contains optional software packages that may have been installed. These can include additional configuration files and binaries.

- **/srv**
  - Contains service data for services installed on the system, such as FTP or HTTP servers.

- **/tmp**
  - Used for temporary files that are often deleted on reboot.

- **/usr**
  - Stands for UNIX System Resources and contains user binaries, utilities, and applications.

- **/proc**
  - A virtual filesystem that provides information about running processes and system information. Contains subdirectories named after process identifiers (PIDs) and files like `cpuinfo` and `meminfo`.

### Navigating the File System
Familiarity with the FHS helps in navigating the file system across different Linux distributions. 

### Example Commands
- **Print Working Directory**:  
  ```bash
  pwd
  ```
- **List Directories**:  
  ```bash
  ls /
  ```
- **Explore `/proc` Directory**:  
  ```bash
  ls /proc
  ```

### Conclusion
Understanding the Linux File System Hierarchy is crucial for effective system navigation and management across various Linux distributions.

## 3. Linux Storage Command Line Tools
Linux offers various command line tools for managing storage, many of which require root privileges. It’s common to use the `sudo` command to run these tools with elevated permissions. Users must be listed in the `sudo` configuration to use this command.

### Common Linux Storage Commands

- **`lsblk`**
  - Purpose: Lists block devices.
  - Use `--scsi` option to show SCSI devices, which most mass storage devices are treated as by the Linux kernel.
  - **SCSI** stands for Small Computer System Interface.

- **`fdisk`**
  - Purpose: Manages disk partitions.
  - Use `-l` to list partitions on a disk. Note that command line parameters are case-sensitive.

- **`mkfs`**
  - Purpose: Creates a file system on a partition.
  - After partitioning with `fdisk`, use `mkfs` to format partitions for file storage (e.g., `mkfs.ext4` for ext4 file system).

- **`parted`**
  - Purpose: A partition management tool that allows for partition creation, resizing, and deletion.
  - It can expand a partition if adjacent free space is available or shrink partitions as needed.

- **`partprobe`**
  - Purpose: Instructs the Linux kernel to reread partition tables.
  - Useful for applying changes without needing to reboot the system.

### Example of Using `parted`
A command screenshot shows:
```bash
sudo parted
```
This command lists devices like `/dev/sda`, allowing you to manage partitions on those devices.

### GUI Disk Management
For users with a graphical interface, like Ubuntu Desktop, disk management utilities are available to manage disk partitioning visually. 

### Virtual Disks in Linux
When using a virtual machine, Linux recognizes virtual disks similarly to physical disks:
- Virtual disks can appear as `/dev/sda`, `/dev/sdb`, etc., in the Linux kernel.
- Example screenshots show disk layouts in VMware Workstation and Microsoft Azure.

### Conclusion
Familiarity with these command line tools is essential for effective management of file systems and storage in Linux environments.

## 4. Creating Linux File Systems
This demonstration focuses on creating Linux file systems via the command line, while also noting how to do so using a desktop GUI.

### Using the GUI for Disk Management
In a desktop environment like Ubuntu Linux, you can manage disks using the Disks tool:

1. Click the **Show Applications** button.
2. Search for "disk" and select the **Disks** tool.
3. In the left pane, view a list of disks. Selecting a disk shows its layout on the right.
4. You can format a partition by clicking the gear icon to access options for:
   - Formatting
   - Resizing
   - Running checks and repairs
   - Configuring mounting options

### Switching to the Command Line
On a command line interface, you can manage partitions using commands like `fdisk`.

1. Run:
   ```bash
   sudo fdisk -l
   ```
   This lists the disk configuration, showing partitions and their types.

2. Identify your disks. For instance, `/dev/sda` might show multiple partitions (e.g., `sda1`, `sda2`, `sda3`).

3. To manage a specific disk, run:
   ```bash
   sudo fdisk /dev/sdb
   ```

### Creating a New Partition
1. If the disk is in use (e.g., by LVM), you can wipe it if you don’t need the data.
2. Press **N** to create a new partition and **P** for a primary partition.
3. Accept the default options for partition number, starting sector, and ending sector.

4. If prompted about an existing file system signature, type **Y** to remove it.
5. Write the changes with **W**.

### Formatting the Partition
Once the partition is created, you need to format it:

1. Run:
   ```bash
   sudo mkfs -t ext4 /dev/sdb1
   ```
   This creates an ext4 file system on the new partition.

### Mounting the New File System
To make the new file system accessible:

1. Create a mount point:
   ```bash
   sudo mkdir /data1
   ```
2. Mount the partition:
   ```bash
   sudo mount /dev/sdb1 /data1
   ```

3. Verify the mount:
   ```bash
   mount | grep sdb1
   ```
   This confirms that `/dev/sdb1` is mounted under `/data1`, allowing you to work with files in that directory.

### Conclusion
This session provided a step-by-step guide on managing disk partitions and formatting in Linux using both command line and GUI tools. You now have the foundational skills to create and manage file systems effectively.

## 5. Mounting Local Linux File Systems
This session focuses on mounting local Linux file systems from local storage, not network storage.

### Listing Current Disk Partitions
1. Use the following command to list disk partitions:
   ```bash
   sudo fdisk -l
   ```
   - Example output shows device partitions like:
     - **/dev/sda**: Boot and Linux file systems.
     - **/dev/sdb**: A single Linux partition.
     - **/dev/sdc**: Unused.

### Checking Mounted File Systems
1. To see current mounts, run:
   ```bash
   mount
   ```
   - To filter for a specific device (e.g., `/dev/sdb`), you can pipe to `grep`:
     ```bash
     mount | grep sdb
     ```

### Creating and Mounting a New Partition
1. To create a new partition on `/dev/sdc`, run:
   ```bash
   sudo fdisk /dev/sdc
   ```
   - Follow the prompts to create a new primary partition.
   - Write changes with **W**.
2. Format the new partition:
   ```bash
   sudo mkfs -t ext4 /dev/sdc1
   ```
3. Create a mount point:
   ```bash
   sudo mkdir /data2
   ```
4. Mount the partition:
   ```bash
   sudo mount /dev/sdc1 /data2
   ```
5. Verify the mount:
   ```bash
   mount | grep sdc
   ```

### Making Mounts Persistent with `/etc/fstab`
1. Open the `fstab` file for editing:
   ```bash
   sudo nano /etc/fstab
   ```
2. Add a new entry for the new partition. The format is:
   ```
   /dev/sdc1   /data2   ext4   rw   0   2
   ```
   - Here:
     - **/dev/sdc1** is the file system.
     - **/data2** is the mount point.
     - **ext4** is the file system type.
     - **rw** specifies read-write access.
     - **0** means no backup with `dump`.
     - **2** specifies the order for `fsck` checks.
3. Save and exit the editor (Ctrl + X, then Y, then Enter).

### Testing the Configuration
1. Reboot the system to test:
   ```bash
   sudo init 6
   ```
2. After rebooting, check if the partition is mounted:
   ```bash
   ls /data2
   ```
3. Verify the mount:
   ```bash
   mount | grep sdc
   ```

### Unmounting the File System
1. To unmount the file system:
   ```bash
   sudo umount /data2
   ```
2. Verify it is unmounted:
   ```bash
   mount | grep sdc
   ```
3. Check the contents of `/data2`:
   ```bash
   ls /data2
   ```

### Remounting
1. To remount the file system:
   ```bash
   sudo mount /dev/sdc1 /data2
   ```
2. Verify the contents are accessible again:
   ```bash
   ls /data2
   ```

### Conclusion
This session demonstrated how to manage local Linux mount points using `mount`, `umount`, and configuring `/etc/fstab` for persistent mounts. You can now effectively manage and automate your file system mounts in Linux.

## 6. Mounting Remote Cloud-based File Systems
This session focuses on creating a shared folder in Microsoft Azure and mounting it on a Linux machine.

### Steps to Create a Cloud Storage Account
1. **Log into Microsoft Azure Portal**.
2. Click on **Create a resource**.
3. Select **Storage account** and click **Create**.
4. Choose a **Resource group** and provide a unique name for the storage account (e.g., `storaccteastyhz765`).
5. Select the **Region** (e.g., East US).
6. Click **Review + Create** and then **Create**.

### Creating a Shared Folder
1. Once the storage account is created, navigate to **File shares** within the storage account.
2. Click on **Add file share**.
3. Name the file share (e.g., `projects`) and click **Create**.
4. Open the new file share and create a directory (e.g., `current_year`).
5. Upload files to the directory (e.g., `Project_A.txt`, `Project_B.txt`, `Project_C.txt`).

### Connecting to the File Share from Linux
1. Click on the **Connect** button within the file share.
2. Select the **Linux** tab to view the mount script.
3. Copy the provided mount command, which uses the `cifs` filesystem type:
   ```bash
   sudo mount -t cifs //storaccteastyhz765.file.core.windows.net/projects /mnt/projects -o credentials=/path/to/credentials/file
   ```

### Accessing the Virtual Machine
1. Navigate to **Virtual machines** in the Azure portal and select your running Ubuntu Linux VM.
2. Copy the **Public IP** address for SSH access.

### Establishing an SSH Connection
1. Use an SSH client (like PuTTY) to connect to your Linux VM using the public IP.

### Executing the Mount Command
1. Paste the copied mount command into the terminal on your Linux VM and press Enter.
2. Verify that the mount entry is present in `/etc/fstab`:
   ```bash
   sudo tail /etc/fstab
   ```

### Verifying the Mount
1. Check the contents of the mounted directory:
   ```bash
   ls /mnt/projects/current_year
   ```
   - You should see the uploaded project files listed (e.g., `Project_A.txt`, `Project_B.txt`, `Project_C.txt`).

### Conclusion
This demonstration highlighted how to create a shared folder in Microsoft Azure, upload files, and mount it on a Linux system using the `cifs` protocol. By adding the mount command to `/etc/fstab`, the connection is persistent across reboots, ensuring easy access to cloud-based storage.

## 7. Hard Links vs. Symbolic Links

#### Hard Links
- **Definition:** A hard link creates a new directory entry for an existing file, sharing the same inode.
- **Inode Sharing:** All hard links to a file point to the same inode, meaning they reference the same data blocks on disk.
- **File Identification:** You cannot distinguish the "original" file from its hard links; they are all equal.
- **Link Count:** The number of hard links is reflected in the file's metadata. When you list files with `ls -l`, the second column shows the number of links.
- **Limitations:** Hard links cannot span different filesystems (e.g., different partitions).

#### Symbolic Links (Symlinks)
- **Definition:** A symbolic link creates a new file that points to the name of another file, effectively acting as a shortcut.
- **New Inode:** Each symlink has its own inode, which points to the original filename rather than the data itself.
- **Flexibility:** Symlinks can span across different filesystems, allowing you to link to files on different partitions.
- **File Metadata:** Symlinks can have different owners, groups, and permissions from the original file.
- **Creation Command:** Use `ln -s <target> <linkname>` to create a symlink. For example:
  ```bash
  ln -s /budgets/file1.xls /home/cblackwell/file1.xls
  ```

### Summary
- **Data Modification:** Both hard links and symlinks allow you to modify the underlying data. Deleting the last link (either hard or symbolic) will remove the data from the filesystem.
- **Use Cases:** Hard links are useful for maintaining file integrity across locations, while symlinks provide more flexibility in linking files across different directories and partitions.

Understanding the differences and uses of hard links and symbolic links is essential for effective file management in Linux.

## 8. Working with Hard and Symbolic Links

#### Overview
Links provide alternative access methods to files in the Linux file system. There are two main types of links:
- **Hard Links**: Share the same inode as the original file.
- **Symbolic Links (Symlinks)**: Have their own inode and point to the original file by name.

### Creating Hard Links
1. **Command**: Use the `ln` command to create a hard link.
   ```bash
   ln customers.txt hardlink_customers.txt
   ```
2. **Verification**: Use `ls -li` to check inodes. Both files will share the same inode number.
   ```bash
   ls -li customers.txt hardlink_customers.txt
   ```
3. **Modifying Files**: If you change the content of the original file, the hard link reflects those changes since they point to the same data blocks.

### Creating Symbolic Links
1. **Command**: Use the `ln -s` command to create a symbolic link.
   ```bash
   ln -s customers.txt softlink_customers.txt
   ```
2. **Verification**: Again, use `ls -li`. The symlink will have a different inode number, indicated by a visual arrow (`->`) pointing to the original file.
   ```bash
   ls -li customers.txt softlink_customers.txt
   ```
3. **Modifying Files**: Changes made to the original file will still be visible through the symlink, as they both point to the same data.

### Key Differences
- **Inodes**: Hard links share the same inode, while symlinks have unique inodes.
- **Cross Filesystems**: Symlinks can link across different filesystems, while hard links cannot.
- **Metadata**: Symlinks can have different permissions, owners, and groups due to their unique inodes.

### Summary
- Hard links provide a straightforward way to access the same data through multiple filenames, maintaining shared metadata.
- Symbolic links offer greater flexibility by allowing links to point across different filesystems, although they are treated as separate entities with distinct metadata.

Understanding these concepts enhances file management efficiency and flexibility within the Linux environment.

## 9. Managing Linux File Systems

#### Overview
Managing a Linux file system involves checking for and repairing corruption that can prevent proper mounting. This guide focuses on using `fsck` for checking file systems and `tune2fs` for modifying file system parameters.

### Key Commands

#### 1. `fsck` (File System Check)
- **Purpose**: Checks and repairs Linux file systems.
- **Usage**:
  ```bash
  sudo fsck /dev/sdb1
  ```
- **Behavior**: 
  - If the specified partition is mounted, `fsck` will abort and display an error.
  - If unmounted, it will check the file system and report its status (e.g., "clean" or indicate errors).

- **Exit Status**: You can check the exit status for different outcomes, which is useful for scripting.

#### 2. Viewing `/etc/fstab`
- **Purpose**: This file contains persistent mount points and settings for file system checks at boot.
- **Key Fields**:
  - The sixth field specifies whether `fsck` should check the file system at boot:
    - `0`: No check
    - `1`: Check first (usually the root file system)
    - `2`: Check afterwards in order

### Example Commands
- **To view the current mount status**:
  ```bash
  sudo mount | grep sdb
  ```

#### 3. `tune2fs`
- **Purpose**: Modifies settings for ext2, ext3, and ext4 file systems.
- **Listing File System Information**:
  ```bash
  sudo tune2fs -l /dev/sdb1
  ```
  This command provides detailed information, including the file system state (clean/dirty).

- **Setting a Volume Label**:
  ```bash
  sudo tune2fs -L HQData /dev/sdb1
  ```
  This assigns a meaningful name to the file system for easier identification.

- **Setting a Check Interval**:
  ```bash
  sudo tune2fs -i 1w /dev/sdb1
  ```
  This configures the file system to be checked once a week.

### Summary
Using `fsck` helps maintain the integrity of your Linux file systems by checking and repairing them, while `tune2fs` allows you to modify parameters for better management. Regular checks and proper labeling enhance system readability and reliability.

## 10. RAID (Redundant Array of Independent Disks)

RAID is a technology that combines multiple physical disks into a single logical unit to improve performance and provide redundancy. It can be implemented using hardware RAID controllers or software RAID within the operating system.

### Common RAID Levels

1. **RAID 0 (Striping)**
   - **Description**: Data is divided into stripes and written across multiple disks.
   - **Performance**: High—improves read/write speeds.
   - **Fault Tolerance**: None—if one disk fails, all data is lost.

2. **RAID 1 (Mirroring)**
   - **Description**: Data is duplicated on two or more disks.
   - **Performance**: Good—improves read speed; write speed is similar to a single disk.
   - **Fault Tolerance**: High—if one disk fails, the other disk(s) still hold a complete copy of the data.

3. **RAID 5 (Striping with Distributed Parity)**
   - **Description**: Data and parity (error recovery information) are striped across at least three disks.
   - **Performance**: Balanced—offers good read speeds and acceptable write speeds.
   - **Fault Tolerance**: Can tolerate one disk failure; data can be reconstructed using the parity information stored on other disks.

4. **RAID 6 (Double Parity)**
   - **Description**: Similar to RAID 5, but with two sets of parity information, requiring at least four disks.
   - **Performance**: Slightly slower than RAID 5 due to additional parity calculations.
   - **Fault Tolerance**: Can tolerate two disk failures, allowing for greater reliability.

5. **RAID 10 (1+0)**
   - **Description**: Combines mirroring (RAID 1) and striping (RAID 0). Requires a minimum of four disks.
   - **Performance**: High—benefits from the speed of striping and the redundancy of mirroring.
   - **Fault Tolerance**: Can tolerate multiple disk failures as long as they do not occur in the same mirrored pair.

### Summary
RAID configurations enhance data availability and performance, making them essential for server environments and applications that require high reliability and speed. Each RAID level has its own benefits and trade-offs regarding performance and fault tolerance, allowing users to choose the right configuration based on their specific needs.

## 11. Configuring Software RAID in Linux

#### Step 1: Verify Available Disks
First, check the block storage devices to identify the disks you will use for RAID:

```bash
sudo lsblk --scsi
```

Then, list the details of the disks:

```bash
sudo fdisk -l /dev/sdc
sudo fdisk -l /dev/sdd
```

#### Step 2: Create Partitions
You need to create partitions on both disks and set them for RAID.

**For Disk 1:**

1. Open `fdisk` for the first disk:
   ```bash
   sudo fdisk /dev/sdc
   ```

2. Create a new partition:
   - Press `N` (New)
   - Select the default options for partition type and size.

3. Change the partition type to RAID:
   - Press `T` (Change type)
   - Type `FD` (Linux RAID autodetect)

4. Write the changes:
   - Press `W` (Write)

**Repeat the same steps for Disk 2:**
```bash
sudo fdisk /dev/sdd
```

#### Step 3: Install `mdadm`
Install the necessary software to manage RAID:

```bash
sudo apt install mdadm
```

#### Step 4: Create the RAID Array
Now, create the RAID 1 array using `mdadm`:

```bash
sudo mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sdc1 /dev/sdd1
```

You’ll be prompted to confirm the creation of the array. Type `yes` if needed.

#### Step 5: Check the Array Status
Monitor the synchronization status of the RAID array:

```bash
sudo mdadm --detail /dev/md1
```

#### Step 6: Create a Filesystem
Once synchronization is complete, create a filesystem on the new RAID device:

```bash
sudo mkfs -t ext4 /dev/md1
```

#### Step 7: Mount the RAID Device
Create a mount point and mount the RAID array:

1. Create a directory:
   ```bash
   sudo mkdir /mirror
   ```

2. Mount the RAID device:
   ```bash
   sudo mount /dev/md1 /mirror
   ```

Now, the RAID array is configured and accessible through the `/mirror` directory, allowing you to read and write data safely with redundancy.

## 12. Logical Volume Management (LVM)

Logical Volume Management (LVM) in Linux provides a flexible way to manage storage volumes. Here are the key points about its purpose and functionality:

#### 1. **Storage Pooling**
LVM allows you to pool together multiple physical storage devices (like hard drives or partitions) into a single logical unit. This pooling enables you to treat multiple disks as one cohesive storage space, making management easier and more efficient.

#### 2. **Dynamic Volume Management**
With LVM, you can create, resize, and delete logical volumes without the need to repartition disks. This flexibility allows you to adjust storage capacity according to changing needs without significant downtime.

#### 3. **Terminology Overview**
- **Physical Volume (PV)**: The actual storage devices (physical disks or partitions) that are used in LVM.
- **Volume Group (VG)**: A collection of physical volumes that form a single pool of storage.
- **Logical Volume (LV)**: A virtual disk that is created from the pooled storage in a volume group. It acts like a traditional disk partition from the operating system’s perspective.

#### 4. **Not a Replacement for RAID**
While LVM offers some features that may seem similar to RAID, it does not provide redundancy or data protection by itself. LVM focuses on managing disk space rather than protecting data. RAID configurations (like RAID 1, 5, etc.) are better suited for data redundancy.

#### 5. **Use Cases**
- **Flexible Storage Allocation**: Easily allocate storage space to applications or users without needing to manage physical partitions manually.
- **Easy Resizing**: Adjust the size of logical volumes on-the-fly, accommodating growing storage needs.
- **Snapshots**: Create snapshots of logical volumes for backup or testing purposes without affecting the live system.

#### 6. **Basic Commands**
- **pvcreate**: Marks a disk or partition as a physical volume for LVM.
- **vgcreate**: Creates a volume group from one or more physical volumes.
- **lvcreate**: Creates a logical volume within a volume group.
- **mount**: Mounts the logical volume to a specified directory for access.

### Conclusion
LVM enhances storage management in Linux by allowing for dynamic resizing, easy allocation of storage, and logical organization of disk space. It's especially useful in environments where storage needs frequently change or where managing multiple disks as a single unit simplifies administration.

## 13. Configuring LVM in Linux

In this section, we’ll walk through the steps to configure Logical Volume Management (LVM) in Linux. This process allows you to efficiently manage storage across multiple physical disks.

#### 1. **Check Available Disks**
Start by identifying which physical disks are available for LVM. Use the command:
```bash
sudo lvmdiskscan
```
This will list all storage devices suitable for LVM. Look for devices like `/dev/sdb`, `/dev/sdc`, and `/dev/sdd`.

#### 2. **Create Physical Volumes**
Next, mark the identified disks as physical volumes using the `pvcreate` command:
```bash
sudo pvcreate /dev/sdb /dev/sdc /dev/sdd
```
You should see a confirmation message indicating that the physical volumes have been successfully created.

#### 3. **View Physical Volumes**
To verify the physical volumes, run:
```bash
sudo pvs
```
This command provides a summary of the physical volumes and their sizes.

#### 4. **Create a Volume Group**
Now, create a volume group that pools the physical volumes together:
```bash
sudo vgcreate VolGroup1 /dev/sdb /dev/sdc /dev/sdd
```
You can check the status of your volume groups with:
```bash
sudo vgs
```
This should show `VolGroup1` along with its total size.

#### 5. **Create a Logical Volume**
Now, create a logical volume from the volume group. Specify the size (making sure to leave some space free for LVM to function):
```bash
sudo lvcreate -L 50G -n projects VolGroup1
```
Adjust the size if necessary based on available space.

#### 6. **Format the Logical Volume**
Once the logical volume is created, format it with a file system (like ext4):
```bash
sudo mkfs -t ext4 /dev/VolGroup1/projects
```

#### 7. **Create a Mount Point**
Next, create a directory to serve as the mount point for the logical volume:
```bash
sudo mkdir /projects
```

#### 8. **Mount the Logical Volume**
Mount the logical volume to the newly created directory:
```bash
sudo mount /dev/VolGroup1/projects /projects
```
You can verify the mount with:
```bash
sudo mount | grep projects
```

#### 9. **Make the Mount Persistent**
To ensure that the mount persists across reboots, you need to edit the `/etc/fstab` file. Open it using a text editor:
```bash
sudo nano /etc/fstab
```
Add the following line at the end:
```
/dev/VolGroup1/projects /projects ext4 defaults 0 0
```
Save the file (Ctrl + X, then Y, and Enter).

#### 10. **Conclusion**
You have now successfully configured LVM in Linux! This setup allows you to manage storage dynamically, resize volumes, and add more disks in the future if needed.

## 14. Network Storage

In this session, we’ll explore how Linux can connect to network storage solutions, focusing on Storage Area Networks (SAN) and Network Attached Storage (NAS).

#### 1. **Storage Area Networks (SAN)**
A SAN is a dedicated network for storage communications, exclusively used for transferring data between servers and storage devices. This setup allows multiple Linux servers to access shared storage over the network without other types of traffic interfering.

- **Centralized Storage:** SANs centralize storage arrays, simplifying backup processes and management. This means backups can be performed at the storage level instead of on each individual server.
- **Booting Over SAN:** Depending on the SAN solution, servers can boot directly from SAN storage.

#### 2. **iSCSI (Internet Small Computer System Interface)**
iSCSI is a protocol that allows SCSI commands to be sent over IP networks. Here’s how it works:

- **Setup:** iSCSI requires standard network equipment (like Ethernet switches) and involves configuring both iSCSI initiators (the Linux servers) and iSCSI targets (the storage devices).
- **Operation:** SCSI commands are encapsulated in IP packets and sent over a dedicated network, which ensures optimal performance by isolating storage traffic from regular network activities.

**Diagram Overview:**
- **Initiators:** Linux and Windows servers using iSCSI initiators (either software-based or via hardware controllers).
- **Targets:** Storage devices that respond to requests from initiators, usually operating on TCP port 3260.

To the Linux server, the iSCSI storage appears as local storage, enabling normal management and partitioning.

#### 3. **Fibre Channel SAN**
Fibre Channel is designed for high-speed storage communication, using specialized hardware rather than standard networking equipment.

- **Equipment:** It requires Host Bus Adapters (HBAs) in servers and Fibre Channel switches to connect consumers to storage providers.
- **Redundancy:** Connections can be configured for multiple paths, enhancing reliability and performance.

**Diagram Overview:**
- **Connection:** Servers with HBAs connect to Fibre Channel switches, which in turn connect to storage arrays. This setup allows for backup units to be linked to the storage arrays.

#### 4. **Security Considerations**
When implementing SAN solutions, consider:
- **LUN Masking:** This restricts which servers can access specific storage areas, enhancing security.
- **Data Encryption:** Assess whether to encrypt data at rest within the storage arrays.
- **File Access Auditing:** Implement targeted auditing to meet compliance requirements without overwhelming your logs.

#### 5. **Network Attached Storage (NAS)**
NAS is a dedicated storage appliance designed to share files over a network.

- **Architecture:** NAS devices come with their own CPUs and RAM, connecting through standard protocols like SMB and NFS.
- **Storage Configuration:** Typically supports configurations like JBOD (Just a Bunch of Disks) or various RAID levels for redundancy.

### Conclusion
Linux systems can effectively utilize network storage solutions like SAN and NAS to improve storage management, backup processes, and performance. Understanding these technologies is crucial for effective enterprise storage solutions.

## 15. Configuring an iSCSI Initiator in Linux

In this tutorial, we’ll walk through the steps to configure a Linux-based iSCSI initiator to connect to an iSCSI target hosted on a Windows Server.

#### Prerequisites
- **Windows Server:** Ensure that the iSCSI Target Server role is installed and configured.
- **Linux Client:** This will be configured as the iSCSI initiator.

### Steps to Configure iSCSI

#### 1. **Setting Up the iSCSI Target on Windows Server**
   - Open **Server Manager**.
   - Click on **Add Roles and Features**.
   - Proceed through the wizard to the **Roles** section.
   - Expand **File and Storage Services**, then **iSCSI**.
   - Enable the **iSCSI Target Server** role and complete the installation.

   **Creating an iSCSI Virtual Disk:**
   - Go to **File and Storage Services** > **iSCSI**.
   - Click **New iSCSI Virtual Disk** under Tasks.
   - Select a storage location (e.g., drive F) and name your disk (e.g., `iSCSI_Vdisk1`).
   - Specify a size (e.g., 9.91 GB dynamically expanding).
   - Create an **iSCSI Target** named `LinuxHosts`.
   - Add the Linux host’s IP address (e.g., `192.168.2.41`) to allow access.

   **Note:** Copy the **iSCSI Qualified Name (IQN)** for later use (e.g., `iqn.1991-05.com.microsoft:win-m6cgn1mfjlq-linuxhosts-target`).

#### 2. **Configuring the iSCSI Initiator on Linux**
   - On your Linux machine, ensure that the `open-iscsi` package is installed. You can do this with:
     ```bash
     sudo apt-get install open-iscsi
     ```

   - Discover the iSCSI target:
     ```bash
     sudo iscsiadm --mode discovery --type sendtargets --portal 192.168.2.167
     ```
     This command checks for available iSCSI targets from the specified portal.

   - Log in to the iSCSI target using the IQN obtained earlier:
     ```bash
     sudo iscsiadm --mode node --targetname iqn.1991-05.com.microsoft:win-m6cgn1mfjlq-linuxhosts-target --portal 192.168.2.167 --login
     ```

#### 3. **Verifying the Connection**
   - Use the following command to list block devices and check for the iSCSI disk:
     ```bash
     lsblk --scsi | grep iscsi
     ```
   - To list all disks:
     ```bash
     sudo fdisk -l
     ```
     Your iSCSI disk should appear as `/dev/sde`.

#### 4. **Partitioning and Formatting the iSCSI Disk**
   - Start partitioning:
     ```bash
     sudo fdisk /dev/sde
     ```
     - Press `n` for a new partition, then `p` for primary, and accept defaults by pressing Enter.
     - Finally, press `w` to write changes.

   - Format the new partition (e.g., `/dev/sde1`) with ext4:
     ```bash
     sudo mkfs -t ext4 /dev/sde1
     ```

#### 5. **Mounting the iSCSI Disk**
   - Create a mount point:
     ```bash
     sudo mkdir /iscsi
     ```
   - Mount the partition:
     ```bash
     sudo mount /dev/sde1 /iscsi
     ```

   - To verify the mount, you can check:
     ```bash
     mount | grep iscsi
     ```

### Conclusion
Now your Linux system is configured as an iSCSI initiator, successfully connecting to the iSCSI target on Windows Server. The iSCSI storage appears as local storage on your Linux machine, allowing for normal file operations.