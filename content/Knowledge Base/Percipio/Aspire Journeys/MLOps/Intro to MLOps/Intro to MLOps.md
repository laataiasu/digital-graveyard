---
date: 2001-01-01
---

# Intro to MLOps

### Core Learning Content

#### DevOps Overview
- **DevOps Definition**: A set of practices that combines software development (Dev) and IT operations (Ops) to improve efficiency, quality, and speed of software development.
- **Importance**: Aims to streamline and automate the deployment, management, and monitoring of software.

#### MLOps Overview
- **MLOps Definition**: Machine Learning Operations, practices to productionize machine learning systems by bridging development and operations.
- **Key Point**: Machine learning models require frequent retraining on the latest data, making MLOps essential.

#### Traditional Software Development Challenges
- **Historical Context**: Development cycles were long, often taking months or years due to limited resources and libraries.
- **Agile Methodology**: Introduced flexibility, collaboration, and iterative processes, enabling quicker releases and customer feedback.

#### DevOps Principles
- **Integration with Agile**: DevOps emerged from Agile, emphasizing collaboration among developers, testers, and operations.
- **Collaboration and Accountability**: All teams work together throughout the product lifecycle, promoting shared ownership and accountability.
- **Automation**: Critical for enabling faster feedback loops and quick software improvements.

#### Key Components of DevOps Culture
1. **Collaboration**: Teams share processes, priorities, and concerns early and often.
2. **Visibility**: Transparent communication among teams to align on goals.
3. **Continuous Learning**: High-performing teams adopt a growth mindset, learning from failures and iterating on their processes.

#### DevOps Practices
1. **Continuous Integration (CI)**: Automates code integration into a central repository, enabling frequent testing and quicker bug resolution.
2. **Continuous Delivery (CD)**: Extends CI by automatically deploying tested code changes to a staging or production environment.
3. **Infrastructure as Code (IaC)**: Manages infrastructure through code for consistent and efficient provisioning.
4. **Microservices Architecture**: Develops applications as independent services that communicate via APIs.
5. **Monitoring**: Tracks the entire lifecycle from development to operations, allowing for rapid identification and resolution of issues.

#### CI/CD Overview
- **Flow**: The CI/CD process involves application code, builds, tests, and deployments, facilitated through a centralized version control system like Git.
- **Automation Steps**:
  - **Build**: Automated code build to catch bugs early.
  - **Testing**: Automated execution of unit and integration tests.
  - **Deployment**: Fully automated deployment to production following successful tests.

#### MLOps vs. DevOps
- **Differences**: MLOps includes the complexities of handling real-world data, requiring ongoing model retraining and adaptation.
- **Challenges**: MLOps faces additional hurdles beyond those in DevOps due to the unpredictability of data and the need for continuous model management.

By understanding and implementing these principles and practices, teams can enhance their development and operational efficiencies in both software and machine learning environments.

### Key Differences Between MLOps and DevOps

#### MLOps Complexity
- **Data Dependency**: MLOps focuses on machine learning models that require training on real-world, constantly evolving data, unlike the controlled environments typical of DevOps.
- **Adoption Stage**: MLOps is less mature than DevOps, with many machine learning models remaining in the prototyping and testing phases.

#### Machine Learning Workflow
- **Complex Infrastructure**: MLOps involves intricate workflows including data collection, preparation, validation, and specialized hardware management.
- **Monitoring Requirements**: Continuous monitoring of data quality and prediction accuracy is essential.

#### Inputs to a Machine Learning Model
- **Inputs**: A machine learning model is trained using both **data** and **code**.
  - **Data**: Evolving and unpredictable, sourced from real-world scenarios.
  - **Code**: Known and predictable, derived from traditional software practices.

#### Divergence Between Code and Data
- **Evolution Paths**: Code evolves predictably within a controlled environment, while data evolves in unpredictable ways based on real-world changes.
- **Challenge in MLOps**: The mismatch in evolution makes automation and productionization complex.

