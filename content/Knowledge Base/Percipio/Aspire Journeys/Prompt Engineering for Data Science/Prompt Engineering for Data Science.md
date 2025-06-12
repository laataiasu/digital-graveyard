# Prompt Engineering for Data Science

Question: Lisa is a data analyst working on a project that involves extensive data manipulation using Python and pandas. She has a large dataset containing information about customer transactions, including details such as transaction date, customer ID, product purchased, and transaction amount. Her goal is to perform various data manipulations, including filtering data based on specific criteria, sorting the DataFrame based on different columns, and iterating through the rows to perform custom operations.
 
Which method should she use to leverage ChatGPT for iterating through the rows and sorting DataFrames in Python, particularly focusing on basic data manipulation tasks?
Result: Correct. Great job! 

Use ChatGPT to generate high-level algorithmic approaches for iterating over DataFrame rows and sorting to implement the logic using pandas functions
Not selected
Good job, you chose not to select this option.

Use ChatGPT to generate custom Python code snippets for iterating over DataFrame rows and apply them to enhance the data processing logic
Not selected
Good job, you chose not to select this option.

Use ChatGPT to provide specific code examples for sorting DataFrames based on multiple columns and iterate over rows with enhanced efficiency
Selected
Good job, you selected this correct option.

Use ChatGPT to recommend pandas functions and methods suitable for iterating over DataFrame rows and sorting data efficiently

---

Joseph is working with a dataset containing information about various products on an e-commerce platform. Each product has attributes such as 'name', 'category', 'price', and 'quantity'.


He has developed the following dataset initially:


products = [

    {'name': 'Laptop', 'category': 'Electronics', 'price': 1200, 'quantity': 50},

    {'name': 'Headphones', 'category': 'Electronics', 'price': 100, 'quantity': 100},

    {'name': 'Backpack', 'category': 'Fashion', 'price': 50, 'quantity': 200},

    {'name': 'Mouse', 'category': 'Electronics', 'price': 20, 'quantity': 150},

    {'name': 'T-shirt', 'category': 'Fashion', 'price': 15, 'quantity': 300},

    {'name': 'External HDD', 'category': 'Electronics', 'price': 80, 'quantity': 80},

]

He wants to perform the following tasks:


1. Calculate the total value of each product by multiplying the 'price' and 'quantity' and create a new 'total_value' attribute for each product.


2. Filter out the products with a total value less than 1000.


3. Find the average price of the remaining products in the 'Electronics' category.


Which code snippet should he use to accomplish these tasks?


Option 1

products = list(map(lambda p: {**p, 'total_value': p['price'] * p['quantity']}, products))

filtered_products = filter(lambda p: p['total_value'] >= 1000, products)

electronics_products = filter(lambda p: p['category'] == 'Electronics', filtered_products)

average_price = sum(map(lambda p: p['price'], electronics_products)) / len(electronics_products)



T Option 2

products = list(map(lambda p: {**p, 'total_value': p['price'] * p['quantity']}, products))

filtered_products = filter(lambda p: p['total_value'] >= 1000, products)

electronics_products = list(filter(lambda p: p['category'] == 'Electronics', filtered_products))

average_price = sum(map(lambda p: p['price'], electronics_products)) / len(electronics_products)



Option 3

products = list(map(lambda p: {**p, 'total_value': p['price'] * p['quantity']}, products))

filtered_products = filter(lambda p: p['total_value'] >= 1000, products)

electronics_products = filter(lambda p: p['category'] == 'Electronics', filtered_products)

average_price = sum(map(lambda p: p['price'], list(electronics_products))) / len(list(electronics_products))



Option 4

products = list(map(lambda p: {**p, 'total_value': p['price'] * p['quantity']}, products))

filtered_products = filter(lambda p: p['total_value'] >= 1000, products)

electronics_products = list(filter(lambda p: p['category'] == 'Electronics', filtered_products))

average_price = sum(map(lambda p: p['price'], electronics_products)) / len(filtered_products)

---
The data analyst is working on a project. He has a DataFrame df that contains information about sales transactions. His goal is to create a new column called 'Total_Price' by multiplying the 'Quantity' and 'Unit_Price' columns. Additionally, he wants to extract the month from the 'Date' column and create a new column named 'Month'.


He has developed the following DataFrame df initially:


import pandas as pd

data = {'Date': ['2022-01-05', '2022-02-15', '2022-03-20'],
        'Product': ['A', 'B', 'A'],
        'Quantity': [10, 15, 8],
        'Unit_Price': [25.5, 12.75, 30.0]}


df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

Which code snippet should he use to achieve the desired transformations?


Option 1

df['Total_Price'] = df['Quantity'] * df['Unit_Price']

df['Month'] = df['Date'].month

print(df)



T Option 2

df['Total_Price'] = df['Quantity'] * df['Unit_Price']

df['Month'] = df['Date'].apply(lambda x: x.month)

print(df)



Option 3

df['Total_Price'] = df['Quantity'] * df['Unit_Price']

df['Month'] = df['Date'].dt.month

print(df)



Option 4

df['Total_Price'] = df.apply(lambda row: row['Quantity'] * row['Unit_Price'], axis=1)

df['Month'] = df['Date'].dt.month

print(df)

---

Bill is a data scientist working on a complex project that involves extensive data manipulation and analysis using pandas in Python. As part of his task, he needs to filter a large dataset by specific column headers and row labels. While performing this operation, he realizes that there are some missing values and outliers that need special attention. So, he decides to leverage Bard AI to enhance the understanding and streamline the process.

What should he do?

Result: Partially correct. The correct answers are indicated. 

Use Bard AI to generate code snippets for filtering by column headers, incorporating techniques to handle missing values, and seek further clarification on outlier detection
Selected
Good job, you selected this correct option.

Pose a general question to Bard AI about pandas filtering, then independently research outlier detection techniques, and apply the findings to your code
Not selected
Good job, you chose not to select this option.

Collaborate with a colleague who has experience in pandas and filtering techniques, using Bard AI to supplement your joint efforts in addressing missing values and outliers
Not selected
Sorry, you should have selected this option.

Ask Bard AI for a step-by-step tutorial on filtering by column headers in pandas, explicitly mentioning your concerns about missing values and outliers
Selected
Sorry, you should not have selected this option.

---

Bill is a data scientist working on a critical project that has a dataset consisting of multiple time series representing financial transactions over a period of five years. His goal is to identify patterns and group transactions based on specific criteria. He decides to leverage BARD AI to accomplish the task.

Which approach should he choose when using BARD AI for grouping and aggregating the time series data?

Result: Correct. Great job! 

Employ manual feature engineering before applying BARD AI to capture domain-specific nuances
Not selected
Good job, you chose not to select this option.

Use a pre-trained BARD AI model with default parameters for quick analysis
Not selected
Good job, you chose not to select this option.

Use BARD AI with a prompt that emphasizes temporal patterns for enhanced time series grouping
Selected
Good job, you selected this correct option.

Fine-tune the BARD AI model for the specific dataset to enhance accuracy
Selected
Good job, you selected this correct option.

---
Bill is a data scientist working on a complex project. He needs to merge and concatenate multiple DataFrames efficiently to derive meaningful insights, using pandas in Python. He plans on leveraging ChatGPT AI to assist in this task.

Which approach would be most effective for combining DataFrames and debugging issues related to pd.concat?

