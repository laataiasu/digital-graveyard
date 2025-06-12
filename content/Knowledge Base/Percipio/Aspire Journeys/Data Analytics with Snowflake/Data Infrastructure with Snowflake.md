# Data Analytics with Snowflake 

Data Infrastructure with Snowflake
3 Hr 53 Min Remaining
Instructions Resources Help  100%
Exercise 1 – Navigating the Snowflake's User Interface
Introduction
In this lab activity, you will navigate Snowflake’s user interface.
Tasks
    1. Login to Snowflake
    2. Navigate the interface
Instructions
Task 1 – Login to Snowflake
In this task, you will log in to Snowflake.
    1. Click the Microsoft Edge icon in the taskbar.
    2. This task requires you to register with Snowflake. You can register for a 48-day free trial using the following URL:
https://signup.snowflake.com/?utm_cta=trial-en-www-homepage-top-right-nav-ss-evg
    3. After registering, you receive an E-mail at the address you provided during registration. You need to first activate your account.
    4. You then need to create a password and confirm it. After you confirm the password, it automatically takes you inside the Snowflake UI.
    5. Alternatively, you can open the E-mail with the subject, Welcome to Snowflake!.
    6. In the E-mail, click LOG IN TO SNOWFLAKE.
    7. The Sign in to Snowflake webpage is displayed. Enter the username and password and click Sign in.
    8. After successful login, you are navigated to the Worksheets tab.
    9. Keep the Snowflake UI open and proceed to the next task.
Task 2 – Navigate the interface
In this task, you will navigate the Snowflake interface.
You must complete the first task in this exercise to continue.
    10. Ensure that Microsoft Edge is open and you are logged on to the Snowflake website.
    11. When you log in, you are automatically on the worksheet tab. Worksheets are used to write and execute queries. By default, there are no worksheets available in the UI.
    12. Click the Dashboards tab. You can create a dashboard to visualize your data.
    13. Click Data. It has three sub-tabs: Databases, Private Sharing, and Provider Studio. When you click Data, by default, the Databases sub-tab is selected. It contains a sample database named SNOWFLAKE. You can also create a new database by clicking on the + Database button.
    14. Click the Private Sharing tab. This tab has three options:
4.1.    Shared With Me: Shows the data shared with you
4.2.    Shared By My Account: Shows the data shared by you
4.3.    Reader Accounts: Shows the data shared by you for the users who are not the Snowflake customers
    5. Click the Provider Studio tab. It contains various tabs:
5.1.    Home: Shows trends, announcements, and action items
5.2.    Analytics: Shows metrics on your listings
5.3.    Listings: Shows draft and published listings
5.4.    Learn: Shows links to various resources
    6. Click Marketplace, which displays the various types of listings by different organizations.
    7. Click Activity. By default, it selects the Query History sub-tab. There is no data displayed to start with. When you run a query, it will show the query information list. The other two tabs are Copy History and Task History.
    8. Click Admin. There are several sub-tabs available. These tabs are:
8.1.    Usage: Displays the warehouse usage
8.2.    Warehouses: Displays the existing warehouses
8.3.    Resource Monitors: Displays the resource monitors associated with the current role
8.4.    Users and Roles: Displays the existing users and roles
8.5.    Security: Displays the network policies that you have created
8.6.    Billing & Terms: Displays the billing method - allows you to add a credit card
8.7.    Partner Connect: Allows you to create trial accounts with the Snowflake partners and use these accounts with Snowflake
    9. Click Help & Support. It displays the Snowflake help as well as a link for the marketplace.
    10. The left corner at the bottom displays the account ID. You can click the drop-down arrow to sign in to another account.
    11. Click the drop-down arrow next to the username in the upper left corner. Notice that it has various options:
11.1.    Username
11.2.    Current role - you can use the Switch role option to change the role
11.3.    Profile
11.4.    Documentation
11.5.    Support
11.6.    Sign Out
    12. Move the mouse over Switch Role. Notice that by default, the ACCOUNTADMIN role is assigned to the user who creates the account. You can create a user account within Snowflake and assign a specific role, such as USERADMIN.
    13. Click Profile. The Profile dialog box is displayed. You can make changes to your profile. For example, you can change your password by clicking the pencil icon. You can also switch the interface by clicking the Default Experience drop-down. Snowsight is the default selection. Select Classic UI.
    14. Click Save on the Profile dialog box.
    15. On the Help us improve Snowsight dialog box, click Skip.
    16. Back on the Profile dialog box, scroll down, and notice that there is an option to select a language and enable notifications and multi-factor authentication. Click Close.
    17. You are back on the UI.
    18. Keep the UI open and proceed to the next exercise.
Check your work
Check each box to confirm completion of the task.
    1. Login to Snowflake
    2. Navigate the interface
Question
When you log on to Snowflake, which is the first tab you are navigated to?
Data
Dashboards
Worksheets
Admin
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 48 Min Remaining
Instructions Resources Help  100%
Exercise 2 – Creating a Simple Warehouse
Introduction
In this lab activity, you will create a simple warehouse.
Tasks
    1. Use the Snowflake UI to create a warehouse