#### Surrounding Ecosystem
- **Complex Interdependencies**: Machine learning systems consist of not only ML code but also various components such as data collection, verification, feature extraction, configuration, monitoring, and resource management.
- **Data Dependency Costs**: Data dependencies are often more expensive and harder to track than code dependencies.

#### Model Quality and Data Management
- **Quality Control**: The quality of a machine learning model is directly tied to the quality of the data used for training.
- **Feature Correlation**: Features in training data can have varying levels of relevance, affecting model performance and making it challenging to identify useful versus redundant features.

#### Model Decay
- **Ongoing Maintenance**: Machine learning models degrade over time as real-world data changes. Continuous retraining is necessary to ensure models reflect the current state of the world.
- **Assumption Changes**: Evolving business objectives or new information may necessitate changes in model architecture or even the creation of entirely new models.

#### Conclusion
- **Dynamic Nature of MLOps**: Unlike traditional software, machine learning models require a dynamic approach to development, emphasizing the importance of robust data management and continual model updates to maintain relevance and accuracy.

### Factors Affecting Machine Learning Models in Production

1. **Data Quality**
   - Machine learning models are sensitive to the quality, semantics, and completeness of input data.
   - The principle "garbage in, garbage out" applies: models are only as good as the training data.

2. **Model Decay**
   - Model performance deteriorates over time due to changes in real-world data that weren't represented during training.

3. **Locality**
   - Models may underperform for new business customers or use cases, especially if trained on different demographics.

### MLOps: An Intersection of Fields
- **Venn Diagram Representation**: MLOps lies at the intersection of machine learning, DevOps, and data engineering.

### Challenges in Deploying Machine Learning Models

1. **Data Quality and Consistency**
   - Ensuring input data in production matches the training data's distribution and quality is challenging.
   - Issues like inconsistencies, missing values, and outliers can impact model performance.

2. **Scalability**
   - ML models must handle large data volumes in real-time and manage concurrent user requests, requiring scalable infrastructure.

3. **Versioning**
   - Unlike traditional software, versioning in MLOps involves managing models, data, and code.
   - Efficient strategies for model storage, updates, and backward compatibility are crucial.

4. **Monitoring**
   - Continuous monitoring for model degradation, data drift, and input distribution changes is vital to maintain performance.

5. **Deployment Environment Management**
   - Addressing resource constraints, security requirements, and compliance regulations is necessary for successful deployment.

6. **Interpretability and Explainability**
   - Understanding model decisions is critical for trust, compliance, and debugging, especially with complex models like neural networks.

7. **Maintenance and Updates**
   - ML models require constant retraining and lifecycle management, complicating maintenance compared to static software systems.

8. **Reproducibility**
   - Ensuring consistent results for debugging and auditing involves tracking dependencies and model configurations.

### Team Dynamics
- **ML Teams vs. Software Teams**: ML teams often consist of data scientists and researchers with less software development experience, emphasizing experimentation and iterative improvement.

### Testing Machine Learning Models
- Model testing is comprehensive, involving:
  - Data validation tests
  - Data integrity tests
  - Model quality tests

### Continuous Integration and Delivery in MLOps
- **Continuous Integration (CI)**:
  - Involves validating not only code but also data schemas and models.
  
- **Continuous Delivery (CD)**:
  - Focuses on the entire ML training pipeline and model prediction services.

- **Continuous Training (CT)**:
  - Unique to ML, this process involves automatically retraining and serving models with new data.

### Step-by-Step Approach to Solving Machine Learning Problems

1. **Understand the Business Use Case**
   - Begin by identifying the business problem you’re trying to solve. This foundational step mirrors traditional software development.
   - **Key Question**: How expensive are wrong predictions? Since machine learning outputs are probabilistic, understanding the cost of errors is crucial. Ensure the business case allows for some tolerance of error before pursuing ML solutions.

