# Train-test split
import pandas as pd
from sklearn.model_selection import train_test_split

# Load preprocessed dataset
file_path = 'normalized_car_sales.csv'
car_sales_data = pd.read_csv(file_path)

# Define features (X) and target (y)
X = car_sales_data.drop(columns=['Sales_in_thousands'])  # Ganti kolom target jika berbeda
y = car_sales_data['Sales_in_thousands']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save train-test sets
X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)