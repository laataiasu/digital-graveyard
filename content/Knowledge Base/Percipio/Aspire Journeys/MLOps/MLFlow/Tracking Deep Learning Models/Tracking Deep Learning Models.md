---
date: 1970-01-01T00:00:00Z
---

# Tracking Deep Learning Models

### Model Training and Tracking with MLflow

**Model Types Trained:**
- Scikit-learn models for classification and regression
- XGBoost models
- Statsmodels for ordinary least squares regression
- Time-series models using the Prophet forecaster

**Transition to Deep Learning:**
- Focus: Build and train deep learning models using MLflow.
- Popular frameworks: TensorFlow and PyTorch.

---

### Introduction to TensorFlow

- **Definition**: Open-source machine learning framework for deep learning.
- **Origin**: Developed by Google; supported by community contributors.
- **Ecosystem**: Comprehensive tools and libraries for tasks ranging from linear regression to deep learning.

---

### Deep Learning Model for Image Classification

- **Objective**: Classify images into 10 categories using Convolutional Neural Networks (CNNs).
- **CNNs**: Designed for processing two-dimensional data (e.g., images, video).
  - **Convolutional Layers**: Extract features from input images.
  - **Pooling Layers**: Aggregate data from convolutional layers.

---

### Setting Up TensorFlow

1. **Install TensorFlow**:
   ```python
   !pip install tensorflow==2.11.0
   ```

2. **Verify TensorFlow Version**:
   ```python
   print(tf.__version__)
   ```

3. **Import Necessary Libraries**:
   ```python
   import mlflow
   import keras
   import numpy as np
   import matplotlib.pyplot as plt
   from keras.utils import to_categorical
   from keras.models import Sequential
   from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
   ```

4. **Dataset**: Use `fashion_mnist` for training.
   ```python
   fashion_mnist = tf.keras.datasets.fashion_mnist
   (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
   ```

5. **Dataset Shape**:
   ```python
   train_images.shape, train_labels.shape, test_images.shape, test_labels.shape
   ```
   - 60,000 training images
   - 10,000 testing images

---

### Image Classification Classes

- **Classes**:
  - T-shirt/top
  - Trouser
  - Pullover
  - Dress
  - Coat
  - Sandal
  - Shirt
  - Sneaker
  - Bag
  - Ankle boot

```python
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
```

---

### Data Visualization

- **Plotting a Single Image**:
   ```python
   plt.imshow(train_images[10])
   plt.title(class_names[train_labels[10]])
   ```

- **Normalization**: Convert pixel values to a range of 0 to 1 for numerical stability.
   ```python
   train_images = train_images / 255.0
   test_images = test_images / 255.0
   ```

- **Plotting Multiple Images**:
   ```python
   for i in range(16):
       plt.subplot(4, 4, i + 1)
       plt.imshow(train_images[i], cmap=plt.cm.binary)
   ```

---

### Understanding Image Data

- **Array Representation**:
   ```python
   train_images[2]
   ```
   - All pixel values should now be between 0 and 1.

- **Tensors**: Fundamental data structure for deep learning, representing multi-dimensional arrays.

---

### Setting Up MLflow Experiment

1. **Create and Set Experiment**
   ```python
   experiment_id = mlflow.create_experiment(name='fashion_images_prediction_tf')
   mlflow.set_experiment(experiment_name='fashion_images_prediction_tf')
   ```

2. **Log Images as Artifacts**
   - Use the `PIL` library to convert image data to a suitable format for logging.
   - For a specific training image (index 7):
   ```python
   fig1 = plt.imshow(train_images[7], cmap=plt.cm.binary)
   ```
   - Convert and resize the image:
   ```python
   from PIL import Image
   im = Image.fromarray(np.uint8(train_images[7] * 255)).resize((200, 200))
   ```

