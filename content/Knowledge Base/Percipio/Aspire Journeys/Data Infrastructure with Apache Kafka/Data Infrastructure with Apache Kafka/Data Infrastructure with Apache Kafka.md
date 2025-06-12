# Data Infrastructure with Apache Kafka

## Overview

### Lab Exercises

1. **Exercise 1: Create and Configure a Spark Cluster**  
   - Task: Set up and configure a Spark cluster.
   - Steps: Follow the step-by-step instructions to complete the configuration.

2. **Exercise 2: Create a Topic, Producer, and Consumer with Kafka**  
   - Task: Create a Kafka topic, set up a producer, and configure a consumer.
   - Steps: Follow the instructions to implement Kafka components.

3. **Exercise 3: Working with Multiple Kafka Topics**  
   - Task: Work with multiple Kafka topics simultaneously.
   - Steps: Learn how to manage and interact with multiple topics in Kafka.

4. **Exercise 4: Configuring a Multi-node Kafka Cluster**  
   - Task: Set up a multi-node Kafka cluster.
   - Steps: Follow the guide to configure a distributed Kafka environment.

---

### Lab Configuration

**Devices:**  
- Ubuntu

**Software:**
- Apache Kafka  
- Apache Cassandra  
- Apache Spark  
- Visual Studio Code  
- Docker  
- Docker Compose

## Exercise 1: Create and Configure a Spark Cluster

### Task 1: Install and Configure Apache Spark

#### 1. **Install Apache Spark**
   - Log into the Ubuntu environment using the provided credentials.
   - Open the terminal by clicking the **Terminal** icon.

#### 2. **Extract Spark Files**
   - Check the current directory for the Hadoop file by running:
     ```bash
     ls
     ```
     - You should see a file named `spark-3.3.0-bin-hadoop3.tgz`.
   - Extract the file using the `tar` command:
     ```bash
     tar -xvzf spark-3.3.0-bin-hadoop3.tgz
     ```
   - To verify the extraction, list the directory contents:
     ```bash
     ls
     ```
     - You should now see the directory `spark-3.3.0-bin-hadoop3`.

#### 3. **Set Spark Environment Variables**
   - Open the `.bash_profile` file to edit the environment variables:
     ```bash
     nano ~/.bash_profile
     ```
   - Add the following lines to set up Spark and Kafka environment variables:
     ```bash
     export KAFKA_HOME=$HOME/tools/kafka_2.12-3.1.0
     export PATH="$KAFKA_HOME/bin:$PATH"
     export SPARK_HOME=~/spark-3.3.0-bin-hadoop3
     export PATH=$PATH:$SPARK_HOME/bin
     ```
   - Save and close the file:  
     - Press `Ctrl + S` to save.  
     - Press `Ctrl + X` to exit.
   
#### 4. **Apply the Changes**
   - To apply the changes made to `.bash_profile`, run:
     ```bash
     source ~/.bash_profile
     ```

#### 5. **Verify Spark Installation**
   - Close the terminal window and open it again.
   - Start the PySpark shell:
     ```bash
     pyspark
     ```
   - Wait for Spark to initialize. After a few seconds, you should see the PySpark shell prompt and a message indicating the web UI is available at a specific IP address (e.g., `http://192.168.1.50:4040`).
   - To verify Spark’s functionality, run:
     ```bash
     sc
     ```
     - You should see output similar to:
       ```
       <SparkContext master = local[*] appName= PySparkShell>
       ```
   - Exit the PySpark shell by pressing `Ctrl + D`.

---

### Task 2: Configure a Spark Cluster

#### 1. **Navigate to Spark Directory**
   - Ensure you are logged in and have the terminal window open.
   - Navigate to the Spark home directory:
     ```bash
     cd $SPARK_HOME
     ```

#### 2. **Start the Spark Master**
   - Change to the `sbin` subdirectory:
     ```bash
     cd sbin
     ```
   - Start the Spark master:
     ```bash
     start-master.sh
     ```
   - This will start the Spark master on the current system.

