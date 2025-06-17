---
date: 1970-01-01
---

# Hyperparameter Tuning ML Models

### Introduction to Databricks

**Databricks Overview**
- **Unified and Cloud-Native**: Databricks is a cloud-native data management platform that consolidates tools for building, deploying, sharing, and maintaining data solutions at an enterprise scale.
- **Founders' Background**: The company was founded by key figures behind Apache Spark and MLflow, linking these technologies closely together.

**Cloud-Native Features**
- Databricks operates on major cloud platforms: AWS, Microsoft Azure, and Google Cloud Platform. Demos will primarily use Microsoft Azure but can adapt with minimal changes for other platforms.

### Use Cases for Databricks
- **Data Processing & Workflow Management**
- **Business Analytics Using SQL**
- **Dashboard Creation & Visualizations**
- **Data Ingestion, Processing, and ETL Pipelines**
- **Data Governance & Security Management**
- **ML Model Training, Serving, and Tracking**

### Core Components of Databricks

#### 1. Apache Spark
- **Managed Version**: Databricks offers a managed version of Spark with enhanced features.
- **Unified Data Processing**: Supports both batch and streaming data, processing data in-memory using data frames.
- **Distributed Architecture**: Built on Hadoop infrastructure, Spark is known for scalability, fault tolerance, and multi-language support (Python, Scala, Java, R).

#### 2. Delta Lake
- **Combining Data Warehousing and Data Lakes**: Delta Lake merges the advantages of both data warehouses and data lakes, making it a competitor to offerings like Google BigQuery and Snowflake.
- **Data Warehouse vs. Data Lake**:
  - **Data Warehouse**: A single source of truth for structured data, mainly used for business intelligence and analytics.
  - **Data Lake**: A repository for raw data (structured, semi-structured, unstructured), facilitating data science and machine learning.

- **Lakehouse Concept**: Delta Lake exemplifies the "Data Lakehouse" model, accommodating structured, semi-structured, and unstructured data for diverse use cases, including BI and ML.

#### 3. Attractions of Delta Lake
- **Cost-Effective Storage**: Utilizes low-cost cloud-native storage solutions (e.g., Amazon S3, Azure Data Lake Storage).
- **Unified Data Processing**: Supports various data types for both batch and real-time processing, extending to BI and ML applications.
- **ACID Transactions**: Provides atomicity, consistency, isolation, and durability, along with schema enforcement for better governance.

### Databricks Environments with MLflow
1. **Databricks SQL**: Focuses on analysts executing SQL queries for dashboards and visualizations.
2. **Databricks Data Science and Engineering**: Targeted at data scientists and engineers working on ETL processes.
3. **Databricks Machine Learning**: Designed for data scientists and ML engineers focused on building and deploying ML models.

MLflow is primarily utilized within the Databricks Machine Learning environment, aligning perfectly with the upcoming demos.

### Hyperparameter Tuning in MLflow with Hyperopt

#### Overview
In the upcoming demos, we will focus on hyperparameter tuning using MLflow and Hyperopt, a Python library for this purpose. We will perform these demos on Databricks, utilizing its machine learning runtime, which includes an optimized version of Hyperopt tightly integrated with MLflow tracking.

#### Setting Up Databricks on Microsoft Azure
1. **Access Azure**: Begin at the Microsoft Azure homepage, where you can view Azure Services and Resources.
2. **Resource Group**: Navigate to your Resource group, noting that there are currently no resources available, as previous ones were deleted.
3. **Create Databricks Workspace**:
   - Click the **Create resource** button.
   - Search for **Azure Databricks** in the Marketplace and select it.
   - Click the **Create** button to set up a new workspace.

4. **Fill in Workspace Details**:
   - Enter the Workspace name (e.g., `looney-db-ws`) and select a Region.
   - Choose the **Trial** Pricing Tier for a 14-day free period on Databricks while paying for the VMs used for compute.

