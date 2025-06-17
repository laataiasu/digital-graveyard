# Creating & Tracking ML Models

### MLflow Tracking Demo

#### Environment Setup
1. **Kernel Setup**: Confirm the kernel is set to `mlflow_venv` in Jupyter Notebook.
2. **MLflow Version**: Check the installed version using:
   ```python
   import mlflow
   print(mlflow.__version__)
   ```

#### MLflow Components
- **Key Components**:
  - MLflow Tracking
  - MLflow Projects
  - MLflow Models
  - MLflow Model Registry
  - MLflow Recipes (formerly MLflow Pipelines)

#### Dataset Setup
1. **Import Libraries**:
   ```python
   import pandas as pd
   import seaborn as sns
   import matplotlib.pyplot as plt
   ```

2. **Fetch Dataset from OpenML**:
   - Use the `fetch_openml` function to retrieve the `house_sales` dataset:
   ```python
   from sklearn.datasets import fetch_openml
   house_price_df = fetch_openml('house_sales', version=1, as_frame=True)
   ```

3. **Data Exploration**:
   - Check the first few rows:
   ```python
   house_price_df.data.head()
   ```

4. **Data Cleaning**:
   - Drop unnecessary columns:
   ```python
   house_price_df.data.drop(columns=['date', 'zipcode'], inplace=True)
   ```
   - Remove duplicates:
   ```python
   house_price_df.data = house_price_df.data.drop_duplicates()
   ```
   - Check the shape of the DataFrame:
   ```python
   print(house_price_df.data.shape)
   ```

5. **Feature Engineering**:
   - Add `age` and `renovation_age` columns:
   ```python
   house_price_df.data['age'] = 2015 - house_price_df.data['yr_built']
   house_price_df.data['renovation_age'] = 2015 - house_price_df.data['yr_renovated']
   ```

#### Data Visualization
1. **Histogram of Prices**:
   ```python
   plt.figure(figsize=(8, 6))
   sns.histplot(x='price', data=house_price_df.data)
   plt.show()
   ```

2. **Boxplot of Prices**:
   ```python
   plt.figure(figsize=(8, 6))
   sns.boxplot(y='price', data=house_price_df.data)
   plt.show()
   ```

3. **Barplot by Waterfront**:
   ```python
   plt.figure(figsize=(8, 6))
   sns.barplot(x='waterfront', y='price', data=house_price_df.data)
   plt.show()
   ```

4. **Regression Plot**:
   ```python
   plt.figure(figsize=(8, 6))
   sns.regplot(data=house_price_df.data, x='sqft_living', y='price')
   plt.show()
   ```

5. **Correlation Heatmap**:
   - Define selected features and compute correlations:
   ```python
   selected_features = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 
                        'sqft_basement', 'yr_built', 'yr_renovated', 'sqft_above', 
                        'age', 'renovation_age']
   cormap = house_price_df.data[selected_features].corr()
   sns.heatmap(cormap, annot=True)
   plt.show()
   ``` 

This structured approach covers the essentials for using MLflow Tracking along with dataset preparation and exploratory data analysis.

### Using `pandas_profiling` for Exploratory Data Analysis

#### Correlation Heatmap
- A correlation heatmap was generated previously, revealing strong relationships between variables in the dataset.

#### Installing `pandas_profiling`
1. **Install Libraries**:
   ```bash
   pip install pandas_profiling
   pip install ipywidgets
   ```

#### Generating a Profile Report
1. **Import the Library**:
   ```python
   import ydata_profiling as pp
   ```

2. **Create the Profile Report**:
   ```python
   profile = pp.ProfileReport(house_price_df.data)
   ```

3. **View the Report**:
   - The report includes tabs: Overview, Variables, Interactions, Correlations, Missing values, and Sample.

#### Overview Section
- Displays dataset statistics: number of columns, rows, variable types (17 Numeric, 3 Categorical), and information about missing and duplicate rows.

#### Variables Section
- Contains distribution visualizations for each variable, including:
  - The `price` column has 4028 distinct values.
  - High correlation links with other columns.
  - Skewness of `price` is 4.023, indicating right skew.

#### Alerts Section
- Identifies potential issues:
  - High correlation between `price` and `sqft_living`.
  - Imbalance in `waterfront` and `view` columns.
  - Zeros in `sqft_basement` and `yr_renovated`.

#### Interactions Section
- Allows exploration of relationships between selected variables.
- Visualizations update based on selected pairs.

