# Creating Time-series Models & Evaluating Models

### MLflow Integration with Prophet for Time Series Forecasting

**Prophet Overview**
- Prophet is a time series forecasting package developed by Meta (formerly Facebook) and open-sourced in 2017.

**Setup and Installation**
1. **Install Required Libraries**:
   ```python
   pip install -U numpy
   pip install -U kaleido
   pip install plotly
   pip install prophet
   pip install nbformat
   ```

2. **Standard Imports**:
   ```python
   import pandas as pd
   import numpy as np
   import matplotlib.pyplot as plt
   from sklearn.model_selection import train_test_split
   ```

**Load and Prepare Data**
1. **Read Gold Prices Dataset**:
   ```python
   gold_price_data = pd.read_csv('datasets/gold.csv')
   ```

2. **Inspect Data**:
   ```python
   gold_price_data.head()
   gold_price_data.tail()
   gold_price_data.info()
   ```

3. **Data Cleaning**:
   - Drop unnecessary columns:
     ```python
     gold_price_data = gold_price_data.drop(columns=['Open', 'High', 'Low', 'Volume', 'Currency'])
     ```
   - Convert 'Date' column to datetime:
     ```python
     gold_price_data['Date'] = pd.to_datetime(gold_price_data['Date'], format='%Y-%m-%d')
     ```

**Visualize Data**
- Create an interactive line plot of gold prices:
  ```python
  import plotly.express as px
  fig = px.line(gold_price_data, x='Date', y='Close')
  fig.show()
  ```

**MLflow Setup**
1. **Import MLflow**:
   ```python
   import mlflow
   mlflow.get_tracking_uri()
   ```

2. **Create and Set Experiment**:
   ```python
   mlflow.create_experiment(name='gold_price_forecasting')
   mlflow.set_experiment(experiment_name='gold_price_forecasting')
   ```

**Prepare Data for Prophet**
1. **Rename Columns**:
   ```python
   gold_price_data = gold_price_data.rename(columns={'Date': 'ds', 'Close': 'y'})
   ```

**Prophet Model Setup**
1. **Import Prophet and Related Functions**:
   ```python
   from prophet import Prophet
   from prophet.diagnostics import cross_validation, performance_metrics
   from mlflow.models.signature import infer_signature
   ```

2. **Start MLflow Run and Fit Model**:
   ```python
   with mlflow.start_run(run_name='Price forecasting using Prophet') as run1:
       prophet_model = Prophet()
       prophet_model.fit(gold_price_data)
   ```

3. **Log Model Parameters**:
   ```python
   model_params = {name: value for name, value in vars(prophet_model).items() if np.isscalar(value)}
   mlflow.log_params(model_params)
   ```

**Make Forecasts**
1. **Create Future DataFrame**:
   ```python
   future_df = prophet_model.make_future_dataframe(periods=180)
   ```

2. **Predict Using Model**:
   ```python
   forecast = prophet_model.predict(future_df)
   ```

3. **Merge Forecast with Actual Data**:
   ```python
   actuals_pred_df = pd.merge(gold_price_data, forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']], on='ds')
   ```

**Next Steps**
- In the next demo, we will analyze the contents of `actuals_pred_df` and evaluate the accuracy of the forecasts.

### Forecasting Gold Prices with Prophet

#### 1. Forecasting Future Prices
- **Code**: `forecast = prophet_model.predict(future_df)`
- **Returned Columns**:
  - `yhat_lower`
  - `yhat_upper`
  - `yhat`
  - `ds`

#### 2. Merging Forecast with Actual Prices
- **Merging Code**:
  ```python
  actuals_pred_df = pd.merge(
      gold_price_data,
      forecast[['ds', 'yhat_lower', 'yhat_upper', 'yhat']],
      on='ds'
  )
  ```

#### 3. Printing Forecast Values
- **Code**: `print(actuals_pred_df.head(10))`