3. **Start MLflow Run**
   ```python
   with mlflow.start_run():
       for i in range(100, 130):
           mlflow.log_image(
               Image.fromarray(np.uint8(train_images[i] * 255)).resize((200, 200)),
               f'{class_names[train_labels[i]]}.png'
           )
   ```

### Training Image Classification Model

1. **Enable MLflow Autologging**
   ```python
   mlflow.tensorflow.autolog(log_models=False)
   ```

2. **Start Run for Training**
   ```python
   with mlflow.start_run() as tf_run:
   ```

3. **Reshape Data for CNN**
   - Reshape training and test images:
   ```python
   X_train = train_images.reshape((train_images.shape[0], 28, 28, 1))
   X_test = test_images.reshape((test_images.shape[0], 28, 28, 1))
   ```
   - Convert labels to categorical:
   ```python
   y_train = to_categorical(train_labels)
   y_test = to_categorical(test_labels)
   ```

4. **Prepare Input Example**
   ```python
   input_example = np.expand_dims(X_train[0], axis=0)  # Shape (1, 28, 28, 1)
   ```

5. **Instantiate the Model**
   ```python
   model = Sequential()
   ```

6. **Define CNN Layers**
   - **First Block**:
   ```python
   model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', kernel_initializer='he_normal', input_shape=(28, 28, 1)))
   model.add(MaxPooling2D((2, 2)))
   model.add(Dropout(0.25))
   ```
   - **Second Block**:
   ```python
   model.add(Conv2D(128, (3, 3), activation='relu'))
   model.add(Dropout(0.4))
   ```
   - **Flatten and Dense Layers**:
   ```python
   model.add(Flatten())
   model.add(Dense(128, activation='relu'))
   model.add(Dropout(0.3))
   model.add(Dense(10, activation='softmax'))  # Softmax for multi-class classification
   ```

7. **Compile Model**
   ```python
   model.compile(loss=keras.losses.categorical_crossentropy,
                 optimizer=keras.optimizers.Adam(),
                 metrics=['accuracy'])
   ```

8. **Train the Model**
   ```python
   model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))
   ```

9. **Log the Model**
   ```python
   signature = infer_signature(X_test, model.predict(X_test))
   mlflow.tensorflow.log_model(model, 'fashion_mnist_cnn', signature=signature, input_example=input_example)
   ```

### Image Classification Model Training with TensorFlow

1. **Access ML UI**:
   - Navigate to the MLflow UI and refresh the page.
   - Find the new run under the `fashion_images_prediction_tf` experiment.

2. **Run Details**:
   - Click on the run to view model parameters:
     - **Parameters**:
       - Batch size: 32
       - Epochs: 10
   - **Metrics**:
     - Training accuracy: 89.8%
     - Validation accuracy: 90.1%

3. **Logged Artifacts**:
   - Artifacts are logged in the TensorFlow SavedModel format, including:
     - `fashion_mnist_cnn` directory with:
       - `data` and `tensorboard_logs` folders
       - Files: `MLmodel`, `conda.yaml`, `input_example.json`, `python_env.yaml`, `requirements.txt`, `model_summary.txt`

4. **SavedModel Structure**:
   - **Complete TensorFlow program**: Includes trained parameters and computation graph.
   - **Assets directory**: Contains resources for model execution (not TensorFlow variables).
   - **Variables directory**: Holds model parameters (weights and biases).
   - **Model architecture**: Stored in `saved_model.pb` (protocol buffer).

5. **MLmodel File**:
   - Serialized using `python_function` and `tensorflow` flavors.
   - Contains `input_example.json` for input specifications:
     - Input type: tensor
     - Shape: `(-1, 28, 28, 1)` (batch size variable)
     - Output type: tensor with shape `(-1, 10)` (probability scores for classes).

6. **Prediction Process**:
   - Load model using the run ID:
     ```python
     logged_model = f'runs:/{tf_run.info.run_id}/fashion_mnist_cnn'
     loaded_model = mlflow.pyfunc.load_model(logged_model)
     predictions = loaded_model.predict(X_test)
     ```
   - View first 10 predictions:
     ```python
     predictions[:10]
     ```