#### Correlations Section
- Features Heatmap and Table views:
  - Correlation coefficients may be affected by missing values.
  
#### Missing Values Section
- Displays count of missing values and a nullity matrix.

#### Sample Section
- Shows the first and last rows for each column, similar to using `head()` and `tail()`.

#### Exporting the Report
- Save the report to an HTML file:
  ```python
  profile.to_file("house_price_profile_report.html")
  ```

This completes the exploration using `pandas_profiling`. The next step will involve introducing MLflow and setting up the first experiment.

### MLflow for ML Model Development

#### Overview of MLflow Tracking
- The lifecycle of ML model development involves:
  1. **Exploration** of the dataset.
  2. **Model evaluation** and training.
  3. **Productionizing** the best-performing models.
- **MLflow Tracking** assists in this workflow, primarily through the concept of **experiments**.

#### Creating an Experiment
1. **Create Experiment**:
   ```python
   experiment_id = mlflow.create_experiment(name='kc_house_price_prediction')
   ```

#### Viewing Experiments in MLflow UI
- Initially, only the **Default** experiment is visible.
- After running the experiment creation code, refresh the MLflow UI to see the new experiment listed.

#### Exploring Experiment Details
- The new experiment will have an associated **Artifact Location** that includes the Experiment ID.
- Check the `mlruns` directory to confirm that a new directory matching the Experiment ID has been created.

#### Data Preparation
- Drop correlated columns from the DataFrame:
  ```python
  house_price_df.data.drop(columns=['yr_built', 'yr_renovated', 'sqft_above', 'bathrooms', 'sqft_living15'], inplace=True)
  ```
- Verify the shape and column names:
  ```python
  house_price_df.data.shape
  house_price_df.data.columns
  ```

#### Writing Feature Names to a File
- Create a comma-separated list of feature names and save to `features.txt`:
  ```python
  features = """'bedrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_basement', 'lat', 'long', 'sqft_lot15', 'age', 'renovation_age'"""
  with open("features.txt", "w") as f:
      f.write(features)
  ```

#### Exploring Experiment Objects
- Retrieve and print details of the Default experiment:
  ```python
  experiment = mlflow.get_experiment("0")
  print("Name: {}".format(experiment.name))
  print("Artifact Location: {}".format(experiment.artifact_location))
  print("Tags: {}".format(experiment.tags))
  print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
  print("Creation timestamp: {}".format(experiment.creation_time))
  ```

#### Retrieving Details of the New Experiment
- Repeat the above steps for the newly created experiment:
  ```python
  experiment = mlflow.get_experiment(experiment_id)
  print("Name: {}".format(experiment.name))
  print("Experiment_id: {}".format(experiment.experiment_id))
  print("Artifact Location: {}".format(experiment.artifact_location))
  print("Tags: {}".format(experiment.tags))
  print("Lifecycle_stage: {}".format(experiment.lifecycle_stage))
  print("Creation timestamp: {}".format(experiment.creation_time))
  ```

#### Tracking URI
- Check the Tracking URI:
  ```python
  mlflow.get_tracking_uri()
  ```
- The Tracking URI indicates where experiment data will be stored, defaulting to the local filesystem when using the MLflow UI.

### Summary
- Created a new experiment in MLflow and verified its details via the UI and APIs.
- Prepared the dataset by dropping unnecessary columns and saving feature names.
- Next steps will involve setting up and executing runs associated with the experiment.

### Working with MLflow Experiments and Runs

#### Setting Up the Experiment
1. **Set Active Experiment**:
   ```python
   mlflow.set_experiment(experiment_name='kc_house_price_prediction')
   ```
   - This command sets `kc_house_price_prediction` as the active experiment.

#### Starting a Run
2. **Start a Run**:
   ```python
   mlflow.start_run()
   ```
   - Every run must belong to an active experiment. If an active experiment isn't set, MLflow defaults to a new one.

3. **Log Figures**:
   ```python
   mlflow.log_figure(fig1, 'histogram_price.png')
   mlflow.log_figure(fig2, 'boxplot_price.png')
   ```
   - This saves the generated figures as artifacts in the current run.

#### Refreshing the MLflow UI
- After logging figures, refresh the MLflow UI to see the newly created run and its artifacts.

#### Ending a Run
4. **End the Run**:
   ```python
   mlflow.end_run()
   ```
   - It's crucial to end a run; otherwise, MLflow will throw an exception if you attempt to start another run.

