# Flood-Prediction-ML

## Project Overview

This project predicts the possibility of floods occurring based on environmental and weather-related data using Machine Learning models.

Flooding has become a serious issue in many parts of India, causing damage to infrastructure, ecosystems, and human life. Early flood prediction systems can help authorities and communities prepare in advance and reduce the impact of such disasters.

This project was created to explore how Machine Learning can be used to analyze environmental patterns and predict flood risk.

## Why did I choose this project?

I was inspired to create this project after watching a Netflix documentary about the flooding of the Tham Luang Cave in Thailand. Even though that incident involved many complex real-world factors, it made me curious about how environmental data and predictive systems could potentially help in disaster preparedness.

I wanted to create a beginner-friendly version of a flood prediction system to strengthen my understanding of Machine Learning concepts while working on a real-world problem.

Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Visual Studio Code
- Machine Learning Concepts Used
- Data Cleaning
- Handling Missing Values
- Feature Selection
- Train-Test Split
- Model Training
- Regression and Classification
- Accuracy Score
- Mean Absolute Error (MAE)
- Dataset
### Dataset Source: Kaggle Flood Prediction Dataset

I chose this dataset because it contains a wide range of environmental and human-induced factors related to floods. The dataset includes features related to rainfall, drainage systems, urbanization, deforestation, climate conditions, and more.

### Some important features in the dataset include:

- Monsoon Intensity
- Drainage Systems
- Urbanization
- Deforestation
- River Management
- Climate Change
- Wetland Loss
- Encroachments
- Agricultural Practices


### Some columns in the dataset represented similar environmental patterns and could introduce redundancy into the model.
- For example: Topography Drainage and Drainage Systems both describe water flow and drainage efficiency.
Agricultural Practices, Deforestation, Urbanization, and Encroachments all reflect human activities affecting flood risk.

- Removing highly similar or correlated features helped reduce redundancy and improve model generalization.

## Models Used
### 1. Linear Regression

Linear Regression was used to predict a continuous flood probability value.

#### Why it did not perform well
- Linear Regression assumes a linear relationship between the input features and the output.
- Flood prediction involves many complex and non-linear relationships between environmental factors.
- The model often predicted values close to the average and struggled to capture complex patterns.
- It also produced values outside the expected probability range of 0 to 1.

Because of these limitations, Linear Regression was not the most suitable model for this problem.

### 2. Logistic Regression

Logistic Regression was used as a classification model to predict whether flooding would occur or not.

#### Why it performed better
- It predicts probabilities and classifies the result into categories such as:
  - Flood
  - No Flood
- Unlike Linear Regression, it does not produce unrealistic output values outside the probability range.
- It performed better because the problem is naturally classification-oriented.
#### Limitations
Logistic Regression still struggles with highly non-linear relationships in the data.

### 3. Random Forest

Random Forest is one of the most suitable algorithms for this problem.

#### Why it works well
- It creates multiple decision trees using random subsets of rows and columns.
- Final predictions are made by combining the outputs of multiple trees.
- It handles non-linear relationships much better than Linear or Logistic Regression.
- It is less sensitive to overfitting compared to a single Decision Tree.

Random Forest performed better because flood prediction depends on multiple interacting environmental conditions rather than a simple linear relationship.

### Results

#### Among the models used:

1. Linear Regression showed weaker performance due to the non-linear nature of the dataset.
3. Logistic Regression improved classification performance significantly.
3. Random Forest produced the best overall predictions for flood risk.

### Evaluation metrics used:

- Accuracy Score
- Mean Absolute Error (MAE)
  
### Future Improvements
- Use larger and more realistic datasets
- Integrate real-time weather APIs
- Experiment with advanced models like XGBoost
- Deploy the project using Flask or Streamlit
- Add data visualization dashboards
- Incorporate satellite and GIS data for improved accuracy