7. **Detailed Prediction**:
   - First prediction (index 0):
     ```python
     predictions[0]
     ```
   - Highest probability class:
     ```python
     class_names[np.argmax(predictions[0])]
     ```

8. **Display Predictions**:
   - Helper function to display images and predictions:
     ```python
     def show(idx, title):
         plt.figure()
         plt.imshow(X_test[idx].reshape(28, 28))
         plt.axis('off')
         plt.title('\n\n{}'.format(title), fontdict={'size': 16})
     ```
   - Loop through predictions (indices 200 to 250):
     ```python
     for i in range(200, 250):
         predicted_class = np.argmax(predictions[i])
         actual_class = test_labels[i]
         show(i, 'Model prediction {} (class{}), actual category{} (class{})'.format(
             class_names[predicted_class], predicted_class,
             class_names[actual_class], actual_class))
     ```

9. **Model Registration**:
   - Navigate to the MLflow Experiment page and register the model:
     - Choose "Create New Model" and name it `fashion_mnist_prediction_model`.
   - Transition the model to the Staging stage.

10. **Deploying the Model**:
    - Use the following code to move the model to Production:
      ```python
      client = MlflowClient()
      client.transition_model_version_stage(
          name='fashion_mnist_prediction_model',
          version=1,
          stage='Production')
      ```

11. **Accessing Run ID**:
    - Copy the run ID for deployment:
      ```python
      tf_run.info.run_id
      ```

12. **Serving the Model Locally**:
    - Run the following command to serve the model:
      ```bash
      mlflow models serve -m runs:/<run_id>/fashion_mnist_cnn --env-manager local --host 127.0.0.1:1234
      ```

13. **Making Predictions via HTTP**:
    - Prepare the input data:
      ```python
      data = json.dumps({'instances': np.expand_dims(X_test[7], axis=0).tolist()})
      ```
    - Send a request to the prediction endpoint:
      ```bash
      !curl http://127.0.0.1:1234/invocations -H 'Content-Type: application/json' -d '<paste_json_here>'
      ```
    - Parse the prediction result:
      ```python
      predictions = json.loads('<paste prediction string here>')
      class_names[np.argmax(predictions)]
      ```

### Deploying a TensorFlow Model to Azure

#### Prerequisites
To deploy your TensorFlow model to Azure, ensure the following Python libraries are installed:
- `azureml-core`
- `azure-ai-ml`
- `azure-identity`
- `azureml-mlflow`

Use the following commands to install these libraries:
```bash
pip install azureml-core
pip install azure-ai-ml azure-identity
pip install azureml-mlflow
```

#### Creating an Azure Machine Learning Workspace
1. **Workspace Creation Issue**: If you encounter issues while creating a workspace programmatically, consider creating a test workspace via the Azure UI, then deleting it. This can resolve resource group creation problems.

2. **Code for Workspace Creation**:
   ```python
   from azureml.core import Workspace
   
   ws = Workspace.create(
       name='loony-mlflow-tf-ws',
       subscription_id='<your_subscription_id>',
       resource_group='loony-mlflow-rg',
       create_resource_group=False,
       location='eastus'
   )
   ```
   - Wait a few minutes for the workspace to be created.
   - Confirm its creation in the Azure portal under the specified resource group.

#### Launch Azure Machine Learning Studio
- Navigate to the Azure Machine Learning Studio for the created workspace to manage ML tasks.

#### Registering the Model
1. Access the local MLflow UI to find your model artifacts from the experiment (`fashion_images_prediction_tf`).

2. **Copy the Model Artifacts Path**:
   - Use the full path to the artifacts for model registration.