5. **Networking and Finalize Setup**:
   - Keep default settings for Networking, Encryption, and Tags.
   - Click **Review + create** and confirm when deployment is successful.
   - Click **Go to resource** to access the new workspace.

#### Launching Databricks Workspace
1. **Workspace Overview**: In the Azure Databricks Service page, observe the Workspace name and Subscription ID.
2. **Launch Workspace**: Click on the **Launch Workspace** button to enter the Databricks interface.

#### Databricks Personas
1. **Selecting Persona**: In Databricks, three personas are available:
   - **Data Science & Engineering**: For users focused on Spark and ETL.
   - **Machine Learning**: For ML model developers.
   - **SQL**: For analysts using Databricks SQL.

2. **Choose Machine Learning Persona**: Switch to the Machine Learning persona to access relevant options such as Notebook, AutoML, and Feature Store.

#### Configuring Compute Resources
1. **Access Compute Settings**: Click on the **Compute** section on the left sidebar.
2. **Create Cluster**:
   - Click the **Create compute** button.
   - Choose a **Single node cluster** and select the Databricks runtime version (e.g., `13.1 ML`, no GPU support).
   - Name the cluster (e.g., `loony-ml-cluster`) and click **Create Cluster**.
   - Wait for the cluster to provision; look for a green checkmark indicating success.

#### Uploading Data to DBFS
1. **Accessing DBFS**: Click on the **Data** section in Databricks.
   - If the **Browse DBFS** button is not visible, enable it by going to **Admin Settings** and adjusting **DBFS File Browser** to Enabled.
   - Refresh the page to see the **Browse DBFS** option.

2. **Uploading Training Data**:
   - Click **Browse DBFS** and navigate to the **FileStore**.
   - Right-click to select **Upload here** and upload the `customer_travel.csv` file.
   - Confirm that the file is accessible to all users with workspace access.

### Setting Up and Running Hyperparameter Tuning in Databricks

#### Overview
In this demo, we will set up our Jupyter Notebook in Databricks, import our code, and establish an MLflow experiment for hyperparameter tuning using Hyperopt.

#### Importing the Jupyter Notebook
1. **Navigating Databricks**: Start by clicking on the **Experiments** section in the left sidebar. You will see the option to create a new experiment, but first, we need to import our Jupyter Notebook.
   
2. **Accessing Workspace**:
   - Click on **Workspace** in the top left corner.
   - Select **Users**, then choose your user account.
   - Click **Import** to upload files from your local machine.

3. **Import the Notebook**:
   - Navigate to the location of your Jupyter Notebook (`hyperparameterTuningUsingHyperopt.ipynb`) and click **Import**. 
   - A success message will confirm the import, and you will now see the notebook listed in your Workspace.

4. **Opening the Notebook**: Right-click on the notebook and select **Open in New Tab** to start working on it.

#### Connecting to Compute Resources
1. **Connecting to Cluster**:
   - Click on the **Connect** button at the top right of the notebook.
   - Select your compute resource (e.g., `looney-ml-cluster`).

2. **Clearing Outputs**: To start fresh, select **Run** from the top menu and choose **Clear all cell outputs**. Confirm the action in the dialog box.

#### Code Overview
1. **Reading Data**: Use `pd.read_csv` to load the dataset from DBFS:
   ```python
   df = pd.read_csv('/dbfs/FileStore/customer_travel.csv')
   ```
   
2. **Setting Up MLflow Experiment**:
   - Import MLflow and set the experiment:
   ```python
   import mlflow
   mlflow.set_experiment('/Users/your_username/hptuning_churn_prediction_model')
   ```

3. **Creating the Experiment**:
   - Navigate to the **Experiments** section and create a new experiment named `hptuning_churn_prediction_model`. You can leave the artifact location blank and hit **Create**.