#### 4. Computing Error Metrics
- **Mean Absolute Percentage Error (MAPE)**:
  ```python
  mape = mean_absolute_percentage_error(
      actuals_pred_df['y'], 
      actuals_pred_df['yhat']
  )
  ```

- **Mean Absolute Error (MAE)**:
  ```python
  mae = mean_absolute_error(
      actuals_pred_df['y'], 
      actuals_pred_df['yhat']
  )
  ```

- **Root Mean Square Error (RMSE)**:
  ```python
  rmse = mean_squared_error(
      actuals_pred_df['y'], 
      actuals_pred_df['yhat'], 
      squared=False
  )
  ```

#### 5. Logging Metrics
- **Metrics Dictionary**:
  ```python
  metrics = {
      'mape': mape,
      'mae': mae,
      'rmse': rmse
  }
  ```

- **Log Metrics**: `mlflow.log_metrics(metrics)`

#### 6. Visualizing Forecast and Components
- **Plotting Forecast**:
  ```python
  fig1 = plot_plotly(prophet_model, forecast)
  ```

- **Plotting Seasonal Components**:
  ```python
  fig2 = plot_components_plotly(prophet_model, forecast)
  ```

- **Log Figures**:
  ```python
  mlflow.log_figure(fig1, 'forecast.jpeg')
  mlflow.log_figure(fig2, 'forecast_components.jpeg')
  ```

#### 7. Inferring Model Signature
- **Inference**:
  ```python
  signature = infer_signature(gold_price_data.drop(columns='y'), forecast)
  ```

- **Log Model**:
  ```python
  model_info = mlflow.prophet.log_model(
      prophet_model, 
      'price-forecasting-model', 
      signature=signature
  )
  ```

#### 8. Examining Logged Outputs
- **MLflow UI**:
  - Navigate to the **Experiments** tab to see logged parameters, metrics, and artifacts.

#### 9. Understanding Model Schema
- **Model Schema**:
  - Input: `ds` (datetime)
  - Outputs include: `trend`, `yhat_lower`, `yhat_upper`, and seasonal components.

#### 10. Visualization Insights
- **Forecast Visualization**:
  - Observed upward trends in gold prices with seasonal peaks.
  
- **Components Visualization**:
  - Annual seasonality peaks in February and September; weekly trends highest at the start and end of the week.

#### 11. Interactive Visualization
- **Interactive Display in Jupyter**:
  ```python
  fig1.show()
  fig2.show()
  ```

- Note: Recent updates may have affected interactivity in the MLflow UI.

### Evaluating Forecast Accuracy with Prophet

**1. Setting Up Test Dates**

Create a DataFrame for testing dates using `pd.date_range`:

```python
test_dates = pd.date_range(start='2022-09-03', end='2023-01-03', freq='D')
test_df = pd.Series(data=test_dates.values, name='ds').to_frame()
```

**2. Loading the Prophet Model**

Load the pre-trained Prophet model using MLflow:

```python
prophet_model_saved = mlflow.pyfunc.load_model(model_info.model_uri)
test_predictions = prophet_model_saved.predict(test_df)
```

**3. Understanding Test Predictions**

The predictions include several columns:

- `ds`: Dates
- `trend`: Predicted trend
- `yhat_lower` and `yhat_upper`: Lower and upper bounds of predictions
- Other terms (additive, weekly, annual, multiplicative)

**4. Cross-Validation with Prophet**

To assess the accuracy of the forecasts, use cross-validation. Begin by importing the necessary function:

```python
from prophet.plot import plot_cross_validation_metric
```

Start a new MLflow run and create the Prophet model:

```python
with mlflow.start_run(run_name='Price forecasting using Prophet with cross-validation') as run2:
    prophet_model = Prophet()
```

**5. Executing Cross-Validation**

Call the `cross_validation` function:

```python
cv_results = cross_validation(prophet_model, initial='2000 days', period='60 days', horizon='60 days')
```

**6. Understanding Cross-Validation Process**

- The initial model is trained on the first 2000 days.
- Predictions are made for the next 60 days (horizon).
- This process repeats, shifting the training window for each subsequent model.