3. **Model Registration Code**:
   ```python
   from azureml.core.model import Model

   model = Model.register(
       workspace=ws,
       model_path='<model_path>',  # Paste the full path here
       model_name='fashion_mnist_classification'
   )
   ```
   - Remove any `file:` prefix from the path to ensure it is an absolute path.

#### Deployment Configuration
1. Import the deployment client:
   ```python
   from mlflow.deployments import get_deploy_client
   
   deploy_config = {'computeType': 'aci'}
   deployment_config_path = 'deployment_config.json'
   
   with open(deployment_config_path, 'w') as outfile:
       outfile.write(json.dumps(deploy_config))
   ```

2. **Setting Up Tracking URI**:
   - Copy the MLflow tracking URI from the Azure portal and set it:
   ```python
   client = get_deploy_client('<ws_tracking_url>')  # Replace with your URI
   mlflow.set_tracking_uri('<ws_tracking_url>')
   ```

3. **Creating the Deployment**:
   ```python
   config = {'deploy-config-file': deployment_config_path}
   model_name = 'fashion_mnist_classification'
   model_version = 1

   client.create_deployment(
       model_uri=f'models:/{model_name}/{model_version}',
       config=config,
       name='fmnist-aci-deployment'
   )
   ```
   - Authenticate if prompted, and wait for the deployment to complete.

#### Using the Deployed Model
1. **Accessing the REST API**:
   - Copy the REST endpoint from the Azure portal under the Consume tab.
   - Replace `<REST_API>` in your code with this endpoint.

2. **Making Predictions**:
   ```python
   import urllib.request
   import json
   import numpy as np

   def allowSelfSignedHttps(allowed):
       # Implementation for self-signed HTTPS verification

   data = {
       # Your input data for prediction
   }

   url = '<REST_API>'
   body = json.dumps(data).encode('utf-8')
   headers = {'Content-Type': 'application/json'}

   req = urllib.request.Request(url, body, headers)
   response = urllib.request.urlopen(req)
   result = response.read()

   prediction = np.argmax(json.loads(result))
   print(class_names[prediction])  # Replace with your class names
   ```

With this setup, you've successfully deployed your TensorFlow model to Azure and can now use the endpoint for predictions.

This demo focuses on using PyTorch and PyTorch Lightning to train an image classification model with the FashionMNIST dataset. Here's a summary of the key steps involved in setting this up:

 1. **Environment Setup**
- **Install Required Libraries**:
  - Use `pip install pytorch-lightning==2.0.2` to install PyTorch Lightning.
  - Use `pip install torchvision` to install the torchvision library, which provides access to datasets, transforms, and pre-trained models.

 2. **Import Necessary Libraries**
- Import PyTorch and related libraries:
  ```python
  import torch
  import torchvision
  import pytorch_lightning as pl
  from torch.nn import functional as F
  from torch.utils.data import DataLoader
  from torchvision import transforms
  from torchvision.datasets import FashionMNIST
  import mlflow.pytorch
  ```

 3. **Define Class Names**
- Create a list for the categories in the FashionMNIST dataset:
  ```python
  class_names = ['T_shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
  ```

 4. **Load FashionMNIST Dataset**
- Load the training dataset and apply transformations:
  ```python
  train_ds = FashionMNIST(os.getcwd(), train=True, download=True, transform=transforms.ToTensor())
  train_loader = DataLoader(train_ds, batch_size=10)
  ```

 5. **Visualize Sample Images**
- Define a function to visualize images:
  ```python
  def imshow(img):
      npimg = img.numpy()
      plt.imshow(np.transpose(npimg, (1, 2, 0)))
      plt.show()
  ```
- Retrieve a batch of images and display them:
  ```python
  dataiter = iter(train_loader)
  images, labels = next(dataiter)
  imshow(torchvision.utils.make_grid(images, nrow=10, normalize=True))
  print(' '.join(f'{class_names[labels[j]]:5s}' for j in range(10)))
  ```

 6. **Check Shapes of Images and Labels**