4. **Logging Parameters and Metrics**:
   - Inside a `with` block for `mlflow.start_run()`, instantiate your model (e.g., `LogisticRegression`), set up a pipeline, and log parameters and metrics:
   ```python
   with mlflow.start_run():
       lr_model = LogisticRegression()
       pipeline = Pipeline(...)
       mlflow.log_params({...})
       mlflow.log_metrics({...})
       mlflow.sklearn.log_model(pipeline, "model")
   ```

#### Running the Code
1. **Execute the Cells**: After setting everything up, run the cells in your notebook. This should execute the code without issues.

2. **Viewing MLflow Run**: A clickable link to the MLflow run will appear in the notebook. Click it to view the run details, including:
   - Run ID, date, source, user, duration, and lifecycle stages.
   - Parameters and metrics logged during the run.
   - Artifacts like the model files, including `MLmodel`, `conda.yaml`, and `model.pkl`.

#### Conclusion
In this demo, we successfully imported a Jupyter Notebook into Databricks, created an MLflow experiment, and executed the code to log a model run. This setup lays the groundwork for hyperparameter tuning using Hyperopt in subsequent demos.

### Hyperparameter Tuning with Hyperopt in Databricks

#### Overview
In this demo, we will focus on hyperparameter tuning using the **Hyperopt** library integrated with **MLflow** in Databricks. We’ll explore how to set up a logistic regression model, define hyperparameters, and implement the tuning process effectively.

#### Key Concepts
- **Model Parameters vs. Hyperparameters**: 
  - **Model Parameters**: Values that the model learns during training (e.g., weights).
  - **Hyperparameters**: Predefined settings that control the learning process (e.g., regularization strength, solver type). These do not change during training and are crucial for model performance.

#### Setting Up the Model
1. **Defining the Logistic Regression Model**:
   ```python
   lr_model = LogisticRegression(C=params['C'], solver=params['solver'], class_weight=params['class_weight'])
   ```
   - **Hyperparameters** to optimize:
     - `C`: Regularization strength.
     - `solver`: Algorithm to use in the optimization problem.
     - `class_weight`: Weights associated with classes in the loss function.

2. **Specifying Hyperparameter Search Space**:
   ```python
   search_space = {
       'C': hp.lognormal('C', 0, 1.0),
       'solver': hp.choice('solver', ['liblinear', 'lbfgs']),
       'class_weight': hp.choice('class_weight', [None, 'balanced'])
   }
   ```
   - `C`: Drawn from a lognormal distribution (mean 0, std dev 1.0).
   - `solver`: Choose between `liblinear` and `lbfgs`.
   - `class_weight`: Options include `None` (equal weight) or `balanced` (inverse frequency weighting).

#### Hyperparameter Tuning Algorithm
1. **Choosing the Algorithm**:
   - We use `tpe.suggest`, which stands for Tree of Parzen Estimators. This is an adaptive search algorithm that learns from previous evaluations.
   ```python
   algo = tpe.suggest
   ```

#### Running Hyperparameter Tuning with MLflow
1. **Setting Up the Top-Level MLflow Run**:
   - Use the `mlflow.start_run()` context to track the hyperparameter tuning process.
   - Call `fmin()` to perform the tuning:
   ```python
   with mlflow.start_run():
       best_lr_params = fmin(
           fn=objective,
           space=search_space,
           algo=algo,
           max_evals=16
       )
       print('Best value found: ', best_lr_params)
   ```
   - `fmin` will repeatedly call the `objective` function with different hyperparameter sets, storing the best performing parameters.

2. **Defining the Objective Function**:
   - The `objective` function should return a value to be minimized (e.g., validation loss). This function is critical for the tuning process, as it evaluates model performance based on the current set of hyperparameters.

### Hyperparameter Tuning with Hyperopt in MLflow: Detailed Walkthrough

In this demo, we will dive deeper into hyperparameter tuning using **Hyperopt** in **MLflow** on **Databricks**. We'll explore the process from the ground up, starting with the implementation of the **objective function** and understanding the nested runs involved in the tuning process.

#### Key Components