#### Creating Named Runs
5. **Start a Named Run**:
   ```python
   mlflow.start_run(run_name='exploratory_data_analysis')
   ```
   - This allows for better identification of runs in the UI.

6. **Log Multiple Figures**:
   ```python
   mlflow.log_figure(fig1, 'histogram_price.png')
   mlflow.log_figure(fig2, 'boxplot_price.png')
   mlflow.log_figure(fig3, 'boxplot_waterfront_vs_price.png')
   mlflow.log_figure(fig4, 'regplot_sqft_living_vs_price.png')
   mlflow.log_figure(fig5, 'correlation_heatmap.png')
   ```

#### Verify in MLflow UI
- Check the UI for the newly created run `exploratory_data_analysis`, which should now display all five logged figures.

#### Logging Non-Image Artifacts
7. **Log a Non-Image Artifact**:
   ```python
   mlflow.start_run(run_name='features_as_artifacts')
   mlflow.log_artifact("features.txt")
   ```

8. **Accessing Active Run Information**:
   ```python
   run = mlflow.active_run()
   print('Active run_id: {}'.format(run.info.run_id))
   mlflow.end_run()
   ```

#### Final Verification in MLflow UI
- Navigate back to the experiment in the UI to confirm that `features_as_artifacts` run exists and that it contains `features.txt`.

### Summary
- We successfully set up and managed experiments and runs in MLflow, logging both figures and non-image artifacts.
- The importance of properly managing the lifecycle of runs was emphasized, ensuring we explicitly start and end each run.
- In the next demo, we will continue exploring more advanced functionalities of MLflow runs.

### Using MLflow with Context Managers for Experiment Tracking

#### Streamlining Run Management with Context Managers
1. **Using `with` Clause**:
   ```python
   with mlflow.start_run(run_name='eda_plots_and_features_as_artifacts') as current_run:
       mlflow.log_figure(fig1, 'histogram_price.png')
       mlflow.log_figure(fig2, 'boxplot_price.png')
       mlflow.log_figure(fig3, 'boxplot_waterfront_vs_price.png')
       mlflow.log_figure(fig4, 'regplot_sqft_living_vs_price.png')
       mlflow.log_figure(fig5, 'correlation_heatmap.png')
       mlflow.log_artifact("features.txt")
   ```
   - This approach automatically calls `end_run()` when exiting the `with` block, simplifying run management.

#### Handling Exceptions
- If an exception occurs within the `with` block, `end_run()` will still be called, ensuring proper cleanup.

#### Accessing the Last Active Run
2. **Getting Run Details**:
   ```python
   last_run = mlflow.last_active_run()
   print(last_run)
   ```
   - This retrieves details about the most recent active run, including its name and associated tags.

#### Querying Runs with MLflow Client
3. **Using `MlflowClient`**:
   ```python
   client = mlflow.MlflowClient()
   data = client.get_run(current_run.info.run_id).data
   print(data)
   ```
   - This allows you to query the MLflow server for details about specific runs and their metrics, parameters, and tags.

#### Verifying Artifacts in the MLflow UI
- Check the MLflow UI for the run `eda_plots_and_features_as_artifacts` to see all logged artifacts, including figures and `features.txt`.

#### Listing All Experiments
4. **Getting Experiments**:
   ```python
   experiments = mlflow.search_experiments()
   print(experiments)
   ```
   - This retrieves a list of all experiments in the current MLflow setup, including their IDs.

### Summary
- We've streamlined run management in MLflow using the context manager approach, simplifying the need to manually call `end_run()`.
- We demonstrated how to access and query run details and how to list all experiments available in the MLflow tracking server.
- The next step involves building and using models within the context of our experiments.

### Typical Machine Learning Workflow with MLflow

In a standard ML workflow, you typically start with a dataset, explore it, preprocess it, and then experiment with various models to find the best one based on test dataset performance. This is where MLflow comes into play, providing a structured way to track experiments and manage models. Let’s go through the steps demonstrated in the MLflow workflow.

#### 1. **Setup and Data Preparation**
- **Imports**:
   ```python
   from sklearn.model_selection import train_test_split
   from sklearn.linear_model import LinearRegression
   from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
   ```
- **Starting a Run**:
   ```python
   with mlflow.start_run(run_name='Simple Linear Regression') as lr_run:
   ```
