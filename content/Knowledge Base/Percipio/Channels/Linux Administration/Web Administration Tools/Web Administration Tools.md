---
date: 1970-01-01
---

# Web Administration Tools

## 1. Introduction to Nginx
Nginx is a fast, high-performance web server commonly used instead of Apache's HTTP server. 

### Installation Steps
1. **Install Nginx**  
   Open the terminal and run the command:
   ```bash
   sudo apt-get install nginx
   ```
   Confirm the installation by typing 'Y' when prompted.

2. **Verify Installation**  
   Open your web browser (e.g., Firefox) and type `localhost` in the address bar. If installed correctly, you should see the message "Welcome to Nginx!" If not, you may have another web server running, which you can remove or configure Nginx to run on a different port.

3. **Locate Default Files**  
   To find where the default files are served from, run:
   ```bash
   ls /usr/share/nginx/html
   ```
   You should see files like `50x.html` and `index.html`.

### Creating a New Directory for Your HTML Files
1. **Create a Directory**  
   Create a new directory for your HTML files:
   ```bash
   sudo mkdir /var/www
   ```

2. **Change Ownership**  
   To allow your user and the web server to access the directory, change the ownership:
   ```bash
   sudo adduser <your_username> www-data
   sudo chown <your_username>:www-data /var/www
   ```

3. **Create Subdirectory**  
   Navigate to `/var/www` and create a subdirectory for your project:
   ```bash
   cd /var/www
   mkdir default
   ```

### Configure Nginx
1. **Edit Configuration File**  
   Open the Nginx configuration file:
   ```bash
   sudo vim /etc/nginx/sites-available/default
   ```
   Look for the line:
   ```nginx
   root /usr/share/nginx/html;
   ```
   Change it to:
   ```nginx
   root /var/www/default;
   ```

2. **Restart Nginx**  
   After saving your changes, restart Nginx to apply the new configuration:
   ```bash
   sudo service nginx restart
   ```

### Adding Your HTML File
1. **Create an Index File**  
   Navigate to the `default` directory and create an `index.html` file:
   ```bash
   cd default
   vim index.html
   ```
   Add the text "Hello, World!" to the file and save it.

2. **Test Your Setup**  
   In your web browser, go to `localhost`. You should now see "Hello, World!" displayed.

### Changing the Listening Port
1. **Modify Listening Port**  
   If you need to run Nginx on a different port (e.g., 8080), edit the configuration:
   ```nginx
   listen 8080 default_server;
   listen [::]:8080 default_server ipv6only=on;
   ```

2. **Restart Nginx Again**  
   Restart Nginx to apply the changes:
   ```bash
   sudo service nginx restart
   ```

3. **Access the New Port**  
   In your web browser, type `localhost:8080` to see your "Hello, World!" message.

### Conclusion
This concludes the introduction to setting up and running a simple Nginx web server. You can now customize your server and explore additional configurations as needed.

## 2. Introduction to MariaDB
MariaDB is a fork of MySQL created after MySQL was acquired by Oracle. It serves as a drop-in replacement for MySQL and is distributed under the GNU GPL license. Software that works with MySQL is also compatible with MariaDB.

### Installation Steps
1. **Install MariaDB**  
   Open the terminal and run the following command to install both the MariaDB client and server:
   ```bash
   sudo apt-get install mariadb-client mariadb-server
   ```
   Enter your password when prompted, and confirm the installation by typing 'Y' when asked.

2. **Set Up the Root Password**  
   During the installation, you will be prompted to set a password for the MariaDB "root" user. Enter a secure password and confirm it when asked.

### Verifying Installation
1. **Check Version**  
   To verify that MariaDB is installed, run:
   ```bash
   mysql --version
   ```
   This command should return the version information for MariaDB.

2. **Access MariaDB**  
   Log in to MariaDB using:
   ```bash
   mysql -u root -p
   ```
   Enter the password you set during installation. You should see a welcome message indicating that you are now in the MariaDB monitor.

### Using MariaDB
1. **Create a Database**  
   To create a new database, run:
   ```sql
   create database some_database;
   ```
   You should see a confirmation message indicating that the database was created successfully.

2. **Exit MariaDB**  
   To exit the MariaDB monitor, type:
   ```sql
   quit;
   ```
   This will return you to the terminal prompt.

### Conclusion
You have successfully installed and configured MariaDB as a drop-in replacement for MySQL. MariaDB functions in the same way as MySQL, allowing you to run commands and manage databases seamlessly. This concludes the introduction to setting up MariaDB.

## 3. Introduction to PHP5-FPM
PHP5-FPM is used to run PHP in FastCGI mode, enabling better performance when used with web servers like Nginx or Apache. This tutorial covers the installation of PHP5-FPM along with the command line interface (CLI).

### Installation Steps
1. **Install PHP5-FPM and PHP5-CLI**  
   Open the terminal and run the following command:
   ```bash
   sudo apt-get install php5-fpm php5-cli
   ```
   Confirm the installation by typing 'Y' when prompted. The installation process will start, and PHP5-FPM will also begin running.