1. **MLflow Run Structure**:
   - The outer run, referred to as the **parent run**, is initiated when we call `fmin()`. 
   - Each call to the `objective` function creates a **nested run** (or child run) within the parent run.

2. **Defining the Objective Function**:
   - The objective function accepts `params` as input, a dictionary containing hyperparameter values:
   ```python
   def objective(params):
       with mlflow.start_run(nested=True):
           # Access hyperparameters
           C = params['C']
           solver = params['solver']
           class_weight = params['class_weight']
           # Model training and evaluation...
   ```
   - The `nested=True` argument indicates that this run is part of a larger parent run, allowing for organized logging of hyperparameter evaluations.

3. **Logging Parameters and Metrics**:
   - Inside the objective function:
     - We instantiate the `LogisticRegression` model using the provided hyperparameters.
     - After training, we log the hyperparameters, metrics (like F1 score), and the model itself using `mlflow.log_params()`, `mlflow.log_metrics()`, and `mlflow.log_model()`.

4. **Returning the Results**:
   - The function returns a dictionary containing the loss and status:
   ```python
   return {'loss': -test_f1_score, 'status': STATUS_OK}
   ```
   - We negate the F1 score because Hyperopt minimizes the loss; thus, maximizing the F1 score corresponds to minimizing the negative F1 score.

5. **Running the Hyperparameter Search**:
   - We set up the search space and specify the algorithm:
   ```python
   search_space = {
       'C': hp.lognormal('C', 0, 1.0),
       'solver': hp.choice('solver', ['liblinear', 'lbfgs']),
       'class_weight': hp.choice('class_weight', [None, 'balanced'])
   }
   algo = tpe.suggest
   ```
   - The search space defines the range of values Hyperopt will explore for each hyperparameter.

6. **Executing the Parent Run**:
   - The main call to start the hyperparameter tuning process looks like this:
   ```python
   with mlflow.start_run():
       best_lr_params = fmin(fn=objective, space=search_space, algo=algo, max_evals=16)
   ```
   - This runs the objective function 16 times with different hyperparameter combinations and logs each trial as a nested run.

#### Viewing and Analyzing Results

1. **Accessing Experiment Runs**:
   - After execution, we can view all runs in the MLflow UI. 
   - Expanding the parent run reveals all nested runs and their associated metrics.

2. **Sorting and Filtering**:
   - We can sort runs by various metrics, such as `Test_f1_score`, to identify the best-performing models quickly.
   - If multiple runs yield the same score, Hyperopt may return any of these as the best model.

3. **Investigating Individual Runs**:
   - Clicking into a specific run allows us to see the logged parameters and metrics, confirming the model's performance.

4. **Cleaning Up**:
   - Before starting a new hyperparameter tuning exercise, it's good practice to clean up old runs. 
   - Deleting the parent run removes all associated nested runs, ensuring a tidy experiment environment.

### Advanced Hyperparameter Tuning with Hyperopt: Real-World Example

In this demo, we’ll explore a more complex hyperparameter tuning exercise using **Hyperopt** in **MLflow** on **Databricks**. Unlike our previous work with logistic regression, this time we'll tune multiple classifiers, making the process much more engaging and relevant for real-world applications.

#### Defining the Search Space

1. **Nested Search Space**:
   - The search space allows us to explore different types of classifiers and their associated hyperparameters.
   ```python
   search_space = hp.choice('classifier_type', [
       {'type': 'svm', 'C': hp.lognormal('C', 0, 1.0), 'kernel': hp.choice('kernel', ['linear', 'rbf'])},
       {'type': 'rf', 'n_estimators': scope.int(hp.quniform('n_estimators', 100, 500, 50)), 'max_depth': hp.choice('max_depth', [None, 10, 20, 30]), 'min_samples_leaf': hp.quniform('min_samples_leaf', 1, 10, 1), 'min_samples_split': hp.quniform('min_samples_split', 2, 10, 1)},
       {'type': 'logrec', 'C': hp.lognormal('C', 0, 1.0)},
       {'type': 'dtc', 'max_depth': hp.choice('max_depth', [None, 10, 20]), 'min_samples_split': hp.quniform('min_samples_split', 2, 10, 1)}
   ])
   ```
   - Each classifier type (SVM, Random Forest, Logistic Regression, Decision Tree) has its own set of hyperparameters, making the search more dynamic and relevant.