2. **Define the Workflow**
   - Outline a high-level workflow for your solution without initially focusing on technology.
   - Determine if AI/ML is suitable for the identified workflow.
   - Identify specific processes powered by machine learning within the broader workflow, detailing inputs and outputs.

3. **Break Down the Process**
   - Decompose the identified process into manageable tasks that can be automated. Not all tasks will require machine learning; evaluate each one individually.
   - For tasks that can benefit from ML, quantify the return on investment (ROI). This assessment should consider the entire lifecycle of ML, including data collection, validation, and training, which can be resource-intensive.

4. **Use the Machine Learning Canvas**
   - Implement the Machine Learning Canvas, a structured tool introduced by Louis Dorard, to organize and clarify your ML project.
   - The canvas connects business goals to specific ML tasks, ensuring that your efforts align with end-user needs. It emphasizes building ML solutions for practical purposes rather than for technology’s sake.

### Key Points to Remember
- **Iterative Exploration**: ML projects often require iterative exploration and adjustments based on findings and business needs.
- **Focus on Outcomes**: Ensure that your project’s vision is centered on delivering value to end users, which helps prevent unnecessary complexity.
- **Resource Consideration**: Be mindful of the resources involved in implementing ML solutions, and strive for clarity and structure in your discussions with stakeholders.

By following these steps, you create a solid foundation for developing effective machine learning solutions that are closely aligned with business objectives.

### The Machine Learning Canvas: Components and Considerations

The Machine Learning Canvas consists of ten essential components that guide the development of effective ML systems. Each component serves a specific purpose and helps ensure that the ML solution aligns with business objectives and user needs.

#### 1. **Value Proposition**
   - **What is the Problem?** Identify the specific issue your ML system addresses.
   - **Why is it Important?** Articulate the value the system provides to users.
   - **Who is the End User?** Define the personas who will benefit from the solution.

#### 2. **Data Sources**
   - Identify internal and external data sources available for training your model.
   - Consider the costs of storing and accessing data, including any potential fees for external data.

#### 3. **Data Collection**
   - Assess the costs and processes involved in collecting new data.
   - Determine how data will be labeled—manually or programmatically—and whether a Human-in-the-loop (HITL) approach will be necessary.

#### 4. **Feature Engineering**
   - Identify the key features that will represent your data in the model.
   - Engage domain experts to help select significant features and plan for any required preprocessing.

#### 5. **Prediction Task**
   - Define whether your model will use supervised or unsupervised learning techniques.
   - Clarify the type of input data (e.g., text, images) and the expected output (e.g., classifications, recommendations).

#### 6. **Making Predictions**
   - Establish when and how predictions will be made available (e.g., real-time, batch processing).
   - Consider the computational costs involved in making predictions and whether HITL support will be included.

#### 7. **Decisions**
   - Outline how predictions will be used in decision-making processes.
   - Identify potential hidden costs associated with these decisions, especially if they involve HITL validation.

#### 8. **Building Models**
   - Determine how often your model needs to be retrained based on the importance of using up-to-date data.
   - Assess the resources and time required for retraining, along with the scaling needs for increased demand.

#### 9. **Offline Evaluation**
   - Set up evaluation metrics (both domain-specific and technical) to assess the model’s performance before deployment.
   - Consider the impact of false positives and negatives, and ensure you have a robust testing dataset.

#### 10. **Live Monitoring and Evaluation**
   - After deployment, continuously monitor the model's performance against defined metrics.
   - Consider A/B testing to compare the model's effectiveness against existing solutions and track overall value creation.

### Deployment Timing: Balancing Risks and Benefits
- **Early Deployment**: Accelerates learning by leveraging real-world data but risks damaging the brand with poor predictions.
- **Late Deployment**: Allows for improved in-house performance but may slow the model's learning curve.

Finding a balance is crucial; aim to deploy a well-tested model that minimizes risks while still allowing for iterative improvements.

### Overview of the Machine Learning Workflow

