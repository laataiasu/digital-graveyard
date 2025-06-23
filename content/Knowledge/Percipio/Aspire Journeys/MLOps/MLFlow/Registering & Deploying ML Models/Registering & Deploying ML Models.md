---
date: 2001-01-01
---

# Registering & Deploying ML Models

### Core Learning Content

#### Dataset and Libraries
- **Dataset**: Travel Churn Prediction from Kaggle, contains features such as Age, FrequentFlyer status, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, and BookedHotelOrNot. The target variable indicates customer churn (1 = churn, 0 = no churn).
- **Key Libraries**:
  - `pandas`, `numpy`, `seaborn`, `matplotlib.pyplot`
  - `sklearn` modules: `RandomForestClassifier`, `ColumnTransformer`, `Pipeline`, `SimpleImputer`, `StandardScaler`, `OneHotEncoder`, `train_test_split`, `LogisticRegression`

#### Data Loading
```python
travel_churn_data = pd.read_csv('./datasets/customer_travel.csv')
```

#### Exploratory Data Analysis
1. **Column Inspection**:
   ```python
   travel_churn_data.columns
   ```
2. **Class Distribution**:
   ```python
   sns.countplot(x='Target', data=travel_churn_data)
   ```
   - Observed: ~700 instances of Target = 0 (no churn) and ~200 instances of Target = 1 (churn).
3. **Boxplot Analysis**:
   ```python
   sns.boxplot(x='AnnualIncomeClass', y='Age', data=travel_churn_data)
   ```
   - Boxplot explains distribution and outliers in Age across income classes.

#### Data Preprocessing
1. **Label Encoding for Ordinal Variable**:
   - Encoding for `AnnualIncomeClass`:
   ```python
   mapper = {'Low income': 0, 'Middle Income': 1, 'High Income': 2}
   travel_churn_data['AnnualIncomeClass'] = travel_churn_data['AnnualIncomeClass'].replace(mapper)
   ```
2. **One-Hot Encoding for Nominal Variables**:
   - Identify categorical features:
   ```python
   categorical_features = ['FrequentFlyer', 'AccountSyncedToSocialMedia', 'BookedHotelOrNot']
   ```
   - Define preprocessing steps using `Pipeline` and `ColumnTransformer`:
   ```python
   categorical_transformer = Pipeline(steps=[('encoder', OneHotEncoder(handle_unknown='ignore', drop='first'))])
   preprocessor = ColumnTransformer(
       transformers=[("cat", categorical_transformer, categorical_features)],
       remainder=StandardScaler()
   )
   ```