- **Preparing the Data**:
   - Split the dataset into features (`X`) and target (`y`).
   - Use `train_test_split` to create training and test datasets.

#### 2. **Model Training and Evaluation**
- **Fitting the Model**:
   ```python
   lr_model = LinearRegression()
   lr_model.fit(X_train.to_numpy().reshape(-1, 1), y_train)
   ```
- **Making Predictions**:
   ```python
   y_pred = lr_model.predict(X_test.to_numpy().reshape(-1, 1))
   ```
- **Calculating Metrics**:
   ```python
   training_score = lr_model.score(X_train.to_numpy().reshape(-1, 1), y_train)
   mean_abs_error = mean_absolute_error(y_test, y_pred)
   root_mean_sq_error = mean_squared_error(y_test, y_pred, squared=False)
   test_score = r2_score(y_test, y_pred)
   ```

#### 3. **Logging Metrics and Tags with MLflow**
- **Logging Metrics**:
   ```python
   mlflow.log_metric('Train_R2_score', training_score)
   mlflow.log_metric('Test_R2_score', test_score)
   mlflow.log_metric('Test_MAE', mean_abs_error)
   mlflow.log_metric('Test_RMSE', root_mean_sq_error)
   ```
- **Setting Tags**:
   ```python
   mlflow.set_tag('Regressor', 'Simple Linear Regression Model')
   ```

#### 4. **Reviewing Run in MLflow UI**
- After running the code, you can check the MLflow UI to see the logged metrics and tags:
   - Metrics include values like `Test_MAE`, `Test_R2_score`, etc.
   - Tags show information about the model type.

#### 5. **Querying Metrics and Parameters**
- Use `MlflowClient` to retrieve logged metrics and parameters:
   ```python
   client = mlflow.tracking.MlflowClient()
   run_data = client.get_run(lr_run.info.run_id)
   print('Model Parameters', run_data.data.params)
   print('Metrics', run_data.data.metrics)
   ```

#### 6. **Transitioning to a More Complex Model**
Next, you can move on to a more complex model, like Multiple Linear Regression:
- **Logging Artifacts**:
   ```python
   mlflow.log_figure(fig5, 'correlation_heatmap.png')
   mlflow.log_artifact("features.txt")
   ```
- **Fitting the Multiple Linear Regression Model**:
   - Similar steps as before, but now use all relevant features.
- **Logging Model Parameters**:
   ```python
   params_reg = lr_model.get_params()
   mlflow.log_params(params_reg)
   ```

#### 7. **Final Steps and UI Review**
- Once the run is completed, check the UI again:
   - Confirm that the new run has all metrics, parameters, and artifacts logged correctly.
   - Metrics and parameters are displayed alongside any artifacts saved during the run.

### Polynomial Regression

1. **Define Polynomial Degree:**
   - Set the polynomial degree:
     ```python
     degree = 2
     ```

2. **Instantiate PolynomialFeatures:**
   - Create a PolynomialFeatures object:
     ```python
     poly = PolynomialFeatures(degree=degree)
     ```

3. **Transform Training and Test Data:**
   - Fit and transform training data:
     ```python
     poly_features_train = poly.fit_transform(X_train)
     ```
   - Transform test data:
     ```python
     poly_features_test = poly.transform(X_test)
     ```

4. **Fit Linear Regression Model:**
   - Create and fit the model:
     ```python
     polylr_model = LinearRegression()
     polylr_model.fit(poly_features_train, y_train)
     ```

5. **Make Predictions:**
   - Predict using the fitted model:
     ```python
     y_pred = polylr_model.predict(poly_features_test)
     ```

6. **Calculate Metrics:**
   - Calculate performance metrics:
     ```python
     training_score = polylr_model.score(poly_features_train, y_train)
     mean_abs_error = mean_absolute_error(y_test, y_pred)
     root_mean_sq_error = mean_squared_error(y_test, y_pred, squared=False)
     test_score = r2_score(y_test, y_pred)
     ```

7. **Log Parameters and Metrics with MLflow:**
   - Log polynomial degree:
     ```python
     mlflow.log_param('Degree of polynomial', degree)
     ```
   - Log metrics:
     ```python
     metrics = {
         'Train_R2_score': training_score,
         'Test_R2_score': test_score,
         'Test_MAE': mean_abs_error,
         'Test_RMSE': root_mean_sq_error
     }
     mlflow.log_metrics(metrics)
     ```
   - Set a tag for the model:
     ```python
     mlflow.set_tag('Regressor', 'Polynomial Regression Model with degree 2')
     ```