2. **Check Installed Modules**  
   To see what other PHP5 modules are available for installation, use:
   ```bash
   apt-cache search php5
   ```
   This will provide a list of possible modules.

3. **Install Additional Modules**  
   A couple of commonly used modules are `php5-curl` and `php5-gd`. To install them, run:
   ```bash
   sudo apt-get install php5-curl php5-gd
   ```
   After installation, PHP5-FPM will automatically restart.

### Configuration Changes
1. **Edit the php.ini File**  
   Before attaching PHP5-FPM to a web server, it is important to modify the configuration. Open the `php.ini` file:
   ```bash
   sudo vim /etc/php5/fpm/php.ini
   ```
   Search for the line:
   ```ini
   ;cgi.fix-pathinfo=1
   ```

2. **Modify the Configuration**  
   Uncomment the line and change it to:
   ```ini
   cgi.fix-pathinfo=0
   ```
   This change mitigates potential security risks by ensuring PHP processes file requests accurately.

3. **Restart PHP5-FPM**  
   After saving your changes, restart the PHP5-FPM service to apply the new configuration:
   ```bash
   sudo service php5-fpm restart
   ```

### Conclusion
You have successfully installed and configured PHP5-FPM, making necessary adjustments for security. This sets the foundation for running PHP applications efficiently with your web server. This concludes the introduction to installing PHP5 FastCGI Process Manager.

## 4. Introduction to LEMP
LEMP stands for:
- **L**: Linux (Ubuntu in this case)
- **E**: nginx
- **M**: MariaDB (a drop-in replacement for MySQL)
- **P**: PHP

### Installation and Configuration Steps

1. **Install PHP MySQL Package**
   - Run the following command to install the PHP MySQL package:
     ```bash
     sudo apt-get install php5-mysql
     ```

2. **Configure PHP5-FPM**
   - Open the PHP5-FPM pool configuration:
     ```bash
     sudo vim /etc/php5/fpm/pool.d/www.conf
     ```
   - Locate and set the `listen` directive:
     ```ini
     listen = /var/run/php5-fpm.sock
     ```

3. **Configure nginx**
   - Edit the default nginx site configuration:
     ```bash
     sudo vim /etc/nginx/sites-available/default
     ```
   - Modify the `index` directive to prioritize `index.php`:
     ```nginx
     index index.php index.html index.htm;
     ```
   - Uncomment and modify the PHP handling block:
     ```nginx
     location ~ \.php$ {
         fastcgi_split_path_info ^(.+\.php)(/.+)$;
         fastcgi_pass unix:/var/run/php5-fpm.sock;
         fastcgi_index index.php;
         include fastcgi_params;
     }
     ```

4. **Restart nginx**
   - Save your changes and restart nginx:
     ```bash
     sudo service nginx restart
     ```

5. **Connect to MariaDB**
   - Launch MariaDB:
     ```bash
     mysql -u root -p
     ```
   - Create a new database:
     ```sql
     CREATE DATABASE lemp_test;
     ```

6. **Create a New User**
   - Create a new user and grant permissions:
     ```sql
     CREATE USER 'phpuser'@'localhost' IDENTIFIED BY 'your_password_here';
     GRANT SELECT, INSERT, UPDATE, DELETE ON lemp_test.* TO 'phpuser'@'localhost';
     FLUSH PRIVILEGES;
     ```

7. **Create the index.php File**
   - Open the index.php file:
     ```bash
     vim /var/www/default.php
     ```
   - Add the following PHP code:
     ```php
     <?php
     $dbo = new mysqli('localhost', 'phpuser', 'your_password_here');
     echo 'select_db returned: '.$dbo->select_db('lemp_test');
     $dbo->close();
     ?>
     ```

8. **Test the Configuration**
   - Open a web browser and navigate to `http://localhost`. 
   - You should see the output: `select_db returned: 1`, confirming that the connection to MariaDB is successful.

### Conclusion
Congratulations! You have successfully configured a basic LEMP stack, which is ready for developing PHP applications. This concludes the introduction to setting up a basic LEMP stack.

## 5. Creating a Self-Signed SSL/TLS Certificate with OpenSSL

#### Objectives
- Create a certificate signing request (CSR) and self-sign it using OpenSSL.

#### Steps:

1. **Install Dependencies**: Ensure Nginx and OpenSSL are installed.

2. **Generate RSA Private Key**:
   - Run the command:
     ```bash
     openssl genrsa -des3 -out myhostname.key 4096
     ```
   - Enter and confirm a secure passphrase.

3. **Create Certificate Signing Request (CSR)**:
   - Execute:
     ```bash
     openssl req -new -key myhostname.key -out myhostname.csr
     ```
   - Provide details such as country code, organization name, and common name (hostname).