**7. Evaluating Performance Metrics**

Define the metrics to evaluate:

```python
cv_metrics = ['mae', 'rmse', 'mape']
metrics_results = performance_metrics(cv_results, metrics=cv_metrics)
```

Average the metrics:

```python
average_metrics = metrics_results.loc[:, cv_metrics].mean(axis=0).to_dict()
```

**8. Visualizing Performance Metrics**

Create a plot for the Mean Absolute Percentage Error (MAPE):

```python
fig = plot_cross_validation_metric(cv_results, metric='mape')
mlflow.log_figure(fig, 'forecast_errors.png')
```

**9. Results Summary**

- The MAPE values increase with the forecast horizon:
  - At 7 days: ~7.4%
  - At 60 days: ~9.7%
  
**10. MLflow UI Overview**

In the MLflow UI, you can explore details such as Run ID, Parameters, Metrics, and Artifacts, confirming that the forecast errors have been logged successfully.

This structured approach helps in evaluating the performance of time-series forecasts using Prophet effectively.

### Model Evaluation and Validation with MLflow

**1. Import Libraries**

Begin with the necessary imports:

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
```

**2. Load Dataset**

Load the dataset into a pandas DataFrame:

```python
bike_purchase_data = pd.read_csv('datasets/bike_buyers.csv')
```

Display the first few rows to understand the structure:

```python
bike_purchase_data.head()
```

**3. Data Overview**

The DataFrame has 1000 rows and 13 columns. The target variable, "Purchased Bike," is categorical (Yes, No), while features include demographic details such as Marital Status, Gender, and Income:

```python
bike_purchase_data.shape
```

**4. Data Preprocessing**

- **Drop ID Column**:

```python
bike_purchase_data.drop(columns='ID', inplace=True)
```

- **Check for Missing Values**:

```python
bike_purchase_data.isnull().sum()
```

- **Handle Missing Values**: Fill numeric columns with the mean and categorical columns with the mode.

```python
for cols in ['Income', 'Children', 'Cars', 'Age']:
    bike_purchase_data[cols].fillna(bike_purchase_data[cols].mean(), inplace=True)

for cols in ['Marital Status', 'Gender', 'Home Owner']:
    bike_purchase_data[cols].fillna(bike_purchase_data[cols].mode()[0], inplace=True)
```

- **Verify Missing Values Handled**:

```python
sum(bike_purchase_data.isnull().sum())
```

- **Remove Duplicates**:

```python
bike_purchase_data = bike_purchase_data.drop_duplicates()
bike_purchase_data.shape
```

**5. Label Encoding Categorical Variables**

- **Encode Ordinal Column** ("Commute Distance") using a mapping dictionary:

```python
comm_dist_mapper = {'0-1 Miles': 0, '1-2 Miles': 1, '2-5 Miles': 2, '5-10 Miles': 3, '10+ Miles': 4}
bike_purchase_data['Commute Distance'] = bike_purchase_data['Commute Distance'].replace(comm_dist_mapper)
bike_purchase_data.sample(5)
```

- **Encode Target Variable** ("Purchased Bike"):

```python
label_mapper = {'No': 0, 'Yes': 1}
bike_purchase_data['Purchased Bike'] = bike_purchase_data['Purchased Bike'].replace(label_mapper)
bike_purchase_data.sample(5)
```

**6. One-Hot Encoding for Nominal Variables**

Use `pd.get_dummies` for nominal columns:

```python
bike_purchase_data = pd.get_dummies(bike_purchase_data,
                                     columns=['Marital Status', 'Gender', 'Education', 'Occupation', 'Home Owner', 'Region'],
                                     drop_first=True)