### Random Forest Regression

1. **Instantiate Random Forest Regressor:**
   - Create the model:
     ```python
     rf_model = RandomForestRegressor()
     ```

2. **Fit Model:**
   - Fit the model on training data:
     ```python
     rf_model.fit(X_train, y_train)
     ```

3. **Log Model Parameters:**
   - Get and log parameters:
     ```python
     params_reg = rf_model.get_params()
     mlflow.log_params(params_reg)
     ```

### Tuned Random Forest Regression

1. **Define Tuned Parameters:**
   - Set specific values for parameters:
     ```python
     n_estimators = 200
     max_depth = 10
     min_samples_split = 5
     min_samples_leaf = 2
     ```

2. **Log Tuned Parameters:**
   - Create parameters dictionary and log:
     ```python
     params = {
         'n_estimators': n_estimators,
         'max_depth': max_depth,
         'min_samples_split': min_samples_split,
         'min_samples_leaf': min_samples_leaf
     }
     mlflow.log_params(params)
     ```

3. **Log Metrics:**
   - Log metrics similarly to previous examples:
     ```python
     metrics = {
         'Train_R2_score': training_score,
         'Test_R2_score': test_score,
         'Test_MAE': mean_abs_error,
         'Test_RMSE': root_mean_sq_error
     }
     mlflow.log_metrics(metrics)
     ```

### Evaluating Model Performance with MLflow

1. **Overview of Runs:**
   - Multiple models date:
     - Random Forest Regression (tuned and default params)
     - Polynomial Regression
     - Multiple Linear Regression
     - Simple Linear Regression

2. **Using MLflow to Evaluate Models:**
   - Navigate to the MLflow UI.
   - Access the **Experiments** tab, specifically the `kc_house_price_prediction` experiment.
   - Customize displayed metrics by clicking the **Columns** button to include:
     - Attributes
     - Metrics
     - Parameters
     - Tags

3. **Sorting Models:**
   - Use the **Sort** feature to order runs:
     - Initially sorts by creation time.
     - Sort by `Train_R2_score` in descending order to identify the best model:
       - Highest `Train_R2_score`: Random Forest Regression (default params) with 0.983.
     - Change sorting to `Test_R2_score`:
       - Best `Test_R2_score`: Random Forest Regression (default params) with 0.872.

4. **Programmatic Evaluation:**
   - Use `mlflow.search_runs` to retrieve and sort runs programmatically:
     ```python
     df_run_metrics = mlflow.search_runs(
         [experiment.experiment_id],
         order_by=['metrics.Test_R2_score DESC']
     )
     ```

5. **Deleting Runs:**
   - Identify a run to delete:
     ```python
     run_id_for_delete = df_run_metrics.loc[5, 'run_id']
     ```
   - Delete the specified run:
     ```python
     mlflow.delete_run(run_id_for_delete)
     ```
   - Verify deletion by re-running:
     ```python
     df_run_metrics = mlflow.search_runs([experiment.experiment_id])
     ```

6. **Filtering Runs:**
   - Search runs based on specific criteria:
     ```python
     df_run_metrics = mlflow.search_runs(
         [experiment.experiment_id],
         filter_string='metrics.Test_R2_score > 0.8',
         order_by=['metrics.Test_R2_score DESC']
     )
     ```
   - Resulting DataFrame displays only runs satisfying the criterion.

### Key Functionalities
- **Sort and Search:** Efficiently identify the best-performing models based on shared metrics.
- **Programmatic Access:** Use MLflow APIs for automation in model selection and management.
- **Manage Runs:** Delete unnecessary runs and filter based on performance metrics to streamline experiments.

### Recap of Key Concepts on Autologging in MLflow

1. **Autologging Overview:**
   - Autologging is a feature in MLflow that automatically tracks parameters, metrics, and artifacts for models without requiring explicit logging commands.
   - It operates by attaching function hooks to important function invocations in Scikit-learn.

2. **Quirks of Autologging:**
   - **Test Metrics Not Logged:** Any test metrics calculated after importing functions will not be logged unless those functions are re-imported after enabling autologging.
   - **Schema Warning:** If the inferred model signature includes integer types, it may cause issues during inference when dealing with missing values, leading to schema enforcement errors.