4. **Remove Passphrase from Private Key** (Optional):
   - Copy the key:
     ```bash
     cp myhostname.key myhostname.key.pw
     ```
   - Run:
     ```bash
     openssl rsa -in myhostname.key.pw -out myhostname.key
     ```
   - Enter the passphrase to write the new key without a password.

5. **Self-Sign the Certificate**:
   - Use the command:
     ```bash
     openssl x509 -req -in myhostname.csr -signkey myhostname.key -out myhostname.crt
     ```

6. **Store Certificates**:
   - Create a directory for SSL certificates:
     ```bash
     sudo mkdir /etc/nginx/ssl
     ```
   - Copy the certificate and key:
     ```bash
     sudo cp myhostname.crt /etc/nginx/ssl
     sudo cp myhostname.key /etc/nginx/ssl
     ```

7. **Edit Nginx Configuration**:
   - Open the configuration file:
     ```bash
     sudo vim /etc/nginx/sites-available/default
     ```
   - Uncomment and modify the HTTPS section with the correct paths:
     ```nginx
     server {
         listen 443;
         server_name localhost;
         ssl on;
         ssl_certificate /etc/nginx/ssl/myhostname.crt;
         ssl_certificate_key /etc/nginx/ssl/myhostname.key;
         ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
     }
     ```

8. **Restart Nginx**:
   - Run:
     ```bash
     sudo service nginx restart
     ```

9. **Test the Configuration**:
   - Open Firefox and navigate to `https://localhost`.
   - A "This Connection is Untrusted" warning will appear; click "Add Exception" to proceed.
   - Confirm the exception, and you should see "Hello, World!" served over HTTPS.

### Conclusion
This tutorial demonstrates how to create and install a self-signed SSL/TLS certificate in Nginx, enabling secure HTTPS connections for your web server.

## 6. Modify the `/etc/hosts` File to Point a Domain to a Local Web Server

### Steps

1. **Create Your Local Web Directory:**
   ```bash
   sudo mkdir /var/www/example
   sudo chgrp www-data /var/www/example
   ```

2. **Create Your `index.html` File:**
   ```bash
   sudo vim /var/www/example.html
   ```
   Add the text:
   ```
   Hello from example.com!
   ```
   Save and exit.

3. **Create Nginx Configuration:**
   Create a file called `example.ngx`:
   ```bash
   vim example.ngx
   ```
   Add the following configuration:
   ```nginx
   server {
       listen 80;
       root /var/www/example;
       index index.html;
       server_name example.com;

       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```
   Save and exit.

4. **Copy Configuration to Nginx:**
   ```bash
   sudo cp example.ngx /etc/nginx/sites-available/
   sudo ln -s /etc/nginx/sites-available/example.ngx /etc/nginx/sites-enabled/
   ```

5. **Modify the `/etc/hosts` File:**
   ```bash
   sudo vim /etc/hosts
   ```
   Add the following line:
   ```
   127.0.0.1 example.com
   ```
   Save and exit.

6. **Restart Nginx:**
   ```bash
   sudo service nginx restart
   ```

7. **Test in Browser:**
   Open your web browser and go to:
   ```
   http://example.com
   ```
   You should see:
   ```
   Hello from example.com!
   ```

### Cleanup After Testing
To remove the local redirect after testing:
1. Edit the `/etc/hosts` file again:
   ```bash
   sudo vim /etc/hosts
   ```
   Remove or comment out the line for `example.com`.
   Save and exit.

2. Reload the web page to access the actual `example.com`.

## 7. Introduction to avconv

### Prerequisites
1. **Install `avconv`**:
   - Open Terminal.
   - Install `libav-tools`:
     ```bash
     sudo apt-get install libav-tools
     ```

2. **Locate Video File**:
   - Default video files are in `/usr/share/example-content/`.
   - Copy a video file to your working directory:
     ```bash
     cp /usr/share/example-content/Ubuntu_Free_Culture_Showcase/How\ fast.ogg ~/Videos
     cd ~/Videos
     ```

### Exercise Steps

1. **Extract Audio from Video**:
   - To extract audio as an MP3:
     ```bash
     avconv -i "How fast.ogg" -vn "how-fast.mp3"
     ```
   - `-vn` disables video, ensuring only audio is processed.

2. **Convert Video to MP4**:
   - To convert the OGG video to MP4:
     ```bash
     avconv -i "How fast.ogg" -strict experimental "how-fast.mp4"
     ```

3. **Extract a Still Image from Video**:
   - To extract a frame at 10 seconds:
     ```bash
     avconv -i "How fast.ogg" -ss 00:00:10 -vframes 1 "f10.jpg"
     ```

### Summary
- You’ve successfully extracted audio, converted video formats, and extracted a still image using `avconv`. You can now find the files in your `Videos` folder.

### Troubleshooting Tips
- If you encounter errors regarding codecs, ensure you use the correct flags (like `-strict experimental`).
- Always check the file formats to confirm compatibility.

### Conclusion
This exercise demonstrates the versatility of `avconv` for handling multimedia files on Ubuntu.

