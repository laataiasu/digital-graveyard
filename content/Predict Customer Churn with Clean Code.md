# Project Overview

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=1d708ea8-93da-416a-9a5f-cc86751b276b&tab=lesson)[Downloads](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=1d708ea8-93da-416a-9a5f-cc86751b276b&tab=resources)

## Project Introduction

In this project, you will implement your learnings to identify credit card customers who are most likely to churn. The completed project will include a Python package for a machine learning project that follows coding (PEP8) and engineering best practices for implementing software (modular, documented, and tested). The package can also be run interactively or from the command-line interface (CLI).

This project will give you practice using your skills for testing and logging and using the best coding practices from this lesson. It will also introduce you to a problem data scientists across companies always face. How do we identify (and later intervene with) customers likely to churn?

If you want to download the data and work locally with the data, start the Workspace and download the data from the `data` folder. This ensures all students have access to the dataset. Below, you have a sample of the dataset:

![](blob:https://learn.udacity.com/2fe0878e-46fa-4dce-89b1-2bcb86af77e5)

**Note:** This project provides all students with a Workspace with all the requirements to develop and run their project. If you want to run it locally, you can download all the files and use your own setup to develop the project.

![Project Workspace Example with all files in the left panel and a screen with one notebook and three files to be developed by the students.](https://video.udacity-data.com/topher/2024/March/65f8d38d_workspace/workspace.png)

Project Workspace

# Instructions

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=95e00756-a92d-4d44-a520-f6ec90c347bf&tab=lesson)[Downloads](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=95e00756-a92d-4d44-a520-f6ec90c347bf&tab=resources)

## Objective

This is a project to implement best coding practices. You will not need to code for this project entirely from scratch.

We have already provided you the _churn_notebook.ipynb_ file containing the solution to identify credit card customers that are most likely to churn, but without implementing the engineering and software best practices.

You will need to refactor the given _**churn_notebook.ipynb**_ file following the best coding practices to generate these files:

1. churn_library.py
2. churn_script_logging_and_tests.py
3. README.md

## Starter Files

Here is the file structure available to you in the workspace next.

`. ├── Guide.ipynb          # Given: Getting started and troubleshooting tips ├── churn_notebook.ipynb # Given: Contains the code to be refactored ├── churn_library.py     # ToDo: Define the functions ├── churn_script_logging_and_tests.py # ToDo: Finish tests and logs ├── README.md            # ToDo: Provides project overview, and instructions to use the code ├── data                 # Read this data │   └── bank_data.csv ├── images               # Store EDA results │   ├── eda │   └── results ├── logs				 # Store logs └── models               # Store models`

The _**Guide.ipynb**_ and _**churn_notebook.ipynb**_ will be your starting point for the project.

## High-Level Instructions

These are the three files you will need to complete after refactoring the _churn_notebook.ipynb_ file:

1. _**churn_library.py**_  
    The _churn_library.py_ is a library of functions to find customers who are likely to churn. You may be able to complete this project by completing each of these functions, but you also have the flexibility to change or add functions to meet the rubric criteria.

The document strings have already been created for all the functions in the **churn_library.py** to assist with one potential solution. In addition, for a better understanding of the function call, see the **Sequence diagram** on the next page.

After you have defined all functions in the _churn_library.py_, you may choose to add an `if __name__ == "__main__"` block that allows you to run the code below and understand the results for each of the functions and refactored code associated with the original notebook.

`ipython churn_library.py`

2. _**churn_script_logging_and_tests.py**_  
    This file should:

- Contain unit tests for the _churn_library.py_ functions. You have to write test for _each_ input function. Use the basic assert statements that test functions work properly. The goal of test functions is to checking the returned items aren't empty or folders where results should land have results after the function has been run.
    
- Log any errors and INFO messages. You should log the info messages and errors in a .log file, so it can be viewed post the run of the script. The log messages should easily be understood and traceable.
    

Also, ensure that testing and logging can be completed on the command line, meaning, running the below code in the terminal should test each of the functions and provide any errors to a file stored in the _/logs_ folder.

`ipython churn_script_logging_and_tests.py`

> **Testing framework**: As long as you fulfil all the rubric criteria, the choice of testing framework rests with the student. For instance, you can use [pytest(opens in a new tab)](https://docs.pytest.org/en/7.1.x/getting-started.html#) for writing functional tests.

3. _**README.md**_  
    This file will provide an overview of the project, the instructions to use the code, for example, it explains how to test and log the result of each function. For instance, you can have the following detailed sections in the _README.md_ file:

- Project description
- Files and data description
- Running the files

## Code Quality Considerations

- **Style Guide** - Format your refactored code using [PEP 8 – Style Guide(opens in a new tab)](https://peps.python.org/pep-0008/). Running the command below can assist with formatting. To assist with meeting pep 8 guidelines, use `autopep8` via the command line commands below:

`autopep8 --in-place --aggressive --aggressive churn_script_logging_and_tests.py autopep8 --in-place --aggressive --aggressive churn_library.py`

- **Style Checking and Error Spotting** - Use [Pylint(opens in a new tab)](https://pypi.org/project/pylint/) for the code analysis looking for programming errors, and scope for further refactoring. You should check the pylint score using the command below.

`pylint churn_library.py pylint churn_script_logging_and_tests.py`

You should make sure you don't have any errors, and that your code is scoring as high as you can get it! Shoot for a `pylint` score exceeding 7 for both Python files.

- **Docstring** - All functions and files should have document strings that correctly identifies the inputs, outputs, and purpose of the function. All files have a document string that identifies the purpose of the file, the author, and the date the file was created.

## Rubric

> **Important**  
> It is good to have a quick look at the [rubric(opens in a new tab)](https://learn.udacity.com/rubric/3094) before you start refactoring the code. The rubric defines the criteria against which Reviewers will evaluate your submission. In other words, it has details on what is needed for a successful solution.

## Final Expectation

The project requires completed versions of these files:

1. churn_library.py
2. churn_script_logging_and_tests.py
3. README.md

The file structure of a completed project should be similar to the below:

![Project Files Structure - a `data` dir, `images` (with `eda` and `results` subdirectories), and `models`; then the churn_notebook.ipynb file, churn_library.py, churn_script_logging_and_tests.py file, and a README file.](https://video.udacity-data.com/topher/2021/March/6058baa0_clean-code-churn-files/clean-code-churn-files.png)

Project Files Structure

## Submission

You can submit through _either_ of the options below:

- [Preferred] SUBMIT PROJECT button in the workspace will automatically zip all file in the workspace directory and submit to the reviewers.
    
- SUBMIT PROJECT button on the last page will prompt you to provide a Github link to your completed project.
    

Both of the options above will send a submission acknowledgement to your mailbox.


# Sequence diagram

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=567ce545-df32-4150-89fd-30d02cd8a50c&tab=lesson)[Downloads](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0580&lessonKey=869330b7-a93b-416d-ba04-c38a6fef2e0b&conceptKey=567ce545-df32-4150-89fd-30d02cd8a50c&tab=resources)

The code in churn_library.py should complete data science solution process including:

- EDA
- Feature Engineering (including encoding of categorical variables)
- Model Training
- Prediction
- Model Evaluation

Refer to the **Save Images & Models** and **Problem Solving** sections in the [rubric(opens in a new tab)](https://learn.udacity.com/rubric/3094) for the specific expectations.

The sequence diagram below shows the sequence of _churn_library.py_ function calls, and the Document Strings section further shows each function's input/output details.

![*churn_library.py* functions [Sequence diagram](https://video.udacity-data.com/topher/2022/March/6240a53a_sequencediagram/sequencediagram.jpeg)](https://video.udacity-data.com/topher/2022/March/62408b12_untitled/untitled.jpeg)

_churn_library.py_ functions [Sequence diagram(opens in a new tab)](https://video.udacity-data.com/topher/2022/March/6240a53a_sequencediagram/sequencediagram.jpeg)

### Help - Document Strings

Below is the docstring for each function present in the _churn_library.py_ file.

- `import_data()`

    `import_data(pth)         returns dataframe for the csv found at pth                 input:                 pth: a path to the csv        output:                 df: pandas dataframe`

- `perform_eda()`

    `perform_eda(df)         perform eda on df and save figures to images folder        input:                 df: pandas dataframe                  output:                 None`

- `perform_feature_engineering()`

    `perform_feature_engineering(df, response)         input:                   df: pandas dataframe                   response: string of response name                  output:                   X_train: X training data                   X_test: X testing data                   y_train: y training data                   y_test: y testing data`

- `encoder_helper()`  
    Use one-hot encoding or mean of the response to fill in categorical columns.

    `encoder_helper(df, category_lst, response)         helper function to turn each categorical column into a new column with         propotion of churn for each category - associated with cell 15 from the notebook                 input:                 df: pandas dataframe                 category_lst: list of columns that contain categorical features                response: string of response name                 output:                 df: pandas dataframe with new columns for`

- `train_models()`

    `train_models(X_train, X_test, y_train, y_test)         train, store model results: images + scores, and store models         input:                   X_train: X training data                   X_test: X testing data                   y_train: y training data                   y_test: y testing data         output:                   None`

- `classification_report_image()`

    `classification_report_image(y_train, y_test, y_train_preds_lr, y_train_preds_rf, y_test_preds_lr, y_test_preds_rf)         produces classification report for training and testing results and stores report as image        in images folder        input:                 y_train: training response values                y_test:  test response values                y_train_preds_lr: training predictions from logistic regression                y_train_preds_rf: training predictions from random forest                y_test_preds_lr: test predictions from logistic regression                y_test_preds_rf: test predictions from random forest                 output:                  None`

- `feature_importance_plot()`

    `feature_importance_plot(model, X_data, output_pth)         creates and stores the feature importances in pth         input:                 model: model object containing feature_importances_                 X_data: pandas dataframe of X values                 output_pth: path to store the figure                  output:                  None`


# Rubric

Use this project rubric to understand and assess the project criteria.

## Code Quality

| Criteria                                                                              | Submission Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The code is following the PEP 8 coding style.                                         | All the code written for this project should follow the [PEP 8 guidelines(opens in a new tab)](https://www.python.org/dev/peps/pep-0008/). Objects have meaningful names and syntax. Code is properly commented and organized. Imports are correctly ordered.<br><br>Running the below can assist with formatting.<br><br> `autopep8 --in-place --aggressive --aggressive script.py`<br><br>Then students should aim for a score exceeding 7 when using `pylint`<br><br>`pylint script.py` |
| The README file provides an overview of the project, the instructions to use the code | The file contains a summary of the purpose and description of the project. Someone should be able to run the code by reading the README.                                                                                                                                                                                                                                                                                                                                                   |
| All functions and files have document strings.                                        | All functions have a document string that correctly identifies the inputs, outputs, and purpose of the function. All files have a document string that identifies the purpose of the file, the author, and the date the file was created.                                                                                                                                                                                                                                                  |

## Testing & Logging

|Criteria|Submission Requirements|
|---|---|
|Tests written for each function.|Each function in `churn_script_logging_and_tests.py` is complete with tests for the input function.|
|Log for info and errors.|Each function in `churn_script_logging_and_tests.py` is complete with logging for if the function successfully passes the tests or errors.|
|Logs stored in a `.log` file.|All log information should be stored in a `.log` file, so it can be viewed post the run of the script.|
|Easy to understand error and info messages.|The log messages should easily be understood and traceable that appear in the `.log` file.|
|Test and logging can be completed on the command line.|The README should inform a user how they would test and log the result of each function.<br><br>Something similar to the below should produce the `.log` file with the result from running all tests.<br><br>`ipython churn_script_logging_and_tests_solution.py`|

## Save Images & Models

|Criteria|Submission Requirements|
|---|---|
|Store EDA plots.|Store result plots including at least one:<br><br>1. Univariate, quantitative plot<br>2. Univariate, categorical plot<br>3. Bivariate plot|
|Store result plots.|Store result plots including:<br><br>1. ROC curves<br>2. Feature Importances|
|Store model objects that can easily be loaded and used in a production environment.|Store at least two models. Recommended using `joblib` and storing models with `.pkl` extension.|

## Problem Solving

|Criteria|Submission Requirements|
|---|---|
|Code completes the process for solving the data science process.|Code in `churn_library.py` completes the process for solving the data science process including:<br><br>1. EDA<br>2. Feature Engineering (including encoding of categorical variables)<br>3. Model Training<br>4. Prediction<br>5. Model Evaluation|
|Handle categorical columns.|Use one-hot encoding or mean of the response to fill in categorical columns. Currently, the notebook does this in an inefficient way that can be refactored by looping. Make this code more efficient using the same method as in the notebook or using one-hot encoding. Tip: Creating a list of categorical column names can help with looping through these items and create an easier way to extend this logic.|

## Suggestions to Make Your Project Stand Out

- Re-organize each script to work as a class.
- Update functions to move constants to their own `constants.py` file, which can then be passed to the necessary functions, rather than being created as variables within functions.
- Work towards pylint score of 10/10.
- Add dependencies and libraries (or dockerfile) to README.md
- Add requirements.txt with needed dependencies and libraries for simple install.