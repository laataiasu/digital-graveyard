# Basic Analytical Methods

**Fundamental Methods of Statistical Analysis**

**Distribution**
- **Definition**: Measures the frequency of occurrences within a scale.
- **Example**: Apparel retailers analyze shirt size distribution and sales channels (online vs. in-store).
- **Visualization**: Frequency distributions are often represented using pie charts and bar charts.
  
**Key Measures of Central Tendency**: The three M's
1. **Mean**: Numerical average of all occurrences.
2. **Median**: Midpoint where 50% of occurrences lie below and 50% above.
3. **Mode**: The most frequently occurring value; can have multiple modes.

**Patterns of Distribution**:
1. **Uniform Distribution**: Equal probability across outcomes (e.g., rolling a die).
2. **Binomial Distribution**: Two possible outcomes (e.g., online vs. in-store sales).
3. **Normal Distribution**: Follows a bell curve; most occurrences are near the average, with "tails" at extremes.

**Characteristics of Normal Distribution**:
- In a perfectly normal distribution, mean, median, and mode are identical.
- Skewness indicates how distribution deviates from normal:
  - **Left Skew**: Mode > Median > Mean (e.g., heights of basketball players).
  - **Right Skew**: Mean > Median > Mode (e.g., heights of jockeys).

**Bimodal Distribution**: Shows two peaks, indicating two different groups or behaviors (e.g., student grades).

**Caution**: Ensure data is sufficient and representative; small or skewed samples can lead to inaccurate conclusions.

---

**Deviation**
- **Definition**: Measures how far occurrences are from the average.
- **Range**: Difference between lowest and highest values, useful for reference but sensitive to outliers.

**Standard Deviation**:
- **Symbol**: Lower case Greek letter sigma (σ).
- **Normal Distribution**: 
  - 68% of occurrences fall within one standard deviation (±1σ) of the mean.
  - 95% within two standard deviations (±2σ).
  - 99.7% within three standard deviations (±3σ).
  
**Interpretation**: Standard deviation provides insight into data spread; smaller ranges indicate clustering around the mean, while larger ranges show more spread.

**Variance**:
- **Definition**: Measures the average squared deviation from the mean; indicates volatility and risk.
- **Example**: Two meals averaging 300 orders/week but with different variances may indicate different reliability in sales.

**Means Comparison**:
- Used to assess differences between groups.
- Example: Pricing market baskets across grocery chains.
- **Statistical Significance**: Determined using tests like t-Tests or ANOVA to ensure differences observed are not due to sampling error.

---

Understanding these core concepts of statistical analysis enhances your ability to evaluate data and work collaboratively with analysts, making your decision-making more effective.

**Examining Relationships Between Variables**

**Covariance**
- **Definition**: Measures how two variables move together.
- **Types**:
  - **Positive Covariance**: Both variables increase together (e.g., temperature and ice cream sales).
  - **Negative Covariance**: One variable increases while the other decreases (e.g., temperature and snow shovel sales).
  - **Zero Covariance**: No relationship between variables (e.g., temperature and screwdriver sales).

**Correlation**
- **Definition**: A more precise measure of the relationship between two variables, on a scale from -1 to +1.
- **Interpretation**:
  - **+1**: Perfect positive correlation (one variable explains the other).
  - **-1**: Perfect negative correlation (one variable decreases as the other increases).
  - **0**: No correlation.
- **Correlation Coefficient (r)**: Indicates the strength of the relationship.
  - **Strong Positive**: e.g., r = +0.85.
  - **Weak Positive**: e.g., r = +0.15.
- **Visualization**: Correlations are visualized using scatter plots, where:
  - A clear upward slope indicates a positive correlation.
  - A downward slope indicates a negative correlation.
  - A horizontal line suggests no correlation.

**Correlation and Causation**
- Correlation does not imply causation. Just because two variables track together does not mean one causes the other.

**Context Matters**
- In scientific fields, high correlations (close to +1) are significant. In social sciences, a correlation of +0.6 may still be meaningful.

---

**Regression Analysis**
- **Purpose**: Quantifies the influence of one variable on another, helping to answer questions about relationships (e.g., customer satisfaction and sales).
- **Dependent vs. Independent Variables**:
  - **Dependent Variable**: The outcome being influenced (e.g., sales).
  - **Independent Variables**: Factors believed to influence the dependent variable (e.g., customer satisfaction).
- **Fitted Line**: The line that best describes the data points in a scatter plot.

**Types of Regression**:
1. **Linear Regression**: Analyzes the effect of a single independent variable on a dependent variable.
   - Example: Customer satisfaction's impact on sales.
2. **Multiple Linear Regression**: Examines the influence of two or more independent variables on a dependent variable.
   - Example: The combined effects of customer satisfaction and store proximity on sales.
3. **Non-Linear Regression**: Used when data describes a curve rather than a straight line, indicating a more complex relationship between variables.

**Applications of Regression**:
- Helps identify performance drivers and predict future values based on trends (e.g., forecasting sales based on marketing spending).

Understanding these statistical concepts enhances your ability to analyze data relationships and make informed business decisions.

**Cluster Analysis**

**Definition**: Cluster analysis, also known as classification analysis or clustering, groups similar objects together while ensuring they are dissimilar to objects in other clusters.

**Applications**:
- **Marketing**: Segmenting customers for targeted promotions and developing customer personas based on characteristics.
- **Customer Service**: Clustering call interactions for routing and service improvement.
- **Finance**: Segmenting profitable customers for special services and identifying high-risk policyholders.
- **Law Enforcement**: Identifying crime "hot spots" to allocate resources effectively.
- **General Use**: Understanding patterns and distributions in any significant population.

**Characteristics**:
- **Unsupervised Method**: Analysts select data objects and attributes but do not designate a dependent variable.
- **Pattern Recognition**: Clustering serves as a method for data mining and identifying patterns within datasets.
- **Objective**: Aim to create high-quality clusters with high intra-cluster similarity and high inter-cluster dissimilarity.

**Visualization**: Clustering can be visualized in scatterplots with two variables, but it often involves multiple dimensions.

**Quality of Clusters**:
- High-quality clusters reveal hidden patterns in customer needs and behaviors.
- Selection of objects, variables, and methods is often subjective, based on prior research and analysis.

**Process**:
- Clustering requires experimentation and iteration to determine when clusters are “good enough.”
- Pragmatic concerns include cluster size and the number of clusters; an optimal number should balance detail and usability.

**Considerations**:
- Too few clusters may oversimplify data, while too many can dilute actionable insights.
- Setting parameters, like a maximum number of segments, can help refine the clustering process.

**Benefits**: Understanding clustering provides insights into natural groupings within data, allowing for more tailored and effective business strategies.