Building and training machine learning models involves a structured workflow comprising three main artifacts: data, the model, and code. Here’s a detailed look at the components and steps involved in this workflow.

### 1. Data Pipeline
The data pipeline is the foundational step in any machine learning project. It involves multiple stages:

- **Data Acquisition**: Collecting data from various sources, which can be in different formats. This step can be resource-intensive and time-consuming.

- **Exploration & Validation**: Understanding the data through profiling, which provides statistical and descriptive summaries. This helps identify issues like missing values or outliers.

- **Cleaning & Wrangling**: This crucial step involves fixing inconsistencies, imputing missing values, and detecting outliers to ensure the data is usable.

- **Data Labeling**: For supervised learning, the data must be labeled, which can be a labor-intensive process. Labeling can be done manually or programmatically, with each method having its challenges.

- **Data Splitting**: Once the data is clean and labeled, it is split into training and testing sets to validate model performance.

### 2. Model Pipeline
The model pipeline is where the core machine learning processes occur:

- **Model Training**: This step involves selecting an ML algorithm and feeding the prepared data into it. It often requires experimentation with feature engineering and hyperparameter tuning.

- **Model Evaluation**: After training, the model is evaluated against predefined metrics to ensure it meets the project’s objectives. This helps assess its accuracy and effectiveness.

- **Testing**: The model is rigorously tested to check for biases and errors, ensuring it produces acceptable results.

- **Model Packaging**: The final, trained model is exported into a serialized format that includes its parameters. This packaged model will be used for predictions.

- **Integration**: The model is integrated into the software product, which involves a separate software pipeline with its own CI/CD processes.

### 3. Software Code Pipeline
The software code pipeline connects the ML model to the product it serves:

- **Model Serving**: The packaged model is deployed in a production environment to make predictions on live data.

- **Monitoring & Logging**: Continuous monitoring of model performance is essential to track its effectiveness over time. Logging every inference helps in debugging and understanding model behavior.

- **Retraining**: Monitoring helps identify when the model needs retraining based on its performance with new data.

### Conclusion
The machine learning workflow is complex and involves interrelated steps across three main artifacts: data, the model, and code. Each component is critical to the overall success of the ML system. By meticulously following these steps and maintaining a focus on integration and performance monitoring, organizations can build robust ML solutions that deliver value in real-world applications.

### Machine Learning Architectural Patterns

Understanding the various architectural styles for operating machine learning models is essential for designing effective systems. We'll explore four architectural patterns based on two key dimensions: **model training** and **model prediction**.

### Dimensions of ML Architectural Patterns

1. **Model Training**
   - **Offline Learning (Static Learning)**: The model is trained on a pre-collected dataset stored in a file system or database. This data is historical and the model is trained periodically. However, models can decay over time due to changes in underlying data trends.
   - **Online Learning (Dynamic Learning)**: The model is continuously updated as new data comes in. This approach helps keep the model relevant and reduces decay by incorporating real-time information.

2. **Model Prediction**
   - **Batch Predictions**: The model processes a batch of records at once, making predictions for all entries in the batch. This is suitable for non-time-sensitive data.
   - **Real-time Predictions (On-demand)**: Predictions are made instantaneously based on the current input data. This is crucial for applications that require immediate responses.

### Four Architectural Patterns

These dimensions combine to create four architectural patterns:

1. **Forecast Workflow**
   - **Training**: Offline (Static Learning)
   - **Prediction**: Batch
   - **Use Case**: Commonly used for research and experimentation, where models are trained on historical data and predictions are made on similar past data.

2. **Web Service**
   - **Training**: Offline (Static Learning)
   - **Prediction**: Real-time (On-demand)
   - **Use Case**: This is the most prevalent architecture, where a model trained on historical data serves predictions via a REST API. Ideal for applications requiring quick responses to individual requests.

3. **Real-time Analysis (Online Learning)**
   - **Training**: Online (Dynamic Learning)
   - **Prediction**: Real-time (On-demand)
   - **Use Case**: This architecture continuously updates the model with incoming data, allowing it to adapt in real time. Useful for environments that demand constant model improvement.