#### 3. **Monitor the Spark Cluster**
   - Open the **Firefox** browser from the left pane.
   - Navigate to the Spark web UI at:
     ```url
     http://localhost:8080
     ```
   - Initially, the web UI may show a "dead worker" node. This is expected.

#### 4. **Start a Spark Worker Node**
   - In the terminal, start the worker node:
     ```bash
     start-worker.sh spark://Udesktop:7077
     ```
   - Refresh the Spark web UI by clicking the **Reload current page** icon.
   - The new worker node should now be listed as "ALIVE."

---

### Check Your Work

- **Install and Configure Apache Spark**: Confirm Spark is installed and configured.
- **Configure a Spark Cluster**: Confirm the cluster is running with a master and worker node.

---

### Question

**Which file should you edit to make Spark binaries accessible via the path environment variable?**

- **Correct Answer**: `.bash_profile`

---

## Exercise 2: Create a Topic, Producer, and Consumer with Kafka

#### Task 1: Extract Contents from the Kafka Compressed File

1. **Log in** to the Ubuntu environment using the provided credentials and open the terminal.
2. **Extract Kafka Files:**
   - Check for the Hadoop file in the current directory:
     ```bash
     ls
     ```
     - You should see a file starting with `kafka_2.12-3.2.3.tgz`.
   - Extract the compressed file:
     ```bash
     tar -xzf kafka_2.12-3.2.3.tgz
     ```
     - This will extract the files into the `kafka_2.12-3.2.3` directory.
   - Verify the extraction:
     ```bash
     ls
     ```
     - You should see the `kafka_2.12-3.2.3` directory.
   - Rename the Kafka directory for easier access:
     ```bash
     mv kafka_2.12-3.2.3 kafka
     ```
   - Clear the screen:
     ```bash
     clear
     ```

#### Task 2: Update the `.bash_profile` File

1. **Edit the `.bash_profile` File:**
   - Open the `.bash_profile` file using Nano:
     ```bash
     nano ~/.bash_profile
     ```
   - Add the following lines to set Kafka environment variables:
     ```bash
     export KAFKA_HOME=$HOME/kafka
     export PATH="$KAFKA_HOME/bin:$PATH"
     ```
   - Save and exit:
     - Press `Ctrl + S` to save.
     - Press `Ctrl + X` to exit.
   
2. **Apply the Changes:**
   - Load the updated `.bash_profile`:
     ```bash
     source ~/.bash_profile
     ```
   - Clear the screen:
     ```bash
     clear
     ```

#### Task 3: Update the Kafka Server Configuration

1. **Edit the `server.properties` File:**
   - Open the `server.properties` file located in the `config` directory:
     ```bash
     nano kafka/config/server.properties
     ```
   - Find the line:
     ```
     #listeners=PLAINTEXT://9092
     ```
     - Remove the `#` and update the line to:
       ```
       listeners=PLAINTEXT://127.0.0.1:9092
       ```
   - Save and exit:
     - Press `Ctrl + S` to save.
     - Press `Ctrl + X` to exit.
   - Clear the screen:
     ```bash
     clear
     ```

#### Task 4: Start the Server and Display Messages

1. **Start Zookeeper:**
   - Start the Zookeeper server:
     ```bash
     sudo bin/zookeeper-server-start.sh /home/labadmin/kafka/config/zookeeper.properties
     ```
   - The server will start immediately. You will be back at the terminal prompt.

2. **Create a Kafka Topic:**
   - Create the `latest_news` topic:
     ```bash
     kafka-topics.sh --create --topic latest_news --bootstrap-server localhost:9092
     ```
   - List existing topics:
     ```bash
     kafka-topics.sh --list --bootstrap-server localhost:9092
     ```
   - Describe the `latest_news` topic:
     ```bash
     kafka-topics.sh --describe --topic latest_news --bootstrap-server localhost:9092
     ```