- Verify the dimensions of the loaded data:
  ```python
  images.shape, labels.shape
  ```

 7. **Understanding Data Shapes**
- The shape of the images tensor is `(10, 1, 28, 28)`, where:
  - 10 is the batch size,
  - 1 is the number of channels (grayscale),
  - 28 is the height and width of the image.
- The labels tensor shape is `(10,)`, corresponding to one label for each image in the batch.


### Setting Up MLflow Experiment in PyTorch

1. **Create and Set Experiment**
   ```python
   experiment_id = mlflow.create_experiment(name='fashion_images_prediction_pytorch')
   mlflow.set_experiment(experiment_name='fashion_images_prediction_pytorch')
   ```

### Defining the Convolutional Neural Network (CNN)

2. **Model Class Definition**
   - Define a class `FashionCNN` inheriting from `pl.LightningModule`.

   ```python
   class FashionCNN(pl.LightningModule):
   ```

3. **Initialization Method**
   - Initialize data directory and transformations in the `__init__` method.
   ```python
   def __init__(self, data_dir=os.getcwd()):
       super(FashionCNN, self).__init__()
       self.data_dir = data_dir
       self.transform = transforms.ToTensor()
   ```

4. **Convolutional Layers**
   - Define layers using `nn.Sequential`.
   ```python
   self.layer1 = nn.Sequential(
       nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1),
       nn.BatchNorm2d(32),
       nn.ReLU(),
       nn.MaxPool2d(kernel_size=2, stride=2)
   )
   self.layer2 = nn.Sequential(
       nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3),
       nn.BatchNorm2d(64),
       nn.ReLU(),
       nn.MaxPool2d(2)
   )
   ```

5. **Fully Connected Layers**
   - Add linear layers and dropout for regularization.
   ```python
   self.fc1 = nn.Linear(in_features=64*6*6, out_features=600)
   self.drop = nn.Dropout(0.25)
   self.fc2 = nn.Linear(in_features=600, out_features=120)
   self.fc3 = nn.Linear(in_features=120, out_features=10)
   ```

### Forward Pass and Training Steps

6. **Forward Method**
   - Define how data passes through the model.
   ```python
   def forward(self, x):
       out = self.layer1(x)
       out = self.layer2(out)
       out = out.view(out.size(0), -1)  # Flatten
       out = self.fc1(out)
       out = self.drop(out)
       out = self.fc2(out)
       return self.fc3(out)
   ```

7. **Training Step**
   - Implement the training logic.
   ```python
   def training_step(self, batch, batch_nb):
       x, y = batch
       logits = self(x)
       loss = F.cross_entropy(logits, y)
       pred = logits.argmax(dim=1)
       acc = accuracy(pred, y, task='multiclass', num_classes=10)
       self.log('train_loss', loss, on_epoch=True)
       self.log('train_acc', acc, on_epoch=True)
   ```

### Validation and Testing

8. **Validation and Test Steps**
   - Similar to the training step but for validation and testing datasets.

   ```python
   def validation_step(self, batch, batch_nb):
       ...
   def test_step(self, batch, batch_nb):
       ...
   ```

### Data Preparation and Loading

9. **Prepare Data**
   - Download and set up the FashionMNIST dataset.
   ```python
   def prepare_data(self):
       FashionMNIST(os.getcwd(), train=True, download=True)
       FashionMNIST(os.getcwd(), train=False, download=True)
   ```

10. **Data Loaders**
    - Create data loaders for training, validation, and testing.
    ```python
    def train_dataloader(self):
        return DataLoader(self.fmnist_train, batch_size=64, num_workers=2)
    ```

### Model Training and Logging

11. **Training Setup**
    - Instantiate the model and trainer, and configure MLflow logging.
    ```python
    fmnist_model = FashionCNN()
    trainer = pl.Trainer(max_epochs=5)
    mlflow.pytorch.autolog(log_models=False)
    ```