Instructions
Task 1 – Use the Snowflake UI to create a warehouse
In this task, you will use the Snowflake UI to create a warehouse.
    1. Connect to the Windows VM.
    2. Log on to the Snowflake account using your credentials
    3. After successful login, you are navigated to the Worksheets tab.
    4. Click Admin and then click Warehouses.
    5. Click the + Warehouse button in the right pane.
    6. Type a name in the Name field on the New Warehouse dialog box and keep the default selection in the Size drop-down. Click the drop-down next to the Advanced Warehouse Options field.
    7. Keep the default options in the Advanced Warehouse Options section and click Create Warehouse.
    8. The new warehouse is now created. Click on the warehouse.
    9. The warehouse page is displayed. It displays Warehouse Activity and Query History.
    10. Keep the Snowflake page option and proceed to the next exercise.
Check your work
Check each box to confirm completion of the task.
    1. Use the Snowflake UI to create a warehouse
Question
Which tab should you visit to create a warehouse?
Data
Worksheets
Dashboards
Admin
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 44 Min Remaining
Instructions Resources Help  100%
Exercise 3 – Creating Databases and Tables from the User Interface (UI)
Introduction
In this lab activity, you will create a database and table using the Snowflake UI.
Tasks
    1. Create a database
    2. Create a table
Instructions
Task 1 – Create a database
In this task, you will create a database.
    1. Connect to the Windows VM.
    2. Log on to the Snowflake account using your credentials
    3. After successful login, you are navigated to the Worksheets tab.
    4. Click Data. The Databases tab is selected automatically.
    5. Click + Database in the right pane.
    6. In the New Database dialog box, type student_info in the Name textbox and click Create.
    7. Back on the Databases page in the right pane, the student_info database is created.
    8. Keep the Snowflake page open and proceed to the next task.
Task 2 – Create a table
In this task, you will create a table.
    1. Ensure that you have completed the previous task.
    2. Click Worksheets in the left pane.
    3. On the Worksheets page in the right pane, click + Worksheet.
    4. A new worksheet is created. You are already navigated to the worksheet page, divided into two panes. The left pane has Worksheets and Databases tabs. In the right pane, click the No Databases selected drop-down and select STUDENT_INFO database.
    5. The PUBLIC schema is selected by default.
    6. Click anywhere in the white area and type the following SQL statements in the right pane:
create table student (
  first_name string ,
  last_name string ,
  email string ,
  year date ,
  course string 
     );
    1. Click the play button in the upper right corner.
    2. The bottom section appears in the right pane. It displays a message that the table, student, is now created.
    3. Click the Databases tab in the left pane.
    4. Expand the STUDENT_INFO database, expand PUBLIC, and then expand Tables. Notice that the STUDENT table is now created.
    5. Select the STUDENT table. Notice that the table columns are displayed in the left pane.
    6. Keep the Snowflake page open and proceed to the next exercise.
Check your work
Check each box to confirm completion of the task.
    1. Create a database
    2. Create a table
Question
Which tab should you visit to create a database?
Worksheets
Admin
Dashboards
Data
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 38 Min Remaining
Instructions Resources Help  100%
Exercise 4 – Running Basic Queries
Introduction
In this lab activity, you will run basic queries in Snowflake.
Tasks
    1. Run queries in worksheets
Instructions
Task 1 – Run queries in worksheets
In this task, you will create a database.
    1. Connect to the Windows VM.
    2. Log on to the Snowflake account using your credentials
    3. After successful login, you are navigated to the Worksheets tab.
    4. If you had completed the previous exercise, you should be on the worksheet page.
    5. Click the Worksheets tab. Notice that it displays the worksheet that was created in the previous exercise.
    6. Let’s execute some basic queries. To list the existing warehouses, press Enter, type the following statement:
show warehouses;
Press Enter. Note that the existing warehouse is now listed.
    1. Press Enter to move to the next line.
    2. To list the databases, type the following statement:
show databases;
Press Enter. The output displays two databases that exist.
    1. Press Enter to move to the next line.
    2. To work with the current warehouse, schema, and database, type the following statement:
select current_warehouse(), current_database(), current_schema();
Press Enter. Notice that the output is displayed in the bottom section of the right pane.
    1. Keep the Snowflake page open and proceed to the next exercise.
Check your work
Check each box to confirm completion of the task.
    1. Run queries in worksheets
Question
You want to execute a query. Which tab should you visit to do the same?
Data
Dashboards
Worksheets
Admin
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 35 Min Remaining
Instructions Resources Help  100%
Exercise 5 – Create Objects Using Snowsight
Introduction
In this lab activity, you will create objects using Snowsight.
Tasks
    1. Create a warehouse as an object