4. **Automated Machine Learning (AutoML)**
   - **Training**: Online (Dynamic Learning)
   - **Prediction**: Real-time (On-demand)
   - **Use Case**: This cutting-edge architecture automates the model training process with minimal user intervention, making it accessible to users without deep machine learning expertise.

### Model Serialization Formats

When deploying models, it's essential to serialize them for use. Serialization formats can be divided into:

- **Language-Agnostic Formats**: These allow models to be packaged and run across different platforms.
- **Vendor-Specific Formats**: These are tied to specific frameworks, such as:
  - Scikit-learn: Saves models as pickled Python objects.
  - TensorFlow: Uses `.pb` files.
  - PyTorch: Uses `.pt` files.

### Model Serving Patterns

Once the model is serialized, you can integrate it into your application using different serving patterns:

1. **Model as a Service**: The model is deployed as an independent microservice accessed through an API. This allows for flexible integration with various applications.

2. **Model as a Dependency**: The model acts like a library within an application. This is more tightly coupled than a microservice.

3. **Precompute Serving**: Predictions are precomputed for a batch of data and stored. When requested, these results are retrieved from a database, ideal for static datasets.

4. **Model On-Demand**: Utilizes a message broker to manage requests, allowing for runtime dependencies rather than direct code dependencies.

5. **Federated Learning (Hybrid Serving)**: Combines global and local models. A shared model updates based on insights from individual user models, maintaining privacy while leveraging community data trends.

### MLOps Maturity Levels

When developing an ML system within an organization, it's essential to understand the maturity levels of MLOps (Machine Learning Operations). This framework helps gauge the automation and efficiency of your ML workflows. Here’s a breakdown of the three levels of MLOps maturity, starting with Level 0.

#### MLOps Level 0: Manual Process

At **MLOps Level 0**, the entire ML process is manual, with no automation in place. Here's a high-level overview of this stage:

- **Workflow Characteristics**:
  - **Manual Steps**: Each part of the workflow, from data extraction to model training, validation, and serving, is performed manually or through script-driven processes. Human intervention is needed at every step.
  - **Siloed Teams**: Data scientists and ML researchers work separately from the operations teams. This separation can lead to communication gaps and inefficiencies.
  - **Infrequent Releases**: Model deployments are ad hoc and not streamlined, resulting in sporadic updates and slow iterations.

- **Challenges**:
  - **Limited Monitoring**: There’s minimal tracking of model performance, making it difficult to detect issues like model degradation or concept drift.
  - **Brittle Deployments**: Manual processes increase the risk of errors, and without regular updates, the models may become outdated or irrelevant.
  - **Concept Drift**: If the model doesn’t adapt to new data or changing real-world conditions, its performance may decline, leading to ineffective predictions.

MLOps Level 0 can be sufficient for prototypes or systems serving a limited user base, but it lacks scalability and reliability for production-level applications.

### Moving Beyond Level 0

To evolve from Level 0, organizations typically progress through subsequent levels of maturity:

#### MLOps Level 1: Basic Automation

At this level, some automation is introduced, but many processes still require manual oversight. Key characteristics include:

- **Automated Steps**: Certain parts of the workflow, such as data preprocessing or model training, may be automated to reduce manual effort.
- **Improved Collaboration**: There’s a greater integration between data science and operations teams, leading to more streamlined workflows.
- **Basic Monitoring**: Some performance tracking is implemented, allowing teams to identify issues more readily.

#### MLOps Level 2: Continuous Training

Organizations at this level have established a more robust pipeline:

- **Continuous Training**: The model is regularly retrained with new data to ensure it remains relevant and effective.
- **CI/CD Practices**: Continuous integration and continuous delivery (CI/CD) pipelines are put in place, allowing for more frequent and reliable deployments.
- **Proactive Monitoring**: Enhanced performance monitoring enables teams to detect drifts and issues more quickly.