2. **Distribution Definitions**:
   - Hyperparameters like `C` for SVM and `n_estimators` for Random Forest are defined using distributions that allow Hyperopt to explore various configurations efficiently.

#### The Objective Function

1. **Function Structure**:
   - The `objective` function is designed to accept a `params` dictionary, where it first identifies the classifier type:
   ```python
   def objective(params):
       with mlflow.start_run(nested=True):
           del params['type']  # Remove type to avoid passing it to classifiers
           if params.get('type') == 'svm':
               clf = SVC(**params)
           elif params.get('type') == 'rf':
               clf = RandomForestClassifier(**params)
           elif params.get('type') == 'logrec':
               clf = LogisticRegression(**params)
           elif params.get('type') == 'dtc':
               clf = DecisionTreeClassifier(**params)
           else:
               return 0
   ```

2. **Instantiating the Classifier**:
   - The classifier is instantiated based on the classifier type. By using the unpacking operator `**`, we pass the remaining parameters from the `params` dictionary to the classifier constructor. This method simplifies managing varying hyperparameter names across different classifiers.

3. **Model Training and Logging**:
   - After fitting the model, we log the parameters and metrics:
   ```python
   mlflow.log_params(params)
   mlflow.log_metrics({'f1_score': test_f1_score})
   mlflow.log_model(clf, "model")
   ```

4. **Returning Results**:
   - Finally, we return the results in the required format:
   ```python
   return {'loss': -test_f1_score, 'status': STATUS_OK}
   ```
   - As before, we negate the F1 score since Hyperopt minimizes the loss.

#### Implementing the Parent Run

- The parent run initiates the tuning process, invoking the `fmin` function with our newly defined search space and objective function:
```python
with mlflow.start_run():
    best_params = fmin(fn=objective, space=search_space, algo=tpe.suggest, max_evals=50)
```
- Here, `max_evals` is set to 50, allowing Hyperopt to explore a substantial number of configurations.

#### Analyzing Results

- Once the tuning completes, we can view the results in the MLflow UI:
  - Examine which classifiers performed best based on the logged metrics.
  - Sort runs to find the configuration that maximized the F1 score or other relevant metrics.

#### Conclusion

This advanced exercise in hyperparameter tuning highlights the flexibility of Hyperopt and the importance of exploring various models and configurations. By leveraging nested search spaces and dynamically passing parameters, we can significantly improve our model's performance in a more realistic setting. In the next demo, we’ll further explore the results of this tuning exercise and see how to extract and analyze the best-performing models.

### Large-Scale Hyperparameter Tuning with Hyperopt on Databricks

In this demo, we’ll dive into a more extensive hyperparameter tuning exercise using **Hyperopt** and **MLflow** on **Databricks**. Building on the groundwork laid in the previous session, we will run the objective function and evaluate results for a variety of classifiers.

#### Setting Up the Search Space

We defined a two-level search space that includes several classifiers:
- **SVM**
- **Random Forest (RF)**
- **Logistic Regression (LogReg)**
- **Decision Tree Classifier (DTC)**

This allows us to experiment with different models and their hyperparameters effectively.

#### Running the Top-Level Parent Run

Here's how we set up and run the hyperparameter tuning:

```python
algo = tpe.suggest  # Using TPE as the optimization algorithm
spark_trials = SparkTrials()  # Setting up SparkTrials for distributed tuning

with mlflow.start_run():  # Start the MLflow run
    best_result = fmin(  # Invoke fmin for hyperparameter tuning
        fn=objective,  # The objective function defined earlier
        space=search_space,  # The search space for tuning
        algo=algo,  # The optimization algorithm
        max_evals=32,  # Total number of evaluations
        trials=spark_trials  # Use SparkTrials for parallel execution
    )
```