Instructions
Task 1 – Create a warehouse as an object
In this task, you will create a warehouse as an object.
    1. Connect to the Windows VM.
    2. Log on to the Snowflake account using your credentials
    3. After successful login, you are navigated to the Worksheets tab.
    4. You should be on the worksheet page if you have completed the previous exercise.
    5. Click the Worksheets tab. Notice that it displays the worksheet that was created in the previous exercise.
    6. Click the + sign in the left pane to open a new worksheet and select New Worksheet.
    7. Keep the default name. You can also overwrite with the name of your choice. Click anywhere in the white space to accept the name.
    8. You had previously created a warehouse. You will now create or replace a warehouse with the same name. To do this, type the following statements in the right pane:
create or replace warehouse skillsoft with
  warehouse_size='X-SMALL'
  auto_suspend = 180
  auto_resume = true
  initially_suspended=false;
This set of SQL statements will create or replace a warehouse named Skillsoft. If it exists, then it will replace its values. If it does not exist, it creates a new warehouse with the defined values.
    1. Click the play button in the upper right corner.
    2. Notice that the Skillsoft warehouse is now created.
    3. Let’s verify the Skillsoft warehouse properties. To do this, click the Home icon.
    4. Click Admin in the left pane.
    5. Click Warehouses.
    6. The right pane displays the SKILLSOFT warehouse. Click the SKILLSOFT warehouse.
    7. The SKILLSOFT page is displayed in the right pane. Scroll down to the Details section. Notice that the properties you set in the SQL statements are displayed here.
    8. Log out from the Snowflake UI and close the web browser window.
Check your work
Check each box to confirm completion of the task.
    1. Create a warehouse as an object
Question
You have created a warehouse as X-Large. You want to create a new warehouse with the same name and replace it with X-Small size. Which of the following keyword should be used in the Create statement?
Modify
Replace
Overwrite
Change
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 32 Min Remaining
Instructions Resources Help  100%
Exercise 6 – Setting Up a Secure Share
Introduction
In this lab activity, you will set up a secure share.
Tasks
    1. Download query results in a file
Instructions
Task 1 – Download query results in a file
In this task, you will log on to the Snowflake classic interface.
    1. Connect to the Windows VM.
    2. Ensure that you have completed the previous exercise and are on the classic interface.
    3. Click the Shares icon in the top bar.
    4. On the Secure Shares page, click Outbound and then click Create.
    5. From the Databases drop-down, select COURSES and then click Select Tables & Secure Views.
    6. In the Tables & Secure Views in: COURSES dialog box, select PUBLIC  Tables and select COURSE_INFO, and click Apply.
    7. Click Create.
    8. On the Data Preview tab, select the available option in the Table or View drop-down.
    9. Click Preview Data.
    10. Notice that the preview of the data is now displayed. Click Next: Add Consumers.
    11. On the Add Consumers dialog box, click Create a Reader account.
    12. Keep the web browser window open with the Snowflake interface and proceed to the next exercise.
    13. On the Create Reader Account dialog box, type an account name. Type a username and password, and then confirm the password. Click Create Account.
    14. Click Done after the account is created. You are back on the Add Consumers dialog box. The new account is now added to the drop-down. Click Add.
    15. Click Done.
    16. Back on the Secure Shares page, the secure share is displayed.
    17. Keep the web browser window open with the Snowflake interface and proceed to the next exercise.
Check your work
Check each box to confirm completion of the task.
    1. Download query results in a file
Question
Other than inbound share, which other type of share can you create?
Secure
Reserved
Outbound
Closed
Select Next below to move to the next exercise.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 

Data Infrastructure with Snowflake
3 Hr 21 Min Remaining
Instructions Resources Help  100%
Exercise 7 – Downloading Query Results from Snowflake
Introduction
Tasks
    1. Download query results in a file
To perform the steps in this exercise, you MUST complete Lab 6: Load data in Snowflake. You must load the data as mentioned in Lab 6.
Instructions
Task 1 – Download query results in a file
In this task, you will download query results in a file.
    1. Connect to the Windows VM.
    2. Ensure that you have completed the previous exercise and are on the classic interface.
    3. Click the Worksheets icon in the top bar.
    4. In the left pane, expand COURSES  PUBLIC  Tables and select COURSE_INFO. Click the … next to COURSE_INFO.
    5. In the right pane, type the following statement:
select * from course.public.course_info;
Click Run.
    1. Drag the bar in the bottom right pane containing two tabs: Results and Data Preview.
    2. Click the Download or View Results button in the bottom section of the right pane.
    3. In the Export Results dialog box, click Export.
    4. A notification is displayed. It mentions that the file is now downloaded. Click Open file.
    5. In the dialog box, uncheck Always use this app to open .tsv files and select Notepad. Click OK.
    6. Notice the results.tsv file is opened in a Notepad window.
    7. Close all open windows.
Check your work
Check each box to confirm completion of the task.
    1. Download query results in a file
Question
In the classic interface, you want to download the outcomes of a query. Which tab should you visit?
Data
Worksheets
Dashboards
Admin
Congratulations! You have completed the lab.

From <https://labclient.labondemand.com/Instructions/d8a27e46-e6f1-4257-bc58-bd60aa2801a1> 