3. **Start the Producer:**
   - Start the Kafka producer to send messages to the `latest_news` topic:
     ```bash
     kafka-console-producer.sh --topic latest_news --bootstrap-server localhost:9092
     ```
   - Enter one or more news items.

4. **Start the Consumer:**
   - Open a new terminal window and start the Kafka consumer:
     ```bash
     kafka-console-consumer.sh --topic latest_news --bootstrap-server localhost:9092
     ```
   - The consumer will display any messages sent by the producer. Enter news in the producer terminal and observe it in the consumer terminal.

5. **View All Messages:**
   - In the consumer terminal, view all messages sent to the topic from the beginning:
     ```bash
     kafka-console-consumer.sh --topic latest_news --bootstrap-server localhost:9092 --from-beginning
     ```

6. **Close the Terminals:**
   - Press `Ctrl + C` to stop the consumer.
   - Clear the screen in each terminal:
     ```bash
     clear
     ```

---

### Check Your Work

- **Extract contents from the Kafka compressed file**
- **Update the `.bash_profile` file**
- **Update the Kafka server configuration**
- **Start the server and display messages**

---

### Question

**Which directory contains the `server.properties` file?**

- **Correct Answer**: `config`

---

## Exercise 3: Working with Multiple Kafka Topics

#### Task 1: Configure Two Producers and a Consumer to Receive Messages from Both

1. **Start the Zookeeper Server:**
   - Log in to Ubuntu and open a terminal.
   - Start the Zookeeper server:
     ```bash
     sudo bin/zookeeper-server-start.sh /home/labadmin/kafka/config/zookeeper.properties
     ```
   - The server will start immediately, and you will be back at the terminal prompt.

2. **Create the First Topic:**
   - Clear the screen:
     ```bash
     clear
     ```
   - Create the `fresh_news` topic:
     ```bash
     kafka-topics.sh --create --topic fresh_news --bootstrap-server localhost:9092
     ```

3. **Start the First Producer:**
   - Start the Kafka producer for `fresh_news`:
     ```bash
     kafka-console-producer.sh --topic fresh_news --bootstrap-server localhost:9092
     ```
   - When the `>` prompt appears, type one or two pieces of news to send.

4. **Start the Consumer:**
   - Open a new terminal window and start the consumer for `fresh_news`:
     ```bash
     kafka/bin/kafka-console-consumer.sh --topic fresh_news --bootstrap-server localhost:9092
     ```
   - Switch to the first terminal (producer window) and type some news. The message will be displayed in the consumer window.

5. **Terminate the Consumer:**
   - Press `Ctrl + C` in the consumer window to stop it.
   - Clear the screen:
     ```bash
     clear
     ```

6. **Create the Second Topic:**
   - Open another terminal window and navigate to the Kafka directory:
     ```bash
     cd kafka/
     ```
   - Clear the screen:
     ```bash
     clear
     ```
   - Create the `great_news` topic:
     ```bash
     bin/kafka-topics.sh --create --topic great_news --bootstrap-server localhost:9092
     ```

7. **Start the Second Producer:**
   - Start the Kafka producer for `great_news`:
     ```bash
     bin/kafka-console-producer.sh --topic great_news --bootstrap-server localhost:9092
     ```
   - Enter one or two lines of news.

8. **Start the Consumer for `fresh_news`:**
   - In the consumer window, start the consumer for `fresh_news` again:
     ```bash
     bin/kafka-console-consumer.sh --topic fresh_news --bootstrap-server localhost:9092
     ```

9. **Terminate the Consumer:**
   - Press `Ctrl + C` to stop the consumer.
   - Clear the screen:
     ```bash
     clear
     ```

10. **Configure the Consumer to Listen to Both Topics:**
    - Open a new terminal window and configure the consumer to listen to both the `fresh_news` and `great_news` topics:
      ```bash
      bin/kafka-console-consumer.sh --whitelist "fresh_news|great_news" --bootstrap-server localhost:9092
      ```
    - This will allow the consumer to receive messages from both topics.