3. **Exploring Logged Information in MLflow UI:**
   - In the MLflow UI, navigate to the relevant experiment and select the most recent run, which includes the autologged details.
   - **Parameters:** A comprehensive list of parameters used in the model (17 total for the Random Forest Regressor).
   - **Metrics:** Includes 6 training metrics, but none of the test metrics were logged due to the quirks mentioned.
   - **Tags:** Three tags displayed, with one explicitly set by the user and two autologged.
   - **Artifacts:** The model and its metadata are stored, including files like `MLmodel`, `conda.yaml`, and `model.pkl`.

4. **Understanding Artifacts:**
   - The model artifact directory includes necessary files for model deployment and inference.
   - The center pane offers code snippets for making predictions using both Spark and Pandas DataFrames, showing how the model can be serialized and utilized.

5. **Model Inputs:**
   - MLflow has inferred the model’s input signature, showing the expected input types. Most inputs are of type long, which relates to the earlier schema warning.

6. **Next Steps:**
   - Click through the model directory in the MLflow UI to explore individual files, which will help understand how MLflow organizes model artifacts and metadata.
   - Address the schema warning by adjusting data types or ensuring that input data used for training includes possible missing values.

### Continuation of Exploring Model Artifacts in MLflow

Let's dive deeper into the details of the model artifacts logged by MLflow during our previous session, specifically focusing on the contents of the model directory and its files.

1. **Model Directory Overview:**
   - The model directory contains several key files:
     - `MLmodel`
     - `conda.yaml`
     - `model.pkl`
     - `python_env.yaml`
     - `requirements.txt`
     - `estimator.html`
     - `metric_info.json`

2. **Key Files Explained:**
   - **model.pkl:** This is the serialized version of our model created using the Python `pickle` library. It's a standard format for saving Python objects, particularly machine learning models.
   
   - **MLmodel:** This file describes how to use the model. It includes:
     - **Flavors:** The model supports both `python_function` and `sklearn`, indicating that it can be invoked as a Python function or as part of an sklearn pipeline.
     - **Environment Links:** References to the `conda.yaml` and `python_env.yaml` files, detailing the environments needed for the model.
     - **Signature:** Inferred input and output specifications, which is where the earlier warning stemmed from, particularly the use of `long` types for many inputs.

3. **Environment Configuration Files:**
   - **conda.yaml:** This file lists the dependencies required to run the model in a Conda environment, including any necessary libraries under the `pip` section.
   - **python_env.yaml:** Similar to `conda.yaml`, but this one details the setup needed for a virtual environment, specifying Python and package versions.

4. **Requirements File:**
   - **requirements.txt:** This file contains a list of libraries and their version numbers, mirroring the libraries in the `pip` section of `conda.yaml`. It's a standard format for Python projects.

5. **Additional Files:**
   - **estimator.html:** This file provides a user-friendly view of the model's parameters, such as `max_depth`, `min_samples_leaf`, and the number of estimators for the Random Forest Regressor.
   - **metric_info.json:** This file provides context for the logged metrics. In our case, it confirmed that only training metrics were logged, specifically detailing the scoring on `X_train` and `y_train`.

6. **Next Steps:**
   - With this thorough understanding of the logged artifacts, we can now focus on tying up loose ends, such as addressing the test metric logging issue discussed earlier.
   - In the next demo, we’ll look into explicitly logging test metrics and signatures to avoid the pitfalls experienced with autologging.

### Addressing Loose Ends in MLflow Model Logging

In this demo, we'll tackle two key issues we identified in our previous session: the warning related to data types in our input features and the omission of test metrics during autologging.

#### 1. Fixing the Data Type Warning

The warning stemmed from our input data being of type `int64`, which was inferred as `long` during model training. This can lead to issues at inference time, especially if any values are missing. To resolve this, we’ll convert the relevant columns to `float64`.

**Steps to Convert Data Types:**
- First, we check the current data types of our DataFrame using `house_price_df.data.info()`.
- Next, we identify the integer-type columns that need conversion.
- We loop through these columns and explicitly convert each to `float64` using the `.astype(float)` method.

Here’s how the code looks:

```python
# Checking current data types
house_price_df.data.info()

# List of integer-type columns
int_columns = ['bedrooms', 'sqft_living', 'sqft_lot', 'waterfront', 'view', 
               'condition', 'grade', 'sqft_basement', 'lat', 'long', 
               'sqft_lot15', 'age', 'renovation_age']

# Convert each integer column to float
for col in int_columns:
    house_price_df.data[col] = house_price_df.data[col].astype(float)

# Verify the conversion
house_price_df.data.info()
```