#### Train-Test Split
- Separate features and target variable:
```python
X = travel_churn_data.drop(labels=['Target'], axis=1)
y = travel_churn_data['Target']
```
- Split the data:
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=124)
```
- Inspect the shape of training and testing sets:
```python
X_train.shape, X_test.shape
```
- Results: 763 rows in training data, 191 rows in testing data.

### Core Learning Content

#### Logging the Model with MLflow
1. **Setting Up Experiment**:
   - Import MLflow and set the experiment:
   ```python
   import mlflow
   mlflow.set_experiment(experiment_name='customer_churn_prediction')
   ```
   - Create the experiment in the MLflow UI, ensuring to specify an **Artifact Location** on the local file system to avoid exceptions.

2. **Confirming Tracking URI**:
   ```python
   mlflow.get_tracking_uri()
   ```

3. **Starting a Run**:
   - Import necessary metrics:
   ```python
   from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
   from mlflow.models.signature import infer_signature
   ```
   - Start the MLflow run:
   ```python
   with mlflow.start_run(run_name='logistic_model') as logistic_run:
   ```

#### Model Training
1. **Define the Model**:
   ```python
   lr_model = LogisticRegression()
   ```
2. **Create a Pipeline**:
   ```python
   pipe_lr = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', lr_model)])
   ```
3. **Fit the Model**:
   ```python
   pipe_lr.fit(X_train, y_train)
   ```

4. **Make Predictions**:
   ```python
   predictions = pipe_lr.predict(X_test)
   predictions_predict_prob = pipe_lr.predict_proba(X_test)
   ```

#### Model Evaluation
1. **Calculate Accuracy**:
   ```python
   train_accuracy_score = pipe_lr.score(X_train, y_train)
   test_accuracy_score = accuracy_score(y_test, predictions)
   ```

2. **Precision and Recall**:
   ```python
   test_precision_score = precision_score(y_test, predictions)
   test_recall_score = recall_score(y_test, predictions)
   ```
   - **Precision**: Proportion of true positive predictions among all positive predictions.
   - **Recall**: Proportion of true positive predictions among all actual positives.

3. **F1 Score**:
   ```python
   test_f1_score = f1_score(y_test, predictions)
   ```
   - **F1 Score**: Harmonic mean of precision and recall, useful for evaluating balance between them.

4. **AUC Score**:
   ```python
   auc_score = roc_auc_score(y_test, predictions_predict_prob[:, 1])
   ```
   - **AUC Score**: Measures model performance by calculating the area under the ROC curve.

#### Logging Model Parameters
1. **Extract and Log Parameters**:
   ```python
   model_params = lr_model.get_params()
   mlflow.log_params(model_params)
   ```

This structured approach ensures that we log our model effectively using MLflow while also evaluating its performance through key metrics.

### Summary of Logging a Model with MLflow

#### Continuing from Line 23: Logging Parameters and Metrics

1. **Extract Model Parameters**:
   ```python
   model_params = lr_model.get_params()
   ```
   - Log the parameters of the logistic regression model.
   ```python
   mlflow.log_params(model_params)
   ```

2. **Construct Metrics Dictionary**:
   - Create a dictionary containing all relevant training and testing metrics:
   ```python
   metrics = {
       'Train_accuracy_score': train_accuracy_score,
       'Test_accuracy_score': test_accuracy_score,
       'Test_precision_score': test_precision_score,
       'Test_recall_score': test_recall_score,
       'Test_f1_score': test_f1_score,
       'AUC_score': auc_score
   }
   ```
   - Log the metrics:
   ```python
   mlflow.log_metrics(metrics)
   ```

#### Logging the Model

1. **Import Necessary Classes**:
   ```python
   from mlflow.models.signature import ModelSignature
   from mlflow.types.schema import Schema, ColSpec
   ```

2. **Define Input and Output Schema**:
   - Construct the input schema:
   ```python
   input_schema = Schema([
       ColSpec('long', 'Age'),
       ColSpec('string', 'FrequentFlyer'),
       ColSpec('long', 'AnnualIncomeClass'),
       ColSpec('long', 'ServicesOpted'),
       ColSpec('string', 'AccountSyncedToSocialMedia'),
       ColSpec('string', 'BookedHotelOrNot')
   ])
   ```
   - Define the output schema:
   ```python
   output_schema = Schema([ColSpec('integer')])
   ```

3. **Create Model Signature**:
   ```python
   signature = ModelSignature(inputs=input_schema, outputs=output_schema)
   ```

4. **Log the Model**:
   - Finally, log the entire pipeline (which includes the logistic regression model):
   ```python
   mlflow.sklearn.log_model(
       pipe_lr,
       'preprocessing_pipeline_with_logistic_regression_model',
       signature=signature
   )
   ```

### Viewing Results in MLflow UI

1. **Check Logged Run**:
   - Navigate to the **customer_churn_prediction** experiment in the MLflow UI.
   - Refresh the page to see the latest run (e.g., `logistic_model`).

2. **Explore Parameters and Metrics**:
   - View the logged parameters (15 parameters related to the model).
   - Check metrics, particularly:
     - Test Accuracy: ~0.743
     - Test Precision: ~37.5%
     - Test Recall: ~21%
     - Test F1 Score: ~0.269
     - AUC Score: ~0.769

3. **Examine Artifacts**:
   - Click on the artifacts directory (`preprocessing_pipeline_with_logistic_regression_model`) to view:
     - Model schema
     - `MLmodel` file with input/output specifications
     - Model binary (`model.pkl`)
     - Environment specifications (`conda.yaml`, `requirements.txt`)

### Understanding Machine Learning Model Predictions and Explainability with SHAP

#### Importance of Model Explainability

In today’s landscape, understanding how machine learning models arrive at their predictions is critical, especially concerning issues of bias and transparency. Users need to grasp why a model made a specific prediction, which has led to increased focus on explainability methods, like SHAP (SHapley Additive exPlanations).

#### Overview of SHAP

SHAP provides insights into how each feature contributes to the model's predictions. By using principles from game theory, SHAP values quantify the importance of each feature for individual predictions, revealing both the direction (positive or negative impact) and magnitude of influence.

#### Integration of SHAP with MLflow

MLflow has integrated support for SHAP, which allows you to log and visualize model explanations efficiently. Here’s how we can leverage SHAP in our workflow:

1. **Installation**:
   ```python
   !pip install shap
   ```

2. **Logging SHAP Values**:
   - Start an MLflow run:
   ```python
   import mlflow.shap
   with mlflow.start_run(run_name='logistic_model_with_explanation') as logistic_run:
   ```
   - Use the preprocessor from your pipeline to transform your training data and log explanations:
   ```python
   observations = pipe_lr.named_steps['preprocessor'].transform(X_train)
   observations_asframe = pd.DataFrame(observations, columns=preprocessor.get_feature_names_out())
   mlflow.shap.log_explanation(pipe_lr.named_steps['classifier'].predict, observations_asframe)
   ```

3. **Calculating SHAP Values**:
   - The SHAP library computes values by considering different combinations of input features and how they affect predictions. It compares these variations to a base prediction, usually the average of the target variable.
   - The resulting SHAP values can indicate how each feature influences the output:
     - **Magnitude**: Importance of the feature.
     - **Sign**: Direction of influence.

#### Analyzing the Output in MLflow UI

After running the code, navigate to the MLflow UI to see the results:
- **Artifacts**: Check for the `model_explanations_shap` directory.
  - Files:
    - `base_values.npy`: Average prediction based on the target variable.
    - `shap_values.npy`: The SHAP values calculated for each input feature.
    - `summary_bar_plot.png`: A visual representation of the SHAP scores.

The bar chart typically shows which features had the most significant impact on predictions, helping to highlight areas of interest or concern.

#### Accessing SHAP Outputs in Python

To access and manipulate SHAP values programmatically:
1. Import necessary libraries:
   ```python
   import os
   from mlflow import MlflowClient
   ```
2. List artifacts and download them:
   ```python
   client = MlflowClient()
   artifact_path = 'model_explanations_shap'
   artifacts = client.list_artifacts(logistic_run.info.run_id, artifact_path)
   dst_path = mlflow.artifacts.download_artifacts(run_id=logistic_run.info.run_id)
   ```

3. Load and print the SHAP values:
   ```python
   base_values = np.load(os.path.join(dst_path, 'base_values.npy'))
   shap_values = np.load(os.path.join(dst_path, 'shap_values.npy'))
   print(base_values)
   print(shap_values)
   ```

### Conclusion

The integration of SHAP with MLflow enhances model transparency and accountability, allowing stakeholders to understand the reasoning behind predictions. As we advance, this capability will be essential for developing fair, unbiased AI systems. In the next session, we’ll explore candidate models with autolog features, building on this foundation of explainability.

### Adding Additional Runs to the Experiment

#### Logistic Model with Autologging

1. **Setup**
   - Enable autologging: `mlflow.sklearn.autolog()`
   - Re-import necessary functions:
     ```python
     from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
     ```
   - Start a new run:
     ```python
     with mlflow.start_run(run_name='logistic model with autologging'):
     ```

2. **Model Training**
   - Create and fit the logistic regression pipeline:
     ```python
     lr_model = LogisticRegression()
     pipe_lr = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', lr_model)])
     pipe_lr.fit(X_train, y_train)
     ```

3. **Predictions and Metrics**
   - Make predictions:
     ```python
     predictions = pipe_lr.predict(X_test)
     predictions_predict_prob = pipe_lr.predict_proba(X_test)
     ```
   - Calculate metrics:
     ```python
     test_accuracy_score = accuracy_score(y_test, predictions)
     test_precision_score = precision_score(y_test, predictions)
     test_recall_score = recall_score(y_test, predictions)
     test_f1_score = f1_score(y_test, predictions)
     ```
   - Log AUC score explicitly (not autologged):
     ```python
     auc_score = roc_auc_score(y_test, predictions_predict_prob[:, 1])
     mlflow.log_metric('AUC_score', auc_score)
     ```
   - Infer signature:
     ```python
     signature = infer_signature(X_train, pipe_lr.predict(X_train))
     ```

4. **MLflow UI**
   - Check the MLflow UI for run details:
     - 43 parameters and 12 metrics logged.
     - AUC score: 0.842.
     - Visualizations: training confusion matrix, precision-recall curve, ROC curve.

---

#### Additional Models

1. **Random Forest Model**
   - Enable autologging:
     ```python
     mlflow.sklearn.autolog()
     ```
   - Start a new run:
     ```python
     with mlflow.start_run(run_name='random forest model default parameters'):
     ```

2. **Support Vector Classifier**
   - Setup:
     ```python
     from sklearn.svm import SVC
     mlflow.sklearn.autolog()
     ```
   - Start run:
     ```python
     with mlflow.start_run(run_name='SVC model default parameters'):
     ```
   - Create and fit the SVC pipeline:
     ```python
     svc_model = SVC()
     pipe_svc = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', svc_model)])
     pipe_svc.fit(X_train, y_train)
     ```

3. **Gradient Boosting Classifier**
   - Setup:
     ```python
     from sklearn.ensemble import GradientBoostingClassifier
     mlflow.sklearn.autolog()
     ```
   - Start run:
     ```python
     with mlflow.start_run(run_name='gradient boosting model default parameters'):
     ```
   - Create and fit the Gradient Boosting pipeline:
     ```python
     gb_model = GradientBoostingClassifier()
     pipe_gb = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', gb_model)])
     pipe_gb.fit(X_train, y_train)
     ```

4. **Predictions and Metrics for Gradient Boosting**
   - Predictions:
     ```python
     predictions = pipe_gb.predict(X_test)
     predictions_predict_prob = pipe_gb.predict_proba(X_test)
     ```
   - Calculate and log metrics:
     ```python
     auc_score = roc_auc_score(y_test, predictions_predict_prob[:, 1])
     mlflow.log_metric('AUC_score', auc_score)
     ```

5. **Confirming Runs in MLflow UI**
   - Refresh to see all runs. Total: 6.

--- 

#### Next Steps
- In the next demo, compare the runs to identify the best candidate model for deployment.

### Comparing Models in MLflow

#### Overview of Runs
- Total Runs: 6 in the `customer_churn_prediction` experiment.
- Key metrics to compare: AUC_score, f1_score_X_test.

#### Customizing MLflow UI View
1. Click on **Columns** button.
2. Select **AUC_score** and **f1_score_X_test** from the drop-down.
3. Observe that:
   - **Highest AUC_score**: Gradient Boosting Model (0.939).
   - **Highest f1_score_X_test**: Gradient Boosting Model (0.658).
   - Some models lack certain metrics (e.g., SVC model has no AUC_score).

#### Comparing Selected Runs
1. Select multiple models (Gradient Boosting, SVC, Random Forest, Logistic Model).
2. Click on **Compare** to view the Parallel Coordinates Plot.
3. Simplify plot by showing only the **classifier** parameter and **training_score** metric.
   - **Training R²** values:
     - SVC: ~0.90
     - Random Forest: 0.95282 (highest)
     - Logistic Regression: 0.81913 (lowest)

4. Add **f1_score_X_test** and **accuracy_score_X_test** metrics.
   - Gradient Boosting ranks highest for f1_score (0.65823) and accuracy (85.864%).
   - Confirm model properties by inspecting parameters, metrics, and tags.

#### Promoting the Best Model Programmatically
1. Switch to Jupyter Notebook.
2. Instantiate MLflow client:
   ```python
   client = mlflow.tracking.MlflowClient()
   ```
3. Search experiments and print the list:
   ```python
   experiments_list = client.search_experiments()
   ```

4. Identify the `customer_churn_prediction` experiment:
   ```python
   experiment = mlflow.get_experiment_by_name(experiments_list[0].name)
   ```

5. Search for runs within this experiment, ordered by accuracy score:
   ```python
   df_run_metrics = mlflow.search_runs([experiment.experiment_id], order_by=['metrics.accuracy_score_X_test DESC'])
   ```

6. Access best run ID:
   ```python
   best_run_id = df_run_metrics.loc[0, 'run_id']
   ```

7. Verify best run ID in MLflow UI.

#### Loading the Best Model
1. Construct model URI using the best run ID:
   ```python
   model_uri = 'runs:/' + best_run_id + '/model'
   ```

2. Load the model:
   ```python
   import mlflow.sklearn
   best_model = mlflow.sklearn.load_model(model_uri=model_uri)
   ```

3. Confirm model details:
   - Displayed output confirms it's the GradientBoostingClassifier.

### Next Steps
- In the upcoming demo, ensure the loaded model produces results consistent with the original model from the run.

### Continuation: Registering and Accessing the Model in MLflow

#### Loading the Best Model
1. **Model Loading Confirmation**:
   - We have successfully loaded the `best_model` using the MLflow API, which matches our original model configuration.

2. **Making Predictions**:
   ```python
   predictions_loaded = best_model.predict(X_test)
   ```
   - This generates predictions from the loaded model.

3. **Comparing Predictions**:
   ```python
   predictions_original = pipe_gb.predict(X_test)
   assert(np.array_equal(predictions_loaded, predictions_original))
   ```
   - The predictions from both models are identical, confirming the loaded model's accuracy.

#### Registering the Model
1. **Registering the Model**:
   - Model registration involves transitioning from the tracking phase to the model registry.
   ```python
   model_name = 'churn_prediction_model'
   model_version = mlflow.register_model(f'runs:/{best_run_id}/model', model_name)
   ```
   - Successfully registered the model as **Version 1**.

2. **Significance of Registration**:
   - Registration provides a unique name and allows for version control and model staging (Production, Staging, Archived).

3. **Model URI Format**:
   - Post-registration, the model URI changes to a more user-friendly format:
   ```python
   model_uri = f'models:/{model_name}/{stage}'
   ```

#### Exploring the MLflow UI
1. **Checking the Model Registration**:
   - Upon switching to the MLflow UI, we observe that the model has been successfully registered under the **Models** tab.
   - The registered model, `churn_prediction_model`, displays its version and registration date.

2. **Viewing Model Details**:
   - Clicking into the model reveals details like inputs, outputs, and version history.

3. **Staging the Model**:
   - We transition the model from **None** to **Staging**, confirming this change in the UI.
   - This transition enables us to manage the model lifecycle effectively.

#### Demoting the Model
1. **Changing Model Stage**:
   - We can demote the model from Staging back to None without any prompts from MLflow, showcasing its flexibility.

#### Making Predictions with the Registered Model
1. **Accessing the Model in Jupyter**:
   - Now, we can use the registered model for predictions.
   ```python
   # Example code to load the registered model
   model_uri = 'models:/churn_prediction_model/Stage'
   best_model = mlflow.sklearn.load_model(model_uri)
   predictions_from_registered_model = best_model.predict(X_test)
   ```

2. **Conclusion**:
   - We have effectively registered the best-performing model, verified its predictions, and managed its lifecycle using MLflow’s Model Registry. The next steps could involve deploying the model for production use or further evaluation based on updated data.

### Transitioning the Model to Production and Loading with MLflow

#### 1. Transitioning Model Stage
- After successfully registering the model, we used the `MlflowClient` to transition the model from **Staging** to **Production**.
  ```python
  from mlflow.tracking import MlflowClient
  
  client = MlflowClient()
  client.transition_model_version_stage(
      name=model_name,
      version=model_version.version,
      stage='Production'
  )
  ```
- The model's stage is now confirmed as **Production**, reflecting this change in the MLflow UI.

#### 2. Loading the Model
- Next, we load the model using the `mlflow.pyfunc.load_model` method, a different approach compared to the earlier use of `mlflow.sklearn.load_model`.
  ```python
  model_name = 'churn_prediction_model'
  stage = 'Production'
  loaded_model = mlflow.pyfunc.load_model(
      model_uri=f'models:/{model_name}/{stage}'
  )
  ```
- The F1 score is calculated:
  ```python
  print(f'F1 score: {f1_score(y_test, loaded_model.predict(X_test))}')
  ```

#### 3. Handling the Warning
- Upon loading the model, a warning appears indicating a mismatch between the MLflow version in the environment and the version specified in the model's dependencies:
  ```
  mlflow.pyfunc: Detected one or more mismatches between the model's dependencies and the current Python environment.
  ```
- The warning highlights that the current version is **2.3.2** while the model specifies **2.3**.

#### 4. Investigating the Warning
- To understand the warning, we checked the **MLflow UI**:
  - The model's **MLmodel** file shows version **2.3.2**.
  - However, the **conda.yaml** and **requirements.txt** files reference version **2.3**.
  
- This discrepancy arises because the `python_function` flavor relies on the `conda.yaml` file for its dependencies, while the `sklearn` flavor does not. Hence, the warning is specific to `mlflow.pyfunc.load_model`.

#### 5. Verifying the F1 Score
- We confirmed the F1 score obtained from the loaded model matches the best score logged during the original run:
  ```python
  best_f1_score = df_run_metrics.loc[0, 'metrics.f1_score_X_test']
  ```
- The F1 score is validated as **0.6582**, ensuring consistency between the two model loading methods.

### Registering a New Model Version Based on Recall Score

#### 1. Finding the Best Model by Recall
- We start by searching for the best run based on the recall score using `mlflow.search_runs`, ordering by the recall score in descending order.
  ```python
  best_run_recall_metrics = mlflow.search_runs(
      [experiment.experiment_id], 
      order_by=['metrics.recall_score_X_test DESC']
  )
  ```

#### 2. Extracting Details
- We print out details of the best run:
  ```python
  print('Classifier_name:', best_run_recall_metrics.loc[0, 'tags.Classifier'])
  print('Run_name:', best_run_recall_metrics.loc[0, 'tags.mlflow.runName'])
  print('Best recall score:', best_run_recall_metrics.loc[0, 'metrics.recall_score_X_test'])
  ```

#### 3. Registering the Model
- Using the run ID of the best recall model, we register this model with `mlflow.register_model`.
  ```python
  best_recall_model = mlflow.register_model(
      f"runs:/{best_run_recall_metrics.loc[0, 'run_id']}/model", 
      model_name
  )
  ```
- This successfully registers the model as version 2 of `churn_prediction_model`.

#### 4. Updating Model Descriptions
- We then programmatically update the descriptions for both versions of the model. For version 2 (the new model):
  ```python
  client.update_model_version(
      name='churn_prediction_model',
      version=2,
      description='This model had the best recall score'
  )
  ```
- For version 1 (the previous model):
  ```python
  client.update_model_version(
      name='churn_prediction_model',
      version=1,
      description='This model had the best accuracy score'
  )
  ```

#### 5. Verifying in MLflow UI
- In the MLflow UI, we confirm that:
  - Version 1 has a description of "This model had the best accuracy score" and is in Production.
  - Version 2 has a description of "This model had the best recall score" and is in None stage.

#### 6. Transitioning Model Stages
- We transition Version 1 to Archived in the UI.
- Next, we programmatically promote Version 2 to Production:
  ```python
  client.transition_model_version_stage(
      name=model_name,
      version=2,
      stage='Production'
  )
  ```

#### 7. Final State in MLflow UI
- After executing the transition, we verify in the MLflow UI:
  - Version 2 is now in Production.
  - Version 1 has been successfully archived.

### Making Inferences with the MLflow Model

#### 1. Getting the Run ID
- We start by retrieving the run ID of the deployed model from the best recall metrics DataFrame.
  ```python
  run_id = best_run_recall_metrics.loc[0, 'run_id']
  ```

#### 2. Serving the Model
- We switch to the terminal and navigate to the MLflow directory. We will use the `mlflow models serve` command to launch a web server.
  ```bash
  mlflow models serve -m runs:/<run_id>/model --env-manager local --host 127.0.0.1:1234
  ```
- Replace `<run_id>` with the actual run ID obtained from Jupyter. This command serves the model on localhost at port 1234.

#### 3. Observing Server Logs
- Once the server is running, we see info messages indicating the backend flavor (python_function) and any warnings related to environment mismatches. The server is now ready to accept requests.

#### 4. Making Predictions with `curl`
- We open a new terminal window to send requests to our model using `curl`.
- The first prediction request is structured as follows:
  ```bash
  curl -X POST -H "Content-Type: application/json" --data '{"dataframe_split": {"columns":["Age","FrequentFlyer","AnnualIncomeClass","ServicesOpted","AccountSyncedToSocialMedia","BookedHotelOrNot"],"data":[[35, "Yes", 2, 1, "No", "No"]]}}' http://127.0.0.1:1234/invocations
  ```
- This command sends a JSON payload with features for a customer, predicting whether they will churn.

#### 5. Interpreting Predictions
- The response to the first prediction is a JSON fragment indicating churn:
  ```json
  [1]
  ```
  - Here, `1` signifies that the customer is expected to churn.

#### 6. Making Another Prediction
- We change the input values for another prediction:
  ```bash
  curl -X POST -H "Content-Type: application/json" --data '{"dataframe_split": {"columns":["Age","FrequentFlyer","AnnualIncomeClass","ServicesOpted","AccountSyncedToSocialMedia","BookedHotelOrNot"],"data":[[23, "No", 1, 0, "No", "No"]]}}' http://127.0.0.1:1234/invocations
  ```
- In this case, the model predicts:
  ```json
  [0]
  ```
  - Here, `0` indicates that the customer will not churn.

### Summary
- We successfully deployed the `churn_prediction_model` to a local endpoint using MLflow's serving capabilities.
- Using `curl`, we sent JSON-formatted data to the model, receiving predictions based on different inputs.
- In the next demo, we'll explore deploying this model to Microsoft Azure, taking our deployment further into a cloud environment.

### Deploying MLflow Model to Azure

#### 1. **Initial Setup in Azure Portal**
- Start by logging into the Azure portal at [portal.azure.com](https://portal.azure.com).
- Create a new resource group for the demo:
  - Navigate to "Resource groups" and click on "+ Create."
  - Name the resource group (e.g., `loony-mlflow-rg`) and select the region (East US).
- Create an Azure Machine Learning workspace:
  - In the resource group, click "Create resources" and find "Azure Machine Learning."
  - Fill in the workspace details (name, region) and complete the setup.

#### 2. **Understanding Azure Structure**
- Azure accounts can have multiple subscriptions, each containing resource groups for organization.
- The first workspace creation also creates a default resource group necessary for future programmatic creations.

#### 3. **Gather Required Information**
- Obtain the subscription ID:
  - Navigate to "Subscriptions" and find the subscription ID.
- Copy this ID for use in your Jupyter notebook.

#### 4. **Setting Up Jupyter Notebook**
- Open the Jupyter notebook and ensure required libraries are installed:
  ```python
  pip install azureml-core
  pip install azure-ai-ml azure-identity
  pip install azureml-mlflow
  ```
- Use the copied subscription ID to create the Azure Machine Learning workspace programmatically:
  ```python
  from azureml.core import Workspace

  ws = Workspace.create(
      name='loony-mlflow-wsp',
      subscription_id='YOUR_SUBSCRIPTION_ID',
      resource_group='loony-mlflow-rg',
      create_resource_group=False,
      location='eastus'
  )
  ```

#### 5. **Verifying Workspace Creation**
- After running the workspace creation code, check Azure portal:
  - Go to the resource group and ensure `loony-mlflow-wsp` is listed.

#### 6. **Registering the MLflow Model**
- In MLflow, navigate to the desired model's run and copy the model directory path.
- Register the model with Azure:
  ```python
  from azureml.core.model import Model

  model_path = 'FULL_MODEL_PATH'  # Use the copied path
  Model.register(
      workspace=ws,
      model_path=model_path,
      model_name='churn-prediction-model'
  )
  ```

#### 7. **Confirming Model Registration**
- Go back to Azure Machine Learning Studio and check the "Models" section:
  - You should see `churn-prediction-model` listed, confirming successful registration.
  - Under the model's details, check artifacts to verify the model files (e.g., `conda.yaml`, `MLmodel`) are present.

#### 8. **Next Steps**
- While the model is registered, it is not yet deployed. The next step will be to create an endpoint for deployment, allowing external requests to access the model.

This process effectively integrates MLflow with Azure, leveraging Azure's capabilities for deploying and managing machine learning models. In the next demo, we will focus on deploying the registered model to an endpoint for inference.

### Model Registration in Azure Machine Learning

1. **Model Registration**: The command `model.register` registers the model in the Azure Machine Learning workspace, indicating that an MLflow server is active.

2. **Model Files**: The model files (conda.yaml, MLmodel, model.pkl) are now stored on the Azure MLflow Tracking server, not on a local server.

3. **Endpoint Status**: After registration, the model has not been deployed, as indicated by the absence of endpoints in the Endpoints section.

### Deployment Process

1. **Import Libraries**:
   ```python
   import json
   from mlflow.deployments import get_deploy_client
   ```

2. **Create Deployment Configuration**:
   ```python
   deploy_config = {"computeType": "aci"}  # ACI = Azure Container Instances
   ```

3. **Write Configuration to JSON**:
   ```python
   deployment_config_path = "deployment_config.json"
   with open(deployment_config_path, "w") as outfile:
       outfile.write(json.dumps(deploy_config))
   ```

4. **Get Deployment Client**:
   - Redirect the client to the Azure MLflow Tracking server:
   ```python
   client = get_deploy_client("<tracking_url>")
   ```

5. **Deployment Configuration**:
   ```python
   config = {"deploy-config-file": deployment_config_path}
   model_name = 'churn-prediction-model'
   model_version = 1
   ```

6. **Set Tracking URI**:
   ```python
   mlflow.set_tracking_uri('<tracking_url>')
   ```

7. **Create Deployment**:
   ```python
   client.create_deployment(
       model_uri=f"models:/{model_name}/{model_version}",
       config=config,
       name="churn-pred-model-aci-deployment"
   )
   ```

### Monitoring Deployment Status

- **Deployment Notifications**: Check Azure portal for notifications regarding deployment progress.
- **Endpoint Monitoring**: 
   - View deployment state (initially "Unhealthy", then "Loading", and finally "Healthy").
   - Access endpoint details in the Azure portal, which provides the REST endpoint for model access.

### Summary of Key Actions

- Successfully registered the model.
- Created deployment configuration for Azure Container Instances (ACI).
- Redirected MLflow to the Azure Tracking server.
- Initiated deployment and monitored status updates until the endpoint became healthy and operational.

Next steps will include consuming the REST endpoint for predictions.

### Consuming the Deployed Endpoint in Azure

1. **Endpoint Overview**:
   - The endpoint is successfully deployed on Azure with:
     - **Deployment State**: Healthy
     - **Operation State**: Succeeded
     - **Compute Type**: Container instance

2. **Accessing the REST Endpoint**:
   - The REST endpoint URL can be found in the Azure portal under the Details section of the endpoint.

3. **Testing the Endpoint**:
   - The input data structure to test the endpoint is a dictionary with:
     - **columns**: List of model input variables (e.g., Age, FrequentFlyer, AnnualIncomeClass).
     - **index**: An integer indicating the number of input variables.
     - **data**: A list containing the values for the input variables.

4. **Example Input Data**:
   ```python
   data = {
       "input_data": {
           "columns": ["Age", "FrequentFlyer", "AnnualIncomeClass", "ServicesOpted", "AccountSyncedToSocialMedia", "BookedHotelOrNot"],
           "index": [6],
           "data": [[28, 'Yes', 2, 6, 'No', 'Yes']]
       }
   }
   ```

5. **Python Code to Consume the Endpoint**:
   - Import necessary libraries:
   ```python
   import urllib.request
   import json
   import os
   import ssl
   ```

   - Allow self-signed HTTPS:
   ```python
   def allowSelfSignedHttps(allowed):
       if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
           ssl._create_default_https_context = ssl._create_unverified_context
   allowSelfSignedHttps(True)
   ```

   - Prepare input data and send request:
   ```python
   body = str.encode(json.dumps(data))
   url = 'http://<your-rest-endpoint>/score'
   headers = {'Content-Type': 'application/json'}
   req = urllib.request.Request(url, body, headers)

   try:
       response = urllib.request.urlopen(req)
       result = response.read()
       print(result)
   except urllib.error.HTTPError as error:
       print("The request failed with status code: " + str(error.code))
       print(error.info())
       print(error.read().decode("utf8", 'ignore'))
   ```

6. **Receiving Predictions**:
   - After sending a request, the model responds with a prediction (e.g., `[1]` indicates churn).
   - To test another instance, modify the `index` and `data` fields in the input structure.

7. **Resource Cleanup**:
   - Delete registered model versions in MLflow:
     - Navigate to Models, select the model, and delete each version.
     - Optionally, change the stage of versions to archived before deletion.

   - Delete the experiment in MLflow:
     - Click the trash can icon to delete the experiment.

   - Delete the Azure Machine Learning workspace:
     - Navigate to the Azure portal and use the Delete option.
     - Confirm deletion by typing the workspace name.

   - Clean up remaining resources in the Azure resource group by selecting all and confirming deletion.

### Summary
This demo showcased the deployment of a model to Azure and how to consume the REST endpoint for predictions. It also covered the importance of cleaning up resources after usage to avoid unnecessary costs.