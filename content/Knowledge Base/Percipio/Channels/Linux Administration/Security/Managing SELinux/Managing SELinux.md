---
date: 2001-01-01
---

# Managing SELinux

## 1. Security-Enhanced Linux (SELinux)

### Overview of SELinux (Security-Enhanced Linux)

SELinux, or Security-Enhanced Linux, is a security architecture integrated into the Linux kernel that implements mandatory access control (MAC). This means that access to resources (files, network sockets, etc.) is regulated by the system rather than individual users, enhancing the overall security of Linux systems, especially in sensitive environments.

---

#### Key Concepts of SELinux

1. **Modes of Operation**:
   - **Disabled**: SELinux is not running.
   - **Permissive**: SELinux is active but only logs actions that would have been denied.
   - **Enforcing**: SELinux actively controls access based on defined policies.

2. **Security Contexts**:
   - Resources are labeled with security contexts, which define their access permissions. This includes files, processes, and network sockets.

3. **SELinux Users and Policies**:
   - Linux users can be mapped to SELinux users through policies, allowing specific access control based on context.

4. **Viewing Contexts**:
   - To see the SELinux context of running processes:
     ```bash
     ps auxZ
     ```
   - To view the SELinux context of files:
     ```bash
     ls -Z
     ```
   - To view the SELinux user context:
     ```bash
     id -Z
     ```

5. **Changing Contexts**:
   - Use the `chcon` command to change the context of files:
     ```bash
     chcon -t httpd_sys_content_t /path/to/file
     ```
   - Use `semanage` for managing file contexts:
     ```bash
     semanage fcontext -a -t httpd_sys_content_t '/path/to/directory(/.*)?'
     ```

---

### Enabling SELinux on Ubuntu

#### Step-by-Step Process

1. **Stop AppArmor** (if active):
   ```bash
   sudo service apparmor stop
   sudo systemctl disable apparmor
   ```

2. **Install SELinux Packages**:
   ```bash
   sudo apt update
   sudo apt install policycoreutils selinux-utils selinux-basics
   ```

3. **Check SELinux Status**:
   ```bash
   sudo sestatus
   sudo getenforce
   ```

4. **Activate SELinux**:
   - Modify the SELinux configuration:
     ```bash
     sudo nano /etc/selinux/config
     ```
   - Change the line to:
     ```
     SELINUX=permissive
     ```

5. **Activate and Reboot**:
   ```bash
   sudo selinux-activate
   sudo init 6  # Reboot
   ```

6. **Post-Reboot Status Check**:
   ```bash
   sudo sestatus
   sudo getenforce
   ```

7. **Switch to Enforcing Mode** (if needed):
   ```bash
   sudo setenforce 1
   ```

8. **Update Configuration for Future Boots**:
   - Ensure `/etc/selinux/config` is set to:
     ```
     SELINUX=enforcing
     ```
   - Reboot again to apply changes.

---

### Important Considerations

- Before setting SELinux to enforcing mode, ensure that your contexts and user mappings are configured correctly to avoid being locked out of your system.
- Always start with permissive mode to monitor what would be denied before enforcing stricter controls.
- Familiarize yourself with SELinux logs to troubleshoot issues related to denied access.

By implementing SELinux, you can significantly enhance the security posture of your Linux systems, particularly when handling sensitive data or operating in high-security environments.

## 2. Configure SELinux

### Basic SELinux Configuration

In this demonstration, we’ll cover essential SELinux configuration tasks, focusing on file contexts and basic management through the configuration file.

---

#### Overview of SELinux Configuration

1. **Check SELinux Status**:
   - First, you can check the current status and mode of SELinux using:
     ```bash
     sudo getenforce
     ```

2. **Modify SELinux Mode**:
   - To change SELinux mode temporarily, use:
     ```bash
     sudo setenforce 1  # Set to enforcing mode
     sudo setenforce 0  # Set back to permissive mode
     ```

3. **Edit SELinux Configuration**:
   - To make permanent changes, edit the configuration file:
     ```bash
     sudo nano /etc/selinux/config
     ```
   - Change `SELINUX=permissive` to `SELINUX=enforcing`, then save and reboot for changes to take effect.

---

#### Working with SELinux Contexts

1. **View User Context**:
   - Check your current SELinux user context:
     ```bash
     id -Z
     ```
   - You may see output like:
     ```
     unconfined_u:unconfined_r:unconfined_t:s0
     ```

2. **View Process Contexts**:
   - To see running processes along with their SELinux contexts:
     ```bash
     ps auxZ
     ```
   - To filter for specific processes (e.g., Apache):
     ```bash
     ps auxZ | grep apache
     ```

3. **Check File Contexts**:
   - Navigate to the default web directory:
     ```bash
     cd /var/www/html
     ```
   - List file contexts with:
     ```bash
     ls -Z
     ```

