# Car Sales
## Project Description
This project aims to analyze car sales data using Exploratory Data Analysis (EDA), preprocessing, train-test splitting, and building a linear regression model to predict car sales based on given features. The results are interpreted to provide business insights and strategic recommendations.

## Project Structure

1. Data
     ● Input Files:
         ● car_sales.csv: The dataset for visualization and EDA.
         ● normalized_car_sales.csv: The normalized preprocessed dataset.
     ● Output Files:
         ● processed_car_sales.csv: The preprocessed dataset.
         ● X_train.csv, X_test.csv, y_train.csv, y_test.csv: Train-test split results.
         ● regression_predictions.csv: Predictions based on the linear regression model.
2. Code
     ● visualisasi EDA.py: Script for data exploration and visualization.
     ● Preprocessing Data.py: Script for preprocessing.
     ● Train Test Split.pt: Script for train-test splitting.
     ● train_test_regression.py: Script for model training and evaluation.

## Steps

1. Exploratory Data Analysis (EDA)
     ● Understand the dataset structure.
     ● Identify patterns and relationships between features through visualization.
2. Preprocessing
     ● Drop irrelevant features.
     ● Normalize data (optional, based on model needs).
3. Train-Test Split
     ● Split the dataset into 80% training data and 20% test data.
4. Modeling
     ● Build a linear regression model to predict the target Sales_in_thousands.
         ● Evaluate the model using metrics:
         ● Mean Squared Error (MSE)
         ● R-squared (R²)
5. Interpretation
        ● Analyze the model results and provide recommendations for further development.

## Results

● Model Evaluation:
    ● MSE: 9.942482599329597e-16
    ● R²: 1.0
● Recomendations: 
    ● A more in-depth analysis of variables with influence can be carried out with high influence to improve model performance.
    ● Other modeling such as regularization regression (Ridge or Lasso) if needed.

## Requirements

● Programming Language: Python 3.8 or later.
      ● Libraries Used:
          ● pandas
          ● numpy
        ● matplotlib
        ● seaborn
        ● scikit-learn

## How to Run
    1. Set Up the Python Environment:
        ● Install all dependencies using:
``` bash
pip install -r requirements.txt
        