1. **Adaptive Search**: We use the **TPE** (Tree-structured Parzen Estimator) algorithm, which adapts based on previous trials to improve efficiency.
2. **Spark Integration**: The `SparkTrials` object enables distributed tuning across Spark nodes, making the process faster and more scalable, especially useful in production environments.

#### Monitoring Progress

As the tuning process runs, we see:
- A progress bar for Spark jobs.
- The number of successful MLflow runs (32 in our case).
- A message indicating that parallelism is automatically set to 4.

This gives us insight into how the tuning is progressing and confirms that all runs have succeeded.

#### Evaluating the Results

After tuning, we utilize the `hyperopt` library to view the best results:

```python
from hyperopt import space_eval

best_parameters = space_eval(search_space, best_result)
print(best_parameters)
```

This provides a dictionary detailing the best hyperparameters found during the tuning process. In this case, it indicates that the best configuration was for a **Decision Tree Classifier** with:
- **Criterion**: Gini
- **Max Depth**: 10
- **Max Features**: 3

#### Viewing in MLflow

We then navigate to the MLflow UI to inspect the results:

1. **Experiment Page**: We find the experiment named `hptuning_churn_prediction_model`, which lists all runs.
2. **Sort Order**: The runs are sorted by **Test F1 Score**, with the highest score at the top. In our results, the best score achieved was **0.706**.

When we delve into the details of the top run:
- **Parameters**: Verify that the parameters correspond to what we observed in the notebook.
- **Metrics**: Confirm the **Test F1 Score** is indeed **0.706**, with a loss of **-0.706**.
- **Tags and Artifacts**: Check that the trial status is recorded as a success and that the model has been logged correctly.

#### Conclusion

In this session, we successfully executed a large-scale hyperparameter tuning exercise using Hyperopt and MLflow on Databricks. By leveraging Spark for distributed computing, we efficiently explored a variety of classifiers and their hyperparameters, ultimately identifying a strong model configuration. This workflow not only demonstrates the power of Hyperopt for hyperparameter optimization but also highlights the integration of Databricks and MLflow for seamless model management.

### Setting Up MLflow with SQLite on a Local Machine

In this demo, we're transitioning from cloud-based environments back to our local setup. We will configure MLflow to use SQLite as its backend store and utilize **statsmodels** for model building instead of **scikit-learn**. Let’s go through the process step by step.

#### Step 1: Installing SQLite

