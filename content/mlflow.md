# Project Overview

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=2e086e14-1d4b-409d-bb9a-8c12c5013606&tab=lesson)

You are working for a property management company renting rooms and properties for short periods of time on various platforms. You need to estimate the typical price for a given property based on the price of similar properties. Your company receives new data in bulk every week. The model needs to be retrained with the same cadence, necessitating an end-to-end pipeline that can be reused.

In this project, you will build such a pipeline.

# Starter Kit & Set Up

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=3ab6def9-caaa-41ab-8bf2-968f73b11b37&tab=lesson)

## Preliminary Steps

### Fork the Starter Kit

Navigate to the [Project Repository(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices) (opens in a new tab) and click the **Fork** button in the upper-right corner of the page. This action creates a **fork** of the repository in your GitHub account—a personal copy of the repository that you can modify independently.

### Clone the Forked Repository

Once the fork is created, clone the repository to your local machine so you can start working on the project. Use the following command, replacing [your gitHub username] with your GitHub username:

`> git clone https://github.com/[your github username]/build-ml-pipeline-for-short-term-rental-prices.git`

### Navigate to the Project Directory

Change into the newly cloned repository’s directory to access the project files:

`> cd build-ml-pipeline-for-short-term-rental-prices`

### Work Locally and Push Your Changes

As you progress on the project, make sure to commit and push your changes to your repository regularly. This ensures your work is backed up and allows you to track your progress. Follow these best practices:

- Add meaningful commit messages that clearly describe the changes or improvements you’ve made.
- Push your commits to your GitHub repository to keep your fork updated.

### Create environment

Make sure to have conda installed and ready, then create a new environment using the `environment.yml` file provided in the root of the repository and activate it:

`> conda env create -f environment.yml > conda activate nyc_airbnb_dev`

### Get API key for Weights and Biases (W&B)

Let's make sure we are logged in to W&B. Get your API key from W&B by going to [https://wandb.ai/authorize(opens in a new tab)](https://wandb.ai/authorize) and click on the copy icon (copy to clipboard), then paste your key into this command:

`> wandb login [your API key]`

You should see a message similar to:

`wandb: Appending key for api.wandb.ai to your netrc file: /home/[your username]/.netrc`

### Cookiecutter: Simplifying Component Creation

To make your work easier, you are provided with a [cookiecutter(opens in a new tab)](https://cookiecutter.readthedocs.io/en/latest/) template. This template allows you to quickly create stubs for new pipeline components, saving time and reducing the need to write boilerplate code. While using the cookiecutter template is optional, it can significantly speed up your development process by generating the necessary structure and files for a new component. Instead of starting from scratch, you can use the pre-generated files as a starting point and then customize them to meet your requirements.

#### How to Use the Cookiecutter Template

Run the following command to use the cookiecutter template:

`> cookiecutter cookie-mlflow-step -o src`

You will be prompted to provide details about the new component. For example:

`step_name [step_name]: basic_cleaning script_name [run.py]: run.py job_type [my_step]: basic_cleaning short_description [My step]: This step cleans the data  long_description [An example of a step using MLflow and W&B]: Performs basic cleaning on the data and saves the results in W&B parameters [parameter1,parameter2]: parameter1,parameter2,parameter3`

#### Generated Component Structure

After entering the required information, the cookiecutter will create a new directory for your component. For example, if the step name is `basic_cleaning`, the structure under `src` will look like this:

`> ls src/basic_cleaning/ conda.yml  MLproject  run.py`

#### Using the Generated Component

The generated run.py script will accept the parameters you specified (e.g., `parameter1`, `parameter2`, `parameter3`). You can run the step with these parameters using the following command:

The script `run.py` will receive the input parameters `parameter1`, `parameter2`, `parameter3` and it will be called like:

`> mlflow run src/step_name -P parameter1=1 -P parameter2=2 -P parameter3="test"`

### The Configuration

As usual, the parameters controlling the pipeline are defined in the `config.yaml` file defined in the root of the starter kit. We will use Hydra to manage this configuration file. Open this file and get familiar with its content. Remember: this file is only read by the `main.py` script (i.e., the pipeline) and its content is available with the `go` function in `main.py` as the `config` dictionary. For example, the name of the project is contained in the `project_name` key under the `main` section in the configuration file. It can be accessed from the `go` function as `config["main"]["project_name"]`.

**Note**: Do not hardcode any parameter when writing the pipeline. All the parameters should be accessed from the configuration file.

### Running the entire pipeline or just a selection of steps

In order to run the pipeline when you are developing, you need to be in the root of the starter kit, then you can execute as usual:

`>  mlflow run .`

This will run the entire pipeline.

When developing, it is useful to be able to run one step at a time. Say you want to run only the `download` step. The `main.py` is written so that the steps are defined at the top of the file, in the `_steps` list, and can be selected by using the `steps` parameter on the command line:

`> mlflow run . -P steps=download`

If you want to run the `download` and the `basic_cleaning` steps, you can similarly do:

`> mlflow run . -P steps=download,basic_cleaning`

You can override any other parameter in the configuration file using the Hydra syntax, by providing it as a `hydra_options` parameter. For example, say that we want to set the parameter modeling -> random_forest -> n_estimators to 10 and etl-> min_price to 50:

`> mlflow run . \   -P steps=download,basic_cleaning \   -P hydra_options="modeling.random_forest.n_estimators=10 etl.min_price=50"`

### Pre-Existing Components

In order to simulate a real-world situation, we are providing you with some pre-implemented reusable components. While you have a copy in your fork, you will be using them from the original repository by accessing them through their GitHub link, like:

`_ = mlflow.run(   f"{config['main']['components_repository']}/get_data",   "main",   parameters={     "sample": config["etl"]["sample"],     "artifact_name": "sample.csv",     "artifact_type": "raw_data",     "artifact_description": "Raw file as downloaded"   }, )`

If you look in the configuration file, you will see that the parameter `components_repository` in the `main` section is set to [https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/tree/main/components(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/tree/main/components). You can see the parameters that they require by looking into their `MLproject` file:

- `get_data`: downloads the data. [MLproject(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/blob/main/components/get_data/MLproject)
- `train_val_test_split`: segregate the data (splits the data) [MLproject(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/blob/main/components/train_val_test_split/MLproject)

## In Case of Errors

When you make an error writing your `conda.yml` file, you might end up with an environment for the pipeline or one of the components that are corrupted. Most of the time `mlflow` realizes that and creates a new one every time you try to fix the problem. However, sometimes this does not happen, especially if the problem is in the `pip` dependencies. In that case, you might want to clean up all conda environments created by `mlflow` and try again. In order to do so, you can get a list of the environments you are about to remove by executing:

`> conda info --envs | grep mlflow | cut -f1 -d" "`

If you are ok with that list, execute this command to clean them up:

**Note**: This will remove _ALL_ the environments with a name starting with `mlflow`. Use at your own risk.

`> for e in $(conda info --envs | grep mlflow | cut -f1 -d" ");    do conda uninstall --name $e --all -y;   done`

This will iterate over all the environments created by `mlflow` and remove them.

## Remaining Project Steps

The rest of the project steps will be up to you to implement, and will be detailed over the following pages!

![](https://uds-assets.udacity.com/glyphs/v2/paper-checklist-one.svg)
# The Main File

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=c3228afc-8492-4ebe-92ee-a1871fe44110&tab=lesson)

The pipeline is defined in the `main.py` file in the root of the starter kit. The file already contains some boilerplate code as well as the download step. Your task will be to develop the needed additional step, and then add them to the `main.py` file.

**Note**: The modeling in this project should be considered a baseline. We kept the data cleaning and the modeling simple because we want to focus on the MLops aspect of the analysis. It is possible with a little more effort to get a significantly-better model for this dataset.

# Step 1: EDA

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=a2401713-cb1d-48a0-af2e-501d116f5e50&tab=lesson)

## Exploratory Data Analysis (EDA)

The scope of this section is to get an idea of how the process of an EDA works in the context of pipelines, during the data exploration phase. In a real scenario you would spend a lot more time in this phase, but here we are going to do the bare minimum.

**Note:** remember to add some markdown cells explaining what you are about to do, so that the notebook can be understood by other people like your colleagues

1. The `main.py` script already comes with the download step implemented. Run the pipeline to get a sample of the data. The pipeline will also upload it to Weights & Biases:

`> mlflow run . -P steps=download`

You will see a message similar to:

`2021-03-12 15:44:39,840 Uploading sample.csv to Weights & Biases`

This tells you that the data is going to be stored in W&B as the artifact named `sample.csv`.

2. Now execute the `eda` step:

`> mlflow run src/eda`

This will install Jupyter and all the dependencies for `pandas-profiling`, and open a Jupyter notebook instance. Click on New -> Python 3 and create a new notebook. Rename it `EDA` by clicking on `Untitled` at the top, beside the Jupyter logo.

3. Within the notebook, fetch the artifact we just created (`sample.csv`) from W&B and read it with pandas:

 `import wandb import pandas as pd  run = wandb.init(project="nyc_airbnb", group="eda", save_code=True)  local_path = wandb.use_artifact("sample.csv:latest").file()  df = pd.read_csv(local_path)`

Note that we use `save_code=True` in the call to `wandb.init` so the notebook is uploaded and versioned by W&B.

4. Using `pandas-profiling`, create a profile:

`import pandas_profiling profile = pandas_profiling.ProfileReport(df) profile.to_widgets()`

What do you notice? Look around and see what you can find. For example, there are missing values in a few columns and the column `last_review` is a date but it is in string format. Look also at the `price` column, and note the outliers. There are some zeros and some very high prices. After talking to your stakeholders, you decide to consider from a minimum of $10 to a maximum of $350 per night.

5. Fix some of the little problems we have found in the data with the following code:

`# Drop outliers min_price = 10 max_price = 350 idx = df['price'].between(min_price, max_price) df = df[idx].copy() # Convert last_review to datetime df['last_review'] = pd.to_datetime(df['last_review'])`

Note how we did not impute missing values. We will do that in the inference pipeline, so we will be able to handle missing values also in production.

6. Create a new profile or check with `df.info()` that all obvious problems have been solved
    
7. Terminate the run by running `run.finish()`
    
8. Save the notebook, then close it (File -> Close and Halt). In the main Jupyter notebook page, click Quit in the upper right to stop Jupyter. This will also terminate the `mlflow run. DO NOT USE CRTL-C

# Step 2: Data Cleaning

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=7d78ae40-a876-4f4c-b88c-2aee8b706038&tab=lesson)

## Data Cleaning

Now we transfer the data processing we have done as part of the EDA to a new `basic_cleaning` step that starts from the `sample.csv` artifact and creates a new artifact `clean_sample.csv` with the cleaned data:

1. Make sure you are in the root directory of the starter kit, then create a stub for the new step. The new step should accept the parameters `input_artifact` (the input artifact), `output_artifact` (the name for the output artifact), `output_type` (the type for the output artifact), `output_description` (a description for the output artifact), `min_price` (the minimum price to consider) and `max_price` (the maximum price to consider):

`> cookiecutter cookie-mlflow-step -o src step_name [step_name]: basic_cleaning script_name [run.py]: run.py job_type [my_step]: basic_cleaning short_description [My step]: A very basic data cleaning long_description [An example of a step using MLflow and Weights & Biases]: Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact parameters [parameter1,parameter2]: input_artifact,output_artifact,output_type,output_description,min_price,max_price`

This will create a directory `src/basic_cleaning` containing the basic files required for an MLflow step: `conda.yml`, `MLproject`, and the script (which we named `run.py`).

2. Modify the `src/basic_cleaning/run.py` script and the ML project script by filling in the missing information about parameters (note the comments like `INSERT TYPE HERE` and `INSERT DESCRIPTION HERE`). All parameters should be of type `str` except `min_price` and `max_price`, which should be `float`.
    
3. Implement in the section marked `# YOUR CODE HERE #` the steps we have implemented in the notebook, including downloading the data from W&B. Remember to use the `logger` instance already provided to print meaningful messages to the screen. Make sure to use `args.min_price` and `args.max_price` when dropping the outliers (instead of hard-coding the values as we did in the notebook). Save the results to a CSV file called `clean_sample.csv` (`df.to_csv("clean_sample.csv", index=False)`).
    

**Note**: Remember to use `index=False` when saving to CSV. Otherwise, the data checks in the next step might fail because there will be an extra `index` column. Then upload it to W&B using:

`artifact = wandb.Artifact(   args.output_artifact,   type=args.output_type,   description=args.output_description, ) artifact.add_file("clean_sample.csv") run.log_artifact(artifact)`

**Remember**: Whenever you are using a library (like pandas), you MUST add it as a dependency in the `conda.yml` file. For example, here we are using pandas so we must add it to `conda.yml` file, including a version:


```dependencies:   - pip=20.3.3   - pandas=1.2.3   - pip:         - wandb==0.10.31```

4. Add the `basic_cleaning` step to the pipeline (the `main.py` file):

`if "basic_cleaning" in active_steps:   _ = mlflow.run(     os.path.join(hydra.utils.get_original_cwd(), "src", "basic_cleaning"),     "main",     parameters={       "input_artifact": "sample.csv:latest",       "output_artifact": "clean_sample.csv",       "output_type": "clean_sample",       "output_description": "Data with outliers and null values removed",       "min_price": config['etl']['min_price'],       "max_price": config['etl']['max_price']     },   )`

Please note how the path to the step is constructed:

`os.path.join(hydra.utils.get_original_cwd(), "src", "basic_cleaning")`

This is necessary because Hydra executes the script in a directory different from the root of the starter kit. You will have to do the same for every step you are going to add to the pipeline.

Remember that when you refer to an artifact stored on W&B, you MUST specify a version or a tag. For example, here the `input_artifact` should be `sample.csv:latest` and NOT just `sample.csv`. If you forget to do this, you will see a message like `Attempted to fetch artifact without alias (e.g., "<artifact_name>:v3" or "<artifact_name>:latest")`

5. Run the pipeline. If you go to W&B, you will see the new artifact type `clean_sample` and within it the `clean_sample.csv` artifact

# Step 3: Data Testing

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=e7576500-bad9-46cb-b9fb-7076528da320&tab=lesson)

## Data Testing

After the cleaning, it is a good practice to put some tests that verify that the data does not contain surprises.

One of our tests will compare the distribution of the current data sample with a reference, to ensure that there is no unexpected change. Therefore, we first need to define a "reference dataset". We will just tag the latest `clean_sample.csv` artifact on W&B as our reference dataset. Go with your browset to `wandb.ai`, navigate to your project, then to the artifact tab. Click on "clean_sample", then on the version with the `latest` tag. This is the last one we produced in the previous step. Add a tag `reference` to it by clicking the "+" in the Aliases section on the right:

![Add a tag reference by clicking on the "+" button next to "Aliases" for the artifact overview.](https://video.udacity-data.com/topher/2021/March/605100cc_wandb-tag-data-test/wandb-tag-data-test.png)

Adding a tag

Now we are ready to add some tests. In the starter kit you can find a `data_tests` step that you need to complete. Let's start by appending to `src/data_check/test_data.py` the following test:

`def test_row_count(data):     assert 15000 < data.shape[0] < 1000000`

which checks that the size of the dataset is reasonable (not too small, not too large).

Then, add another test `test_price_range(data, min_price, max_price)` that checks that the price range is between `min_price` and `max_price` (hint: you can use the `data['price'].between(...)` method). Also, remember that we are using closures, so the name of the variables that your test takes in MUST BE exactly `data`, `min_price` and `max_price`.

Now add the `data_check` component to the main file, so that it gets executed as part of our pipeline. Use `clean_sample.csv:latest` as `csv` and `clean_sample.csv:reference` as `ref`. Right now they point to the same file, but later on they will not: we will fetch another sample of data and therefore the `latest` tag will point to that. Also, use the configuration for the other parameters. For example, use `config["data_check"]["kl_threshold"]` for the `kl_threshold` parameter.

Then run the pipeline and make sure the tests are executed and that they pass. Remember that you can run just this step with:

`> mlflow run . -P steps="data_check"`

You can safely ignore the following DeprecationWarning if you see it:

`DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc'  is deprecated since Python 3.3, and in 3.10 it will stop working`

# Step 4: Initial Training

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=78b76980-cb72-4cf1-8fa6-2c0dfa8d9392&tab=lesson)

## Data Splitting

Use the provided component called `train_val_test_split` to extract and segregate the test set. Add it to the pipeline, and then run the pipeline. As usual, use the configuration for the parameters like `test_size`, `random_seed` and `stratify_by`. Look at the `modeling` section in the config file.

**Hint**: The path to the step can be expressed as:

`mlflow.run(f"{config['main']['components_repository']}/train_val_test_split", ...)`

You can see the parameters accepted by this step [here(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/blob/main/components/train_val_test_split/MLproject)

After you execute, you will see something like:

`2021-03-15 01:36:44,818 Uploading trainval_data.csv dataset 2021-03-15 01:36:47,958 Uploading test_data.csv dataset`

in the log. This tells you that the script is uploading 2 new datasets: `trainval_data.csv` and `test_data.csv`.

## Train Random Forest

Complete the script `src/train_random_forest/run.py`. All the places where you need to insert code are marked by a `# YOUR CODE HERE` comment and are delimited by two signs like `######################################`. You can find further instructions in the file.

Once you are done, add the step to `main.py`. Use the name `random_forest_export` as `output_artifact`.

**Note**: the main.py file already provides a variable `rf_config` to be passed as the `rf_config` parameter.

## Optimize Hyperparameters

Re-run the entire pipeline, varying the hyperparameters of the Random Forest model. This can be accomplished easily by exploiting the Hydra configuration system. Use the multi-run feature (adding the `-m` option at the end of the `hydra_options` specification), and try setting the parameter `modeling.max_tfidf_features` to 10, 15, and 30 and the `modeling.random_forest.max_features` to 0.1, 0.33, 0.5, 0.75, 1.

**Hint:** if you don't remember the hydra syntax, you can take inspiration from this example, where we vary two other parameters (this is NOT the solution to this step):

`> mlflow run . \   -P steps=train_random_forest \   -P hydra_options="modeling.random_forest.max_depth=10,50,100 modeling.random_forest.n_estimators=100,200,500 -m"`

you can change this command line to accomplish your task.

While running this simple experimentation is enough to complete this project, you can also explore more and see if you can improve the performance. You can also look at the Hydra documentation for even more ways to do hyperparameters optimization. Hydra is very powerful, and allows even to use things like Bayesian optimization without any change to the pipeline itself.

## Select the Best Model

Go to W&B and select the best-performing model.

![Look for your best model within W&B](https://video.udacity-data.com/topher/2021/March/605103d6_wandb-select-best/wandb-select-best.gif)

Selecting the best model

**Hint**: you should switch to the Table view (second icon on the left), then click on the upper right on "columns", remove all selected columns by clicking on "Hide all", then click on the left list on "ID", "Job Type", "max_depth", "n_estimators", "mae" and "r2". Click on "Close". Now in the table view you can click on the "mae" column on the three little dots, then select "Sort asc". This will sort the runs by ascending Mean Absolute Error (best result at the top).

When you have found the best job, click on its name, then go to its artifacts and select the "model_export" output artifact. You can now add a `prod` tag to it to mark it as "production ready".

## Test

Use the provided step `test_regression_model` to test your production model against the test set. Implement the call to this component in the `main.py` file. As usual you can see the parameters in the corresponding [MLproject(opens in a new tab)](https://github.com/udacity/build-ml-pipeline-for-short-term-rental-prices/blob/main/components/test_regression_model/MLproject) file. Use the artifact `random_forest_export:prod` for the parameter `mlflow_model` and the test artifact `test_data.csv:latest` as `test_artifact`.

**Note**: This step is NOT run by default when you run the pipeline. In fact, it needs the manual step of promoting a model to `prod` before it can complete successfully. Therefore, you have to activate it explicitly on the command line:

`> mlflow run . -P steps=test_regression_model`

# Step 5: Pipeline Release and Updates

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=37f1c00c-b96b-4bb3-90a3-8e4a9dc7df3a&tab=lesson)

## Visualize the pipeline

You can now go to W&B, go the Artifacts section, select the model export artifact then click on the `Lineage` tab. You will see something like this:

![Visualization of the pipeline](https://video.udacity-data.com/topher/2023/December/656d2d46_screenshot_5/screenshot_5.jpeg)

Visualization of the pipeline

## Release the pipeline

First copy the best hyper parameters you found in your `configuration.yml` so they become the default values. Then, go to your repository on GitHub and make a release. If you need a refresher, here are some [instructions(opens in a new tab)](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository#creating-a-release) on how to release on GitHub.

Call the release `1.0.0`:

![Tagging release 1.0.0 on Github, along with a release message. This example uses "Train a random forest model to the NYC Airbnb dataset" as its message.](https://video.udacity-data.com/topher/2021/March/605104a4_tag-release-github/tag-release-github.png)

Tagging release 1.0.0 on Github

If you find problems in the release, fix them and then make a new release like `1.0.1`, `1.0.2` and so on.

## Train the model on a new data sample

Let's now test that we can run the release using `mlflow` without any other pre-requisite. We will train the model on a new sample of data that our company received (`sample2.csv`):

(be ready for a surprise, keep reading even if the command fails)

`> mlflow run https://github.com/[your github username]/nd0821-c2-build-model-workflow-starter.git \              -v [the version you want to use, like 1.0.0] \              -P hydra_options="etl.sample='sample2.csv'"`

But, wait! It failed! The test `test_proper_boundaries` failed, apparently there is one point which is outside of the boundaries. This is an example of a "successful failure", i.e., a test that did its job and caught an unexpected event in the pipeline (in this case, in the data).

You can fix this by adding these two lines in the `basic_cleaning` step just before saving the output to the csv file with `df.to_csv`:

`idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2) df = df[idx].copy()`

This will drop rows in the dataset that are not in the proper geolocation.

Then commit your change, make a new release (for example `1.0.1`) and retry (of course you need to use `-v 1.0.1` when calling mlflow this time). Now the run should succeed and voit la', you have trained your new model on the new data.

# Submission

[Lesson](https://learn.udacity.com/nd0821?version=3.0.7&partKey=cd0581&lessonKey=f4891718-7bee-4464-84f3-b92a29d016d4&conceptKey=075d4b1a-4c95-4095-83c6-49585517e5ff&tab=lesson)

## Submission

In order to submit your project, there are a few things to check ahead of time.

1. Review the project rubric to ensure you have completed all steps. The instructions should closely match this, but it's worth confirming everything is completed, as reviewers will use this to grade your submission.
2. Make sure your W&B project is public. Then, make sure to **include a link to your public project** in both:
    - The _**README.md**_ file in your GitHub repository
    - In the _**Submission Details**_ text box that you'll see during the submission process,
3. You will only be able to submit a Github repository link for your submission to ensure you did use a Github repository, as reviewers will need to be able to see items such as releases. Note that similar to the W&B project link, **you must also include the Github link** in both:
    - The _**README.md**_ file in your GitHub repository
    - In the _**Submission Details**_ text box that you'll see during the submission process,

> ### Important!
> 
> You must include both links the the _**README**_ and the _**Submission Details**_. Your reviewer will receive a zip of your most recent commit but will need your GitHub link to see the actual releases and the Weights & Biases project.

Once you have everything above ready, you are ready to submit your project!

# Rubric

Use this project rubric to understand and assess the project criteria.

## W&B Set-Up

|Criteria|Submission Requirements|
|---|---|
|Public W&B project `nyc_airbnb`|Your W&B project nyc_airbnb should be made public, so that your reviewer can access it. This is needed so the reviewer can check that the W&B steps have been executed successfully.<br><br>**Make sure the link to your W&B project, as well as your Github repository (i.e. two links), are included in a README file or given to the reviewer in the "Submission Details" box you can use when initiating the submission process.**|

## Exploratory Data Analysis

|Criteria|Submission Requirements|
|---|---|
|Obtain sample data|There is a sample.csv artifact in W&B.<br><br>The pipeline has been run to get a sample of the data, which has been uploaded to W&B.|
|Utilize an EDA notebook|There is a notebook called EDA in the students’ repository (most probably in the src/eda directory).<br><br>The EDA notebook contains a properly formatted Jupyter notebook with comments and markdown cells.|
|Fetch data into the notebook|At the beginning of the notebook, fetch the sample.csv artifact from W&B.|
|Clean the sample data|The data is clean at the end of the notebook. Note that there will still be some missing entries, because we are not imputing missing values.<br><br>Properly implemented the checks suggested in the `notes.md` file.|

## Data Cleaning

|Criteria|Submission Requirements|
|---|---|
|Create a “basic_cleaning” step in the Github repository|There is a new “basic_cleaning” step in the Github repository (under the src directory).<br><br>The basic_cleaning step respects the MLFlow structure: a conda.yml, a MLproject and a python script. It has the parameters input_artifact, output_name, output_type, output_description, min_price and max_price.|
|Update the conda.yml file|The conda.yml file has been updated to add the `pandas` dependency.|
|Update all parameters|Add docstrings and the proper type to all parameters, both in the script and in the MLproject file.|
|Run basic_cleaning without errors|The basic_cleaning step re-implements in a MLFlow step the data cleaning you performed during the EDA. It should be added to the main.py file and run without errors.<br><br>In the main.py file all parameters are taken from the configuration file, and not hard-coded.|
|Create clean_data.csv in W&B|At the end of the run of this step, there should be a clean_data.csv artifact uploaded to W&B.|

## Data Testing

|Criteria|Submission Requirements|
|---|---|
|Create a “reference” tag for the latest version of the clean_sample.csv artifact|In W&B, manually add a tag called “reference” to the latest version of the clean_sample.csv artifact.|
|Implement the test_row_count and the test_price_range tests in src/data_check/test_data.py|Implements the test_row_count and the test_price_range tests in src/data_check/test_data.py.<br><br>The added tests are checking respectively for a proper size of the dataset, and for a proper price range.|
|The pipeline runs successfully|The pipeline runs after this step, and all the tests pass.|

## Data Splitting

|Criteria|Submission Requirements|
|---|---|
|Split data into training, validation and test sets.|Adds the train_val_test_split component to the main.py file.<br><br>The train_val_test_split has been provided to you. You can just add it to the `main.py` file and fill in the parameters appropriately.|
|The pipeline again runs successfully|The pipeline runs. At the end there should be 2 new artifacts on W&B: trainval_data.csv, test_data.csv.|

## Train the Random Forest

|Criteria|Submission Requirements|
|---|---|
|Complete the `src/train_random_forest/run.py` script|The `src/train_random_forest/run.py` script is completed.<br><br>When checking the script, there should be the following steps in the script, marked by clear comments:<br><br>1. Download the train data using W&B.<br>2. In the get_inference_pipeline function, implement a pipeline called `non_ordinal_categorical_preproc` with two steps: a `SimpleImputer(strategy="most_frequent")` and a `OneHotEncoder()` step<br>3. In the `get_inference_pipeline` function, create the inference pipeline called `sk_pipe` containing the preprocessing step and the Random Forest<br>4. In the go function, fit the pipeline.<br>5. In the go function, export the pipeline using MLFlow model export.<br>6. Upload the artifact to W&B<br>7. Log the variable MAE to W&B|
|The pipeline again runs successfully|The pipeline again runs successfully.<br><br>The `train_random_forest` step is added to the `main.py` file.|
|Create the model_export artifact on W&B|There should be an artifact created on W&B called model_export.<br><br>The model_export artifact should contain a MLflow sklearn serialized model.|

## Optimize Hyperparameters

|Criteria|Submission Requirements|
|---|---|
|Run training with different hyperparameters|Using the Hydra system, run a hyper-parameter search.<br><br>On W&B there should be the results of several (>2) training jobs with different hyperparameters.|

## Select the Best Model

|Criteria|Submission Requirements|
|---|---|
|Select the best performing model and tag it as “prod”|Add the tag “prod” to the trained model with the best MAE.|

## Test Set Verification

|Criteria|Submission Requirements|
|---|---|
|Verify test set performance is comparable to performance on the validation set (no overfitting)|Implement the `test_regression_model` function in the `main.py` file. The test_regression_model is provided just as in the “data splitting” step.<br><br>Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred).|

## Visualize the Pipeline

|Criteria|Submission Requirements|
|---|---|
|Visualize the pipeline and verify proper structure|Navigate to W&B, to the artifact section, then click on “Graph view”. The resulting visualization should show the pipeline properly organized. Refer to the reference plot in notes.md.|

## Release the Pipeline

|Criteria|Submission Requirements|
|---|---|
|Release v1.0.0 of the pipeline in Github|A release of the pipeline is cut from the Github repository, with version 1.0.0 or similar (if you need more trials, you might assign versions like 1.0.1 or 1.0.2, which is totally fine).|

## Train the Model on a New Data Sample

|Criteria|Submission Requirements|
|---|---|
|Run the released pipeline on a new sample of data, with initial failure|Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv.|
|Add a new cleaning step in basic_cleaning|Implement a new cleaning step that removes data points that are outside of the area of NYC in `basic_cleaning`.|
|Prepare a new release|After adding the new cleaning step and committing and pushing to the repository, release a new version (for example, 1.0.1).|
|Run the new release successfully|Re-running with the new release should produce a new trained model.|

## Suggestions to Make Your Project Stand Out

1. In the data exploration step, you can go far beyond what is shown here, such as including visualizations and other data cleaning steps. This should allow you to get even better performance from the model.
2. Explore other models beyond the RandomForest trained here, creating a new separate step or customizing the random forest one to accommodate different types of models.
3. Add discussion to a README file concerning other changes you might consider in future releases of your pipeline.