```

- **Sample Data After One-Hot Encoding**:

```python
bike_purchase_data.sample(5)
```

**7. Data Overview Post-Processing**

Verify the DataFrame structure after preprocessing and ensure all categorical variables are appropriately encoded. The dataset is now ready for model training and evaluation.

### Model Evaluation with MLflow

In this demo, we’ll continue from our preprocessed dataset and leverage MLflow's evaluation capabilities. Let's walk through the steps to set up and evaluate our logistic regression model.

**1. Inspect the Target Variable**

First, check the distribution of the target variable, "Purchased Bike":

```python
bike_purchase_data['Purchased Bike'].value_counts()
```

This confirms a balanced dataset, which is beneficial for our evaluation metrics.

**2. Split the Data**

Next, we split our data into training and testing sets:

```python
X = bike_purchase_data.drop(labels=['Purchased Bike'], axis=1)
y = bike_purchase_data['Purchased Bike']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=124)
```

We should check the shapes of our datasets:

```python
X_train.shape, y_train.shape, X_test.shape, y_test.shape
```

**3. Convert Data Types**

To avoid warnings when using MLflow, convert input columns to `float64`:

```python
X_train = X_train.astype('float64')
X_test = X_test.astype('float64')
```

**4. Set Up MLflow**

Import MLflow and set up the tracking URI:

```python
import mlflow
import mlflow.sklearn

mlflow.get_tracking_uri()
```

**5. Create and Set the Experiment**

Create an experiment for logging:

```python
experiment_id = mlflow.create_experiment('bike_purchase_prediction')
mlflow.set_experiment('bike_purchase_prediction')
```

**6. Model Training and Logging**

Now, let’s train a logistic regression model as our baseline:

```python
import xgboost
import shap
from mlflow.models.signature import infer_signature

with mlflow.start_run(run_name='LR model evaluation') as run:
    lr_model = LogisticRegression().fit(X_train, y_train)
    
    # Infer signature for model
    signature = infer_signature(X_train, lr_model.predict(X_train))
    
    # Prepare evaluation data
    eval_data = X_test.copy()
    eval_data['label'] = y_test
    
    # Log the model
    mlflow.sklearn.log_model(lr_model, 'log_reg_model', signature=signature)
    
    # Get the model URI
    model_uri = mlflow.get_artifact_uri('log_reg_model')
```

**7. Evaluate the Model**

Finally, use MLflow’s evaluate function to assess the model:

```python
result = mlflow.evaluate(
    model_uri,
    eval_data,
    targets='label',
    model_type='classifier',
    evaluators=['default']
)
```

### Key Points

- **Balanced Dataset**: The target variable is well-distributed, which is critical for reliable metric evaluation.
- **Data Splitting**: We use a typical 70-30 split for training and testing.
- **Model Logging**: The logistic regression model is logged along with its signature, which facilitates easier future usage and understanding of inputs/outputs.
- **Evaluation Metrics**: The evaluation process automatically tailors metrics based on whether the model is binary or multiclass. The results will include confusion matrices, lift curves, and various performance metrics.

### Next Steps

In the next demo, we will explore the artifacts generated by the `mlflow.evaluate` function, examining the various metrics and visualizations it provides to better understand model performance.

### Running the Model Evaluation and Viewing Results in MLflow

Let's kick off the model evaluation we previously detailed, observe the output, and then transition to the MLflow UI to analyze the logged results.

**1. Start the Evaluation Run**

In the Jupyter Notebook, execute the code to start the run:

```python
with mlflow.start_run(run_name='LR model evaluation') as run:
    # Model training and evaluation steps...