Result: Correct. Great job! 

Use ChatGPT to generate specific prompts for the pd.concat function, guiding it to offer insights into potential debugging strategies
Selected
Correct answer.

Use ChatGPT to draft custom error messages related to pd.concat issues and use them as prompts for iterative debugging
Not selected. Not selected is correct.

Use ChatGPT to create a script that automates the process of combining DataFrames, with embedded error-checking mechanisms for pd.concat issues
Not selected. Not selected is correct.

Use ChatGPT to generate concise documentation snippets explaining the nuances of using pd.concat for DataFrame concatenation, focusing on common pitfalls and solutions

---

Question
 
Adam is a data scientist who has developed the following code snippet designed for exploring univariate visualizations.


What will be the output or behavior of the given code snippet?

```
import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

> Assume 'data' is a pandas DataFrame loaded with relevant data

> Code snippet

sns.set(style="whitegrid")

> Prompt Engineering: Creating a new feature 'engineered_feature' based on existing data

data['engineered_feature'] = data['feature_A'] * data['feature_B']

> Univariate visualization

plt.figure(figsize=(10, 6))

choices = ["histogram", "boxplot", "violinplot", "countplot", "ecdf_plot", "scatter_plot"]

selected_choice = choices[2]  

> Change the index to select different visualization


> Different visualization options

if selected_choice == "histogram":

    sns.histplot(data['engineered_feature'], kde=True)

    plt.title("Histogram of Engineered Feature")

    plt.xlabel("Engineered Feature Values")

    plt.ylabel("Frequency")

elif selected_choice == "boxplot":

    sns.boxplot(x=data['engineered_feature'])

    plt.title("Boxplot of Engineered Feature")

    plt.xlabel("Engineered Feature")

elif selected_choice == "violinplot":

    sns.violinplot(y=data['engineered_feature'])

    plt.title("Violin Plot of Engineered Feature")

    plt.ylabel("Engineered Feature")

elif selected_choice == "countplot":

    sns.countplot(x=data['engineered_feature'])

    plt.title("Count Plot of Engineered Feature")

    plt.xlabel("Engineered Feature")

elif selected_choice == "ecdf_plot":

    sns.ecdfplot(data['engineered_feature'])

    plt.title("Empirical Cumulative Distribution Function (ECDF) Plot of Engineered Feature")

    plt.xlabel("Engineered Feature Values")

    plt.ylabel("Cumulative Probability")

elif selected_choice == "scatter_plot":

    sns.scatterplot(x=data['feature_A'], y=data['engineered_feature'])

    plt.title("Scatter Plot between Feature A and Engineered Feature")

    plt.xlabel("Feature A")

    plt.ylabel("Engineered Feature")

plt.show()

Instruction: Choose the option that best answers the question. 

Shows a count plot of the values in the engineered feature

Produces a violin plot illustrating the distribution of the engineered feature

T Displays a histogram of the engineered feature with a kernel density estimate

Presents a boxplot showcasing the distribution of the engineered feature

---
The data scientist of a large E-Commerce platform is working on a project that involves merging two datasets on multiple columns and validating the relationships between them. The datasets represent information about customers and their purchases. His goal is to create a merged dataset that combines relevant information from both datasets and ensure the integrity of the relationships between the columns. His team decides to use ChatGPT AI to assist in this task. He has the following code snippets.


Which code snippet can he use to perform merge on multiple columns and validate relationships?


Option 1

import openai

openai_prompt = "Merge the datasets 'customer_data' and 'purchase_data' using pandas on columns 'customer_id' and 'purchase_id'. Verify that the relationships between the merged columns are maintained."

response = openai.Completion.create(

  engine="text-davinci-002",

  prompt=openai_prompt,

  max_tokens=100

)

merged_dataset = pd.DataFrame(response.choices[0].text)



Option 2

import pandas as pd


customer_data = pd.read_csv('customer_data.csv')

purchase_data = pd.read_csv('purchase_data.csv')

merged_dataset = pd.concat([customer_data, purchase_data], axis=1)

merged_dataset = merged_dataset[['customer_id', 'purchase_id', 'other_columns']]



Option 3

import openai

openai_prompt = "Combine the 'customer_data' and 'purchase_data' datasets using pandas on columns 'customer_id' and 'purchase_id'. Ensure the integrity of relationships between the merged columns."

response = openai.Completion.create(

  engine="text-davinci-002",

  prompt=openai_prompt,

  max_tokens=100
)

merged_dataset = pd.read_csv(StringIO(response.choices[0].text))



Option 4

import pandas as pd

customer_data = pd.read_csv('customer_data.csv')

purchase_data = pd.read_csv('purchase_data.csv')

merged_dataset = pd.merge(customer_data, purchase_data, on=['customer_id', 'purchase_id'], validate='many_to_one')

--- 

The data scientist of a large E-Commerce platform is working on a project that involves merging two datasets on multiple columns and validating the relationships between them. The datasets represent information about customers and their purchases. His goal is to create a merged dataset that combines relevant information from both datasets and ensure the integrity of the relationships between the columns. His team decides to use ChatGPT AI to assist in this task. He has the following code snippets.


Which code snippet can he use to perform merge on multiple columns and validate relationships?


Option 1

import openai

openai_prompt = "Merge the datasets 'customer_data' and 'purchase_data' using pandas on columns 'customer_id' and 'purchase_id'. Verify that the relationships between the merged columns are maintained."

response = openai.Completion.create(

  engine="text-davinci-002",

  prompt=openai_prompt,

  max_tokens=100

)

merged_dataset = pd.DataFrame(response.choices[0].text)



Option 2

import pandas as pd


customer_data = pd.read_csv('customer_data.csv')

purchase_data = pd.read_csv('purchase_data.csv')

merged_dataset = pd.concat([customer_data, purchase_data], axis=1)

merged_dataset = merged_dataset[['customer_id', 'purchase_id', 'other_columns']]



Option 3

import openai

openai_prompt = "Combine the 'customer_data' and 'purchase_data' datasets using pandas on columns 'customer_id' and 'purchase_id'. Ensure the integrity of relationships between the merged columns."

response = openai.Completion.create(

  engine="text-davinci-002",

  prompt=openai_prompt,

  max_tokens=100
)

merged_dataset = pd.read_csv(StringIO(response.choices[0].text))



T Option 4

import pandas as pd

customer_data = pd.read_csv('customer_data.csv')

purchase_data = pd.read_csv('purchase_data.csv')

merged_dataset = pd.merge(customer_data, purchase_data, on=['customer_id', 'purchase_id'], validate='many_to_one')
Instruction: Choose the option that best answers the question. 

---
Lisa is working on a data engineering project, and she has a pandas DataFrame named df that represents information about customer orders. The DataFrame has columns such as 'OrderID', 'Product', 'Quantity', 'Price', 'Discount', and 'Total'. However, due to some data entry errors, there are missing values in certain rows. She has developed the following code snippet to clean the data by filling in the missing values using pandas.


import pandas as pd

df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

df['Discount'].fillna(0, inplace=True)

df['Total'].fillna(df['Quantity'] * df['Price'], inplace=True)

> Display the updated DataFrame

print(df)

She is using the ChatGPT to get the output of the given code snippet. What will be the response of ChatGPT?

Result: Incorrect. The correct answer is indicated. 

Missing values in the 'Quantity' column are filled with the maximum value
Not selected. Not selected is correct.

Missing values in the 'Total' column are filled with the sum of 'Quantity' and 'Price'
Not selected. Not selected is correct.

Missing values in the 'Quantity' column are filled with the median value
Selected
Incorrect answer.

Missing values in the 'Discount' column are filled with the mean value
Not selected
Correct answer.

---
Adam is a data scientist working on a project that involves grouping and aggregating time series data using Generative AI techniques. He has a dataset containing time series data with multiple variables, and he needs to group the data based on a specific criterion and perform aggregation. He wants to use BARD AI to generate code snippets that efficiently handle this task.


Which code snippet will help him use BARD AI to accomplish the task?


Option 1

import bard_ai

prompt = "Group and aggregate time series data based on variable X using BARD AI."

code = bard_ai.generate_code(prompt)

result = execute_code(code)



Option 2

import bard_ai

prompt = "Aggregate time series data using BARD AI."

code = bard_ai.generate_code(prompt)

result = execute_code(code)



Option 3

import bard_ai

prompt = "Group time series data by variable Y and calculate the average using BARD AI."

code = bard_ai.generate_code(prompt)

result = execute_code(code)



T Option 4

import bard_ai

prompt = "Aggregate time series data by summing up values for variable Z using BARD AI."

code = bard_ai.generate_code(prompt)

result = execute_code(code)
Instruction: Choose the option that best answers the question. 

---
James has the following code snippet for reshaping and aggregating data using pivot tables.


import pandas as pd

> Sample DataFrame

data = {'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-01'],
        'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 15, 20, 25, 30]}

df = pd.DataFrame(data)

> Pivot table creation

pivot_table = pd.pivot_table(df, values='Value', index='Date', columns='Category', aggfunc='sum')

print(pivot_table)

What will be the output of the given code snippet?


Option 1

Category       A   B
Date               
2022-01-01    40   15
2022-01-02    20   25



T Option 2

Category       A   B
Date               
2022-01-01    10   15
2022-01-02    20   25



Option 3

Category       A   B
Date               
2022-01-01    30   15
2022-01-02    20   25



Option 4

Category       A   B
Date               
2022-01-01    10   30
2022-01-02    20   25
Instruction: Choose the option that best answers the question. 

---
Anna is a data scientist working on a large dataset containing information about customer transactions on an e-commerce platform. Her task is to perform grouped aggregations using pandas in Python to extract meaningful insights. The current challenge she faces is related to optimizing the aggregation function for a specific customer segment. She decides to leverage ChatGPT to enhance her understanding and streamline the process.

Which approach should she choose to overcome this hurdle?

Result: Incorrect. The correct answer is indicated. 

Use ChatGPT to generate a custom aggregation function tailored to the characteristics of the target customer segment
Not selected. Not selected is correct.

Use ChatGPT to analyze the dataset and suggest potential feature engineering techniques before performing the grouped aggregations
Selected
Incorrect answer.

Use ChatGPT to identify the most relevant grouping variables that can enhance the granularity of the aggregations for the target customer segment
Not selected. Not selected is correct.

Use ChatGPT to seek clarifications on the appropriate pandas method to handle complex aggregations for the specified customer segment
Not selected
Correct answer.

---
Consider the following code snippet:


import pandas as pd

> Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

> Using .info() to view DataFrame information
df.info()

What will be the output of the given code snippet?


T Option 1

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 >   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    3 non-null      object
 1   Age     3 non-null      int64 
 2   City    3 non-null      object
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes


Option 2

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 >   Column    Dtype 
---  ------  --------------  ----- 
 0   Name          object
 1   Age          int64 
 2   City         object
dtypes: int64(1), object(2)


Option 3

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 >       Dtype 
---  ------  --------------  ----- 
 0      object
 1      int64 
 2      object
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes


Option 4

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 3 entries, 0 to 2
Data columns (total 3 columns):
 >   Column  
---  ------  
 0   Name    
 1   Age      
 2   City   
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes

---
Luca is data scientist working on a complex project that involves analyzing large datasets using Python's pandas library. In the process of optimizing his workflow, he decides to leverage ChatGPT for prompt engineering to iterate over and sort DataFrames efficiently. He has a DataFrame named "sales_data" with columns: 'Date', 'Product', 'Quantity', and 'Revenue'. His goal is to sort the DataFrame based on the 'Date' column in ascending order and then within each date, sort the 'Revenue' column in descending order.

Which prompt should he use to efficiently achieve this task using ChatGPT?

Result: Correct. Great job! 

What is the most efficient way to perform a multi-level sort on a pandas DataFrame based on 'Date' in ascending order and 'Revenue' in descending order?
Not selected. Not selected is correct.

Discussing prompt engineering for pandas: How to sort a DataFrame by 'Date' in ascending order and within each date, sort 'Revenue' in descending order for efficient data analysis.
Not selected. Not selected is correct.

Pandas DataFrame sorting: ascending order by date and descending order by revenue. Provide code.
Selected
Correct answer.

Sort pandas DataFrame by date and revenue in ascending and descending order respectively.
Not selected. Not selected is correct.

---
Adam, a data engineer, has been tasked with enhancing the interactivity of the time series visualization. He has developed the following code snippet using Plotly to create interactive time series visualizations.


import plotly.express as px

import pandas as pd

> Assume 'df' is a pandas DataFrame containing time series data

> with columns 'Date' and 'Stock_Price'

fig = px.line(df, x='Date', y='Stock_Price', title='Stock Price Analysis')

fig.update_layout(

    xaxis_title='Date',

    yaxis_title='Stock Price',

    hovermode='x unified'

)

fig.show()

Adam asks the ChatGPT for modification to enhance the interactivity of the time series visualization. Which modification would ChatGPT suggest?

Instruction: Choose the option that best answers the question. 

Remove fig.show() and replace it with fig.show(config={'scrollZoom': False})

Introduce a new line of code: fig.update_traces(mode='markers+lines') after fig.update_layout(yaxis_title='Stock Price'

Add: fig.update_layout(clickmode='event+select') after fig.update_layout(hovermode='x unified')

T Replace hovermode='x unified' with hovermode='closest'

---

William is data scientist working on a project that involves visualizing time series data to derive insights for a major financial institution. The dataset contains information about stock prices, trading volumes, and market trends over the past decade. He decides to use ChatGPT to generate meaningful visualizations. The dataset is vast and complex, requiring precise instructions for effective visualization.


 


Which approach should he choose to formulate a prompt for ChatGPT to generate insightful visualizations?

Result: Partially correct. The correct answers are indicated. 

Incorporate domain-specific jargon and terminology in the prompt to ensure ChatGPT understands the context
Selected
Good job, you selected this correct option.

Formulate a prompt instructing ChatGPT to highlight specific patterns in stock prices over the past year
Not selected
Sorry, you should have selected this option.

Craft a prompt asking ChatGPT to visualize overall trends in the entire dataset
Not selected
Good job, you chose not to select this option.

Experiment with different prompt lengths to observe how the model's response varies and select the one that yields the most informative visualizations
Selected
Sorry, you should not have selected this option.

---
Eva is working on a data manipulation project using Python and pandas. She has developed the following code snippet.


import pandas as pd

> Consider the following DataFrame 'df' with sample data
data = {'A': [1, 2, 3, 4, 5],

        'B': [10, 20, 30, 40, 50],

        'C': [100, 200, 300, 400, 500]}

df = pd.DataFrame(data)


df_result_1 = df[['A', 'C']]

What will be the resultant DataFrame of the given code snippet?

Result: Correct. Great job! 

df.drop('B', axis=1)
Not selected. Not selected is correct.

df.drop(['A', 3])
Not selected. Not selected is correct.

df[['A', 'C']]
Not selected. Not selected is correct.

df.loc[:, ['B', 'C']].drop(2)
Selected
Correct answer.

---
Karen is a data scientist working for a retail company, and she has been tasked with analyzing sales data to identify trends and patterns. The dataset she is working with is in a messy format, and she needs to reshape and aggregate the data using pivot tables to derive meaningful insights. The sales data contains the following information about products, regions, and dates.


1. There is a column in the dataset that records customer feedback scores for each product. 
2. The sales data includes a column indicating the payment method used for each transaction. 
3. The dataset also contains information about promotions and discounts applied to certain products. 
4. There is a column in the dataset representing the inventory levels of each product.


Help her match the task to the correct code snippet to perform specific data manipulations.


Code Snippet A

import pandas as pd

pivot_table_1 = pd.pivot_table(df, values='sales', index=['product'], columns=['region'], aggfunc='sum')



Code Snippet B

import pandas as pd

pivot_table_2 = pd.pivot_table(df, values='feedback_score', index=['product_category'], columns=['region'], aggfunc='mean')



Code Snippet C

import pandas as pd

pivot_table_3 = pd.pivot_table(df, values='sales', index=['payment_method'], columns=['month'], aggfunc='sum')



Code Snippet D

import pandas as pd

pivot_table_4 = pd.pivot_table(df, values='sales', index=['product'], columns=['variations'], aggfunc='sum')



Code Snippet E

import pandas as pd

pivot_table_5 = pd.pivot_table(df, values='discounted_amount', index=['product_category'], columns=['quarter'], aggfunc='sum')



Code Snippet F

import pandas as pd

pivot_table_6 = pd.pivot_table(df, values='inventory_levels', index=['product_category'], columns=['region'], aggfunc='mean')
Instruction: For each option, select the best answer choice. 

Answer Choices
A:Code Snippet F
B:Code Snippet A
C:Code Snippet D
D:Code Snippet B
E:Code Snippet C
F:Code Snippet E

Options:

-Creating a pivot table for average inventory levels by product category and region

-Generating a pivot table for total discounted amount by product category over different quarters

-Pivoting data to compare total sales amounts for each payment method in different months

-Reshaping data to see total sales for each product in each region over time

-Creating a pivot table for average feedback scores by product category and region

-Creating a pivot table to break down total sales for each product by its variations

---

Lisa is working on a project that involves analyzing a dataset containing information about various environmental factors. She has a dataset named environment_data.csv with columns: 'temperature', 'humidity', 'air_quality', and 'location'. She has the following requirements.


1. Create an interactive scatter plot to visualize the relationship between 'temperature' and 'humidity'.
2. Generate a seaborn heatmap to show the correlation matrix of all variables in the dataset.
3. Set appropriate labels, titles, and color schemes for both visualizations.
4. Ensure that the scatter plot is interactive, allowing users to hover over points and view detailed information.


Select the most appropriate code snippet for creating these visualizations.


Option 1

import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset('environment_data.csv')

sns.scatterplot(x='temperature', y='humidity', data=data)

plt.title('Temperature vs Humidity')

plt.show()

sns.heatmap(data.corr(), annot=True, cmap='viridis')

plt.title('Correlation Matrix')

plt.show()



Option 2

import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset('environment_data.csv')

sns.scatterplot(x='temperature', y='humidity', data=data)

plt.title('Temperature vs Humidity')

plt.show()

sns.heatmap(data[['temperature', 'humidity', 'air_quality']].corr(), annot=True, cmap='viridis')

plt.title('Correlation Matrix')

plt.show()



Option 3

import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset('environment_data.csv')

sns.scatterplot(x='temperature', y='humidity', data=data, hue='location')

plt.title('Temperature vs Humidity')

plt.show()

sns.heatmap(data.corr(), annot=True, cmap='coolwarm')

plt.title('Correlation Matrix')

plt.show()



T Option 4

import seaborn as sns

import matplotlib.pyplot as plt

data = sns.load_dataset('environment_data.csv')

sns.scatterplot(x='temperature', y='humidity', data=data, hue='location', palette='Set2')

plt.title('Temperature vs Humidity')

plt.show()

sns.heatmap(data.corr(), annot=True, cmap='YlGnBu')

plt.title('Correlation Matrix')

plt.show()

---

A data scientist is working on a complex analysis project that requires exploring various join types to merge datasets effectively. As he navigates through the project, he encounters a situation where he needs to choose the most suitable join type for a particular task.


 


Which approach should he select to leverage Bard AI for exploring other join types?

Result: Incorrect. The correct answer is indicated. 

Choose "Left Join" as Bard AI is known for handling cases where you want to keep all records from the left dataset and match those from the right dataset
Not selected. Not selected is correct.

Choose "Inner Join" as Bard AI excels in optimizing queries for this type, providing efficient results, and speeding up your analysis
Selected
Incorrect answer.

Choose "Cross Join" as Bard AI has unique capabilities in optimizing queries that involve Cartesian products between datasets
Not selected. Not selected is correct.

Choose "Outer Join" because Bard AI is proficient in dealing with scenarios where you want to keep all records from both datasets, matching where possible
Not selected
Correct answer.

---

Jason is a data scientist working on a complex project that involves analyzing a large dataset using the pandas library in Python. His goal is to identify and remove duplicate entries from the dataset to ensure the accuracy of the analysis. He decides to leverage the power of ChatGPT to improve the approach of using pandas for duplicate removal.


 


Which approach should he follow?

Result: Partially correct. The correct answers are indicated. 

Provide a detailed description of your dataset and ask ChatGPT to generate a comprehensive script that covers both identification and removal of duplicates
Selected
Sorry, you should not have selected this option.

Seek general advice from ChatGPT on the principles of data deduplication and then manually translate the guidance into pandas code for the specific dataset
Not selected
Good job, you chose not to select this option.

Experiment with different prompt variations, focusing on verbosity and specificity, to find the most effective way to elicit accurate and concise code snippets for duplicate removal in pandas
Selected
Good job, you selected this correct option.

Formulate a prompt that explicitly instructs ChatGPT to generate code snippets for identifying duplicate entries based on a specific column in the pandas DataFrame
Selected
Good job, you selected this correct option.

---

A data analyst is working on raw data for personalization and business forecasting.

Arrange the steps in the data analysis process in the correct sequence.

Result: Correct. Great job! 
Data Cleaning
Correct answer.
Data Manipulation
Correct answer.
Data Exploration
Correct answer.
Data Visualization
Correct answer.

---

William is a data analyst working on a complex analysis project. He has a large dataset containing information about customer transactions. The DataFrame, named "customer_data," has columns such as 'Customer_ID,' 'Transaction_Date,' 'Product_ID,' 'Quantity,' 'Price,' and 'Payment_Method.' He needs to create a new DataFrame that includes only the relevant columns for analysing the customer needs and requirements.

Which prompt should William use with ChatGPT AI for dropping and selecting columns from the DataFrame?

Result: Correct. Great job! 

Prompt: "Choose 'Transaction_Date,' 'Product_ID,' and 'Payment_Method' columns from the DataFrame 'customer_data' while dropping the rest, using ChatGPT AI to streamline the process."
Not selected. Not selected is correct.

Prompt: "Drop unnecessary columns and select only 'Customer_ID,' 'Transaction_Date,' and 'Quantity' columns from the DataFrame 'customer_data' using ChatGPT AI."
Selected
Correct answer.

Prompt: "Retain only 'Product_ID' and 'Price' columns in the DataFrame 'customer_data' by using ChatGPT AI for efficient column manipulation."
Not selected. Not selected is correct.

Prompt: "Optimize the DataFrame 'customer_data' by selecting 'Quantity' and 'Payment_Method' columns only, excluding the others, through ChatGPT AI prompt engineering."

---
William is working as a Data Engineer at a leading tech company. His team is tasked with processing a large dataset containing information about software development projects. The dataset is stored in a pandas DataFrame named projects_data, and includes columns such as 'project_name', 'start_date', 'end_date', and 'programming_language'. The team has developed the following code snippet to filter the data.


import pandas as pd

> Assume 'projects_data' is a DataFrame loaded with the relevant dataset

> Code Snippet

filtered_data = projects_data[
    (projects_data['start_date'] >= '2023-01-01') &
    (projects_data['end_date'] <= '2023-12-31') &
    
(projects_data['programming_language'].str.contains('Python|Java'))

]

Which statement is true regarding the output (filtered_data) based on the specified filtering conditions?

Result: Correct. Great job! 

The output will contain projects with start dates in 2023 and end dates in 2024, regardless of the programming language
Not selected. Not selected is correct.

The output will contain projects that started on or after January 1, 2023, and ended on or before December 31, 2023, involving only Python programming language
Selected
Correct answer.

The output will contain projects with start dates in 2022 and end dates in 2024, regardless of the programming language
Not selected. Not selected is correct.

The output will contain projects regardless of start and end dates, but only those with the programming language as Python or Java

---

Anna is a data engineer working with a DataFrame named df containing information about sales transactions. Each row represents a transaction with columns 'Date', 'Product', 'Category', 'Quantity', and 'Revenue'. She has developed the following code snippet for performing multi-column grouping and split-apply-combine on a DataFrame df containing sales transactions.


import pandas as pd

> Assume df is the DataFrame with the given columns

> Define a custom aggregation function

def custom_aggregation(x):

    return x.sum() / x.count()

> Perform multi-column grouping and split-apply-combine

result = df.groupby(['Date', 'Category']).agg({
    'Quantity': 'sum',
    'Revenue': ['mean', custom_aggregation]
}).reset_index()

> Prompt Engineering: Create a new feature 'Profit_Per_Quantity' by multiplying 'Revenue' mean and 'Quantity' sum

result['Profit_Per_Quantity'] = result[('Revenue', 'mean')] * result[('Quantity', 'sum')]

> Display the result

print(result.head())

What will be the output of the given code?

Instruction: Choose the option that best answers the question. 

A DataFrame with 'Date', 'Category', 'Quantity_sum', 'Revenue_custom_aggregation', 'Profit_Per_Quantity' as columns

A DataFrame with 'Date', 'Category', 'Quantity_sum', 'Revenue_mean', 'Revenue_custom_aggregation', 'Profit_Per_Quantity' as columns

T A DataFrame with 'Date', 'Category', 'Quantity_sum', 'Revenue_mean', 'Profit_Per_Quantity' as columns

A DataFrame with 'Date', 'Category', 'Quantity_sum', 'Revenue_mean', 'Revenue_custom_aggregation' as columns

---
Anna is a data engineer working on a project that involves processing and analyzing a large dataset using Pandas in Python. The dataset contains information about customer transactions on an e-commerce platform, including customer IDs, product details, transaction amounts, and timestamps. She plans to use Bard AI for effective knowledge about performing filtering and querying operations on the data.


 


Which approach would be most effective for using Bard to extract transactions made by customers with a transaction amount above $500 in the 'Electronics' category between January 1, 2023, and June 30, 2023?

Result: Partially correct. The correct answers are indicated. 

Combine a pre-built SQL query with Bard AI-generated natural language to filter the pandas DataFrame efficiently
Selected
Sorry, you should not have selected this option.

Utilize Bard AI to generate a natural language query and directly apply it to the pandas DataFrame for filtering
Selected
Good job, you selected this correct option.

Use Bard AI to autonomously analyze the dataset and identify the relevant transactions
Not selected
Good job, you chose not to select this option.

Implement custom Python functions to preprocess the data before applying Bard AI for enhanced filtering
Not selected
Sorry, you should have selected this option.

---
Jason is a data scientist working on a project that involves analyzing the relationship between two features, Feature_A and Feature_B, in a dataset. He decides to use ChatGPT's recommendations for bivariate visualizations to gain insights. He has developed the following code snippet for it.


1. import pandas as pd

2. import seaborn as sns

3. import matplotlib.pyplot as plt

4. > Sample Data

5. data = {

6.     'Feature_A': [1, 2, 3, 4, 5],

7.     'Feature_B': [5, 4, 3, 2, 1],

8.     'Category': ['A', 'B', 'A', 'B', 'A']

9. }

10. df = pd.DataFrame(data)

11. > Code for Bivariate Visualization

12. plt.figure(figsize=(8, 6))

13. > Code for bivariate visualization recommendation using ChatGPT

14.  

15. > Display the plot

16. plt.show()

Which code snippet should he insert at Line 14 to create an effective bivariate visualization for exploring the relationship between Feature_A and Feature_B?

Instruction: Choose the option that best answers the question. 

sns.barplot(x='Feature_A', y='Feature_B', data=df, hue='Category')

sns.lineplot(x='Feature_A', y='Feature_B', data=df, hue='Category')

sns.boxplot(x='Feature_A', y='Feature_B', data=df, hue='Category')

T sns.scatterplot(x='Feature_A', y='Feature_B', data=df, hue='Category')

---

Anna is working on a data science project where she needs to create an interactive time series visualization using the plotly library to analyze the trends in temperature data over the past year. She has developed the following code snippet to generate the visualization.


import plotly.express as px

import pandas as pd

> Assume 'temperature_data.csv' contains columns 'Date' and 'Temperature'

df = pd.read_csv('temperature_data.csv')



fig = px.line(df, x='Date', y='Temperature', title='Temperature Trends Over Time')

fig.update_xaxes(type='category')

> Adding a range slider for interactive zooming

fig.update_layout(xaxis_rangeslider_visible=True)

fig.show()

What will be the output of this code snippet?

Instruction: Choose the option that best answers the question. 

An error will occur because the 'Date' column should be converted to a datetime type before plotting

The code will run successfully but without any interactivity in the visualization

T The code will generate an interactive line chart displaying temperature trends over time with a range slider for zooming

The code will generate a bar chart instead of a line chart due to the 'update_xaxes' function

---
The data scientist of a major e-commerce company is tasked with analyzing sales data to identify trends that will help make informed business decisions. The data is stored in a CSV file named "sales_data.csv," which includes columns such as "ProductID," "ProductName," "Category," "Date," "QuantitySold," and "Revenue."


His goal is to create different types of pivot table using the pandas library in Python.


Match the tasks that he performs to the appropriate code snippets required to accomplish the tasks.

Code Snippet A

result = pivot_table.loc[:, '2023-01-01':'2023-12-31'].sum(axis=1, level='Date')

Code Snippet B

import pandas as pd

result = pivot_table.groupby(level=['ProductID', 'Category']).sum().loc[:, '2023-01-01':'2023-12-31']

Code Snippet C

result = pivot_table.loc[pivot_table.index.get_level_values('Date').between('2023-01-01', '2023-12-31')]

Code Snippet D

result = pivot_table.loc[pivot_table.index.get_level_values('Date').between('2023-01-01', '2023-12-31')].sum(axis=1, level='Date')

Options:

    - Filter the date range and category within the specified range: C
    - Group by ProductID and Category: D
    - Filter the date range, providing the total revenue for each product: B
    - Provide the total revenue for each product and category within the specified range: A

---

Anna is a data scientist working on dataset containing information about individuals. The variables of interest are 'income' and 'education level'. Her goal is to create effective visualizations that provide insights into the relationship between these two variables.


Which code snippet will help create a meaningful visualization of the relationship between 'income' and 'education level'?


Option 1

import seaborn as sns

import matplotlib.pyplot as plt

sns.scatterplot(x='education_level', y='income', data=df)

plt.title('Relationship between Income and Education Level')

plt.show()



Option 2

import matplotlib.pyplot as plt

df.boxplot(column='income', by='education_level')

plt.title('Income Distribution by Education Level')

plt.show()



Option 3

import pandas as pd

import matplotlib.pyplot as plt

pivot_table = pd.pivot_table(df, values='income', index='education_level', aggfunc='mean')

plt.imshow([pivot_table.values], cmap='viridis', aspect='auto')

plt.xticks(range(len(pivot_table.columns)), pivot_table.columns)

plt.yticks(range(len(pivot_table.index)), pivot_table.index)

plt.colorbar()

plt.title('Heatmap of Income by Education Level')

plt.show()



T Option 4

import seaborn as sns

import matplotlib.pyplot as plt

sns.jointplot(x='education_level', y='income', data=df, kind='scatter')

plt.suptitle('Joint Plot of Income and Education Level')

plt.show()

---
Adam is developing a Generative AI model that is designed to compose music in a sequential manner, generating notes and melodies. To enhance the model's performance, he decides to implement Chain-of-Thought Prompting for a sequence of operations. This involves guiding the model through a logical flow of instructions to create a coherent musical piece.


Which code snippet should he use to achieve his objective?


T Option 1

def generate_music_sequence(model, initial_prompt, sequence_length):

    music_sequence = []

    current_prompt = initial_prompt
    
    for _ in range(sequence_length):

        generated_notes = model.generate_notes(current_prompt)

        music_sequence.extend(generated_notes)

        current_prompt = update_prompt(current_prompt, generated_notes)
    
    return music_sequence




Option 2

def generate_music_sequence(model, initial_prompt, sequence_length):

    music_sequence = []

    for _ in range(sequence_length):

        generated_notes = model.generate_notes(initial_prompt)

        music_sequence.extend(generated_notes)

        initial_prompt = update_prompt(initial_prompt, generated_notes)
    
    return music_sequence




Option 3

def generate_music_sequence(model, initial_prompt, sequence_length):

    music_sequence = []

    for _ in range(sequence_length):

        generated_notes = model.generate_notes(initial_prompt)

        music_sequence.extend(generated_notes)

        initial_prompt += generated_notes
    
    return music_sequence




Option 4

def generate_music_sequence(model, initial_prompt, sequence_length):

    music_sequence = []


   for _ in range(sequence_length):

        generated_notes = model.generate_notes(initial_prompt)

        music_sequence.append(generated_notes)

        initial_prompt = update_prompt(initial_prompt, generated_notes)
    
    return music_sequence
Instruction: Choose the option that best answers the question. 

---
The Data Engineer of an organization is working on a data engineering project. He has a dataset contains information about sales transactions. He has loaded the dataset into the DataFrame, named df_data. However, some cells have missing values. He has written the following code snippet to fill in those missing values.


1. import pandas as pd

2. > Creating a sample DataFrame

3. data = {'Product': ['A', 'B', 'C', 'A', 'B', 'C'],

        'Quantity': [10, 20, 30, None, 15, None],

        'Price': [50, 60, None, 40, 30, 25]}

4. df_data = pd.DataFrame(data)

5. > <Add code to fill missing values>

6. df_data.fillna('your_code_here', inplace=True)

7. > Displaying the modified DataFrame

8. print(df_data)

He leverages Bard AI to find the line code to add at Line 5 of the code snippet. Which code snippet will Bard AI suggest?

Instruction: Choose the option that best answers the question. 

T df_data.fillna({'Quantity': df_data['Quantity'].mean(), 'Price': df_data['Price'].median()})

df_data.fillna(method='bfill')

df_data.fillna({'Quantity': df_data['Quantity'].mean(), 'Price': df_data['Price'].median()}, inplace=True)

df_data.fillna(method='ffill')

---

Bill is a data scientist working on a project that involves exploring, debugging, and reading CSV files into pandas DataFrames. He comes across a challenging dataset that requires careful handling. He decides to leverage the capabilities of Bard AI. While using Bard AI for exploring, debugging, and reading CSV files into pandas DataFrames, he encounters an issue with missing values in the dataset.

What would be the most appropriate course of action to address this challenge immediately?

Result: Partially correct. The correct answers are indicated. 

Employ Bard AI's debugging module to trace the source of missing values and rectify any errors in the CSV file
Selected
Good job, you selected this correct option.

Utilize Bard AI's automated imputation feature to fill in missing values based on statistical methods
Selected
Good job, you selected this correct option.

---

The Data Engineer of an organization is creating interactive scatter plots and seaborn heatmaps. He has developed the following code snippet accomplish the task.


import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

from plotly.subplots import make_subplots

import plotly.express as px

> Generate sample data

np.random.seed(42)

data = pd.DataFrame({

    'A': np.random.rand(50),

    'B': np.random.rand(50),

    'C': np.random.randint(1, 5, 50),

})

> Scatter plot using seaborn

plt.figure(figsize=(10, 6))

sns.scatterplot(x='A', y='B', hue='C', data=data, palette='viridis', size='C', sizes=(20, 200))

plt.title('Interactive Scatter Plot')

plt.show()

> Heatmap using plotly

fig = make_subplots(rows=1, cols=2, subplot_titles=['Heatmap - Option 1', 'Heatmap - Option 2'])

heatmap_option_1 = px.imshow(data.corr(), color_continuous_scale='Blues')

heatmap_option_2 = px.imshow(data.pivot_table(index='A', columns='B', values='C').fillna(0), color_continuous_scale='Reds')

fig.add_trace(heatmap_option_1.data[0], row=1, col=1)

fig.add_trace(heatmap_option_2.data[0], row=1, col=2)

fig.update_layout(title_text='Seaborn Heatmaps')

fig.show()

Which of the statements correctly describes the output of this code snippet?

Instruction: Choose the option that best answers the question. 

The scatter plot shows a relationship between columns 'A' and 'B', and the size of the markers corresponds to the values in column 'C'. The first heatmap (Option 1) displays a pivot table of the data

The scatter plot uses a color palette 'Reds' for the markers, and the size of the markers represents the values in column 'C'. The second heatmap (Option 2) represents the correlation matrix of the data

T The scatter plot displays the relationship between columns 'A' and 'B', and the size of the markers represents the values in column 'C'. The first heatmap (Option 1) represents the correlation matrix of the data

The scatter plot only uses two colors in the palette, representing columns 'A' and 'B', and the size of the markers does not depend on any column. The second heatmap (Option 2) visualizes the distribution of column 'C'

---

Question
 
You are working on a data analysis project. You have a DataFrame named df containing information about sales transactions. The DataFrame has columns such as "TransactionID," "ProductID," "Quantity," and "TransactionDate." You need to sort the DataFrame based on the "TransactionDate" column in ascending order. However, you notice that the sorting is not happening as expected.

Which is the best approach of getting effective assistance from ChatGPT to debug the sorting issues in the DataFrame?

Instruction: Choose the option that best answers the question. 

Seek suggestions from ChatGPT on alternative libraries or functions that might handle DataFrame sorting more efficiently

T Share the specific code snippet related to sorting that you are using and ask ChatGPT to identify potential issues or errors

Ask ChatGPT to provide the general syntax for sorting a DataFrame in pandas and implement it in your code

Request ChatGPT to explain the theory behind sorting algorithms and hope to gain insights into optimizing DataFrame sorting performance

---

Consider the following code snippet:


import pandas as pd

> Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

> Using .head() to display the first few rows of the DataFrame
print(df.head())

What will be the output of the given code snippet?


Option 1

City
0       New York
1       San Francisco
2       Los Angeles


Option 2

      Age         City
0    25       New York
1    30       San Francisco
2    35       Los Angeles 


T Option 3

     Name        Age         City
0    Alice        25          New York
1    Bob          30          San Francisco
2   Charlie       35          Los Angeles


Option 4

      Name          
0    Alice   
1    Bob   
2    Charlie
Instruction: Choose the option that best answers the question. 

---
Sara is a data scientist working on a project that involves analyzing the relationship between two variables in a dataset. She has created a scatter plot with the dataset.


 


However, the dataset is extensive, and Sara wants to ensure the plot is optimized for clarity and insights.


 


Match the options to the appropriate modification that improves the clarity and insights gained from the scatter plot.

Result: Correct. Great job! 
Answer Choices
A:Change the color of the scatter plot markers to red
B:Add a regression line to the scatter plot
C:Include a histogram for each variable on the x and y-axes
D:Rotate the x-axis labels by 45 degrees
E:Set the x and y-axis scales to be logarithmic
F:Increase the size of the markers in the scatter plot
Options

Use the s parameter in sns.scatterplot

A

B

C

D

E

F
Use the s parameter in sns.scatterplot, correct, you answered Increase the size of the markers in the scatter plot .
Correct answer.

Use plt.xticks(rotation=45)

A

B

C

D

E

F
Use plt.xticks(rotation=45), correct, you answered Rotate the x-axis labels by 45 degrees.
Correct answer.

Use sns.regplot

A

B

C

D

E

F
Use sns.regplot, correct, you answered Add a regression line to the scatter plot.
Correct answer.

Use the color parameter in sns.scatterplot

A

B

C

D

E

F
Use the color parameter in sns.scatterplot, correct, you answered Change the color of the scatter plot markers to red.
Correct answer.

Use plt.xscale('log') and plt.yscale('log')

A

B

C

D

E

F
Use plt.xscale('log') and plt.yscale('log'), correct, you answered Set the x and y-axis scales to be logarithmic.
Correct answer.

Use sns.histplot

A

B

C

D

E

F
Use sns.histplot, correct, you answered Include a histogram for each variable on the x and y-axes.
Correct answer.

---
James is working with a DataFrame called employee_data that contains information about employees in a company. The DataFrame has columns such as 'Employee_ID', 'Salary', and 'Years_Worked'. He is tasked with calculating a new column called 'Performance_Bonus' based on specific conditions.


He has developed the following code snippet in Python using the pandas library.


import pandas as pd

> Sample DataFrame

employee_data = pd.DataFrame({
    'Employee_ID': [1, 2, 3, 4, 5],
    'Salary': [50000, 60000, 70000, 55000, 75000],
    'Years_Worked': [2, 4, 6, 3, 5]
})

employee_data['Performance_Bonus'] = 0  

employee_data.loc[(employee_data['Salary'] > 60000) & (employee_data['Years_Worked'] >= 4), 'Performance_Bonus'] = 0.10

employee_data.loc[employee_data['Salary'] < 55000, 'Performance_Bonus'] = 0.05

employee_data.loc[(employee_data['Salary'] <= 60000) & (employee_data['Salary'] >= 55000) & (employee_data['Years_Worked'] < 4), 'Performance_Bonus'] = 0.02

print(employee_data)

What will be the 'Performance_Bonus' assigned to the employee with Employee_ID 3?

Result: Correct. Great job! 

0.00
Not selected. Not selected is correct.

0.05
Not selected. Not selected is correct.

NaN
Not selected. Not selected is correct.

0.02
Selected
Correct answer.

---

Anna is working on a data science project that involves merging two datasets using inner joins to gain valuable insights. The datasets, 'sales_data' and 'customer_info', both have 'customer_id' as a common key.


Dataset 'sales_data':


sales_data = pd.DataFrame({

    'customer_id': [101, 102, 103, 104],

    'sales_amount': [200, 150, 300, 180]
})

Dataset ' customer_info':


customer_info = pd.DataFrame({

    'customer_id': [101, 102, 105, 106],

    'customer_name': ['Alice', 'Bob', 'Charlie', 'David']

})

Which code snippet demonstrates the proper way to perform the inner join?

Result: Correct. Great job! 

merged_data = pd.merge(sales_data, customer_info, on='customer_id', how='right')
Not selected. Not selected is correct.

merged_data = pd.merge(sales_data, customer_info, on='customer_id', how='left')
Not selected. Not selected is correct.

merged_data = pd.concat([sales_data, customer_info], axis=1, join='inner')
Not selected. Not selected is correct.

merged_data = pd.merge(sales_data, customer_info, on='customer_id', how='inner')
Selected
Correct answer.

---

Refer to the following code for a Pandas series:


import pandas as pd 

> create a series from a list 

animal_series =pd.Series(['Dog', 'Cat', 'Lion'])

> print the Series 
animal_series

What will be the output of this code?


Option 1

['Dog', 'Cat', 'Lion']


Option 2

Dog
Cat
Lion


Option 3

Lion
Cat
Dog


Option 4

{'Dog', 'Cat', 'Lion'}
Result: Correct. Great job! 

Option 4
Not selected. Not selected is correct.

Option 3
Not selected. Not selected is correct.

Option 2
Selected
Correct answer.

Option 1
Not selected. Not selected is correct.

---
Adam is data engineer tasked with cleaning categorical data using pandas in a Python script. He is working on a dataset that contains a column named 'category', which has some inconsistent values, including misspellings and variations. He has developed the following code snippet to standardize these values for better analysis.


import pandas as pd

> Consider a DataFrame 'df' containing information about products in an online store

data = {'ProductID': [101, 102, 103, 104, 105],
        'Category': ['Electronics', 'Clothing', 'Electronics', 'Books', 'Toys'],

        'Availability': ['In Stock', 'Out of Stock', 'In Stock', 'In Stock', 'Out of Stock']}

df = pd.DataFrame(data)

Adam task is to clean the 'Category' and 'Availability' columns using the following criteria:


1. For the 'Category' column, convert all categories to lowercase.
2. For the 'Availability' column, replace 'In Stock' with 1 and 'Out of Stock' with 0.


Which code snippets will help Adam accomplish the task?


Option 1

> df['Category'] = df['Category'].apply(lambda x: x.lower())

> df['Availability'] = df['Availability'].map({'In Stock': 1, 'Out of Stock': 0})



Option 2

> df['Category'] = df['Category'].lower()

> df['Availability'] = df['Availability'].replace({'In Stock': 1, 'Out of Stock': 0})



Option 3

> df['Category'] = df['Category'].str.lower()

> df['Availability'] = df['Availability'].map({'In Stock': 1, 'Out of Stock': 0})



Option 4

> df['Category'] = df['Category'].lower()

> df['Availability'] = df['Availability'].apply(lambda x: 1 if x == 'In Stock' else 0)
Result: Correct. Great job! 

Option 1
Selected
Good job, you selected this correct option.

Option 3
Selected
Good job, you selected this correct option.

Option 4
Not selected
Good job, you chose not to select this option.

Option 2
Not selected
Good job, you chose not to select this option.

---
The data scientist has a dataset named employee_data.csv containing information about employees in a company, with columns such as "Employee_ID," "Department," "Salary," and "Years_of_Experience." He has created a DataFrame and added a line to print the output using the following code snippet.


import pandas as pd

employee_df = pd.read_csv('employee_data.csv')

> Insert code snippet here

print(avg_salary)

He needs to use a query to find the average salary of employees in the 'Marketing' department with more than 5 years of experience. He prompts Bard AI for queries that will help him in his task.


Which code snippet will help him achieve his objective?

Result: Correct. Great job! 

avg_salary = employee_df.query('Department == "Marketing" and Years_of_Experience > 5')['Salary'].mean()
Selected
Good job, you selected this correct option.

avg_salary = employee_df[(employee_df['Department'] == 'Marketing') & (employee_df['Years_of_Experience'] > 5)]['Salary'].mean()
Selected
Good job, you selected this correct option.

avg_salary = employee_df.groupby('Department').mean().loc['Marketing', 'Salary']
Not selected
Good job, you chose not to select this option.

avg_salary = employee_df[(employee_df['Department'] == 'Marketing') | (employee_df['Years_of_Experience'] > 5)]['Salary'].mean()
Not selected
Good job, you chose not to select this option.

---

You have a list of dictionaries, each representing information about a student, with keys 'Name', 'Age', and 'Grade'.


Which code snippet will correctly create a pandas DataFrame from this list?


T Option 1

import pandas as pd
student_list = [{'Name': 'Alice', 'Age': 20, 'Grade': 'A'},
                {'Name': 'Bob', 'Age': 22, 'Grade': 'B'},
                {'Name': 'Charlie', 'Age': 21, 'Grade': 'C'}]

df = pd.DataFrame(student_list)



Option 2

import pandas as pd
student_list = [{'Alice', 20, 'A'},
                {'Bob', 22, 'B'},
                {'Charlie', 21, 'C'}]

df = pd.DataFrame(student_list, 


columns=['Name', 'Age', 'Grade'])



Option 3

import pandas as pd
student_list = [['Alice', 20, 'A'],
                ['Bob', 22, 'B'],
                ['Charlie', 21, 'C']]
df = pd.DataFrame(student_list, columns=['Name', 'Age', 'Grade'])



T Option 4

import pandas as pd
student_list = {'Name': ['Alice', 'Bob', 'Charlie'],
                'Age': [20, 22, 21],
                'Grade': ['A', 'B', 'C']}
df = pd.DataFrame(student_list)
Instruction: Choose all options that best answer the question. 

---

A data scientist has developed the following Python code snippet that involves writing data using multiple formats in pandas DataFrames.


import pandas as pd

> Create a sample DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)

> Write the DataFrame to different file formats

df.to_csv('data.csv', index=False)

df.to_excel('data.xlsx', index=False)

df.to_json('data.json', orient='records')

> Read the written files back into DataFrames

csv_df = pd.read_csv('data.csv')

excel_df = pd.read_excel('data.xlsx')

json_df = pd.read_json('data.json')

> Find the output of the following statement

output_statement = (csv_df['Age'].mean(), excel_df['Age'].max(), json_df['Age'].min())

What will be the output of output_statement in terms of the mean, maximum, and minimum age values for the DataFrames read from the CSV, Excel, and JSON files, respectively?

Result: Incorrect. The correct answer is indicated. 

(30.0, 30, 35)
Not selected. Not selected is correct.

(30.0, 35, 25)
Selected
Incorrect answer.

(30.0, 30, 30)
Not selected
Correct answer.

(30.0, 35, 30)
Not selected. Not selected is correct.

---

The data scientist of an organization has developed the following code snippet using the pandas library for data manipulation and analysis.


import pandas as pd

> Sample dataset

data = {'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02', '2022-01-03'],
        'Category': ['A', 'B', 'A', 'B', 'A'],
        'Value': [10, 15, 20, 25, 30]}

df = pd.DataFrame(data)

pivot_table = df.pivot_table(values='Value', index='Date', columns='Category', aggfunc='sum', fill_value=0)

print(pivot_table)

What will be the output of the given code snippet?


Option 1

Category       A   B
Date               
2022-01-01    10  15
2022-01-02    20  25
2022-01-03    30   0



Option 2

Category       A   B
Date               
2022-01-01    10   0
2022-01-02    20  25
2022-01-03    30  15



Option 3

Category       A   B
Date               
2022-01-01    10   0
2022-01-02    20   0
2022-01-03    30   0



T Option 4

Category       A   B
Date               
2022-01-01    10  15
2022-01-02    20  25
2022-01-03    30  15
Instruction: Choose the option that best answers the question. 

---

Nancy is developing a Generative AI model for creating personalized poetry. She wants to implement a process that considers the user's input, generates an initial draft, refines it through iterative steps, and produces a final polished poem. Her goal is to generate a sequence of operations using Chain-of-Thought Prompting to enhance the coherence and creativity of the generated poems.


Arrange the code snippets in the correct sequence that will help her in the task.

Code Snippet B

def get_user_input():

    user_input = input("Enter a theme or topic for your poem: ")

    return user_input

Code Snippet C

def generate_initial_draft(theme):

    initial_draft = generate_poem(theme)

    return initial_draft


Code Snipper E

def refine_poem(poem):

    refined_poem = apply_refinement(poem)

    return refined_poem


Code Snippet F

def iterate_refinement(initial_draft, iterations=3):

    current_poem = initial_draft

    for _ in range(iterations):

        current_poem = refine_poem(current_poem)

    return current_poem

Code Snippet A

def polish_poem(poem):

    polished_poem = apply_polishing(poem)

    return polished_poem


Code Snippet D

user_theme = get_user_input()

draft = generate_initial_draft(user_theme)

final_poem = iterate_refinement(draft)

final_poem = polish_poem(final_poem)

print(final_poem)



Instruction: Rank the following items in the correct sequence, by dragging with your mouse or finger. 