#### MLOps Level 3: Fully Automated

At **MLOps Level 3**, the process is fully automated, representing a mature MLOps environment:

- **End-to-End Automation**: All aspects of the ML workflow, from data ingestion to model serving, are automated with minimal human intervention.
- **Real-Time Adaptation**: Models can adapt to changes in data and environment automatically, reducing the risk of obsolescence.
- **High Velocity**: The organization can rapidly iterate on models, leading to timely updates and continuous improvements in model performance.

### MLOps Level 1: Automated Machine Learning Pipelines

In this video, we delve into **MLOps Level 1**, where the focus is on automating the machine learning (ML) pipeline while still maintaining some manual processes for software code. At this level, organizations aim for continuous training of their ML models to enable seamless delivery of prediction services.

#### Key Features of MLOps Level 1

1. **Automated ML Pipeline**:
   - The machine learning pipeline is automated, allowing for the continuous training and serving of models based on incoming data.
   - Automated components include:
     - **Data Extraction and Preparation**: This step gathers and processes new data for model training.
     - **Model Training and Validation**: Models are trained on the new data and validated for performance.
     - **Model Registry**: Trained models are stored for deployment.

2. **Orchestrated Experimentation**:
   - The ML experiment phase is orchestrated, facilitating the transition between different steps, like data validation, model training, and evaluation.
   - Although some steps are automated, complete automation is not yet achieved, and testing still requires manual intervention.

3. **Modularized Code**:
   - Code for different pipeline components is modularized, making it easier to manage and maintain.
   - However, exploratory data analysis may still reside in notebooks, and code reproducibility between development and production environments is crucial.

4. **Automated Trigger Mechanisms**:
   - The pipeline can trigger model retraining based on various factors, such as new data availability or performance degradation, enhancing the model's adaptability.

#### Characteristics of the Automated Pipeline

- **Data Validation**: Automatically checks for data schema and value skews, determining whether the pipeline should continue or retrain the model.
- **Model Validation**: After training, the model's performance is assessed to ensure it meets the required standards before production deployment.
- **Feature Store**: An optional centralized repository that allows data scientists to reuse features across models, enhancing efficiency.

#### Challenges at MLOps Level 1

- **Manual Deployment of Changes**: Any updates to the pipeline require manual deployment, which can be cumbersome and error-prone.
- **Testing Limitations**: Because model code changes are not automated, testing can be manual and may lead to inconsistencies if changes occur frequently.
- **Integration Gaps**: While the ML pipeline is automated, integration with broader software development practices may not be, leading to inefficiencies.

---

### Transitioning to MLOps Level 2: Fully Automated Pipelines

In the next phase, **MLOps Level 2**, organizations achieve full automation of their ML workflows through Continuous Integration and Continuous Delivery (CI/CD). Here’s what this entails:

#### Key Features of MLOps Level 2

1. **Complete Automation**:
   - Every aspect of the ML pipeline, including model training, testing, and deployment, is automated.
   - CI/CD processes ensure that any code changes trigger automated builds and tests.

2. **Smooth Workflow Orchestration**:
   - The transition between experiment steps is fully automated, leading to a seamless workflow that enhances productivity.

3. **Robust Testing Framework**:
   - Continuous integration includes unit and integration testing for all changes, ensuring code reliability before deployment.
   - Continuous delivery automates the movement of artifacts through different environments (development, staging, production).

4. **Retention of Features from Level 1**:
   - All features present in Level 1, such as data validation and model retraining triggers, are retained and enhanced.

#### Conclusion

By progressing from **MLOps Level 0** through **Level 1** to **Level 2**, organizations can greatly enhance their machine learning capabilities. Each level builds upon the previous one, allowing for greater efficiency, faster deployments, and improved model performance. As automation increases, the complexity of managing ML systems decreases, enabling teams to focus on innovation and performance rather than manual processes.