1. **Download SQLite**: Visit [sqlite.org](https://sqlite.org.html) and click on the "Download" button. Choose the appropriate precompiled binaries for your operating system (e.g., Mac or Windows).
2. **Extract the Files**: Once downloaded, unzip the file to access the SQLite executables.

#### Step 2: Configuring the Environment

1. **Modify `.zshrc`**: Open your terminal and edit the `.zshrc` file to add SQLite to your PATH:
   ```bash
   nano ~/.zshrc
   ```
   Add the following line to export the path:
   ```bash
   export PATH="/path/to/sqlite-tools:$PATH"
   ```
   Replace `/path/to/sqlite-tools` with the actual path where you extracted SQLite.

2. **Source the File**: Apply the changes to your current terminal session:
   ```bash
   source ~/.zshrc
   ```

#### Step 3: Setting Up MLflow

1. **Activate Virtual Environment**:
   ```bash
   source mlflow_venv/bin/activate
   ```

2. **Create a Database Directory**:
   ```bash
   mkdir database && cd database
   ```

3. **Create SQLite Database**:
   Create an empty SQLite database file:
   ```bash
   touch mlflow.db
   ```

4. **Open SQLite Shell**:
   Enter the SQLite shell:
   ```bash
   sqlite3 mlflow.db
   ```

5. **Check Tables**: Initially, there will be no tables:
   ```sql
   .tables
   ```

#### Step 4: Running MLflow Server with SQLite

1. **Stop Any Running MLflow UI**: If you have the MLflow UI running, stop it with `Ctrl+C` as we need to run the MLflow server directly.

2. **Upgrade MLflow**: Since we encountered compatibility issues with version 2.3.2, let’s upgrade to the latest version:
   ```bash
   pip install mlflow -U
   ```

3. **Run MLflow Server**:
   Start the MLflow server with SQLite as the backend store:
   ```bash
   mlflow server --backend-store-uri sqlite:////path/to/mlflow.db --host localhost -p 5000
   ```
   Replace `/path/to/mlflow.db` with the actual path to your database file.

#### Step 5: Accessing the MLflow UI

1. **Open the Browser**: Navigate to `http://localhost:5000` to access the MLflow UI. You should see the default experiment listed.

2. **Check SQLite Database**: Go back to the SQLite shell and check the tables again:
   ```sql
   .tables
   ```

3. **View Experiments**:
   Run a query to see the experiments:
   ```sql
   SELECT * FROM experiments;
   ```

4. **View Schema**:
   Check the schema of the runs table:
   ```sql
   .schema runs
   ```

5. **Check Runs and Metrics**:
   Initially, the runs and metrics tables will be empty:
   ```sql
   SELECT * FROM runs;
   SELECT * FROM metrics;
   ```

#### Conclusion

We successfully configured MLflow to use SQLite as its backend store on a local machine, setting the stage for our next steps in model training and logging with **statsmodels**. This setup allows us to easily track experiments and manage models locally before potentially scaling to more complex setups. In the next demo, we will execute model runs and populate the SQLite database with meaningful data.

### Working with Statsmodels in MLflow

In this demo, we'll transition from using **scikit-learn** to **statsmodels** for our regression model while continuing to leverage **MLflow** for experiment tracking. Let’s walk through the steps to set this up.

#### Step 1: Install Statsmodels

First, we need to install the **statsmodels** library, which is more focused on statistical modeling than machine learning. Run the following command in your terminal:

```bash
pip install statsmodels
```

Verify the installation by checking the version:

```python
import statsmodels
print(statsmodels.__version__)  # Should display 0.14.0 or similar
```

#### Step 2: Import Necessary Libraries

Next, we’ll import the libraries we need. In your Jupyter Notebook, include the following imports:

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm
import mlflow
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
```

#### Step 3: Load and Prepare the Dataset

Load your dataset (e.g., an eCommerce dataset) and prepare it for modeling:

```python
# Load the dataset
data = pd.read_csv('ecommerce_data.csv')

# Drop categorical columns
data = data.drop(['Email', 'Address', 'Avatar'], axis=1)

# Separate features and target variable
X = data.drop('Yearly Amount Spent', axis=1)
y = data['Yearly Amount Spent']
```

#### Step 4: Standardize the Features

Set up a pipeline to standardize the features:

```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

#### Step 5: Configure MLflow

Since we are running the MLflow server manually, we need to set the tracking URI:

```python
mlflow.set_tracking_uri("http://localhost:5000")
```

Create a new experiment for tracking:

```python
experiment_id = mlflow.create_experiment("ecommerce_revenue_prediction")
mlflow.set_experiment("ecommerce_revenue_prediction")
```

#### Step 6: Run Statsmodels Regression

Now, we’ll set up and run a regression model using **statsmodels**:

```python
# Start an MLflow run
with mlflow.start_run():
    # Add a constant to the model (intercept)
    X_scaled_with_const = sm.add_constant(X_scaled)
    
    # Fit the model
    model = sm.OLS(y, X_scaled_with_const).fit()
    
    # Get the summary
    summary = model.summary()
    
    # Log parameters and metrics
    for param in model.params.index:
        mlflow.log_param(param, model.params[param])
    
    mlflow.log_metric("R_squared", model.rsquared)

    # Log the summary as an artifact (optional)
    with open("model_summary.txt", "w") as f:
        f.write(summary.as_text())
    mlflow.log_artifact("model_summary.txt")
```

#### Step 7: Check the MLflow UI

1. **Refresh the MLflow UI** at `http://localhost:5000`.
2. You should see a new run in the **ecommerce_revenue_prediction** experiment.
3. Click on the run to view the logged parameters, metrics (like R-squared), and the model summary as an artifact.

#### Step 8: Interpret the Results

In the MLflow UI, you'll find the coefficients for each of your features. As a reminder:

- **Positive coefficients** indicate a direct relationship with the target variable (e.g., higher spending).
- **Negative coefficients** indicate an inverse relationship.
- Standardization allows for easier comparison of the coefficients.

---

In this demo, we'll walk through building a regression model using **statsmodels** with MLflow's autologging feature. We will also cover how to manage models within MLflow and how to register them for easier access.

### Step 1: Set Up Autologging with Statsmodels

We start by integrating **MLflow** with **statsmodels** for autologging. Import the necessary libraries and configure autologging:

```python
import mlflow
import mlflow.statsmodels
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mlflow.models.signature import infer_signature

# Enable autologging with statsmodels
mlflow.statsmodels.autolog(log_models=False)
```

*Note:* Setting `log_models=False` allows us to explicitly log the model later.

### Step 2: Load and Prepare the Dataset

Load your eCommerce dataset and prepare it for modeling:

```python
# Load the dataset
data = pd.read_csv('ecommerce_data.csv')

# Drop categorical columns
data = data.drop(['Email', 'Address', 'Avatar'], axis=1)

# Split features and target variable
X = data.drop('Yearly Amount Spent', axis=1)
y = data['Yearly Amount Spent']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

### Step 3: Fit the Statsmodels Model

We will add a constant for the intercept and fit the model:

```python
# Start an MLflow run
with mlflow.start_run(run_name="run2"):
    # Add constant for intercept
    X_train_scaled = sm.add_constant(X_train_scaled)
    X_test_scaled = sm.add_constant(X_test_scaled)
    
    # Fit the Ordinary Least Squares (OLS) model
    model = sm.OLS(y_train, X_train_scaled).fit()
    
    # Make predictions
    predictions = model.predict(X_test_scaled)

    # Log metrics and model
    mlflow.log_metrics({"R_squared": model.rsquared})
    signature = infer_signature(X_test_scaled, predictions)
    mlflow.statsmodels.log_model(model, "model", signature=signature)
```

### Step 4: Check the MLflow UI

1. Refresh the **MLflow UI** at `http://localhost:5000`.
2. You should see the new run titled "run2" listed with the parameters and metrics logged.

### Step 5: Register the Model

After logging the model, we can register it for easier access:

```python
# Register the model
mlflow.register_model("runs:/<RUN_ID>/model", "revenue_prediction_model")
```

Replace `<RUN_ID>` with the actual ID from your logged run.

### Step 6: Transition to Production

To transition the registered model to production:

1. Go to the **Models** tab in the MLflow UI.
2. Click on your registered model.
3. Click "Transition to Production".

### Step 7: Load the Model from Production

Now we can load the model directly from production using the model URI:

```python
# Load the model from production
model_uri = "models:/revenue_prediction_model/Production"
loaded_model = mlflow.pyfunc.load_model(model_uri)

# Make predictions
predictions = loaded_model.predict(X_test)

# Compare actual vs. predicted values
results = pd.DataFrame({"Actual": y_test, "Predicted": predictions})
print(results.head())
```

### Step 8: Cleanup

Finally, when you're done, you can stop the MLflow server if it's running:

```bash
# Stop the server
Ctrl + C
```

### Step 9: Version Control

If needed, you can uninstall and reinstall specific versions of MLflow:

```bash
# Uninstall current version
pip uninstall mlflow

# Reinstall specific version
pip install mlflow==2.3.2
```