After running this code, we should no longer see the warning when training the model.

#### 2. Logging Test Metrics

Next, we’ll ensure that test metrics are logged by re-importing the necessary metric functions after enabling autologging. This way, MLflow will instrument these functions to log metrics properly.

**Steps to Log Test Metrics:**
- First, we enable autologging with `mlflow.sklearn.autolog()`.
- Next, we import the necessary metric functions after enabling autologging.

Here’s the relevant code snippet:

```python
# Enable autologging
mlflow.sklearn.autolog()

# Import metric functions
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Start a new MLflow run
with mlflow.start_run(run_name='Random Forest Regression tuned params and metrics autologged'):
    # Calculate test metrics
    mean_abs_error = mean_absolute_error(y_test, y_pred)
    root_mean_sq_error = mean_squared_error(y_test, y_pred, squared=False)
    test_score = r2_score(y_test, y_pred)

    # Log a tag
    mlflow.set_tag('Regressor', 'RF tuned parameters and autologged metrics')
```

After executing this code, we can check the MLflow UI to verify the successful logging of test metrics.

#### 3. Verifying Changes in MLflow UI

Upon switching to the MLflow UI:
- We can see that the latest run is at the top of the list.
- Clicking into that run will reveal an increased number of logged metrics, now totaling 8, which includes both training and test metrics.

**Metrics Recorded:**
- The test metrics we should see are:
  - `mean_absolute_error_X_test`
  - `mean_squared_error_X_test`
  - `r2_score_X_test`

### Comparing Model Performance Using MLflow UI

In this demo, we will leverage MLflow's UI to compare the performance of two models across various attributes. This is a powerful way to visualize how different parameters and metrics influence model outcomes. Let’s get started!

#### Step 1: Accessing the Experiment Runs

First, navigate back to the Experiments tab by clicking on the experiment name, `kc_house_price_prediction`. Here, you'll see details for all matching runs. Currently, we have a total of 10 runs displayed.

**Visual Elements:**
- **Checkbox Selection:** You can select individual runs by clicking the checkboxes next to them. 
- **Comparison Buttons:** Once you select runs, new options like Rename, Delete, and Compare become available.

#### Step 2: Selecting Runs for Comparison

To compare models, select the following runs:
1. **Random Forest Regression with Default Params**
2. **Random Forest Regression with Tuned Params**

Once both runs are selected, click on the **Compare** button to access the comparison interface.

#### Step 3: Exploring the Comparing Runs UI

You will be taken to the **Comparing Runs** interface, which may take a bit of getting used to. This UI is quite informative, allowing you to visualize and understand the differences between the selected runs.

**Visualizations Section:**
- **Tabs Available:** You have access to several visualization options: Parallel Coordinates Plot, Scatter Plot, Box Plot, and Contour Plot.

#### Step 4: Parallel Coordinates Plot

Start with the **Parallel Coordinates Plot** to understand parameter and metric relationships:
- **Run Details:** Here, you’ll see two columns corresponding to the two selected runs.
- **Parameters Overview:** The parameters displayed will show values for both models. If you want to focus only on differences, use the **Show diff only** slider.

**Example Parameter Differences:**
- **n_estimators:** The default model uses 100, while the tuned model uses 200.
- **max_depth:** The default model is `None`, whereas the tuned model has it set to 10.

**Metrics Comparison:**
- Check the **Train_R2_score** and **Test_R2_score**. For instance, the default model has a higher Train_R2_score (0.983) compared to the tuned model (0.929).

#### Step 5: Customizing the Parallel Coordinates Plot

You can customize the Parallel Coordinates Plot:
- **Select Parameters:** Choose `n_estimators` and `max_depth`.
- **Select Metrics:** Add `Train_R2_score` and `Test_R2_score`.

This visualization connects parameter settings to their respective scores, showing clear paths for both runs.

#### Step 6: Analyzing the Scatter Plot

Switch to the **Scatter Plot** for a more intuitive comparison:
- **X-axis:** Set this to `n_estimators`.
- **Y-axis:** Set this to `Test_MAE`.

The scatter plot will show two points representing the two runs, allowing you to visualize the relationship between the number of estimators and the Test Mean Absolute Error (MAE).