```

As you run this, you might see some warnings about version mismatches, which are common when there are discrepancies between the `mlflow` version and the MLmodel configuration files. An INFO message will confirm that the model is being evaluated as a binary classifier with the positive label as 1 and the negative label as 0.

**2. Switch to the MLflow UI**

Next, open the MLflow UI to examine the experiment results. Refresh the page, navigate to the `bike_purchase_prediction` experiment, and you should see the logged run titled "LR model evaluation."

**3. Analyze the Metrics**

In the run details, focus on the Metrics section:

- You should see several standard metrics for a binary classifier, such as accuracy, precision, recall, F1 score, and ROC AUC.
- Notably, an accuracy score of **51.4%** suggests the model performs no better than random guessing on this balanced dataset.
- The F1 score is **0.329**, indicating significant room for improvement. Review the precision (0.507) and recall (0.243) metrics to assess the classifier's performance further.

**4. Review the Artifacts**

Next, let's dive into the Artifacts section:

- You'll find a folder named `log_reg_model`, which contains model-related files (like `MLmodel`, `conda.yaml`, `model.pkl`, etc.) and several `.png` files for visual evaluation.
- Start with the **Confusion Matrix**. This normalized matrix gives a clear picture of how well the model distinguishes between classes. The values indicate the percentage of true positive and true negative predictions, providing insights into areas where the model struggles.

**5. Inspect the Lift Curve**

The **Lift Curve** is another critical visual:

- It plots lift against the percentage of the sample, helping assess how well the model performs compared to a random guess.
- Notice the blue and orange lines (representing classes 0 and 1, respectively) and how they relate to the baseline. A good classifier would maintain higher lift for a more extended portion of the curve before declining.

**6. Further Visuals: Precision-Recall and ROC Curves**

In the next demo, we will examine additional visuals like the Precision-Recall Curve and the ROC Curve:

- **Precision-Recall Curve**: This will help us understand the trade-offs between precision and recall for different thresholds.
- **ROC Curve**: This curve will provide insight into the model's true positive rate against the false positive rate at various thresholds, with the area under the curve (AUC) serving as a measure of overall performance.

### Continuing Model Evaluation: Analyzing Precision-Recall and ROC Curves

In this demo, we’ll explore additional visuals related to our model evaluation, focusing on the Precision-Recall Curve and the ROC Curve, followed by the interpretation of SHAP values through various plots.

#### 1. Precision-Recall Curve

Let's start with the **Precision-Recall Curve**:

![Precision-Recall Curve](precision_recall_curve_plot.png)

- **Axes**: 
  - Y-axis represents Precision (for positive label: 1).
  - X-axis represents Recall.
  
- **Understanding the Curve**: 
  - Precision is calculated as $\text{TP} / (\text{TP} + \text{FP})$, while Recall is $\text{TP} / (\text{TP} + \text{FN})$.
  - The trade-off between precision and recall is evident in this curve. 
  - A higher threshold (towards 1) results in high precision but low recall, as fewer positive cases are identified.

- **Average Precision (AP)**: 
  - The AP value shown here is **0.534**, indicating the model's performance is just above random guessing (0.5).

#### 2. ROC Curve

Next, let’s look at the **ROC Curve**:

![ROC Curve](roc_curve_plot.png)

- **Axes**:
  - Y-axis represents the True Positive Rate (TPR).
  - X-axis represents the False Positive Rate (FPR).
  
- **Curve Interpretation**:
  - Ideally, we want to be as close to the top left corner as possible, where TPR is high and FPR is low.
  - The AUC (Area Under the Curve) here is **0.544**, again indicating performance slightly better than random guessing, which would be 0.5.

#### 3. SHAP Value Visualizations

Now, let’s explore the SHAP value visualizations, which provide insight into feature importance and impact on predictions.

##### a. SHAP Feature Importance Plot

![SHAP Feature Importance](shap_feature_importance_plot.png)

- **Y-axis**: Displays feature names (e.g., Income, Age, Children).
- **X-axis**: Measures the mean absolute SHAP value, indicating feature importance.
- **Key Takeaways**:
  - Income and Age are the most significant features, with mean SHAP values of +0.15 and +0.1, respectively.

##### b. SHAP Beeswarm Plot

![SHAP Beeswarm Plot](shap_beeswarm_plot.png)

- **Structure**: Each point represents a single prediction and its SHAP value, color-coded by feature value (from low to high).
- **Interpreting the Plot**:
  - The height of the swarm indicates the density of points at each SHAP value.
  - For Income, higher values correspond to positive SHAP values, suggesting a strong correlation between higher income and the likelihood of purchasing a motorcycle.
  - Conversely, lower income correlates with negative SHAP values, indicating a decreased likelihood of purchase.

##### c. SHAP Summary Plot

![SHAP Summary Plot](shap_summary_plot.png)

- This plot provides a similar overview to the beeswarm plot but may display the data differently. It offers insights into feature impact across the dataset.

#### Summary

In this segment, we've analyzed:

- **Precision-Recall and ROC Curves**: Key metrics highlighting model performance.
- **SHAP Visualizations**: These plots provide a deeper understanding of which features drive model predictions and how they impact individual predictions.

As we move forward, these insights will guide us in refining our model and making informed decisions about feature selection and model tuning.

Here’s the content reformatted for better learning, with unnecessary parts removed:

---

### Jupyter Notebook Steps for Model Evaluation

1. **Import Required Libraries**
   ```python
   from mlflow.models import MetricThreshold
   ```

2. **Create Candidate Model**
   ```python
   candidate_model = xgboost.XGBClassifier().fit(X_train, y_train)
   ```
   - Note: This is the first xgboost model; previous demos used logistic regression.

3. **Alternative Candidate Model (Commented Out)**
   ```python
   # candidate_model = xgboost.XGBClassifier(n_estimators=200, max_depth=10).fit(X_train, y_train)
   ```
   - The alternative model trains for longer with more trees.

4. **Set Baseline Model**
   ```python
   baseline_model = LogisticRegression().fit(X_train, y_train)
   ```

5. **Infer Model Signature**
   ```python
   signature = infer_signature(X_train, candidate_model.predict(X_train))
   ```

6. **Prepare Evaluation Data**
   ```python
   eval_data = X_test.copy()
   eval_data['label'] = y_test
   ```

7. **Define Metric Thresholds**
   ```python
   thresholds = {
       'f1_score': MetricThreshold(
           threshold=0.66,
           min_absolute_change=0.10,
           min_relative_change=0.10,
           greater_is_better=True,
       )
   }
   ```
   - **Key Metrics:**
     - `threshold`: Minimum f1_score required (0.66).
     - `min_absolute_change`: f1_score must improve by at least 0.1 over baseline.
     - `min_relative_change`: f1_score must be at least 10% better than baseline.

8. **Start MLflow Run**
   ```python
   with mlflow.start_run(run_name='XGBoost candidate model evaluation') as run2:
   ```

9. **Log Candidate Model**
   ```python
   candidate_model_uri = mlflow.sklearn.log_model(candidate_model, 'candidate_model', signature=signature).model_uri
   ```

10. **Log Baseline Model**
    ```python
    baseline_model_uri = mlflow.sklearn.log_model(baseline_model, 'baseline_model', signature=signature).model_uri
    ```

11. **Evaluate Models**
    ```python
    mlflow.evaluate(
        candidate_model_uri,
        eval_data,
        targets='label',
        model_type='classifier',
        validation_thresholds=thresholds,
        baseline_model=baseline_model_uri
    )
    ```

12. **Handle Evaluation Results**
    - If the candidate model fails to meet any criteria, an exception is raised:
      ```
      ModelValidationFailedException: Metric f1_score value threshold check failed: candidate model f1_score is 0.64.
      ```

13. **Switch to Alternative Candidate Model**
    - Uncomment and run the second candidate model to compare performance:
    ```python
    candidate_model = xgboost.XGBClassifier(n_estimators=200, max_depth=10).fit(X_train, y_train)
    ```

14. **Re-evaluate the Updated Model**
    - Successful evaluation indicated by:
      ```
      Model validation has passed.
      ```

15. **Check MLflow UI for Results**
    - Metrics like f1_score should exceed the threshold and show improvements over baseline.

16. **Artifacts Overview**
    - Review confusion matrix, lift curve, and SHAP plots for detailed insights on model performance.

### Key Findings
- **Model Performance:** The updated model surpasses the baseline and meets all validation criteria.
- **SHAP Analysis:** Discriminating features show clear separations, indicating better model interpretability.

--- 

This structure allows for easy navigation and understanding of the steps involved in model evaluation using MLflow.