12. **Training Execution**
    - Train and test the model, logging relevant information.
    ```python
    with mlflow.start_run():
        trainer.fit(fmnist_model)
        trainer.test()
    ```

13. **Logging Model Signature**
    - Define input and output schemas for the model.
    ```python
    input_schema = Schema([TensorSpec(np.dtype(np.float32), (-1, 1, 28, 28))])
    output_schema = Schema([TensorSpec(np.dtype(np.float32), (-1, 10))])
    signature = ModelSignature(inputs=input_schema, outputs=output_schema)
    ```

14. **Log the Model**
    ```python
    mlflow.pytorch.log_model(fmnist_model, 'model-cnn', signature=signature)
    ```

### MLflow Model Evaluation and Prediction Process

#### Accessing the MLflow UI
1. Navigate to the **MLflow UI**.
2. Open the **fashion_images_prediction** experiment.
3. Click on the single run to examine the **Parameters** and **Metrics**.
   - **Parameters**: E.g., number of epochs (5).
   - **Metrics**: 
     - Training accuracy (`train_acc`): 87.3%
     - Test accuracy (`test_acc`): 84.9%
     - Validation accuracy (`val_acc`): 85%
   - **Tags**: `Mode` is set to **testing**.

#### Examining Artifacts
1. Locate the **Artifacts** folder, default path: `model-cnn`.
2. **Model Schema**:
   - **Inputs**: Images passed to the model.
   - **Outputs**: Predictions from the model.
3. **Serialized Model**: 
   - `model.pth` contains the learned parameters (weights and biases).
4. **MLmodel File**:
   - Logged using `python_function` and `pytorch` flavors.
   - Input signature: Batch of grayscale images (28x28).
   - Output signature: Probability scores for 10 classes.
5. **Model Summary**: `model_summary.txt` specifies layers and parameters.

#### Deserializing and Making Predictions
1. **Accessing Test Data**:
   - Use `iter()` on the `test_dataloader`.
   - Get the second batch: 
     ```python
     it = iter(fmnist_model.test_dataloader())
     next(it)  # Skip the first batch
     test_imgs, test_labels = next(it)  # Get the second batch
     ```
   - Confirm shape of `test_imgs` (should be 64 images).

2. **Retrieve Run ID**:
   ```python
   run_id = mlflow.last_active_run().info.run_id
   ```

3. **Load the Model**:
   ```python
   logged_model = f'runs:/{run_id}/model-cnn'
   loaded_model = mlflow.pyfunc.load_model(logged_model)
   predictions = loaded_model.predict(test_imgs.numpy())
   ```
   - Check shape of predictions (should be 64x10).

#### Analyzing Predictions
1. **Logits vs. Probabilities**:
   - Logits are unnormalized outputs; use `np.argmax()` to find the predicted class.
   - Example:
     ```python
     predicted_class = np.argmax(predictions[4])
     ```
   - Class names can be accessed using indices.

2. **Visualize Predictions**:
   - Define a helper function to show images:
     ```python
     def show(idx, title):
         plt.figure()
         plt.imshow(test_imgs.squeeze()[idx].numpy())
         plt.axis('off')
         plt.title('\n\n{}'.format(title), fontdict={'size': 16})
     ```
   - Loop through images and display predictions:
     ```python
     for i in range(64):
         predicted_class = np.argmax(predictions[i])
         actual_class = test_labels[i]
         show(i, f'Model prediction: {class_names[predicted_class]} (class {predicted_class}), actual category: {class_names[actual_class]} (class {actual_class})')
     ```

#### Registering the Model
1. Go to the MLflow UI and click on **Register Model**.
2. Create a new model: **fmnist-image-predictor**.
3. Check the **Models** tab to see **Version 1** of the model.