4. **Create a New Directory and File**:
   - Create a new web directory and file:
     ```bash
     sudo mkdir /site1
     sudo touch /site1.html
     ```

5. **Check New File Context**:
   - Check the context of the new file:
     ```bash
     ls -Z /site1
     ```
   - You may notice it has an incorrect context for Apache access.

---

#### Changing File Contexts

1. **Change File Context**:
   - To adjust the context so that Apache can access the new directory, use:
     ```bash
     sudo chcon -R -t httpd_sys_content_t /site1
     ```

2. **Verify the Change**:
   - After changing the context, verify it again:
     ```bash
     ls -Z /site1
     ```
   - The type should now show `httpd_sys_content_t`, indicating proper access permissions.

---

### Summary

- SELinux provides robust security through mandatory access control by managing user and file contexts.
- Ensure you check and configure user mappings to avoid access issues when switching to enforcing mode.
- Use commands like `ls -Z`, `ps auxZ`, and `id -Z` to effectively manage and monitor SELinux contexts across files and processes.
- Remember to use `chcon` to adjust file contexts as needed to ensure applications can access their required resources correctly. 

This foundational understanding of SELinux will help you manage security configurations effectively in your Linux environment.

## 3. Managing SELinux Users

### Managing SELinux Users

In this demonstration, we will focus on mapping Linux user accounts to SELinux users, which is crucial for accessing resources governed by SELinux policies. 

---

#### Step 1: Check Current SELinux Status

1. **View SELinux Mode**:
   ```bash
   getenforce
   ```
   - This will show whether SELinux is in **permissive** or **enforcing** mode.

#### Step 2: Attempt SSH Login

2. **SSH Session Check**:
   - Open a second SSH session as user `cblackwell` to see if you can log in while SELinux is in permissive mode.

#### Step 3: Change to Enforcing Mode

3. **Set Enforcing Mode**:
   ```bash
   sudo setenforce 1
   ```
   - This will switch SELinux to enforcing mode.

4. **Attempt Another SSH Login**:
   - Try logging in again as `cblackwell`. You should be denied access because `cblackwell` has not been mapped to an SELinux user.

#### Step 4: View SELinux Users

5. **List SELinux Users**:
   ```bash
   sudo semanage user -l
   ```
   - This will display the existing SELinux users. Note the default user, `staff_u`.

#### Step 5: Map Linux User to SELinux User

6. **Check Existing Mappings**:
   ```bash
   sudo semanage login -l
   ```
   - Here, you will check if `cblackwell` is already mapped to an SELinux user.

7. **Map User**:
   - To map `cblackwell` to `staff_u`, run:
   ```bash
   sudo semanage login -a -s staff_u cblackwell
   ```

8. **Verify Mapping**:
   - Check the mappings again:
   ```bash
   sudo semanage login -l
   ```
   - You should see `cblackwell` now mapped to `staff_u`.

#### Step 6: Test SSH Access Again

9. **Retry SSH Login**:
   - Attempt to SSH into the server again as `cblackwell`. This time, the login should succeed since the user is now mapped to an SELinux user that has the necessary permissions.

#### Step 7: Remove User Mapping

10. **Unmap User**:
    - If you need to remove the mapping, you can do so with:
    ```bash
    sudo semanage login --delete -s staff_u cblackwell
    ```

11. **Verify Removal**:
    - Check the mappings again to confirm that `cblackwell` has been removed:
    ```bash
    sudo semanage login -l
    ```

#### Conclusion

- Properly managing SELinux users is essential for maintaining access control in an SELinux-enabled environment.
- Always remember to check and manage user mappings, especially when switching between permissive and enforcing modes.
- Be aware of the restrictions associated with different SELinux user types, such as `staff_u` versus `unconfined_u`, to ensure appropriate access levels are maintained.

This process will help ensure that your users can access necessary resources without compromising the security measures provided by SELinux.

## 4. Managing the Apache Process and Files

### Managing Processes and File Access with SELinux in Enforcing Mode

In this demonstration, we'll manage processes and their file access when SELinux is set to enforcing mode, specifically focusing on the Apache web server.

---

#### Step 1: Check Running Processes

1. **View Processes with Context**:
   ```bash
   ps -auxZ | grep apache2
   ```
   - The output will show the Apache processes and their SELinux types, such as `httpd_t`.

#### Step 2: Examine Apache Binary and Document Root

2. **Check Apache Binary**:
   ```bash
   ls -Z /usr/sbin/apache2
   ```
   - This should show the type as `httpd_exec_t`, indicating it can execute as an Apache process.

3. **Check Document Root**:
   ```bash
   ls -Z /var/www/html
   ```
   - The default index file should have a type of `httpd_sys_content_t`, allowing Apache to serve it.

#### Step 3: Set SELinux to Enforcing Mode

