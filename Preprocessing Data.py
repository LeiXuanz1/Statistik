# Preprocessing data
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load dataset
file_path = 'Car_sales.csv' 
car_sales_data = pd.read_csv(file_path)

# Handle missing values
numerical_cols = car_sales_data.select_dtypes(include=['float64']).columns
categorical_cols = car_sales_data.select_dtypes(include=['object']).columns

# Imputer for numerical and categorical columns
num_imputer = SimpleImputer(strategy='median')
cat_imputer = SimpleImputer(strategy='most_frequent')

# Apply imputers
car_sales_data[numerical_cols] = num_imputer.fit_transform(car_sales_data[numerical_cols])
car_sales_data[categorical_cols] = cat_imputer.fit_transform(car_sales_data[categorical_cols])

# Encode categorical features
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    car_sales_data[col] = le.fit_transform(car_sales_data[col])
    label_encoders[col] = le

# Save processed data to a new CSV
car_sales_data.to_csv('processed_car_sales.csv', index=False)