#### Serving the Model
1. Transition the model to **Production stage** in the MLflow UI.
2. Use the following command in the terminal to serve the model:
   ```bash
   mlflow models serve -m runs:/{run_id}/model-cnn --env-manager local --host 127.0.0.1:1234
   ```

#### Making Predictions via REST API
1. Prepare the input for the prediction endpoint:
   ```python
   data = json.dumps({"instances": test_imgs[4].unsqueeze(dim=0).tolist()})
   ```
2. Use `curl` to send a request to the prediction endpoint:
   ```bash
   curl http://127.0.0.1:1234/invocations -H 'Content-Type: application/json' -d '<paste_output_here>'
   ```
3. Extract and analyze the logits from the response:
   ```python
   predictions = json.loads('<paste_predictions_here>')['predictions'][0]
   predicted_label = class_names[np.argmax(predictions)]
   ```

This structured approach enables efficient evaluation and deployment of your machine learning model using MLflow.

### Introduction to Large Language Models (LLMs) and MLflow

**Large Language Models (LLMs)**:
- LLMs are designed for understanding and generating human language.
- Trained on extensive text data, they perform tasks like:
  - Text generation
  - Machine translation
  - Sentiment analysis
- As of mid-2023, LLMs are a significant trend in AI.

**MLflow Enhancements**:
- MLflow 2.3 introduces features for logging and tracking LLMs.
- New model flavors supported:
  - **HuggingFace Transformers**
  - **OpenAI Functions**
  - **LangChain**

### Demo: Tracking a Pre-trained Transformer Model

**Overview of Transformers**:
- Transformers revolutionized NLP by effectively capturing contextual relationships in text.
- They use a self-attention mechanism to weigh the importance of words or tokens in sequences.

**Using HuggingFace for Sentiment Analysis**:
1. **Installation**: Install the Transformers library.
   ```python
   !pip install transformers
   ```

2. **Creating an Experiment**:
   ```python
   import mlflow
   experiment_id = mlflow.create_experiment(name='sentiment_analysis_transformers')
   mlflow.set_experiment(experiment_name='sentiment_analysis_transformers')
   ```

3. **Accessing Pre-trained Model**:
   - Load the **DistilBERT** model for text classification.
   - Instantiate the sentiment analysis pipeline:
   ```python
   import transformers
   sentiment_analysis_pipeline = transformers.pipeline(model='distilbert-base-uncased-finetuned-sst-2-english')
   ```

4. **Logging the Model**:
   - Use MLflow to log the pipeline:
   ```python
   with mlflow.start_run(run_name='Sentiment Analysis'):
       model_info = mlflow.transformers.log_model(
           transformers_model=sentiment_analysis_pipeline,
           artifact_path='Sentiment Analyzer',
           input_example='This is an amazing movie.'
       )
   ```

### Viewing Model Artifacts
- Navigate to the experiment to check logged model artifacts.
- **Model Schema**: Input and output types are both strings.
- **Metadata**: Includes tokenizer details, model configuration, and vocabulary.
- **Model Card**: Contains important information about the model's intended use and ethical considerations.

### Using the Logged Model for Predictions
1. **Load the Model**:
   ```python
   sentiment_analysis_model = mlflow.pyfunc.load_model(model_info.model_uri)
   ```

2. **Make Predictions**:
   - Positive sentiment example:
   ```python
   sentiment_analysis_model.predict('The weather is now so pleasant.')  # Output: 'POSITIVE'
   ```
   - Negative sentiment example:
   ```python
   sentiment_analysis_model.predict('The batting performance of the team was terrible.')  # Output: 'NEGATIVE'
   ```
   - Another positive example:
   ```python
   sentiment_analysis_model.predict('We are planning a fun picnic today.')  # Output: 'POSITIVE'
   ```
   - Negative sentiment example:
   ```python
   sentiment_analysis_model.predict('It was way too tiring a journey with not much to show for it.')  # Output: 'NEGATIVE'
   ```