11. **Send News from Both Producers:**
    - Switch to the first producer and type a line of news.
    - Switch to the second producer and type a line of news.
    - Switch back to the consumer. Both news messages will be displayed.

12. **Close All Terminal Windows:**
    - Press `Ctrl + C` to stop the consumer and close all terminal windows.

---

### Check Your Work

- **Configure Two Producers and Configure a Consumer to Receive Messages from Both**: Ensure that the consumer is receiving messages from both `fresh_news` and `great_news` topics.

---

### Question

**Which directory contains the `zookeeper.properties` file?**

- **Correct Answer**: `config`

---

## Exercise 4: Configuring a Multi-node Kafka Cluster

#### Task 1: Configure Kafka as a Multi-node Cluster

1. **Create Directories for Brokers:**
   - Log in to the Ubuntu system and open a terminal in the `kafka/` directory.
   - Create a `data` directory:
     ```bash
     mkdir data
     ```
   - Navigate to the `data` directory:
     ```bash
     cd data
     ```
   - Create the `zookeeper` directory for Zookeeper logs:
     ```bash
     mkdir zookeeper
     ```
   - Create directories for two Kafka brokers:
     ```bash
     mkdir broker-0
     mkdir broker-1
     ```

2. **List Subdirectories:**
   - Verify the created directories:
     ```bash
     ls
     ```

3. **Edit Zookeeper Configuration:**
   - Open the `zookeeper.properties` file in the `kafka/config` directory.
   - Modify the `dataDir` property to use the `zookeeper` directory:
     ```properties
     dataDir=/home/labadmin/kafka/data/zookeeper
     ```
   - Enable the Zookeeper admin server by setting `admin.enableServer=true`.
   - Change the admin server port to `9090`:
     ```properties
     admin.enableServer=true
     admin.server.port=9090
     ```
   - Add the Zookeeper server configuration for the current server (`server.1`):
     ```properties
     server.1=localhost:2888:3888
     ```
   - Save and close the file.

4. **Start Zookeeper:**
   - Start the Zookeeper server:
     ```bash
     sudo bin/zookeeper-server-start.sh /home/labadmin/kafka/config/zookeeper.properties
     ```
   - Enter the password if prompted. The server will start and you’ll be returned to the terminal prompt.

5. **Access Zookeeper Shell:**
   - Access the Zookeeper shell to verify active Kafka brokers:
     ```bash
     /bin/zookeeper-shell.sh localhost:2181
     ```
   - Check the active brokers:
     ```bash
     ls /brokers/ids
     ```
   - The output will show `0` (indicating no brokers are connected yet).

6. **Create Multiple Server Configuration Files:**
   - Navigate to the `kafka/config` directory and copy the `server.properties` file to create configuration files for multiple brokers.
   - Rename the copies as `server-0.properties` and `server-1.properties`.

7. **Configure the First Broker:**
   - Edit the `server-0.properties` file for Broker 0:
     - Set `broker.id=0` (default).
     - Modify `advertised.listeners`:
       ```properties
       advertised.listeners=PLAINTEXT://127.0.0.1:9092
       ```
     - Modify the `log.dirs` property:
       ```properties
       log.dirs=/home/labadmin/kafka/data/broker-0
       ```
   - Save the file.

8. **Configure the Second Broker:**
   - Edit the `server-1.properties` file for Broker 1:
     - Set `broker.id=1`.
     - Modify `listeners`:
       ```properties
       listeners=PLAINTEXT://127.0.0.1:9093
       ```
     - Modify `advertised.listeners`:
       ```properties
       advertised.listeners=PLAINTEXT://127.0.0.1:9093
       ```
     - Modify the `log.dirs` property:
       ```properties
       log.dirs=/home/labadmin/kafka/data/broker-1
       ```
   - Save the file.

---

### Check Your Work

- **Configure Kafka as Multi-node Cluster**: Ensure you have configured both brokers and Zookeeper properly.

---

### Question

**To enable a multi-node cluster, which file should you edit to set the `admin.enableServer` property to true?**

- **Correct Answer**: `zookeeper.properties`

---

