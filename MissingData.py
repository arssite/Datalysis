import pandas as pd

# Load the dataset
df = pd.read_csv('your_dataset.csv')

# Check for missing values
print(df.isnull().sum())

# Option 1: Remove rows or columns with missing values
# Remove rows with missing values
df_cleaned_rows = df.dropna()

# Remove columns with missing values
df_cleaned_columns = df.dropna(axis=1)

# Option 2: Impute missing values with mean or median
# Impute missing values with mean
df_imputed_mean = df.fillna(df.mean())

# Impute missing values with median
df_imputed_median = df.fillna(df.median())

# Option 3: Use advanced techniques for imputation
# For example, using regression to predict missing values
from sklearn.linear_model import LinearRegression

# Split the data into features and target variables
X = df.drop('target_variable', axis=1)
y = df['target_variable']

# Create a regression model
regressor = LinearRegression()

# Train the model on rows without missing values
X_train = X.dropna()
y_train = y.dropna()
regressor.fit(X_train, y_train)

# Predict missing values
X_missing = X[X.isnull().any(axis=1)]
y_pred = regressor.predict(X_missing)

# Fill missing values with predictions
df_imputed_regression = df.copy()
df_imputed_regression.loc[X_missing.index, 'target_variable'] = y_pred

# Note: The above code assumes the target variable is numeric. Adjustments may be needed for categorical targets.

# Check the resulting datasets after handling missing data
print(df_cleaned_rows)
print(df_cleaned_columns)
print(df_imputed_mean)
print(df_imputed_median)
print(df_imputed_regression)