4. **Change SELinux to Enforcing Mode**:
   ```bash
   sudo setenforce 1
   ```

5. **Check Apache Status**:
   ```bash
   sudo service apache2 status
   ```
   - Ensure Apache is active and running.

6. **Access the Default Web Page**:
   - Open a web browser and navigate to the server's IP address (e.g., `http://192.168.2.156`). You should see the default Apache page.

#### Step 4: Create a New Web Directory

7. **Create a New Directory for Custom Site**:
   ```bash
   sudo mkdir /mysite
   cd /mysite
   sudo nano index.html
   ```
   - Add basic HTML content and save the file.

#### Step 5: Configure Apache to Use the New Directory

8. **Edit Apache Configuration**:
   ```bash
   sudo nano /etc/apache2/sites-enabled/000-default.conf
   ```
   - Change the `DocumentRoot` to `/mysite`.

9. **Restart Apache**:
   ```bash
   sudo service apache2 restart
   ```

#### Step 6: Test Access in Enforcing Mode

10. **Set SELinux to Enforcing Again**:
    ```bash
    sudo setenforce 1
    ```

11. **Refresh Web Page**:
    - Go back to your web browser and refresh the page. You should see a "Forbidden" error because Apache cannot access the new directory.

#### Step 7: Check File Contexts

12. **Check File Context in /mysite**:
    ```bash
    ls -Z /mysite
    ```
    - The file should show `default_t`, which means SELinux is blocking access.

#### Step 8: Change File Context

13. **Change Context of the New Directory**:
    ```bash
    sudo chcon -R -t httpd_sys_content_t /mysite
    ```

#### Step 9: Verify Context Change

14. **Verify the Change**:
    ```bash
    ls -Z /mysite
    ```
    - Now, `index.html` should have the type `httpd_sys_content_t`.

#### Step 10: Refresh the Page

15. **Refresh Web Page Again**:
    - Check the browser again. The page should now load correctly, showing your custom content.

### Conclusion

- This demo illustrates how SELinux enforces access controls on processes and files.
- Properly managing file contexts ensures that processes like Apache can serve content without running into permission issues.
- Always verify SELinux contexts when configuring services to operate under enforcing mode.

## 5. Exploring AppArmor

### Managing AppArmor in Linux

In this demonstration, we’ll explore AppArmor, a mandatory access control (MAC) system used in distributions like Ubuntu and SUSE Linux. AppArmor helps restrict the capabilities of processes, similar to SELinux.

---

#### Step 1: Check AppArmor Status

1. **View Current AppArmor Profiles**:
   ```bash
   sudo apparmor_status
   ```
   - This command displays the loaded profiles and their modes. Look for profiles in "enforce" or "complain" mode.

#### Step 2: Understand AppArmor Modes

2. **Modes**:
   - **Complain Mode**: Similar to SELinux's permissive mode; it logs policy violations but does not enforce them.
   - **Enforce Mode**: Similar to SELinux's enforcing mode; it actively restricts access based on defined profiles.

#### Step 3: Set Profiles to Enforce Mode

3. **Set All Profiles to Enforce Mode**:
   ```bash
   sudo aa-enforce /etc/apparmor.d/*
   ```
   - If you encounter a "command not found" error, install the required utilities:
   ```bash
   sudo apt install apparmor-utils
   ```

4. **Verify Profile Status**:
   ```bash
   sudo apparmor_status
   ```
   - Check the number of profiles in enforce mode.

#### Step 4: Switch to Complain Mode

5. **Set All Profiles to Complain Mode**:
   ```bash
   sudo aa-complain /etc/apparmor.d/*
   ```

6. **Check Profile Status Again**:
   ```bash
   sudo apparmor_status
   ```
   - This should show the updated status of profiles.

#### Step 5: Manage Individual Profiles

7. **Focus on a Specific Profile**:
   - Change to the AppArmor directory:
   ```bash
   cd /etc/apparmor.d
   ls
   ```

8. **Set a Specific Profile to Enforce Mode**:
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.sbin.tcpdump
   ```

9. **Edit the Profile**:
   ```bash
   sudo nano /etc/apparmor.d/usr.sbin.tcpdump
   ```
   - Review the settings, noting that defaults are generally sufficient for most applications.

#### Step 6: Disable AppArmor on Boot

10. **Prevent AppArmor from Starting Automatically**:
    ```bash
    sudo systemctl disable apparmor
    ```
   - This will ensure that AppArmor does not start on the next reboot.

### Conclusion

- AppArmor provides a robust framework for controlling process behavior through defined profiles.
- You can switch between enforce and complain modes to monitor activity without immediate restrictions.
- Custom applications may require tailored profiles for optimal functionality under AppArmor.
- Disabling AppArmor at startup can be useful in development or troubleshooting scenarios.

